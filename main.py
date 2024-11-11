#Solving Mazes with A*
from pyamaze import maze,agent,textLabel,COLOR
from queue import PriorityQueue
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2) + abs(y1-y2)
def aStar(m):
    aPath = {}
    fwdPath = {}
    start=(m.rows,m.cols)
    g = {cell: float('inf') for cell in m.grid}
    g[start]=0
    f = {cell: float('inf') for cell in m.grid}
    f [start] = h(start, (1, 1))

    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    while not open.empty():
        currentCell=open.get()[2]
        if currentCell==(1,1):
            break
        for d in 'EWNS':
            if m.maze_map[currentCell][d]==True:
                if d=='E':
                    childCell=(currentCell[0],currentCell[1]+1)
                if d=='W':
                    childCell=(currentCell[0],currentCell[1]-1)
                if d=='N':
                    childCell=(currentCell[0]-1,currentCell[1])
                if d=='S':
                    childCell=(currentCell[0]+1,currentCell[1])

                temp_g_score=g[currentCell]+1
                temp_f_score=temp_g_score+h(childCell,(1,1))

                if temp_f_score < f[childCell]:
                    g[childCell]= temp_g_score
                    f[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(1,1)),childCell))
                    aPath[childCell]=currentCell
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(50,50)
    m.CreateMaze(theme=COLOR.light)
    path=aStar(m)

    #animate the solution
    a=agent(m,filled = True, footprints=True)
    m.tracePath({a:path})
    l=textLabel(m,'A Star Path Length',len(path)+1)

    m.run()