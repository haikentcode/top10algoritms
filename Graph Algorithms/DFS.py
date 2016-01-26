def dfs_iter(graph, start, path=[]):
    q=[start]
    while q:
        v = q.pop(0)
        if v not in path:
            path += [v]
            q += graph[v]
    return path

def dfs_rec(graph, start, path=[]):
    path = path + [start]
    for node in graph[start]:
        if not node in path:
            path = dfs_rec(graph, node, path)
    return path
if __name__ == '__main__':
    graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
    print dfs_iter(graph, 'A')

    print dfs_rec(graph, 'A')
