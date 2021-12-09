import sys
sys.path.append('/Users/jack/Python/AdventOfCode/2019')
import helper
import numpy as np

def getMaxes(paths):
    min_xs = []
    max_xs = []
    min_ys = []
    max_ys = []

    for path in paths:
        [min_x, max_x, min_y, max_y] = getMaxesForPath(path)
        min_xs.append(min_x)
        max_xs.append(max_x)
        min_ys.append(min_y)
        max_ys.append(max_y)

    return [min(min_xs), max(max_xs), min(min_ys), max(max_ys)]

def getMaxesForPath(path):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    curr_x = 0
    curr_y = 0
    for seg in path:
        direction = seg[0]
        length = int(seg[1:]) + 1
        if direction == 'U':
            curr_y += length
            if curr_y > max_y:
                max_y = curr_y
        if direction == 'D':
            curr_y -= length
            if curr_y < min_y:
                min_y = curr_y
        if direction == 'L':
            curr_x -= length
            if curr_x < min_x:
                min_x = curr_x
        if direction == 'R':
            curr_x += length
            if curr_x > max_x:
                max_x = curr_x
    return [min_x, max_x, min_y, max_y]

def addSegPoints(points, seg, pos_x, pos_y):
    direction = seg[0]
    length = int(seg[1:])

    if direction == 'U':
        rows = np.full((length+1), pos_x, np.int)
        cols = np.arange(0, length+1, 1)
        cols = np.add(cols, pos_y)
        points[rows, cols] = 1
        pos_y += length  
    if direction == 'D':
        rows = np.full((length+1), pos_x, np.int)
        cols = np.arange(-length, 1, 1)
        cols = np.add(cols, pos_y)
        points[rows, cols] = 1
        pos_y -= length   
    if direction == 'L':
        rows = np.arange(-length, 1, 1)
        rows = np.add(rows, pos_x)
        cols = np.full((length+1), pos_y, np.int)
        points[rows, cols] = 1
        pos_x -= length    
    if direction == 'R':
        rows = np.arange(0, length+1, 1)
        rows = np.add(rows, pos_x)
        cols = np.full((length+1), pos_y, np.int)
        points[rows, cols] = 1
        pos_x += length

    return [pos_x, pos_y] #return the new starting position

def addPathPoints(path, points, start_x, start_y):
    pos_x = start_x
    pos_y = start_y 
    for seg in path:
        [pos_x, pos_y] = addSegPoints(points, seg, pos_x, pos_y)
    
def getSteps(path):
    steps = []
    for seg in path:
        direction = seg[0]
        length = int(seg[1:])
        steps += length * [direction]
    return steps

def stepWire(steps, step_pos, wire_pos):
    direction = steps[step_pos]
    if direction == 'U':
        wire_pos += np.add(wire_pos, [1,0])
    if direction == 'D':
        wire_pos += np.add(wire_pos, [-1,0])
    if direction == 'L':
        wire_pos += np.add(wire_pos, [0,-1])
    if direction == 'R':
        wire_pos += np.add(wire_pos, [0,1])

def getStepsToPoint(path, points, start_x, start_y, point):
    pos_x = start_x
    pos_y = start_y
    steps = 0
    for seg in path:
        [pos_x, pos_y] = addSegPoints(points, seg, pos_x, pos_y)

        length = int(seg[1:])
        if points[point[0], point[1]] == 1:
            direction = seg[0]
            if direction == 'U':
                steps += abs(pos_y - length - point[1])
            if direction == 'D':
                steps += abs(pos_y + length - point[1])
            if direction == 'L':
                steps += abs(pos_x + length - point[0])
            if direction == 'R':
                steps += abs(pos_x - length + point[0])
            break
        else:
            steps += length
    return steps

def getMatchingIdxs(paths, start_pos_x, start_pos_y, pts_0, pts_1):
    pos_x_0 = start_pos_x
    pos_y_0 = start_pos_y
    pos_x_1 = start_pos_x
    pos_y_1 = start_pos_y

    for seg_cnt in range(0, min([len(paths[0]), len(paths[1])])):
        seg_0 = paths[0][seg_cnt]
        seg_1 = paths[1][seg_cnt]

        [pos_x_0, pos_y_0] = addSegPoints(pts_0, seg_0, pos_x_0, pos_y_0)
        [pos_x_1, pos_y_1] = addSegPoints(pts_1, seg_1, pos_x_1, pos_y_1)

    matching_pts = pts_0 == pts_1
    matching_idxs = np.nonzero(matching_pts)
    return matching_idxs

def getClosestIntersect(dists):
    manhatten_dists = np.add(abs(match_cpy[0]), abs(match_cpy[1]))
    subset_idx = np.argmin(manhatten_dists[np.nonzero(manhatten_dists)])
    parent_idx = np.arange(manhatten_dists.shape[0])[np.nonzero(manhatten_dists)][subset_idx]
    intersect_pt = [matching_idxs[0][parent_idx], matching_idxs[1][parent_idx]]
    return intersect_pt

def main(filename):
    #paths = helper.getInputArr(filename, 2)
    paths = []
    #paths.append('R8,U5,L5,D3'.split(','))
    #paths.append('U7,R6,D4,L4'.split(','))

    paths.append('L3,D3,R3,D20'.split(','))
    paths.append('U1,L2,D4,R5'.split(','))

    [min_x, max_x, min_y, max_y] = getMaxes(paths)

    pts_0 = np.zeros((max_x - min_x, max_y - min_y))
    pts_1 = pts_0.copy() - 1

    start_pos_x = abs(min_x)
    start_pos_y = abs(min_y)

    addPathPoints(paths[0], pts_0, start_pos_x, start_pos_y)
    addPathPoints(paths[1], pts_1, start_pos_x, start_pos_y)

    matching_pts = pts_0 == pts_1
    matching_idxs = np.nonzero(matching_pts)

    manhattan_dist = abs(matching_idxs[0] - start_pos_x) + abs(matching_idxs[1] - start_pos_y)
    manhattan_dist = manhattan_dist.astype('float')
    manhattan_dist[manhattan_dist == 0] = 'nan' #convert 0s to nan
    min_dist = np.nanmin(manhattan_dist)
    
    #print(min_dist)

    #Part 2
    pts_0 = np.zeros((max_x - min_x, max_y - min_y))
    pts_1 = pts_0.copy() - 1

    matching_idxs = getMatchingIdxs(paths, start_pos_x, start_pos_y, pts_0, pts_1)
    #intersect_pt = getClosestIntersect(matching_idxs)  

    distsToIntersect = []
    for pt in range(len(matching_idxs[0])):
        if matching_idxs[0][pt]==0 and matching_idxs[1][pt]==0:
            continue

        intersect_pt = [matching_idxs[0][pt], matching_idxs[1][pt]]

        steps_1 = getStepsToPoint(paths[0], np.zeros((max_x - min_x, max_y - min_y)), start_pos_x, start_pos_y, intersect_pt)
        steps_2 = getStepsToPoint(paths[1], np.zeros((max_x - min_x, max_y - min_y)), start_pos_x, start_pos_y, intersect_pt)

        distsToIntersect.append(steps_1 + steps_2)

    print(np.min(distsToIntersect))

if __name__ == "__main__":
    main('Day3/day3input.txt')