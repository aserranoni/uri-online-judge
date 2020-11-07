def read_instance():
    first_line=input()
    n=int(first_line.split()[0])
    k = int(first_line.split()[1])
    if n==0:
        return False
    else:
        seq = input().split()
        for i in range(len(seq)):
            seq[i]=int(seq[i])
        return n,k,seq

def subsequence_counter(mat,k):
    counter = 0
    for list in mat:
        for elem in list:
            if elem == k:
                counter = counter +1
    return counter

def LCS(x,y):
    c=[]
    for i in range(len(x)+1):
        c.append([0])
    for  j in range(len(y)):
        c[0].append(0)
    for i in range(1,len(x)):
        for j in range(1,len(y)):
            if x[i]==y[j]:
                c[i].append(c[i-1][j-1] +1)
            else:
                c[i].append(max(c[i-1][j] , c[i][j-1]))
    return c[len(x)]


def solution(vec,size):
    c=[]
    for i in range(len(vec)):
        c.append([1])
    for j in range(1,size):
        for i in range(len(vec)):
            soma= 0
            for k in range(i):
                if vec[k] < vec[i]:
                    soma = soma + c[k][j-1]
            c[i].append(soma)
    ans = 0
    for l in c:
        ans=ans+l[-1]
    return ans

if __name__ == "__main__":
    while True:
        var = read_instance()
        if var == False:
            break
        else:
            print(solution(var[2],var[1]))
