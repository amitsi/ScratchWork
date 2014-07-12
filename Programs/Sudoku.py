import SATSolver
import time

def uniqueConstraint(clause):
    clauses.append(clause)
    [[clauses.append([-clause[l],-clause[m]]) for m in range(l+1,len(clause))] for l in range(len(clause))]

def rowClauses():
    for i in range(n*n):
        temp = [j+i*n for j in range(1,n+1)]
        uniqueConstraint(temp)

def colClauses():
    for i in range(1,n*n+1):
        temp = [n*n*j+i for j in range(n)]
        uniqueConstraint(temp)

def boxClauses():
 for p in range(0,n,n/3):
    for i in range(n):
        temp = [n*n*p+j+i*n for j in range(1,n+1)]
        map(uniqueConstraint,(map(lambda k: [i+n*n*l for i in temp[k:k+3] for l in range(n/3)] ,range(0,n,3))))

def conflictClauses():
    for k in range(n):
        for i in range(n):
            temp = [n*n*k+i+1+j*n for j in range(n)]
            uniqueConstraint(temp)

def encodeInput():
    for i in range(n):
        clauses.extend(map(lambda x: [x],[n*n*i+n*(a[i][j]-1)+j+1 for j in range(n) if a[i][j]!=0]))        

clauses = []
n = int(input("Enter sudoku Size (It solves sudoku of sizes 6 and 9) :"))
print "Input the sudoku: (0 for unknown value) Enter Row-Wise "
a = [[input() for j in range(n)] for i in range(n)]
encodeInput()
rowClauses()
colClauses()
boxClauses()
conflictClauses()
print "-----------------------------------"
print "Solving....Please Wait"
st = time.time()
var = SATSolver.solve(n*n*n,clauses)
et = time.time()
if(var!=0):
    temp = [var[i] for i in range(len(var))]
    for k in range(n):
        for i in range(n):
            b =  (map(lambda x : temp[x-1],(map(lambda j: n*n*k+i+1+j*n,range(n)))))
            for j in range(len(b)):
                if(b[j]): print j+1," ",
        print ""
    print "-----------------------------------"
    print "Solved in ",et-st,"seconds"

