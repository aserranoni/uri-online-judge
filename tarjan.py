def read_instance():
    line = input().split()
    if int(line[0]) ==0:
        return False
    else:
        edges=[]
        s_line = input().split()
        for i in range(int(len(s_line)/2)):
            edges.append((int(s_line[2*i])-1,int(s_line[2*i + 1])-1))
    return int(line[0]) , edges

def edges_to_lists(n,edges):
    mat = [[] for i in range(n)]
    for tup in edges:
        mat[tup[0]].append(tup[1])
    return mat

def find_components(graph):
    n = len(graph)
    ide=0
    low = [0 for i in range(n)]
    ids = [-1 for i in range(n)]
    on_stack = [False for i in range(n)]
    stack =[]
    for at in range(n):
        if ids[at] == -1:
            ide,low,stack,on_stack,ids =dfs_visit(graph,at,ide,low,stack,on_stack,ids)
    return low

def dfs_visit(graph,at,ide,low,stack,on_stack,ids):
    stack.append(at)
    on_stack[at] =True
    ide = ide +1
    ids[at] = ide
    low[at] =ide
    for to in graph[at]:
        if ids[to] == -1:
            ide,low,stack,on_stack,ids =dfs_visit(graph,to,ide,low,stack,on_stack,ids)
        if on_stack[to]:
            low[at] =min(low[at],low[to])
    if ids[at] ==low[at]:
        #print(stack)
        #print(on_stack)
        while stack !=[]:
            node = stack.pop()
            on_stack[node] =False
            low[node] = low[at]
            if node == at:
                #print("while broken at node " + str(node))
                break
    return ide, low,stack,on_stack,ids

def find_bottom(graph,val):
    n= len(graph)
    bottom = [i+1 for i in range(n)]
    for i in range(len(graph)):
        for v in graph[i]:
            if val[i] != val[v] and i+1 in bottom:
                bottom.remove(i+1)
    return bottom


if __name__ == "__main__":
    while True:
        graph = read_instance()
        if graph == False:
            break
        else:
            graph =edges_to_lists(graph[0],graph[1])
            print(*find_bottom(graph,find_components(graph)))

