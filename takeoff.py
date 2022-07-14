from droneblocks.DroneBlocksTello import DroneBlocksTello

tello = DroneBlocksTello()

tello.connect()
tello.takeoff()

tello.move_up(100)
tello.rotate_counter_clockwise(90)
tello.move_forward(100)

tello.land()