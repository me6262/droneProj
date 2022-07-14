from djitellopy import Tello
import time
import cv2
from droneblocksutils.aruco_utils import detect_markers_in_image,detect_distance_from_image_center


def main():
    fly=True
    completed = False
    drone = Tello()
    drone.connect()
    if fly==True:
        drone.takeoff()
    drone.streamon()
    time.sleep(6)
    while not completed:
        time.sleep(1/30)
        if fly:
            def
            image = drone.get_frame_read().frame
            image, marker_details = detect_markers_in_image(image, draw_center=True,
                                                            draw_reference_corner=False,
                                                            target_id=None,
                                                            draw_target_id=True,
                                                            draw_border=False)
             #this just means if a marker is detected aka if something is detected.
            if len(marker_details)!=0:
                #markdeets is the x and y of the ArucoMarker position.
                # x is index 0, y is index 1.
                markdeets=marker_details[0][0]
                center_x=markdeets[0]
                center_y=markdeets[1]

                founddist=detect_distance_from_image_center(image,center_x,center_y)
                image, x_distance, y_distance, distance = founddist
                if center_y<0:
                    drone.rotate_counter_clockwise(5)






                cv2.imshow("Feedback", image)
            if cv2.waitKey(1) & 0xFF == ord('v'):
                if fly==True:
                    drone.land()
                break
    drone.streamoff()


if __name__ == "__main__":
    main()
