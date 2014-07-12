import math
'''
3 4 6    1 2 3
1 7 2 => 4 5 6
5 8 9    7 8 9

Heuristic 1: How many numbers are out of place

Heuristic 2: How far is numbers from its actual position
'''

def h1(a):
    count = 0
    a = list(a)
    for i in range(len(a)):
        if(int(a[i]) != i+1):
            count += 1
    return count

def h2(a):
    count = 0
    a = list(a)
    for i in range(len(a)):
        count += int(math.fabs(int(a[i])-i-1))
    return count

def Astar(start,goal,heuristic):
    closedSet = []
    openSet = [start]
    came_from = {}
    g_Score = {}
    f_Score = {}
    g_Score[start] = 0
    f_Score[start] = g_Score[start] + heuristic(start)
        
    while len(openSet)!=0:
        current = lowest_F_Score_Node(openSet,f_Score)
        if current == goal:
            return reconstruct_Path(came_from, goal)
        openSet.remove(current)
        closedSet.append(current)
        for neighbour in neighbour_Nodes(current):
            if neighbour in closedSet:
                continue
            tentative_g_score = g_Score[current] + 1
            if (neighbour not in openSet) or (tentative_g_score < g_Score[neighbour]):
                came_from[neighbour] = current
                g_Score[neighbour] = tentative_g_score
                f_Score[neighbour] = g_Score[neighbour] + heuristic(neighbour)
                if neighbour not in openSet:
                    openSet.append(neighbour)
    return None

def lowest_F_Score_Node(nodeSet,f_Score):
    temp = dict(map(lambda x: (x,f_Score.get(x)),filter(lambda x: x in nodeSet,f_Score.keys())))
    return min(temp,key=temp.get)    
     
def reconstruct_Path(came_from, current_node):
    if current_node in came_from:
        p= reconstruct_Path(came_from, came_from[current_node])
        return p+" --> "+current_node
    else:
        return current_node    
         
def neighbour_Nodes(current):
    neighbours = []
    cur = list(current)
    key = len(current)
    i = cur.index(str(key))
    n = int(math.sqrt(key))
    if i not in filter(lambda x: x%n==0,range(len(cur))):
        neighbours.append(''.join(cur[0:i-1])+cur[i]+cur[i-1]+''.join(cur[i+1:]))
    if i not in filter(lambda x: (x+1)%n==0,range(len(cur))):
        neighbours.append(''.join(cur[0:i])+cur[i+1]+cur[i]+''.join(cur[i+2:]))
    if (i-n)>=0:
        neighbours.append(''.join(cur[0:i-n])+cur[i]+''.join(cur[i-n+1:i])+cur[i-n]+''.join(cur[i+1:]))
    if (i+n)<key:
        neighbours.append(''.join(cur[0:i])+cur[i+n]+''.join(cur[i+1:i+n])+cur[i]+''.join(cur[i+n+1:]))
    return neighbours

i = '941573286'
i = '642538197'
i = '415679328'
i = '531862497'
i = '342917658'
i = '591748263'
f = '123456789'
i = str(input("Enter String:"))
print(Astar(i,f,h2))
