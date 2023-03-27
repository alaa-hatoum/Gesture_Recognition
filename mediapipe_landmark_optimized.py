import cv2
import mediapipe as mp
import math
import numpy as np
from picamera2 import Picamera2


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

counter = 0
# with mp_hands.Hands(
#     model_complexity=0,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as hands:
#   while cap.isOpened() and  counter<=100:
#     success, image = cap.read()
#     if not success:
#       print("Ignoring empty camera frame.")
#       # If loading a video, use 'break' instead of 'continue'.
#       continue

#     # To improve performance, optionally mark the image as not writeable to
#     # pass by reference.
#     image.flags.writeable = False
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = hands.process(image)

#     # Draw the hand annotations on the image.
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
#     wrstx= 0 
#     wrsty= 0
#     thmx=0
#     thmy=0
#     indx=0
#     indy=0
#     midx=0
#     midy=0
#     rngx=0
#     rngy=0
#     pnkx=0
#     pnky = 0
#     knix = 0
#     kniy = 0
#     knmx = 0
#     knmy = 0
#     knrx = 0
#     knry = 0
#     knpx = 0
#     knpy = 0
#     wrstxi=wrstyi=thmxi=thmyi=indxi=indyi=midxi=midyi=rngxi=rngyi=pnkxi=pnkyi = knixi = kniyi = knmxi = knmyi= knrxi =knryi = knpxi = knpyi = 0
#     image_height, image_width, _ = image.shape

#     if results.multi_hand_landmarks :
#       for hand_landmarks in results.multi_hand_landmarks:
#         mp_drawing.draw_landmarks(
#             image,
#             hand_landmarks,
#             mp_hands.HAND_CONNECTIONS)
#         #print(hand_landmarks.landmark[0])
#       for ids, landmrk in enumerate(hand_landmarks.landmark):
#         if ids == 0:
#             wrstx+= landmrk.x * image_width
#             wrsty+= landmrk.y*image_height
#             wrstxi+=1
#             wrstyi+=1
#         elif ids == 4:
#             thmx +=landmrk.x * image_width
#             thmy += landmrk.y*image_height
#             thmxi+=1
#             thmyi+=1
#         elif ids == 5:
#             knix +=landmrk.x * image_width
#             kniy += landmrk.y*image_height
#             knixi+=1
#             kniyi+=1
#         elif ids == 8:
#             indx +=landmrk.x * image_width
#             indy += landmrk.y*image_height
#             indxi+=1
#             indyi+=1 
#         elif ids == 9:
#             knmx +=landmrk.x * image_width
#             knmy += landmrk.y*image_height
#             knmxi+=1
#             knmyi+=1 
#         elif ids == 12:
#             midx +=landmrk.x * image_width
#             midy += landmrk.y*image_height
#             midxi+=1
#             midyi+=1 
#         elif ids == 13:
#             knrx +=landmrk.x * image_width
#             knry += landmrk.y*image_height
#             knrxi+=1
#             knryi+=1
#         elif ids == 16:
#             rngx +=landmrk.x * image_width
#             rngy += landmrk.y*image_height
#             rngxi+=1
#             rngyi+=1
#         elif ids == 17:
#             knpx +=landmrk.x * image_width
#             knpy += landmrk.y*image_height
#             knpxi+=1
#             knpyi+=1
#         elif ids == 20:
#             pnkx +=landmrk.x * image_width
#             pnky += landmrk.y*image_height
#             pnkxi+=1
#             pnkyi+=1          
#     counter += 1      
    
#     # Flip the image horizontally for a selfie-view display.
#     cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
#     if cv2.waitKey(5) & 0xFF == ord("q"):
#       break
# cap.release()

# wrstx =   wrstx/wrstxi  
# wrsty =   wrsty/wrstyi  
# thmx =   thmx/thmxi  
# thmy =   thmy/thmyi  
# indx =   indx/indxi  
# indy =   indy/indyi  
# midx =   midx/midxi  
# midy =   midy/midyi  
# rngx =   rngx/rngxi  
# rngy =   rngy/rngyi  
# pnkx =   pnkx/pnkxi  
# pnky =   pnky/pnkyi  
# knix =   knix/knixi  
# kniy =   kniy/kniyi  
# knmx =   knmx/knmxi  
# knmy =   knmy/knmyi  
# knrx =   knrx/knrxi  
# knry =   knry/knryi  
# knpx =   knpx/knpxi  
# knpy =   knpy/knpyi  

# ind_dis = math.sqrt((indx-wrstx)**2 + (indy-wrsty)**2)
# mid_dis = math.sqrt((midx-wrstx)**2 + (midy-wrsty)**2)
# rng_dis = math.sqrt((rngx-wrstx)**2 + (rngy-wrsty)**2)
# pnk_dis = math.sqrt((pnkx-wrstx)**2 + (pnky-wrsty)**2)

