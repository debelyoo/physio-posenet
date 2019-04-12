import numpy as np
import cv2
import time
import subprocess
import os
import ast
import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        start3 = time.time()
        #time.sleep(5)
        start4 = time.time()
        comma2="sshpass -p Avalls2018bcn scp -c arcfour ./sample.jpeg Avalls2018bcn@azure.rabbyte.club:~/perceive2perfect/OpenPose/sample.jpeg"
        subprocess.call(comma2, shell=True)
        done4 = time.time()
        elapsed4 = done4 - start4
        print("Temps pujar imatge: ")
        print(elapsed4)

        start5 = time.time()
        comma="ssh -S ctrl-socket Avalls2018bcn@azure.rabbyte.club -t 'cd perceive2perfect/OpenPose/ && python OpenPoseImage.py > Output-Keypoints.txt && cat Output-Keypoints.txt | sed -n 2p ' < echo"
        result = subprocess.check_output(comma, shell=True)
        done5 = time.time()
        elapsed5 = done5 - start5
        print("Temps processar imatge: ")
        print(elapsed5)
        #escriure a fitxer
        start6 = time.time()
        objecte = open("Output_Keypoints.txt", "w")
        objecte.write(result)
        objecte.close()
        done6 = time.time()
        elapsed6 = done6 - start6
        print("Temps escriure al fitxer: ")
        print(elapsed6)


        done3 = time.time()
        elapsed3 = done3 - start3
        print("Temps del thread: ")
        print(elapsed3)

        


