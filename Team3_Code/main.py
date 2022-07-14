# import math
from Path import *
import Move_Nextpt
# these are the files/ folders that this code is pulling into the main. So if i was to run main.py then the code that is in
#those pulled folders will also run and then come back and end back in main.

def main(filename):
            #this reads the waypoints in the Directions and Path folder
    waypoints = readWayPointFile(filename)

    print(Move_Nextpt.Path(waypoints[0], waypoints[1:]))
if __name__ == '__main__':
    main("waypoint.txt")