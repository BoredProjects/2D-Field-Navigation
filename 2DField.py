import random

maze = [[0 for x in range(10)]for x in range(10)]
start = (random.randint(0,9),random.randint(0,9))
maze[start[0]][start[1]] = 1
end = (random.randint(0,9),random.randint(0,9))
maze[end[0]][end[1]] = -1

if start == end:
    end = (random.randint(0,9),random.randint(0,9))

print("Fresh Field")
for i in maze:
    print(i)

def right(point):
    if point[1] != 9 and maze[point[0]][point[1] + 1] != -1 and maze[point[0]][point[1] + 1] == 0:
        newPoint = (point[0],point[1]+1)
        maze[newPoint[0]][newPoint[1]] = maze[point[0]][point[1]] + 1
        return newPoint
    elif point[1] != 9 and maze[point[0]][point[1] + 1] == -1:
        return -1
    else:
        return point

def up(point):
    if maze[point[0] - 1][point[1]] != -1 and point[0] != 0 and maze[point[0] - 1][point[1]] == 0:
        newPoint = (point[0]-1,point[1])
        maze[newPoint[0]][newPoint[1]] = maze[point[0]][point[1]] + 1
        return newPoint
    elif maze[point[0] - 1][point[1]] == -1:
        return -1
    else:
        return point

def down(point):
    if point[0] != 9 and maze[point[0]+1][point[1]] != -1 and maze[point[0] + 1][point[1]] == 0:
        newPoint = (point[0]+1,point[1])
        maze[newPoint[0]][newPoint[1]] = maze[point[0]][point[1]] + 1
        return newPoint
    elif point[0] != 9 and maze[point[0]+1][point[1]] == -1:
        return -1
    else:
        return point

def left(point):
    if maze[point[0]][point[1] - 1] != -1 and point[1] != 0 and maze[point[0]][point[1] - 1] == 0:
        newPoint = (point[0],point[1] - 1)
        maze[newPoint[0]][newPoint[1]] = maze[point[0]][point[1]] + 1
        return newPoint
    elif maze[point[0]][point[1] - 1] == -1:
        return -1
    else:
        return point

def clearOld(new,old):
    for i in range(len(new)-1,-1,-1):
        if new[i] == -1:
            new.clear()
            new.append(-1)
            return new
        elif new[i] in old:
            new.pop(i)


    return new

def findPath(maze):
    pathway = []
    pathway.append(start)
    point = start

    while point != end:
        if end[0] > point[0]:
            pathway.append((point[0] + 1,point[1]))
            point = (point[0] + 1, point[1])
        elif end[1] > point[1]:
            pathway.append((point[0], point[1] + 1))
            point = (point[0], point[1] + 1)
        elif end[1] < point[1]:
            pathway.append((point[0], point[1] - 1))
            point = (point[0], point[1] - 1)
        else:
            pathway.append((point[0] - 1, point[1]))
            point = (point[0] - 1, point[1])

    maze.clear()
    maze = [[0 for x in range(10)] for x in range(10)]

    spot = 1
    for i in pathway:
        maze[i[0]][i[1]] = spot
        spot = spot + 1

    return maze, len(pathway)

oldPos = []
oldPos.append(start)
pos = []

while True:

    if -1 in oldPos:
        break


    for i in oldPos:

        pos.append(right(i))
        pos.append(up(i))
        pos.append(left(i))
        pos.append(down(i))



    oldPos = clearOld(pos,oldPos)
    oldPos = list(oldPos)

print("\n")
maze, distance = findPath(maze)

print("Final Field")
for i in maze:
    print(i)

print("Distance from start: " + str(distance))




