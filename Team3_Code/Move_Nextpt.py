import Directions
def Path(home, Waypoints):
    Curr = home
    order = []
    while len(Waypoints) > 0:
        nextWp = Directions.next_point(Waypoints, Curr)
        Waypoints.remove(nextWp)
        order.append(nextWp)
        Curr = nextWp
    order.append(home)
    return order