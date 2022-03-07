# Recursive solution for Towers on Hanoi problem

'''
def thp(n, S, T, I):
    if n == 1:
       T.append(S.pop())
       print(S, I, T)
    else:
        thp(n - 1, S, I, T)
        T.append(S.pop())
        thp(n - 1, I, T, S)
'''

def thp_str(n, S, T, I):
    if n == 1:
        print("Move disk from peg {} to peg {}".format(S, T))
    else:
        thp_str(n - 1, S, I, T)
        print("Move disk from peg {} to peg {}".format(S, T))
        thp_str(n - 1, I, T, S)
    return 0

def solve(n):
    S = [0] * n
    I = [0] * n
    T = [0] * n
    for i in range(n):
        S[i] = i
    #thp(n, S, T, I)
    
    S = "S"
    I = "I"
    T = "T"
    thp_str(n, S, T, I)


print(solve(5))
