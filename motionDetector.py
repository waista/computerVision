import cv2
import numpy as np

buffer_size = 5
alarm_threshold = 200

def save_webcam(outPath, fps, mirror=False):
    buffer = []
    # Capturing video from webcam:
    cap = cv2.VideoCapture(0)
    currentFrame = 0
    # Get current width of frame
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # float
    # Get current height of frame
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(outPath, fourcc, fps, (int(width), int(height)))
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            if mirror == True:
                # Mirror the output video frame
                frame = cv2.flip(frame, 1)
                # Saves for video
                out.write(frame)
                # Display the resulting frame
                cv2.imshow('frame', frame)
                if len(buffer) <= buffer_size :
                    buffer.append(frame)
                else:
                    process_frames(buffer)
                    buffer = []
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # if 'q' is pressed then quit
            break
        # To stop duplicate images
        currentFrame += 1
    # When everything done, release the capture
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def process_frames(frames):
    average = cv2.absdiff(frames[0], frames[1])
    for i in [1,len(frames)-1]:
        average += cv2.absdiff(frames[0], frames[i])
    cv2.imshow("bonjour", average)
    average = average / buffer_size
    hist, bins = np.histogram(average.ravel(), 25, [5, 25])
    change_level = np.mean(hist)
    if change_level > alarm_threshold:
        print("alert ! movement !")
    else:
        print(".")

def main():
    save_webcam('output.avi', 30.0, mirror=True)

if __name__ == '__main__':
    main()