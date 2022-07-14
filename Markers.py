import cv2
from cv2 import aruco
import imutils
from droneblocksutils.aruco_utils import detect_markers_in_image, detect_distance_from_image_center

    drone.streamon()
    time.sleep(4)
    while True:
        image=drone.get_frame_read().frame
        cv2.imshow("Feedback",image)
        image, marker_details = detect_markers_in_image(image, draw_center=True,
                                                        draw_reference_corner=True,
                                                        target_id=None,
                                                        draw_target_id=True,
                                                        draw_border=True)

if__name__ = '__main__':