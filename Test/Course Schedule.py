#5️⃣ Course Schedule (Cycle Detection)  Can you finish all courses?

def can_finish(n, prereq):
    graph = {i:[] for i in range(n)}

    for a, b in prereq:
        graph[a].append(b)

    visit = set()

    def dfs(node):
        if node in visit:
            return False
        if graph[node] == []:
            return True

        visit.add(node)

        for nei in graph[node]:
            if not dfs(nei):
                return False

        visit.remove(node)
        graph[node] = []
        return True

    for i in range(n):
        if not dfs(i):
            return False

    return True