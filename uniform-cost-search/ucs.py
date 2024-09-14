import util


graph = [
    [0, 3, 4, 0, 0, 0, 0],
    [3, 0, 2, 3, 5, 0, 0],
    [4, 2, 0, 0, 2, 0, 0],
    [0, 3, 0, 0, 1, 0, 0],
    [0, 5, 2, 1, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 2],
    [0, 0, 0, 0, 6, 2, 0]
]

def ucs(adj_matrix):
    explored_set = set()
    frontier = util.PriorityQueue()
    frontier.push(, 0)
    while True:
        if frontier.isEmpty():
            return []
        