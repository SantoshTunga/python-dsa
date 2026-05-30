from collections import deque


def add_vertex(graph: dict[int, list[int]], vertex: int) -> None:
    graph.setdefault(vertex, []).append(vertex)


def add_edge(graph: dict[int, list[int]], node: int, neighbor: int) -> None:
    graph.setdefault(node, []).append(neighbor)
    graph.setdefault(neighbor, []).append(node)


def traverse_all_nodes(graph: dict[int, list[int]]) -> None:
    visited = set()
    for node in graph.keys():
        if node not in visited:
            visited.add(node)
            breadth_first_order(graph, node, visited)


def breadth_first_order(graph: dict[int, list[int]], vertex: int, visited: set) -> None:
    queue = deque()
    queue.append(vertex)
    while queue:
        vertex = queue.popleft()
        print(f" item {vertex} ")
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
