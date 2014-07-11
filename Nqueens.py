import SATSolver
clauses = []
n = int(input("Enter n: "))

def onlyOneConstraint(clause):
    n = len(clause)
    [[clauses.append([-clause[l],-clause[m]]) for m in range(l+1,n)] for l in range(n)]

def getRowColClauses():
    for i in range(n):
        temp = [[],[]]
        for j in range(n):
            temp[0].append(i+1+(j*n))
            temp[1].append((j+1)+(i*n))
        clauses.extend(temp)
        onlyOneConstraint(temp[0])
        onlyOneConstraint(temp[1])
                
def diagonalClauses(diagonal):
    skip = n-1
    for i in range(2*n-1):
        k = j = (j-1) if (i>=n) else i%n + 1
        temp = []
        while k!=0:
            if(i<n*n):
                if(diagonal[i][1]!=1):
                    temp.append(diagonal[i][0]+1)
                    diagonal[i][1] = 1
                    i += skip
                    k -= 1
                else: i += 1
            else: break
        if(len(temp)!=1): onlyOneConstraint(temp)

def genClauses():
    getRowColClauses()
    diagonal = [list(i) for i in enumerate([0 for i in range(n*n)])]
    diagonalClauses(diagonal)
    diagonal2 = [[x-1,0] for xs in [[i+n-j for j in range(1,n+1)] for i in range(1,n*n+1,n)] for x in xs]
    diagonalClauses(diagonal2)
genClauses()
var = SATSolver.solve(n*n,clauses)
if(var!=0):
    for i in range(len(var)): print str(var[i])+'\n' if (i+1)%n==0 else var[i],
