def parallelogramme(A,B,C):
    D = []
    D.append(A[0]-B[0]+C[0])
    D.append(A[1]-B[1]+C[1])
    return (D)


A= [12,1]
B = [-5,6]
C = [7, 5]

print(parallelogramme(A,B,C))