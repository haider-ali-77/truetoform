
import cv2
from .configs import KEYPOINT_EDGE_INDS_TO_COLOR


def draw_kp_on_image(img, kps, confidence=0.5, lines=True, lines_to_colors=KEYPOINT_EDGE_INDS_TO_COLOR):
    img = img.copy()
    point_shape = {'color':(0, 0, 255), 
                 'markerType':cv2.MARKER_CROSS, 
                 'markerSize':5, 
                 'thickness':2, 
                 'line_type':cv2.LINE_AA}
    for kp in kps:
        if kp[2] < confidence:
            continue
        img = cv2.drawMarker(
            img,
            tuple(kp[:2]),
        **point_shape
        )
    
    if lines:
        line_shape = {'thickness':5}
        for key, val in lines_to_colors.items():
            if kps[key[0], 2] >= confidence and kps[key[1], 2] > confidence:
                 img = cv2.line(img, tuple(kps[key[0], :2]), tuple(kps[key[1], :2]), color=val)
    return img

def rgb(img):
    return img[...,::-1]