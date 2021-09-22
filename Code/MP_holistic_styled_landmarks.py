from modules import *

mp_holistic = mp.solutions.holistic 
mp_drawing = mp.solutions.drawing_utils




def draw_styled_landmarks(image, results):

    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS, 
                             mp_drawing.DrawingSpec(color=(80,100,10), thickness=1, circle_radius=1), 
                             mp_drawing.DrawingSpec(color=(80,250,120), thickness=1, circle_radius=1)
                             ) 

    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(80,20,10), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(80,40,120), thickness=2, circle_radius=2)
                             ) 

    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(120,20,80), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(120,40,250), thickness=2, circle_radius=2)
                             ) 
  
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(250,120,70), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(250,70,230), thickness=2, circle_radius=2)
                             )