def Compare_Skeletons(points):
    INF = 1000000

    POSE_PAIRS_ORIGINAL = [[0, 1], [1, 2], [2, 3], [3, 4], [1, 5], [5, 6], [6, 7], [1, 14], [14, 8], [8, 9], [9, 10], [14, 11], [11, 12], [12, 13]]
    

   # Connected nodes information to check
    POSE_PAIRS = [[8, 9], [11, 12], [9, 10], [12, 13], [1, 14], [2, 3], [5, 6], [3, 4], [6, 7], [0, 1]]

    # Messages acording to area
    messages = {0: "Move your head",
                2: "Move your right elbow",
                3: "Move your right hand",
                5: "Move your left elbow", 
                6: "Move your left hand",
                1: "Move your brust",
                8: "Move your right knee",
                9: "Move your right feet",
                11: "Move your left knee",
                12: "Move your left feet"}


    def get_angle(p0, p1, p2):
        v0 = np.array(p0) - np.array(p1)
        v1 = np.array(p2) - np.array(p1)
        angle = np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1))
        return np.degrees(angle)

    def get_axis(p0, p1, p2):
        v0 = np.array(p0) - np.array(p1)
        v1 = np.array(p2) - np.array(p1)
        v2 = v0 + v1
        return v2[1]/v2[0]

    # 0
    #points_1 = [(205, 93), (205, 160), (166, 160), (146, 93), (195, 40), (244, 174), (273, 93), (225, 40), (185, 334), (195, 441), (215, 549), (234, 321), (332, 374), (225, 374), (205, 254)]

    # Aleix
    #points_2 = [(208, 73), (208, 125), (166, 125), (153, 83), (194, 41), (236, 125), (250, 83), (208, 41), (194, 229), (222, 333), (236, 406), (236, 219), (306, 250), (250, 313), (208, 177)]

    # 1
    #points_1 = [(205, 182), (205, 243), (171, 259), (182, 182), (194, 106), (240, 259), (240, 182), (217, 121), (194, 396), (205, 487), (228, 579), (251, 380), (331, 426), (240, 426), (217, 320)]

    # 3
    #points_2 = [(146, 110), (146, 165), (124, 187), (139, 110), (139, 66), (176, 176), (169, 110), (154, 66), (139, 286), (146, 374), (154, 451), (176, 275), (235, 319), (169, 308), (154, 231)]

    # Aleix1
    #points_1 =  [(250, 62), (250, 114), (208, 135), (153, 156), (166, 208), (278, 156), (278, 198), (292, 219), (222, 240), (222, 333), (236, 406), (264, 229), (333, 260), (278, 333), (236, 187)]

    # Aleix6
    #points_2 =  [(180, 62), (194, 114), (153, 146), (111, 187), (69, 229), (236, 135), (264, 177), (292, 219), (222, 240), (222, 333), (236, 406), (264, 229), (320, 229), (389, 271), (222, 187)]

    # Aleix7
    points_1 =  [(236, 62), (236, 114), (208, 146), (194, 198), (194, 250), (278, 135), (292, 198), (292, 250), (222, 250), (236, 323), (236, 406), (264, 250), (264, 323), (278, 406), (250, 198)]

    # Aleix9
    #points_2 =  [(264, 73), (250, 114), (222, 135), (194, 198), (194, 250), (278, 146), (292, 198), (292, 250), (222, 250), (236, 323), (236, 406), (264, 250), (264, 323), (278, 406), (250, 198)]

    # Aleix10
    points_2 =  [(166, 52), (180, 104), (153, 135), (125, 198), (97, 250), (222, 135), (250, 177), (292, 229), (208, 240), (222, 333), (236, 417), (250, 229), (306, 281), (375, 333), (208, 187)]
    #print(type(points))
    #print (len(points))
    #points.pop()
    #print (len(points))
    points_2 = points
    #print(points_2)

    # Aleix19
    #points_1 =  [(236, 62), (236, 114), (208, 135), (166, 166), (139, 219), (278, 146), (306, 198), (306, 250), (222, 250), (236, 333), (236, 406), (264, 250), (264, 323), (278, 406), (250, 198)]
    # Aleix20
    #points_2 =  [(236, 62), (236, 114), (208, 146), (166, 177), (180, 219), (278, 146), (306, 198), (306, 250), (222, 250), (236, 323), (236, 406), (264, 250), (264, 323), (278, 406), (250, 198)]


    frame = cv2.imread("./images/vrkasana1.jpg")
    frameCopy = np.copy(frame)
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    threshold = 0.1
    cv2.circle(frame, (200,300), 600, (255, 255, 255), thickness=-1, lineType=cv2.FILLED)

    corrections = {}
    directions = {}
    worst = []

    # Calculate diferences in inclination for all connections
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]

        if points_1[partA] and points_1[partB] and points_2[partA] and points_2[partB]:
        
            # Calculate inclinations
            deltaY_1 = (points_1[partA][0] - points_1[partB][0])
            if (abs(deltaY_1) > 0.0000005) :
                incl_1 = (points_1[partA][1] - points_1[partB][1]) / deltaY_1
            else:
                incl_1 = INF
            deltaY_2 = (points_2[partA][0] - points_2[partB][0])
            if (abs(deltaY_2) > 0.0000005) :
                incl_2 = (points_2[partA][1] - points_2[partB][1]) / deltaY_2
            else:
                incl_2 = INF

            if (incl_1 != 0):
                diff = abs((incl_1 - incl_2)/incl_1)
            else: 
                diff = abs(incl_1 - incl_2)
                
            # See if the segments are too different
            if partA == 8 or partA == 11:
                thr = 0.7
            else:
                thr = 0.5
            if diff > thr:
                print("Massa diferent en el punt ", partA, " : ", partB )
                corrections[partA] = 1
                
                # In which direction should be corrected?
                if (partA, partB) == (0,1) or (partA, partB) == (1,14):
                    # pivota respecte a B
                    p0 = np.array([points_1[partA][0], points_1[partA][1]])
                    p1 = np.array([points_1[partB][0], points_1[partB][1]])
                    p2 = np.array([points_2[partA][0], points_2[partA][1]])
                    p3 = np.array([points_2[partB][0], points_2[partB][1]])
                    
                    v0 = p0 - p1
                    v1 = p2 - p3
                    v2 = v0 + v1
                    
                    a = abs(np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1)))
                    worst.append((a, partA))
                    
                    if abs(v2[1]/v2[0]) < 1: # Verticals - inclements en les Y
                        if p0[1] - p1[1] - p2[1] + p3[1] < 0:
                            directions[partA] = "higher."
                        else:
                            directions[partA] = "lower."
                    else: # Horitzontals - increments en les X
                        if p0[0] - p1[0] - p2[0] + p3[0] < 0:
                            directions[partA] = "to the right."
                        else:
                            directions[partA] = "to the left."
                    
                else:
                    # pivota respecte a A
                    p0 = np.array([points_1[partB][0], points_1[partB][1]])
                    p1 = np.array([points_1[partA][0], points_1[partA][1]])
                    p2 = np.array([points_2[partB][0], points_2[partB][1]])
                    p3 = np.array([points_2[partA][0], points_2[partA][1]])
                    
                    #a = get_angle(p0, p1, p2)
                    #print("Angle entre ", partA, " y ", partB, " es ", a)
                    #print("La incl interna mitja es ", get_axis(p0, p1, p2))
                    v0 = p0 - p1
                    v1 = p2 - p3
                    v2 = v0 + v1
                    
                    a = abs(np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1)))
                    worst.append((a, partA))
                    
                    if abs(v2[1]/v2[0]) < 1: # Verticals
                        if p0[1] - p1[1] - p2[1] + p3[1] < 0:
                            directions[partA] = "higher."
                        else:
                            directions[partA] = "lower."
                    else: # Horitzontals
                        if p0[0] - p1[0] - p2[0] + p3[0] < 0:
                            directions[partA] = "to the right."
                        else:
                            directions[partA] = "to the left."
                
                
            else:
                corrections[partA] = 0
            

            # PRINT CHIVATO #  
            pA0 = points_1[partA][0] + points_2[14][0] - points_1[14][0]
            pA1 = points_1[partA][1] + points_2[14][1] - points_1[14][1]
            pB0 = points_1[partB][0] + points_2[14][0] - points_1[14][0]
            pB1 = points_1[partB][1] + points_2[14][1] - points_1[14][1]
                
            cv2.line(frame, (pA0, pA1), (pB0, pB1), (200, 80, 80), 2)
            cv2.circle(frame, (pA0, pA1), 8, (255, 0, 0), thickness=-1, lineType=cv2.FILLED)
            
            cv2.line(frame, points_2[partA], points_2[partB], (40, 200, 40), 2)
            cv2.circle(frame, points_2[partA], 8, (0, 255, 0), thickness=-1, lineType=cv2.FILLED)
         
            
    cv2.imshow('Output-Skeleton', frame)
    cv2.imwrite('Output-Skeleton-C.jpg', frame)
                
    cv2.waitKey(1)

    worst.sort()   
    print(worst)         
    print(messages[worst[-1][1]], directions[worst[-1][1]])
                
    #for key in corrections:
    #    if corrections[key] != 0:
    #        print(messages[key], directions[key])
    #print(key, " has level ", corrections[key], " and message ", messages[key])







