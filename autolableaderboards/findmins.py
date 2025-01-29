from bs4 import BeautifulSoup

# Example HTML structure
html_content = open('scores.html', 'r')
html_content_str = ""
for line in html_content:
    html_content_str += line

# Parse the HTML
soup = BeautifulSoup(html_content_str, 'html.parser')

# Extract rows
rows = soup.find_all('tr')

# Parse numbers
parsed_data = []
for row in rows:
    numbers = [int(td.get_text(strip=True)) for td in row.find_all('td') if td.get_text(strip=True).isdigit()]
    parsed_data.append(numbers)

# print(parsed_data)

mins = []

allscores = []

for datapoint in parsed_data:
    rank = datapoint[0]
    version = datapoint[1]
    score = datapoint[2]
    totalops = datapoint[3]
    
    data = datapoint[4:]
    if score == 57:
        allscores.append(data)

for i in range(0, len(allscores[0])):
    col = [allscores[j][i] for j in range(0, len(allscores))]
    mins.append(min(col))

print(mins)
print()
print(sum(mins))