# kni_dis = math.sqrt((wrstx-knix)**2 + (wrsty-kniy)**2)
# knm_dis = math.sqrt((wrstx-knmx)**2 + (wrsty-knmy)**2)
# knr_dis = math.sqrt((wrstx-knrx)**2 + (wrsty-knry)**2)
# knp_dis = math.sqrt((wrstx-knpx)**2 + (wrsty-knpy)**2)

# ind_rat = math.sqrt((indx-knix)**2 + (indy-kniy)**2)/(math.sqrt((indx-knix)**2 + (indy-kniy)**2) + kni_dis)
# mid_rat = math.sqrt((midx-knmx)**2 + (midy-knmy)**2)/(math.sqrt((midx-knmx)**2 + (midy-knmy)**2) + knm_dis)
# rng_rat = math.sqrt((rngx-knrx)**2 + (rngy-knry)**2)/(math.sqrt((rngx-knrx)**2 + (rngy-knry)**2) + knr_dis)
# pnk_rat = math.sqrt((pnkx-knpx)**2 + (pnky-knpy)**2)/(math.sqrt((pnkx-knpx)**2 + (pnky-knpy)**2) + knp_dis)

# print(ind_rat)
# print(mid_rat)
# print(rng_rat)
# print(pnk_rat)

wrstxC= 0 
wrstyC= 0
thmkxC = 0 
thmkyC = 0
thmxC=0
thmyC=0
indxC=0
indyC=0
midxC=0
midyC=0
rngxC=0
rngyC=0
pnkxC=0
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
          wrstxC  ,wrstyC = landmrk.x * image_width, landmrk.y*image_height    
        elif ids == 1:
          thmkxC, thmkyC = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 4:
          thmxC,thmyC = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 5:
          knixC,kniyC = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 8:
          indxC, indyC = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 9:
          knmxC,knmyC = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 12:
          midxC, midyC = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 13:
          knrxC,knryC = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 16:
          rngxC,rngyC = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 17:
          knpxC,knpyC = landmrk.x * image_width, landmrk.y*image_height
        elif ids == 20:
          pnkxC, pnkyC = landmrk.x * image_width, landmrk.y*image_height
            
        ind_disC = math.sqrt((indxC-wrstxC  )**2 + (indyC-wrstyC)**2)
        mid_disC = math.sqrt((midxC-wrstxC  )**2 + (midyC-wrstyC)**2)
        rng_disC = math.sqrt((rngxC-wrstxC  )**2 + (rngyC-wrstyC)**2)
        pnk_disC = math.sqrt((pnkxC-wrstxC  )**2 + (pnkyC-wrstyC)**2)
        
        thm_disC = math.sqrt((thmxC - knpxC)**2 + (thmyC - knpyC)**2)*1.25
        thmk_disC = math.sqrt((thmkxC - knpxC)**2 + (thmkyC - knpyC)**2)
        
        kni_disC = math.sqrt((wrstxC  -knixC)**2 + (wrstyC-kniyC)**2)
        knm_disC = math.sqrt((wrstxC  -knmxC)**2 + (wrstyC-knmyC)**2)
        knr_disC = math.sqrt((wrstxC-knrxC)**2 + (wrstyC-knryC)**2)
        knp_disC = math.sqrt((wrstxC-knpxC)**2 + (wrstyC-knpyC)**2)
        
        if ind_disC<kni_disC:
          print("index fully bent")
        if mid_disC<knm_disC:
          print("middle finger fully bent")
        if rng_disC<knr_disC:
          print("ring finger fully bent")      
        if pnk_disC<knp_disC:
          print("pinky finger fully bent")
        if thm_disC<thmk_disC:
          print("thumb is fully bent")
          
             
        ind_ratC = math.sqrt((indxC-knixC)**2 + (indyC-kniyC)**2)/(math.sqrt((indxC-knixC)**2 + (indyC-kniyC)**2) + kni_disC)
        mid_ratC = math.sqrt((midxC-knmxC)**2 + (midyC-knmyC)**2)/(math.sqrt((midxC-knmxC)**2 + (midyC-knmyC)**2) + knm_disC)
        rng_ratC = math.sqrt((rngxC-knrxC)**2 + (rngyC-knryC)**2)/(math.sqrt((rngxC-knrxC)**2 + (rngyC-knryC)**2) + knr_disC)
        pnk_ratC = math.sqrt((pnkxC-knpxC)**2 + (pnkyC-knpyC)**2)/(math.sqrt((pnkxC-knpxC)**2 + (pnkyC-knpyC)**2) + knp_disC)

    # Flip the image horizontally for a selfie-view display.
    # cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == ord("q"):
      break
cap.release()