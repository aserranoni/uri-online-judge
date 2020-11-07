def read_instance():
    first_line= input()
    first_line=first_line.split()
    n = int(first_line[0])
    W = int(first_line[1])
    if n == 0:
        return False
    else:
        v=[]
        w=[]
        for i in range(n):
            line = input()
            line = line.split()
            w.append(int(line[0]))
            v.append(int(line[1]))
        return n,w,v,W


def solve_instance(n,w,v,W):
    t=[]
    for Y in range(W+1):
        t.append(0)
        for i in range(n):
            if w[i] <= Y:
                t[Y] = max(t[Y], t[Y-w[i]] + v[i])
    return str(t[W])


if __name__ == "__main__":
    counter = 1
    while True:
        var = read_instance()
        if var == False:
            break
        else:
            print("Instancia " + str(counter))
            print(solve_instance(var[0],var[1],var[2],var[3]))
            print("\n")
            counter = counter + 1
