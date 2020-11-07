def read_input():
    mat=[]
    size= int(input())
    for i in range(size):
        line=input()
        mat.append(line.split())
    return mat

def verify_insertion(mat, clique, elem):
    if len(clique)==0:
        return True
    else:
        var = True
        for v in clique:
            if mat[elem][v] == "0" :
                var = False
        return var

def solve_problem(mat):
    a=[]
    b=[]
    a.append(0)
    for i in range(1,len(mat[0])):
        if mat[0][i] =="0":
            if verify_insertion(mat,b,i):
                b.append(i)
            else:
                return False
        else:
            a.append(i)
    x = len(a)
    for i in range(1,x-1):
        for j in range(i+1,x):
            if mat[a[i]][a[j]] == "0":
                if verify_insertion(mat,b,a[i]):
                    b.append(a[i])
                    #a.remove(a[i])
                    x=-1
                else:
                    return False
    return a,b

def print_output(arg):
    if arg == False:
        print("Fail!\n")
    else:
        print("Bazinga!\n")

if __name__ == "__main__":
    print_output(solve_problem(read_input()))
