import haversine as hs

def next_point(Waypoints, current):
    #Wp = Waypoints.copy()
 # this is only the copy of the Waypoints in the Def and because of this copy it can be used in the function below the one is def
 #is not being changed only the copy.
    #Wp =[]
    distList = []
    current = (current[1], current[2])
    for i in range(0,len(Waypoints)):
        Wp = (Waypoints[i][1], Waypoints[i][2])
        print(current)
        print(Wp, tuple(current))
        dist = hs.haversine(current,Wp, unit='ft')
        #
        distList.append(dist)
        #
    print(distList)
    minDist = min(distList)
    #This finds the minimum value and put it into the distList
    index = distList.index(minDist)
    #This would then find the index or the str in the distList that the minDist or the distance it is paralle to
    return Waypoints[index]