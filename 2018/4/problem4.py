import os

def createKey(timestamp):
    date = timestamp.split(' ')[0]
    date = date.replace('[', '')
    date_arr = date.split('-')
    year = int(date_arr[0])
    month = int(date_arr[1])
    day = int(date_arr[2])
    time = timestamp.split(' ')[1]
    time_arr = time.split(':')
    hour = int(time_arr[0])
    minute = int(time_arr[1])

    key = (minute * 100**0) + (hour * 100**1) + (day * 100**2) + (month * 100**3) + (year * 100**4)
    return key

def getSleepiestGuard(sorted_dict):
    sleep_dict = {}
    asleep_time = 0
    max_sleep_time = 0
    sleepiest_guard = -1
    for entry in sorted_dict:
        action = entry[1].split(' ') 
        if action[0] ==  'Guard':
            curr_guard = action[1].replace('#', '')
        elif action[0] == 'falls':
            asleep_time = entry[0]%100
        elif action[0] == 'wakes':
            wake_time = entry[0]%100
            time_sleeping = wake_time - asleep_time
            if curr_guard in sleep_dict:
                sleep_dict[curr_guard] += time_sleeping
            else:
                sleep_dict[curr_guard] = time_sleeping

            if sleep_dict[curr_guard] > max_sleep_time:
                max_sleep_time = sleep_dict[curr_guard]
                sleepiest_guard = curr_guard
    return sleepiest_guard

def getSleepistMinute(sleepiest_guard, sorted_dict):
    sleep_dict = {}
    minutes_asleep_dict = {}
    max_time = 0
    sleepiest_minute = -1
    for entry in sorted_dict:
        action = entry[1].split(' ') 
        if action[0] ==  'Guard':
            curr_guard = action[1].replace('#', '')
        elif action[0] == 'falls' and curr_guard == sleepiest_guard:
            asleep_time = entry[0]%100
        elif action[0] == 'wakes' and curr_guard == sleepiest_guard:
            wake_time = entry[0]%100
            for time in range(asleep_time, wake_time):
                if time in minutes_asleep_dict:
                    minutes_asleep_dict[time] += 1
                else:
                    minutes_asleep_dict[time] = 1
                
                if minutes_asleep_dict[time] > max_time:
                    max_time = minutes_asleep_dict[time]
                    sleepiest_minute = time
    return [sleepiest_minute, max_time]

def getGuards(sorted_dict):
    guards = set()
    for entry in sorted_dict:
        action = entry[1].split(' ') 
        if action[0] ==  'Guard':
            curr_guard = action[1].replace('#', '')
            if curr_guard not in guards:
                guards.add(curr_guard)
    return guards


def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    action_dict = {}
    
    for line in lines:
        timestamp = line.split('] ')[0]
        action = line.split('] ')[1]
        key = createKey(timestamp)
        action_dict[key] = action
    
    sorted_dict = sorted(action_dict.items())
    #sleepiest_guard = getSleepiestGuard(sorted_dict)
    #sleepiset_minute = getSleepistMinute(guard, sorted_dict)
    #print(int(sleepiest_guard) * sleepiest_minute)
    
    guards = getGuards(sorted_dict)
    max_guard = -1
    max_guard_time = -1
    max_sleepiest_minute = -1
    for guard in guards:
        [sleepiest_minute, max_time] = getSleepistMinute(guard, sorted_dict)
        if max_time > max_guard_time:
            max_guard_time = max_time
            max_guard = guard
            max_sleepiest_minute = sleepiest_minute
    print('guard = ' + max_guard)
    print('time = ' + str(max_sleepiest_minute))
    print(int(max_guard) * max_sleepiest_minute)

if __name__== "__main__":
    main()