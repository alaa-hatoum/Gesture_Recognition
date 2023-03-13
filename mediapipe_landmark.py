import cv2
import mediapipe as mp
import math
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
counter = 0
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened() and  counter<=100:
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
    
    wrstx= [] 
    wrsty =[]
    thmx=[]
    thmy=[]
    indx=[]
    indy=[]
    midx=[]
    midy=[]
    rngx=[]
    rngy=[]
    pnkx=[]
    pnky = []
    knix = []
    kniy = []
    knmx = []
    knmy = []
    knrx = []
    knry = []
    knpx = []
    knpy = []
    wrstxi=wrstyi=thmxi=thmyi=indxi=indyi=midxi=midyi=rngxi=rngyi=pnkxi=pnkyi = 0
    image_height, image_width, _ = image.shape

    if results.multi_hand_landmarks :
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS)
        #print(hand_landmarks.landmark[0])
      for ids, landmrk in enumerate(hand_landmarks.landmark):
        if ids == 0:
            wrstxi,wrstyi = landmrk.x * image_width, landmrk.y*image_height
            wrstx.append(wrstxi)
            wrsty.append(wrstyi)
        elif ids == 4:
            thmxi,thmyi = landmrk.x * image_width, landmrk.y*image_height
            thmx.append(thmxi)
            thmy.append(thmyi)
        elif ids == 5:
            knixi,kniyi = landmrk.x * image_width, landmrk.y*image_height
            knix.append(knixi)
            kniy.append(knixi)
        elif ids == 8:
            indxi, indyi = landmrk.x * image_width, landmrk.y*image_height
            indx.append(indxi)
            indy.append(indyi)
        elif ids == 9:
            knmxi,knmyi = landmrk.x * image_width, landmrk.y*image_height
            knmx.append(knmxi)
            knmy.append(knmyi)
        elif ids == 12:
            midxi, midyi = landmrk.x * image_width, landmrk.y*image_height
            midx.append(midxi)
            midy.append(midyi)
        elif ids == 13:
            knrxi,knryi = landmrk.x * image_width, landmrk.y*image_height
            knrx.append(knrxi)
            knry.append(knryi)
        elif ids == 16:
            rngxi,rngyi = landmrk.x * image_width, landmrk.y*image_height
            rngx.append(rngxi)
            rngy.append(rngyi)
        elif ids == 17:
            knpxi,knpyi = landmrk.x * image_width, landmrk.y*image_height
            knpx.append(knpxi)
            knpy.append(knpyi)
        elif ids == 20:
            pnkxi, pnkyi = landmrk.x * image_width, landmrk.y*image_height
            pnkx.append(pnkxi)
            pnky.append(pnkyi)         
    counter += 1      
    
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == ord("q"):
      break
cap.release()

wrstx = sum(wrstx)/len(wrstx)
wrsty = sum(wrsty)/len(wrsty)
thmx = sum(thmx)/len(thmx)
thmy = sum(thmy)/len(thmy)
indx = sum(indx)/len(indx)
indy = sum(indy)/len(indy)
midx = sum(midx)/len(midx)
midy = sum(midy)/len(midy)
rngx = sum(rngx)/len(rngx)
rngy = sum(rngy)/len(rngy)
pnkx = sum(pnkx)/len(pnkx)
pnky = sum(pnky)/len(pnky)
knix = sum(knix)/len(knix)
kniy = sum(kniy)/len(kniy)
knmx = sum(knmx)/len(knmx)
knmy = sum(knmy)/len(knmy)
knrx = sum(knrx)/len(knrx)
knry = sum(knry)/len(knry)
knpx = sum(knpx)/len(knpx)
knpy = sum(knpy)/len(knpy)

ind_rat = math.sqrt((indx-knix)**2 + (indy-kniy)**2)/(math.sqrt((indx-knix)**2 + (indy-kniy)**2) + math.sqrt((wrstx-knix)**2 + (wrsty-kniy)**2))
mid_rat = math.sqrt((midx-knmx)**2 + (midy-knmy)**2)/(math.sqrt((midx-knmx)**2 + (midy-knmy)**2) + math.sqrt((wrstx-knmx)**2 + (wrsty-knmy)**2))
rng_rat = math.sqrt((rngx-knrx)**2 + (rngy-knry)**2)/(math.sqrt((rngx-knrx)**2 + (rngy-knry)**2) + math.sqrt((wrstx-knrx)**2 + (wrsty-knry)**2))
pnk_rat = math.sqrt((pnkx-knpx)**2 + (pnky-knpy)**2)/(math.sqrt((pnkx-knpx)**2 + (pnky-knpy)**2) + math.sqrt((wrstx-knpx)**2 + (wrsty-knpy)**2))


print(ind_rat)
print(mid_rat)
print(rng_rat)
print(pnk_rat)

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
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

    if results.multi_hand_landmarks :
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS)
        #print(hand_landmarks.landmark[0])
      for ids, landmrk in enumerate(hand_landmarks.landmark):
        if ids == 0:
            wrstx,wrsty = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 4:
            thmx,thmy = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 5:
            knix,kniy = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 8:
            indx, indy = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 9:
            knmx,knmy = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 12:
            midx, midy = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 13:
            knrx,knry = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 16:
            rngx,rngy = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 17:
            knpx,knpy = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 20:
            pnkx, pnky = landmrk.x * image_width, landmrk.y*image_height
            
        ind_dis = math.sqrt((indx-wrstx)**2 + (indy-wrsty)**2)
        mid_dis = math.sqrt((midx-wrstx)**2 + (midy-wrsty)**2)
        rng_dis = math.sqrt((rngx-wrstx)**2 + (rngy-wrsty)**2)
        pnk_dis = math.sqrt((pnkx-wrstx)**2 + (pnky-wrsty)**2)
        
        kni_dis = math.sqrt((wrstx-knix)**2 + (wrsty-kniy)**2)
        knm_dis = math.sqrt((wrstx-knmx)**2 + (wrsty-knmy)**2)
        knr_dis = math.sqrt((wrstx-knrx)**2 + (wrsty-knry)**2)
        knp_dis = math.sqrt((wrstx-knpx)**2 + (wrsty-knpy)**2)
        
        if ind_dis<kni_dis:
          print("index fully bent")
        if mid_dis<knm_dis:
          print("middle finger fully bent")
        if rng_dis<knr_dis:
          print("ring finger fully bent")      
        if pnk_dis<knp_dis:
          print("pinky finger fully bent")
          
             
        ind_rat = math.sqrt((indx-knix)**2 + (indy-kniy)**2)/(math.sqrt((indx-knix)**2 + (indy-kniy)**2) + kni_dis)
        mid_rat = math.sqrt((midx-knmx)**2 + (midy-knmy)**2)/(math.sqrt((midx-knmx)**2 + (midy-knmy)**2) + knm_dis)
        rng_rat = math.sqrt((rngx-knrx)**2 + (rngy-knry)**2)/(math.sqrt((rngx-knrx)**2 + (rngy-knry)**2) + knr_dis)
        pnk_rat = math.sqrt((pnkx-knpx)**2 + (pnky-knpy)**2)/(math.sqrt((pnkx-knpx)**2 + (pnky-knpy)**2) + knp_dis)

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == ord("q"):
      break
cap.release()