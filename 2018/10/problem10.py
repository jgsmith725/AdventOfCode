import os

class Point():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
    
    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    points = []
    for line in lines:
        point = parseLine(line)
        points.append(point)

    count = 0
    while True:
        num_connecting = getNumConnectingPoints(points[0], points, [])
        print('num_connecting = ' + str(num_connecting) + ' count = ' + str(count))
        count += 1
        #if num_connecting > 10:
        if count == 10613:
            displayPoints(points)
            break
        for point in points:
            point.move()
        print('\n\n\n')

def displayPoints(points):
    [left, right, up, down] = getBoundingBox(points)
    grid_str = ''
    for y in range (down, up):
        row_str = ''
        for x in range(left, right):
            found = False
            if pointInPoints(Point([x, y], []), points):
                row_str = row_str + "#"
            else:
                row_str = row_str + "."
        grid_str = grid_str + row_str + '\n'
    print(grid_str)

    
def pointInPoints(search_point, points):
    for point in points:
        if search_point.pos == point.pos:
            return True
    return False

def getNumConnectingPoints(starting_point, points, points_found):
    numConnectingPoints = 0
    point_left = Point([starting_point.pos[0] - 1, starting_point.pos[1]], [])
    point_right =  Point([starting_point.pos[0] + 1, starting_point.pos[1]], [])
    point_above =  Point([starting_point.pos[0], starting_point.pos[1] + 1], [])
    point_below =  Point([starting_point.pos[0], starting_point.pos[1] - 1], [])
    if pointInPoints(point_left, points) and not pointInPoints(point_left, points_found):
        numConnectingPoints += 1
        points_found.append(point_left)
        numConnectingPoints += getNumConnectingPoints(point_left, points, points_found)
    if pointInPoints(point_right, points) and not pointInPoints(point_right, points_found):
        numConnectingPoints += 1
        points_found.append(point_right)
        numConnectingPoints += getNumConnectingPoints(point_right, points, points_found)
    if pointInPoints(point_above, points) and not pointInPoints(point_above, points_found):
        numConnectingPoints += 1
        points_found.append(point_above)
        numConnectingPoints += getNumConnectingPoints(point_above, points, points_found)
    if pointInPoints(point_below, points) and not pointInPoints(point_below, points_found):
        numConnectingPoints += 1
        points_found.append(point_below)
        numConnectingPoints += getNumConnectingPoints(point_below, points, points_found)
    return numConnectingPoints

def getBoundingBox(points):
    first_point = True
    count = 0
    for point in points:
        if first_point:
            left = point.pos[0]
            right = point.pos[0]
            up = point.pos[1]
            down = point.pos[1]
            first_point = False
        else:
            if point.pos[0] < left:
                left = point.pos[0]
            if point.pos[0] > right:
                right = point.pos[0]
            if point.pos[1] < down:
                down = point.pos[1]
            if point.pos[1] > up:
                up = point.pos[1]
    return [left-1, right+1, up+1, down-2]


def parseLine(line):
    pos_str = line.split('position=<')[1].split('> velocity=')[0]
    pos = [int(pos_str.split(', ')[0]), int(pos_str.split(', ')[1])]
    vel_str = line.split('velocity=<')[1].split('>')[0]
    vel = [int(vel_str.split(', ')[0]), int(vel_str.split(', ')[1])]
    return Point(pos, vel)

if __name__== "__main__":
    main()