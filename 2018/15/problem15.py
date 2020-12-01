import os
from enum import Enum
import queue

class Path():
    def __init__(self, current_path_node):
        self.current_path_node = current_path_node
        self.path_dict = {}
        self.path_dict[self.getKey(current_path_node.loc)] = current_path_node
    
    def addPath(self, pathnode):   
        self.path_dict[self.getKey(pathnode.loc)] = pathnode
        self.current_path_node.addPath(pathnode)

    def setCurrentPath(self, loc):
        self.current_path_node = self.path_dict[self.getKey(loc)]
    
    def getKey(self, loc):
        s = [str(i) for i in loc]
        return "".join(s)


class PathNode():
    def __init__(self, loc):
        self.loc = loc
        self.children = []
        self.parent = None

    def addPath(self, pathnode):
        self.children.append(pathnode)
        pathnode.parent = self

    def getPenultimateNodeLoc(self):
        penultimate_node = self
        if penultimate_node.parent == None:
            return None
        
        while True:
            if penultimate_node.parent.parent == None:
                return penultimate_node.loc
            penultimate_node = penultimate_node.parent


class UnitType(Enum):
    Elf = 0
    Goblin = 1

class Unit():
    def __init__(self, unit_type):
        self.unit_type = unit_type
        self.health = 200
        self.attack = 3
        self.done = False

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'test.txt')
    f=open(my_file, "r")
    lines = f.readlines()

    [grid, units] = parseInput(lines)
    rounds = 0
    done = False

    while True:
        #if rounds > 140 or rounds < 5:
        print('round = ' + str(rounds))
        printGrid(grid, units)
        for y_loc in range(len(grid)):
            if done:
                break
            for x_loc in range(len(grid[y_loc])):
                obj = grid[y_loc][x_loc]
                if obj >= 0:
                    done = processUnit(grid, obj, units, x_loc, y_loc)
                    if done:
                        break

        if done:
            break                            
                                    
        for unit in units:
            unit.done = False
        rounds += 1

    printGrid(grid, units)
    print(getAnswer(grid, units, rounds))

def processUnit(grid, unit_id, units, x_loc, y_loc):
    unit = units[unit_id]
    done = False
    if unit.done or unit.health <= 0:
        return done
        
    unit.done = True
    [nearest_enemy_loc, step_loc] = getNearestEnemyLoc(grid, units, unit.unit_type, x_loc, y_loc)
    curr_y_loc = y_loc
    curr_x_loc = x_loc
    if step_loc is not None:
        grid[y_loc][x_loc] = -1
        curr_y_loc = step_loc[0]
        curr_x_loc = step_loc[1]
        grid[curr_y_loc][curr_x_loc] = unit_id
    victim_loc = getVictim(grid, curr_x_loc, curr_y_loc, units)
    if victim_loc is not None:
        victim = units[grid[victim_loc[0]][victim_loc[1]]]
        victim.health -= unit.attack
        if victim.health <= 0:
            done = victimDied(grid, units, victim_loc)
    return done

def victimDied(grid, units, victim_loc):
    victim = units[grid[victim_loc[0]][victim_loc[1]]]
    grid[victim_loc[0]][victim_loc[1]] = -1
    done = True
    for unit in units:
        if unit.health <= 0:
            continue
        if unit.unit_type == victim.unit_type:
            done = False
            break
    return done

def getAnswer(grid, units, rounds):
    total_health = 0
    for y_loc in range(len(grid)):
        for x_loc in range(len(grid[y_loc])):
            obj = grid[y_loc][x_loc]
            if obj >= 0:
                unit = units[obj]
                if unit.health > 0:
                    total_health += unit.health
    return str(total_health) + " " + str(rounds) + " " + str(total_health * rounds)


def printGrid(grid, units):
    for y_loc in range(len(grid)):
        row = ""
        append_row = ""
        for x_loc in range(len(grid)):
            if grid[y_loc][x_loc] == -2:
                row += "#"
            elif grid[y_loc][x_loc] == -1:
                row += "."
            elif grid[y_loc][x_loc] >= 0:
                unit = units[grid[y_loc][x_loc]]
                if unit.unit_type == UnitType.Elf:
                    row += "E"
                    append_row += " E(" + str(unit.health)  + "),"
                else:
                    row += "G"
                    append_row += " G(" + str(unit.health)  + "),"
        print(row + append_row)