comm = "sshpass -p Avalls2018bcn ssh -M -S ctrl-socket -fnNT Avalls2018bcn@azure.rabbyte.club "
subprocess.call(comm, shell=True)

cap = cv2.VideoCapture(1)

factor = 2.5

fgbg = cv2.createBackgroundSubtractorMOG2()

for x in range(0,120):
    ret, frame = cap.read()
    if ret == 0:
        break
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


print("Stand still for a little bit")
threshold = 0
for x in range(0,30):
    ret, frame = cap.read()
    if ret == 0:
        break
    fgmask = fgbg.apply(frame)
    threshold = threshold + fgmask.sum()
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
threshold = threshold / 30
print('El threshold es ')
print(threshold)
start8 = time.time()
first = True
while(1):
    ret, frame = cap.read()
    if ret == 0:
        break
    fgmask = fgbg.apply(frame)
    currentsum = fgmask.sum()
    #print(currentsum)
    if(currentsum < factor*threshold):
        show = "ESTA QUIET"
        
        thread1 = myThread(1, "Thread-1", 1)
        thread1.start()
        
        while(thread1.isAlive()):

            ret, frame = cap.read()
            if ret == 0:
                break
            cv2.imshow('frame',frame)
            show = "ANALITZANT...."
            cv2.putText(frame, show, (50, 50), cv2.FONT_HERSHEY_COMPLEX, .8, (255, 50, 0), 2, lineType=cv2.LINE_AA)
            cv2.imshow('frame',frame)

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
        #LLegir fitxer
        start7 = time.time()
        objecte1 = open("Output_Keypoints.txt", "r")
        result = objecte1.read()
        objecte1.close()
        print result
        result = ast.literal_eval(result)
        Compare_Skeletons(result)
        done7 = time.time()
        elapsed7 = done7 - start7
        print("Temps stickman i update pantalla: ")
        print(elapsed7)

        

    else:

        show = "ESTA EN MOVIMENT"
        done8 = time.time()
        elapsed8 = done8 - start8
        if(elapsed8 > 0.5):
            print("Temps total: ")
            print(elapsed8)
            start8 = time.time()
    


    cv2.putText(frame, show, (50, 50), cv2.FONT_HERSHEY_COMPLEX, .8, (255, 50, 0), 2, lineType=cv2.LINE_AA)
    cv2.imshow('frame',frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

comm_final = "rm ctrl-socket"
subprocess.call(comm_final, shell=True)
