def beam_search(graph, heuristic, start, goal, beam_width):

    beam = [start]
    parent = {start: None}

    while beam:

        print("\nCurrent Beam:", beam)

        # Check if goal is found
        if goal in beam:
            path = []

            current = goal
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Goal Found!")
            print("Final Path:", " -> ".join(path))

            return path

        candidates = []

        # Expand all nodes in current beam
        for node in beam:
            for neighbor in graph.get(node, []):

                if neighbor not in parent:
                    parent[neighbor] = node

                candidates.append(neighbor)

        # Remove duplicates
        candidates = list(dict.fromkeys(candidates))

        print("Candidates:", candidates)

        # Sort according to heuristic
        candidates.sort(key=lambda x: heuristic[x])

        print(
            "Sorted:",
            [(node, heuristic[node]) for node in candidates]
        )

        # Keep only best W nodes
        beam = candidates[:beam_width]

        print(
            "Selected:",
            [(node, heuristic[node]) for node in beam]
        )

    print("Goal could not be reached.")
    return None


# -------------------------------
# Graph
# -------------------------------

graph = {
    "S": ["A", "B", "C"],
    "A": ["D", "E"],
    "B": ["F", "G"],
    "C": ["H", "I"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
    "H": [],
    "I": []
}


# -------------------------------
# Heuristic values
# -------------------------------

heuristic = {
    "S": 10,
    "A": 6,
    "B": 3,
    "C": 5,
    "D": 4,
    "E": 7,
    "F": 2,
    "G": 6,
    "H": 3,
    "I": 8
}


# -------------------------------
# Parameters
# -------------------------------

start = "S"
goal = "F"
beam_width = 2


# -------------------------------
# Run Beam Search
# -------------------------------

beam_search(
    graph,
    heuristic,
    start,
    goal,
    beam_width
)