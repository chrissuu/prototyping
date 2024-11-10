import requests
import time
from bs4 import BeautifulSoup
from difflib import ndiff
import argparse
# Function to get only the visible text from the page
def get_visible_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()
        
        # Extract visible text
        text = soup.get_text(separator=' ')
        
        # Clean up the text by removing extra whitespace
        cleaned_text = ' '.join(text.split())
        
        return cleaned_text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

# Function to monitor page and detect text changes
def get_page_diff_after_interval(url, interval):
    '''Gets differences in page and returns an added, removed array. 
    Pages are queried after "interval" seconds'''
    # Get initial visible text content
    added = []
    removed = []

    last_text = get_visible_text(url)
 
    time.sleep(interval)
        
    current_text = get_visible_text(url)
        
    # Compare current text with the previous text
    if current_text != last_text:
        print("The page's visible text has changed! Here are the differences:\n")
            
        # Word-by-word comparison
        diff = ndiff(last_text.split(), current_text.split())
        for change in diff:
            if change.startswith('+'):
                print(f"Added: {change[2:]}")
                added.append(change)
            elif change.startswith('-'):
                print(f"Removed: {change[2:]}")
                removed.append(change)
            
        # Update last_text with the current version for next comparison
        last_text = current_text
    else:
        print("No visible text change detected.")

    return added, removed

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Monitor a webpage for visible text changes.")
    parser.add_argument("url", type=str, help="The URL of the webpage to monitor.")
    parser.add_argument("--interval", type=int, default=15, help="Interval in seconds to check for changes (default: 15).")
    
    args = parser.parse_args()
    
    # Run the monitoring function with provided parameters
    added, removed = get_page_diff_after_interval(args.url, args.interval)
    print(added)
    print('\n\n')
    print(removed)
