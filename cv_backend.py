import cv2
import mediapipe as mp
import math
import serial
import time

WIDTH = 128
HEIGHT = 128
FPS = 2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc("M", "J", "P", "G"))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)


def get_hand_state():
    """Return the hand state as a binary integer"""

    counter = 0

    wrstxC = 0
    wrstyC = 0
    thmkxC = 0
    thmkyC = 0
    thmxC = 0
    thmyC = 0
    indxC = 0
    indyC = 0
    midxC = 0
    midyC = 0
    rngxC = 0
    rngyC = 0
    pnkxC = 0
    pnkyC = 0
    knixC = 0
    kniyC = 0
    knmxC = 0
    knmyC = 0
    knrxC = 0
    knryC = 0
    knpxC = 0
    knpyC = 0

    # cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
        model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5
    ) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            image_height, image_width, _ = image.shape

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS
                    )
                    # print(hand_landmarks.landmark[0])

                state = 31

                for ids, landmrk in enumerate(hand_landmarks.landmark):
                    if ids == 0:
                        wrstxC, wrstyC = (
                            landmrk.x * image_width,
                            landmrk.y * image_height,
                        )
                    elif ids == 1:
                        thmkxC, thmkyC = (
                            landmrk.x * image_width,
                            landmrk.y * image_height,
                        )
                    elif ids == 4:
                        thmxC, thmyC = landmrk.x * image_width, landmrk.y * image_height
                    elif ids == 5:
                        knixC, kniyC = landmrk.x * image_width, landmrk.y * image_height
                    elif ids == 8:
                        indxC, indyC = landmrk.x * image_width, landmrk.y * image_height
                    elif ids == 9:
                        knmxC, knmyC = landmrk.x * image_width, landmrk.y * image_height
                    elif ids == 12:
                        midxC, midyC = landmrk.x * image_width, landmrk.y * image_height
                    elif ids == 13:
                        knrxC, knryC = landmrk.x * image_width, landmrk.y * image_height
                    elif ids == 16:
                        rngxC, rngyC = landmrk.x * image_width, landmrk.y * image_height
                    elif ids == 17:
                        knpxC, knpyC = landmrk.x * image_width, landmrk.y * image_height
                    elif ids == 20:
                        pnkxC, pnkyC = landmrk.x * image_width, landmrk.y * image_height

                ind_disC = math.sqrt((indxC - wrstxC) ** 2 + (indyC - wrstyC) ** 2)
                mid_disC = math.sqrt((midxC - wrstxC) ** 2 + (midyC - wrstyC) ** 2)
                rng_disC = math.sqrt((rngxC - wrstxC) ** 2 + (rngyC - wrstyC) ** 2)
                pnk_disC = math.sqrt((pnkxC - wrstxC) ** 2 + (pnkyC - wrstyC) ** 2)

                thm_disC = math.sqrt((thmxC - knpxC) ** 2 + (thmyC - knpyC) ** 2) * 1.05
                thmk_disC = math.sqrt((thmkxC - knpxC) ** 2 + (thmkyC - knpyC) ** 2)

                kni_disC = math.sqrt((wrstxC - knixC) ** 2 + (wrstyC - kniyC) ** 2)
                knm_disC = math.sqrt((wrstxC - knmxC) ** 2 + (wrstyC - knmyC) ** 2)
                knr_disC = math.sqrt((wrstxC - knrxC) ** 2 + (wrstyC - knryC) ** 2)
                knp_disC = math.sqrt((wrstxC - knpxC) ** 2 + (wrstyC - knpyC) ** 2)

                if thm_disC < thmk_disC:
                    state -= 16
                    #print("thumb down")
                if ind_disC < kni_disC:
                    state -= 8
                    #print("index down")
                if mid_disC < knm_disC:
                    state -= 4
                    #print("middl down")
                if rng_disC < knr_disC:
                    state -= 2
                    #print("ring_ down")
                if pnk_disC < knp_disC:
                    #print("pinky down")
                    state -= 1

                # ind_ratC = math.sqrt((indxC-knixC)**2 + (indyC-kniyC)**2)/(math.sqrt((indxC-knixC)**2 + (indyC-kniyC)**2) + kni_disC)
                # mid_ratC = math.sqrt((midxC-knmxC)**2 + (midyC-knmyC)**2)/(math.sqrt((midxC-knmxC)**2 + (midyC-knmyC)**2) + knm_disC)
                # rng_ratC = math.sqrt((rngxC-knrxC)**2 + (rngyC-knryC)**2)/(math.sqrt((rngxC-knrxC)**2 + (rngyC-knryC)**2) + knr_disC)
                # pnk_ratC = math.sqrt((pnkxC-knpxC)**2 + (pnkyC-knpyC)**2)/(math.sqrt((pnkxC-knpxC)**2 + (pnkyC-knpyC)**2) + knp_disC)

                # Flip the image horizontally for a selfie-view display.
                #cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
                if cv2.waitKey(5) & 0xFF == ord("q"):
                    cap.release()

                return state


if __name__ == "__main__":
    ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
    ser.reset_input_buffer()
    print("started CV backend")
    while True:
        num = get_hand_state()
        num = num.to_bytes(1, "big")
        #print(num)
        ser.write(num)
        # line = ser.readline().decode('utf-8').rstrip()
        # print(line)
        # time.sleep(1)  