def getVictim(grid, x_loc, y_loc, units):
    attacker = units[grid[y_loc][x_loc]]
    lowest_health = 999
    lowest_victim_loc = None
    
    if grid[y_loc-1][x_loc] >= 0:
        victim = units[grid[y_loc-1][x_loc]]
        if victim.health > 0 and not victim.unit_type == attacker.unit_type and victim.health < lowest_health:
            lowest_health = victim.health
            lowest_victim_loc = [y_loc-1, x_loc]
    if grid[y_loc][x_loc-1] >= 0:
        victim = units[grid[y_loc][x_loc-1]]
        if victim.health > 0 and not victim.unit_type == attacker.unit_type and victim.health < lowest_health:
            lowest_health = victim.health
            lowest_victim_loc = [y_loc, x_loc-1]
    if grid[y_loc][x_loc+1] >= 0:
        victim = units[grid[y_loc][x_loc+1]]
        if victim.health > 0 and not victim.unit_type == attacker.unit_type and victim.health < lowest_health:
            lowest_health = victim.health
            lowest_victim_loc = [y_loc, x_loc+1]
    if grid[y_loc+1][x_loc] >= 0:
        victim = units[grid[y_loc+1][x_loc]]
        if victim.health > 0 and not victim.unit_type == attacker.unit_type and victim.health < lowest_health:
            lowest_health = victim.health
            lowest_victim_loc = [y_loc+1, x_loc]

    return lowest_victim_loc

def getNearestEnemyLoc(grid, units, curr_unit_type, x_loc, y_loc):
    visited_grid=[[False for i in range(len(grid[y_loc]))] for j in range(len(grid))]
    q = queue.SimpleQueue()
    q.put_nowait([y_loc, x_loc])
    path = Path(PathNode([y_loc, x_loc]))
    step_loc = None
    while True:
        if q.empty():
            break

        [curr_y_loc, curr_x_loc] = q.get_nowait()
        visited_grid[curr_y_loc][curr_x_loc] = True
        path.setCurrentPath([curr_y_loc, curr_x_loc])
        
        nearest_enemy_loc = checkLoc(grid, units, curr_unit_type, q, visited_grid, curr_x_loc, curr_y_loc-1, path)
        if nearest_enemy_loc is not None:
            step_loc = path.current_path_node.getPenultimateNodeLoc()
            break

        nearest_enemy_loc = checkLoc(grid, units, curr_unit_type, q, visited_grid, curr_x_loc-1, curr_y_loc, path)
        if nearest_enemy_loc is not None:
            step_loc = path.current_path_node.getPenultimateNodeLoc()
            break

        nearest_enemy_loc = checkLoc(grid, units, curr_unit_type, q, visited_grid, curr_x_loc+1, curr_y_loc, path)
        if nearest_enemy_loc is not None:
            step_loc = path.current_path_node.getPenultimateNodeLoc()
            break

        nearest_enemy_loc = checkLoc(grid, units, curr_unit_type, q, visited_grid, curr_x_loc, curr_y_loc+1, path)
        if nearest_enemy_loc is not None:
            step_loc = path.current_path_node.getPenultimateNodeLoc()
            break

    return [nearest_enemy_loc, step_loc]
    

def checkLoc(grid, units, curr_unit_type, q, visited_grid, x_loc, y_loc, path):
    if visited_grid[y_loc][x_loc] == False:
        obj = grid[y_loc][x_loc]
        if obj == -1:
            path.addPath(PathNode([y_loc, x_loc]))
            if adjacentToEnemy(grid, units, curr_unit_type, x_loc, y_loc):
                path.setCurrentPath([y_loc, x_loc])
                return [y_loc, x_loc]
            else:
                q.put_nowait([y_loc, x_loc])
                visited_grid[y_loc][x_loc] = True
        #else do nothing because this is a wall
    return None

def adjacentToEnemy(grid, units, curr_unit_type, x_loc, y_loc):
    if grid[y_loc-1][x_loc] > 0 and units[grid[y_loc-1][x_loc]].health > 0 and units[grid[y_loc-1][x_loc]].unit_type != curr_unit_type:
        return True
    if grid[y_loc][x_loc-1] > 0 and units[grid[y_loc][x_loc-1]].health > 0 and units[grid[y_loc][x_loc-1]].unit_type != curr_unit_type:
        return True
    if grid[y_loc][x_loc+1] > 0 and units[grid[y_loc][x_loc+1]].health > 0 and units[grid[y_loc][x_loc+1]].unit_type != curr_unit_type:
        return True
    if grid[y_loc+1][x_loc] > 0 and units[grid[y_loc+1][x_loc]].health > 0 and units[grid[y_loc+1][x_loc]].unit_type != curr_unit_type:
        return True
    return False

def parseInput(lines):
    units = []
    grid = []
    for line in lines:
        row = []
        for char in line:
            if char == '#':
                row.append(-2)
            elif char == '.':
                row.append(-1)
            elif char == 'E':
                row.append(len(units))
                units.append(Unit(UnitType.Elf))
            elif char == 'G':
                row.append(len(units))
                units.append(Unit(UnitType.Goblin))
        grid.append(row)
    return [grid, units]


if __name__== "__main__":
    main()
