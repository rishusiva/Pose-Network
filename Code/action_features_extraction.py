from modules import *
from MP_holistic_styled_landmarks import mp_holistic, draw_styled_landmarks
from folder_setup import *
from mediapipe_detection import mediapipe_detection
from keypoints_extraction import extract_keypoints


cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

    for action in actions:
        for sequence in range(number_sequences):
            for frame_num in range(sequence_length):

                
                ret, frame = cap.read()
                image, results = mediapipe_detection(frame, holistic)
                draw_styled_landmarks(image, results)
                
                # Wait 
                if frame_num == 0: 
                    cv2.putText(image, 'START NEW ACTION', (120,200), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                    cv2.imshow('Action Detection', image)
                    cv2.waitKey(2000)
                else: 
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                    cv2.imshow('Action Detection', image)
                

                keypoints = extract_keypoints(results)
                keypoint_path = os.path.join(DATA_PATH, action, str(sequence), str(frame_num))
                np.save(keypoint_path, keypoints)


                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                    
    cap.release()
    cv2.destroyAllWindows()


