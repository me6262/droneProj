import os
import sys

# EX file waypoint = 42.35893N 54.9280E 10  H
#                    Lat.      Lon.    Alt.  Type
# Output: H 42.35893, 54.928, 10
#       type   Lat.   Lon.    Alt.
# also a converson process that turns the numbers into a seires of strings that are sorted in a list
def readWayPointFile(filename):
        Wps = []
        # this is the end point of how the waypoints will end in a bigger list
        with open(filename, "r") as Wp:
            for line in Wp:
                line = line.strip()
               # print(line) << same as the bottom one # this gets rid of the black and not needed spaces in the line. aka a trim
                temp  = line.split(" ")
                #print(temp) << we used it to check an error #it takes the a bigger string splitting it into
                # sub strings and then putting it in a list.
                Curr_Wp = []
                Curr_Wp.append(temp[5])
                # this is how we turned the waypoints into a list that we can pull/use out of. and then temp[]
                # is where we take an element in the list so it can be used.
               # temp[0] = temp[0].removesuffix("N")
               # temp[1] = temp[1].removesuffix("E")
                # I removed the suffix at the end of the coordinates # this has been commented out because if the letter variable is not spaced out
                Curr_Wp.append(float(temp[0]))
                Curr_Wp.append(float(temp[2]))
                Curr_Wp.append(float(temp[4]))
                # then we organized the series of strings into the order that we want it to be which is the
                # lable first and then the points
                Wps.append(Curr_Wp)
                #This is how it transfers all of the sorted waypoints in the [] that was stated at the begining of the code
            print(Wps)
        return Wps

readWayPointFile("waypoint.txt")
# the file that the whole code is reading from