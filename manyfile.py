def parse_input():
    try:
        n = int(input())
        graph = []
        for i in range(n):
            line = (input().split())[1:]
            graph.append(line)
    except EOFError:
        return False
    return list(reversed(sorted(graph, key=len)))

def assert_feasibility(graph):
    for i in range(len(graph)):
        for j in graph[i]:
            j=int(j)
            for k in graph[j-1]:
                k=int(k)-1
                if k ==i:
                    return False
    return True

def dfs(graph):
    if assert_feasibility(graph) == True:
        colors = ["Branco" for i in range(len(graph))]
        start = [1000 for i in range(len(graph))]
        end = [0 for i in range(len(graph))]
        time=0
        for u in range(len(graph)):
            if colors[u] == "Branco":
                time,start,end = dfs_visit(u,colors,graph,time,start,end)
        return start, end
    else:
        return [-1],[-1]

def dfs_visit(v,colors,graph,time,start,end):
    time = time + 1
    start[v] = time
    colors[v] = "Cinzento"
    for i in graph[v]:
        j=int(i)
        if colors[j-1] == "Branco":
            time,start,end=dfs_visit(j-1,colors,graph,time,start,end)
    colors[v] = "Preto"
    time=time+1
    end[v] =time
    return time,start,end

def parse_results(start,end):
    if start[0] == -1:
        return -1
    else:
        diff = [0 for i in range(len(start))]
        for i in range(len(start)):
             diff[i] =end[i]-start[i]
        m = max(diff)
        return int(((m-1)/2)+1)

if __name__ == '__main__':
    while True:
        var=parse_input()
        if var != False:
            a=dfs(var)
            print(parse_results(a[0],a[1]))
        else:
            break
