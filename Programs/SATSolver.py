def satisfy(clauses):
    global var
    tcount = 0
    for i in clauses:
        fcount = 0
        for j in i:
            if (j<0 and var[abs(j)-1] == 0) or (j>0 and var[abs(j)-1] == 1):
                tcount += 1
                break
            elif var[abs(j)-1]!=-1: fcount += 1
        if fcount == len(i): return 0
    if(tcount==len(clauses)): return 1
    for clause in clauses: unitClause(clause)
    try:
        i = var.index(-1)
        var[i] = 1 
        if(satisfy(clauses)): return 1
        var[i] = 0
        if(satisfy(clauses)): return 1
        var[i] = -1
        return 0
    except:
        if(satisfy(clauses)): return 1
        else:   return 0
'''
def unitClause(clause):
    un = -1
    f = 0
    for i in clause:
        if(var[abs(i)-1]==-1):
            un = i
        elif((i>0 and var[i-1]==0) or (i<0 and var[abs(i)-1]==1)):
            f += 1
    if(un != -1 and f == len(clause)-1):
        var[abs(un)-1] = 0 if un<0 else 1
'''
def unitClause(clause):
    if(len(clause)==1):
        var[clause[0]-1] = 1 if clause[0]>0 else 0

def solve(n,clauses): 
    global var
    var = [-1 for x in range(n)] 
    if satisfy(clauses): return var
    else:
        print 'UNSAT'
        return 0

