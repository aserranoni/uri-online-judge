import math

def fibonacci(n: int):
    f_ant=0
    f_atual=1
    for i in range(2,n+1):
        f_prox=f_ant+f_atual
        f_ant=f_atual
        f_atual=f_prox
    return f_atual

def fast_fibonacci(n: int):
    phi = ( 1 + math.sqrt(5) ) / 2
    psi  = ( 1 - math.sqrt(5) ) / 2
    ans = (round(phi**n,10) - round(psi**n,10))/math.sqrt(5)
    return round(ans)

def convert_to_decimal(binstring: str):
    return   int(binstring, 2)

def format_output(number : int):
    if len(str(number)) < 3:
        rest = 3-len(str(number))
        return "0"*rest+ str(number)
    else:
        return str(number)[-3:]

n_instances=int(input())
for i in range(n_instances):
    num =fast_fibonacci(convert_to_decimal(input()))
    print(format_output(num))
