import os

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    points = []
    for line in lines:
        pointstr = line.split(', ')
        point = [int(pointstr[0]), int(pointstr[1])]
        points.append(point)

    #print(part1(points))
    print(part2(points))

def part1(points):
    infinite_points = getInfinitePoints(points)
    biggest_area = 0
    for point in points:
        if point in infinite_points:
            continue
        area = getAreaForPoint(point, points)
        if area > biggest_area:
            biggest_area = area
    return biggest_area

def part2(points):
    [left, right, up, down] = getContainingBox(points)

    safe_points = []
    for loc_x in range(left, right+1):
        for loc_y in range(down, up+1):
            total_manhattan_dist = getTotalManhattanDist([loc_x, loc_y], points)
            if total_manhattan_dist < 10000:
                if [loc_x, loc_y] not in safe_points:
                    safe_points.append([loc_x, loc_y])
    return len(safe_points)


def getTotalManhattanDist(search_point, points):
    total_manhattan_dist = 0
    for point in points:
        manhattan_dist = getManhattanDistance(search_point, point)
        total_manhattan_dist += manhattan_dist
    return total_manhattan_dist


def getAreaForPoint(point, points):
    area = 0
    [left, right, up, down] = getSearchGrid(point, points)
    for loc_x in range (left, right+1):
        for loc_y in range (down, up+1):
            closest_point = getClosestPoint([loc_x, loc_y], points)
            if closest_point == point:
                area += 1
    return area


def getSearchGrid(point, points):
    #Find left
    done = False
    loc_x = point[0]
    loc_y = point[1]
    while not done:
        loc_x -= 1
        closest_point = getClosestPoint([loc_x, loc_y], points)
        if closest_point != point:
            left = loc_x+1
            done = True
    
    #Find right
    done = False
    loc_x = point[0]
    loc_y = point[1]
    while not done:
        loc_x += 1
        closest_point = getClosestPoint([loc_x, loc_y], points)
        if closest_point != point:
            right = loc_x-1
            done = True

    #Find up
    done = False
    loc_x = point[0]
    loc_y = point[1]
    while not done:
        loc_y += 1
        closest_point = getClosestPoint([loc_x, loc_y], points)
        if closest_point != point:
            up = loc_y-1
            done = True

    #Find down
    done = False
    loc_x = point[0]
    loc_y = point[1]
    while not done:
        loc_y -= 1
        closest_point = getClosestPoint([loc_x, loc_y], points)
        if closest_point != point:
            down = loc_y+1
            done = True

    return [left, right, up, down]

def getContainingBox(points):
    left = points[0][0]
    right = points[0][0]
    up = points[0][1]
    down = points[0][1]
    for point in points:
        if point[0] < left:
            left = point[0]
        if point[0] > right:
            right = point[0]
        if point[1] > up:
            up = point[1]
        if point[1] < down:
            down = point[1]
    return [left, right, up, down]

#We determine the infinite points by creating a box one pixel outside of our outermost points.
#Any points which are the closest to a point on the box are considered infinite
def getInfinitePoints(points):
    infinite_points = []
    [left, right, up, down] = getContainingBox(points)

    #left border
    loc_x = left-1
    for loc_y in range (down-1, up+2):
        closest_point = getClosestPoint([loc_x, loc_y], points)
        if closest_point not in infinite_points:
            infinite_points.append(closest_point)
    #right border
    loc_x = right+1
    for loc_y in range (down-1, up+2):
        closest_point = getClosestPoint([loc_x, loc_y], points)
        if closest_point not in infinite_points:
            infinite_points.append(closest_point)
    #top border
    loc_y = up+1
    for loc_x in range (left-1, right+2):
        closest_point = getClosestPoint([loc_x, loc_y], points)
        if closest_point not in infinite_points:
            infinite_points.append(closest_point)

    #bottom border
    loc_y = down-1
    for loc_x in range (left-1, right+2):
        closest_point = getClosestPoint([loc_x, loc_y], points)
        if closest_point not in infinite_points:
            infinite_points.append(closest_point)
    return infinite_points


def getClosestPoint(search_point, points):
    firstPoint = True
    for point in points:
        manhattan_dist = getManhattanDistance(search_point, point)
        if firstPoint == True:
            lowest_dist = manhattan_dist
            closest_point = point
            firstPoint = False
        elif manhattan_dist < lowest_dist:
            lowest_dist = manhattan_dist
            closest_point = point

    return closest_point

def getManhattanDistance(point1, point2):
    x_dist = abs(point2[0] - point1[0])
    y_dist = abs(point2[1] - point1[1])
    return x_dist + y_dist 

if __name__== "__main__":
    main()