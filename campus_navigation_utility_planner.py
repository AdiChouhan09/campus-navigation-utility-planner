import heapq


class Building:
    def __init__(self, code, name, btype, zone):
        self.code = code       # unique short code (e.g., CS, LIB, ADM)
        self.name = name       # full name
        self.btype = btype     # Academic / Hostel / Admin / Sports / Other
        self.zone = zone       # North / South / Block-A / etc.

    def __str__(self):
        return f"{self.code} - {self.name} | Type: {self.btype} | Zone: {self.zone}"


class CampusGraph:
    def __init__(self):
        self.buildings = {}   # code -> Building
        self.adj = {}         # code -> list of (neighbor_code, distance)

    def add_building(self, code, name, btype, zone):
        if code in self.buildings:
            print("Building code already exists, updating building information.")
        self.buildings[code] = Building(code, name, btype, zone)
        if code not in self.adj:
            self.adj[code] = []

    def add_road(self, code1, code2, distance):
        if code1 not in self.buildings or code2 not in self.buildings:
            print("Both buildings must exist before connecting them.")
            return
        self.adj.setdefault(code1, [])
        self.adj.setdefault(code2, [])
        self.adj[code1].append((code2, distance))
        self.adj[code2].append((code1, distance))
        print(f"Road added between {code1} and {code2} with distance {distance}.")

    def display_map(self):
        if not self.buildings:
            print("No buildings in campus map yet.")
            return
        print("\n--- Buildings ---")
        for b in self.buildings.values():
            print(" ", b)
        print("\n--- Road Network (Adjacency List) ---")
        for code, neighbors in self.adj.items():
            edges = ", ".join(f"{nbr}({dist})" for nbr, dist in neighbors)
            print(f" {code} -> {edges}")
        print()

    def bfs(self, start_code):
        if start_code not in self.buildings:
            print("Start building code not found.")
            return
        visited = set()
        queue = [start_code]
        visited.add(start_code)
        order = []
        while queue:
            u = queue.pop(0)
            order.append(u)
            for v, _ in self.adj.get(u, []):
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        print("BFS traversal order (by building code):", " -> ".join(order))

    def dfs(self, start_code):
        if start_code not in self.buildings:
            print("Start building code not found.")
            return
        visited = set()
        order = []

        def _dfs(u):
            visited.add(u)
            order.append(u)
            for v, _ in self.adj.get(u, []):
                if v not in visited:
                    _dfs(v)

        _dfs(start_code)
        print("DFS traversal order (by building code):", " -> ".join(order))

    def dijkstra(self, start_code, end_code):
        if start_code not in self.buildings or end_code not in self.buildings:
            print("Start or destination building code not found.")
            return
        dist = {code: float("inf") for code in self.buildings}
        prev = {code: None for code in self.buildings}
        dist[start_code] = 0.0
        heap = [(0.0, start_code)]

        while heap:
            current_dist, u = heapq.heappop(heap)
            if current_dist > dist[u]:
                continue
            if u == end_code:
                break
            for v, w in self.adj.get(u, []):
                nd = current_dist + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(heap, (nd, v))

        if dist[end_code] == float("inf"):
            print("No path found between the given buildings.")
            return

        path_codes = []
        cur = end_code
        while cur is not None:
            path_codes.append(cur)
            cur = prev[cur]
        path_codes.reverse()

        print("\nShortest path (by building code):", " -> ".join(path_codes))
        print("Total distance:", dist[end_code])
        print("Detailed path:")
        for code in path_codes:
            print(" ", self.buildings[code])


class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []


class BuildingHierarchyTree:
    def __init__(self):
        self.root = None

    def set_root(self, name):
        if self.root is None:
            self.root = TreeNode(name)
        else:
            self.root.name = name
        print("Root set to:", self.root.name)

    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        for child in node.children:
            res = self._find(child, name)
            if res:
                return res
        return None

    def add_child(self, parent_name, child_name):
        if self.root is None:
            print("Create root first.")
            return
        parent = self._find(self.root, parent_name)
        if parent is None:
            print("Parent not found in hierarchy.")
            return
        parent.children.append(TreeNode(child_name))
        print(f"Added '{child_name}' under '{parent_name}'.")

    def _display(self, node, level):
        if node is None:
            return
        print("  " * level + "- " + node.name)
        for child in node.children:
            self._display(child, level + 1)

    def display(self):
        if self.root is None:
            print("Hierarchy tree is empty.")
            return
        print("\n--- Building Hierarchy ---")
        self._display(self.root, 0)
        print()


def read_float(prompt, minimum=None):
    while True:
        try:
            val = float(input(prompt))
            if minimum is not None and val < minimum:
                print(f"Value must be >= {minimum}")
                continue
            return val
        except ValueError:
            print("Invalid number, try again.")


def main():
    graph = CampusGraph()
    hierarchy = BuildingHierarchyTree()

    while True:
        print("\n====== CAMPUS NAVIGATION AND UTILITY PLANNER ======")
        print("1. Add Building")
        print("2. Add Road / Connection")
        print("3. Display Campus Map")
        print("4. Shortest Path (Dijkstra)")
        print("5. BFS Traversal")
        print("6. DFS Traversal")
        print("7. Manage Building Hierarchy Tree")
        print("8. Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            code = input("Building code (e.g., CS, LIB, ADM): ").strip().upper()
            name = input("Building name: ").strip()
            btype = input("Type (Academic/Hostel/Admin/Sports/Other): ").strip()
            zone = input("Zone/Block (e.g., North, South, Block-A): ").strip()
            graph.add_building(code, name, btype, zone)

        elif choice == "2":
            c1 = input("From building code: ").strip().upper()
            c2 = input("To building code: ").strip().upper()
            d = read_float("Distance / cost between them: ", minimum=0.0)
            graph.add_road(c1, c2, d)

        elif choice == "3":
            graph.display_map()

        elif choice == "4":
            start = input("Start building code: ").strip().upper()
            end = input("Destination building code: ").strip().upper()
            graph.dijkstra(start, end)

        elif choice == "5":
            start = input("Start building code for BFS: ").strip().upper()
            graph.bfs(start)

        elif choice == "6":
            start = input("Start building code for DFS: ").strip().upper()
            graph.dfs(start)

        elif choice == "7":
            while True:
                print("\n--- Building Hierarchy Management ---")
                print("1. Set / Change Root Category")
                print("2. Add Child Category / Building")
                print("3. Display Hierarchy")
                print("4. Back to Main Menu")
                sub = input("Select option: ").strip()
                if sub == "1":
                    name = input("Root name (e.g., Campus, University): ").strip()
                    hierarchy.set_root(name)
                elif sub == "2":
                    parent = input("Parent name: ").strip()
                    child = input("Child name: ").strip()
                    hierarchy.add_child(parent, child)
                elif sub == "3":
                    hierarchy.display()
                elif sub == "4":
                    break
                else:
                    print("Invalid option.")

        elif choice == "8":
            print("Exiting Campus Navigation and Utility Planner. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
