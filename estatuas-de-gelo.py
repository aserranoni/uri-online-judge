def read_instance():
    x = input().split()
    n= int(x[0])
    m=int(x[1])
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return m,n,a

def solve_instance(m,n,a):
    c=[0 for i in range(m)]
    c[0]=m
    a = list(sorted(a))
    #print(a)
    j=0
    for i in range(1,m):
        if i%a[j] == 0:
            c[i] =int(i/a[j])
            if j+1 < n:
                j = j +1
        else:
            b=[]
            for k in range(i):
                b.append(c[k] + c[i-k])
            #print(b)
            c[i] = min(b)
    return c[m-1]

def solve_instance2(m,n,a)

if __name__ == "__main__" :
    n_instances = int(input())
    for i in range(n_instances):
        vec= read_instance()
        print(solve_instance(vec[0],vec[1],vec[2]))
