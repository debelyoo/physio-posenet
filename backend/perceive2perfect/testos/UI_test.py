import Tkinter
import PIL.Image, PIL.ImageTk
import numpy as np
import cv2
import time
import subprocess
import os
import ast
import threading
import time
from gtts import gTTS 
import pyttsx

archery =  [(176, 194), (157, 250), (129, 264), (55, 264), (111, 250), (185, 264), (259, 264), (315, 250), (139, 403), (129, 500), (120, 612), (185, 389), (213, 486), (241, 570), (157, 333)]
vrksasana =  [(273, 150), (273, 244), (221, 263), (182, 150), (260, 75), (326, 263), (365, 150), (300, 75), (234, 470), (247, 639), (286, 808), (313, 470), (456, 545), (300, 545), (273, 376)]
squats =  [(313, 104), (250, 229), (187, 271), (360, 292), (438, 271), (250, 271), (516, 271), (563, 271), (46, 563), (266, 563), (172, 813), (46, 542), (375, 563), (281, 772), (156, 417)]



#############################  Computer Vision Algorithms ############################

language = 'en'

MODE = "MPI"

LOCALITY = "LOCAL"

if MODE is "COCO":
    protoFile = "pose/coco/pose_deploy_linevec.prototxt"
    weightsFile = "pose/coco/pose_iter_440000.caffemodel"
    nPoints = 18
    POSE_PAIRS = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]

elif MODE is "MPI" :
    protoFile = "../OpenPose/pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
    weightsFile = "../OpenPose/pose/mpi/pose_iter_160000.caffemodel"
    nPoints = 15
    POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        if(LOCALITY == "CLOUD"):
            comma2="sshpass -p Avalls2018bcn scp ./sample.jpeg Avalls2018bcn@azure.rabbyte.club:~/perceive2perfect/OpenPose/sample.jpeg"
            subprocess.call(comma2, shell=True)

            comma="ssh -S ctrl-socket Avalls2018bcn@azure.rabbyte.club -t 'cd perceive2perfect/OpenPose/ && python OpenPoseImage.py > Output-Keypoints.txt && cat Output-Keypoints.txt | sed -n 2p ' > Output-Keypoints.txt"
            subprocess.call(comma, shell=True)
        else:
            frame = cv2.imread("sample.jpeg")
            frameCopy = np.copy(frame)
            frameWidth = frame.shape[1]
            frameHeight = frame.shape[0]
            threshold = 0.1

            net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

            # input image dimensions for the network
            inWidth = 368
            inHeight = 368
            inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
                                      (0, 0, 0), swapRB=False, crop=False)

            net.setInput(inpBlob)

            output = net.forward()
            #print("time taken by network : {:.3f}".format(time.time() - t))

            H = output.shape[2]
            W = output.shape[3]

            # Empty list to store the detected keypoints
            points = []

            for i in range(nPoints):
                # confidence map of corresponding body's part.
                probMap = output[0, i, :, :]

                # Find global maxima of the probMap.
                minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
                
                # Scale the point to fit on the original image
                x = (frameWidth * point[0]) / W
                y = (frameHeight * point[1]) / H

                if prob > threshold : 
                    cv2.circle(frameCopy, (int(x), int(y)), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
                    cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)

                    # Add the point to the list if the probability is greater than the threshold
                    points.append((int(x), int(y)))
                else :
                    points.append(None)


            #cv2.imshow('Output-Keypoints', frameCopy)
            #cv2.imshow('Output-Skeleton', frame)

            #print (points)
            #cv2.imwrite('Output-Keypoints.jpg', frameCopy)
            #cv2.imwrite('Output-Skeleton.jpg', frame)

            #print("Total time taken : {:.3f}".format(time.time() - t))
            print("Step 1")
            objecte1 = open("Output-Keypoints.txt", "w")
            result = objecte1.write(str(points))
            objecte1.close()
            print("Rip")


def Compare_Skeletons(points_1, points_2):
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
                1: "Move your torso",
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
    # archery
    #points_1 =  [(176, 194), (157, 250), (129, 264), (55, 264), (111, 250), (185, 264), (259, 264), (315, 250), (139, 403), (129, 500), (120, 612), (185, 389), (213, 486), (241, 570), (157, 333)]
    # squats
    #points_1 =  [(313, 104), (250, 229), (187, 271), (360, 292), (438, 271), (250, 271), (516, 271), (563, 271), (46, 563), (266, 563), (172, 813), (46, 542), (375, 563), (281, 772), (156, 417)]
    # virabhadrasana
    #points_1 = [(391, 114), (376, 166), (360, 187), (391, 114), (376, 135), (376, 187), (376,   125), (376, 62), (360, 302), (266, 313), (250, 406), (376, 302), (454, 375), (548, 417), (360, 240)]


    # 0
    #points_1 = [(205, 93), (205, 160), (166, 160), (146, 93), (195, 40), (244, 174), (273, 93), (225, 40), (185, 334), (195, 441), (215, 549), (234, 321), (332, 374), (225, 374), (205, 254)]

    # Aleix
    #points_1 = [(208, 73), (208, 125), (166, 125), (153, 83), (194, 41), (236, 125), (250, 83), (208, 41), (194, 229), (222, 333), (236, 406), (236, 219), (306, 250), (250, 313), (208, 177)]

    # 1
    #points_1 = [(205, 182), (205, 243), (171, 259), (182, 182), (194, 106), (240, 259), (240, 182), (217, 121), (194, 396), (205, 487), (228, 579), (251, 380), (331, 426), (240, 426), (217, 320)]

    # 3
    #points_2 = [(146, 110), (146, 165), (124, 187), (139, 110), (139, 66), (176, 176), (169, 110), (154, 66), (139, 286), (146, 374), (154, 451), (176, 275), (235, 319), (169, 308), (154, 231)]

    # Aleix1
    #points_1 =  [(250, 62), (250, 114), (208, 135), (153, 156), (166, 208), (278, 156), (278, 198), (292, 219), (222, 240), (222, 333), (236, 406), (264, 229), (333, 260), (278, 333), (236, 187)]

    # Aleix6
    #points_2 =  [(180, 62), (194, 114), (153, 146), (111, 187), (69, 229), (236, 135), (264, 177), (292, 219), (222, 240), (222, 333), (236, 406), (264, 229), (320, 229), (389, 271), (222, 187)]

    # Aleix7
    #points_1 =  [(236, 62), (236, 114), (208, 146), (194, 198), (194, 250), (278, 135), (292, 198), (292, 250), (222, 250), (236, 323), (236, 406), (264, 250), (264, 323), (278, 406), (250, 198)]

    # Aleix9
    #points_2 =  [(264, 73), (250, 114), (222, 135), (194, 198), (194, 250), (278, 146), (292, 198), (292, 250), (222, 250), (236, 323), (236, 406), (264, 250), (264, 323), (278, 406), (250, 198)]

    # Aleix10
    #points_2 =  [(166, 52), (180, 104), (153, 135), (125, 198), (97, 250), (222, 135), (250, 177), (292, 229), (208, 240), (222, 333), (236, 417), (250, 229), (306, 281), (375, 333), (208, 187)]
    #print(type(points))
    #print (len(points))
    #points.pop()
    #print (len(points))
    #print(points_2)

    # Aleix19
    #points_1 =  [(236, 62), (236, 114), (208, 135), (166, 166), (139, 219), (278, 146), (306, 198), (306, 250), (222, 250), (236, 333), (236, 406), (264, 250), (264, 323), (278, 406), (250, 198)]
    # Aleix20
    #points_2 =  [(236, 62), (236, 114), (208, 146), (166, 177), (180, 219), (278, 146), (306, 198), (306, 250), (222, 250), (236, 323), (236, 406), (264, 250), (264, 323), (278, 406), (250, 198)]


    frame = cv2.imread("../OpenPose/images/vrkasana1.jpg")
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
                #thr = 0.7
                thr = 1.4
            else:
                #thr = 0.5
                thr = 1.2
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
            if points_2[14] and points_1[14]:
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
    if(len(worst)==0):
        return "Good job!"         
    else:
        return messages[worst[-1][1]] + " " + directions[worst[-1][1]]
               
    #for key in corrections:
    #    if corrections[key] != 0:
    #        print(messages[key], directions[key])
    #print(key, " has level ", corrections[key], " and message ", messages[key])













class Application:
    
    def start(self):
        print "Starting configuration"

        comm = "sshpass -p Avalls2018bcn ssh -M -S ctrl-socket -fnNT Avalls2018bcn@azure.rabbyte.club "
        subprocess.call(comm, shell=True)
###
        cap = self.vid
        factor = 2
        fgbg = cv2.createBackgroundSubtractorMOG2()

        for x in range(0,120):
            ret, frame, f = cap.get_frame()
            if ret == 0:
                break
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = Tkinter.NW)
            self.canvas.update() 
            fgmask = fgbg.apply(f)
            cv2.imshow('frame',fgmask)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break


        print("Stand still for a little bit")
        myobj = gTTS(text="Stand still for a little bit", lang=language, slow=False) 
        myobj.save("welcome.mp3")  
        os.system("mpg321 welcome.mp3")
        threshold = 0
        for x in range(0,30):
            ret, frame, f = cap.get_frame()
            if ret == 0:
                break
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = Tkinter.NW)
            self.canvas.update() 
            fgmask = fgbg.apply(f)
            threshold = threshold + fgmask.sum()
            cv2.imshow('frame',fgmask)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
        #threshold = threshold / 30
        print('El threshold es ')
        print(threshold)
        
        threshold = threshold/30

        i = 50
        last_eval = ""

        while(last_eval != "Good job!"):
            i = i+1
            ret, frame, f = cap.get_frame()
            if ret == 0:
                break
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = Tkinter.NW)
            self.canvas.update() 
            fgmask = fgbg.apply(f)
            currentsum = fgmask.sum()
            #print(currentsum)
            if(currentsum < factor*threshold and i > 120):
                i = 0
                cv2.imwrite('sample.jpeg', frame)
                thread1 = myThread(1, "Thread-1", 1)
                thread1.start()
                #engine = pyttsx.init()
                #engine.say('Analyzing.')
                #engine.runAndWait()
                myobj = gTTS(text="Analyzing.", lang=language, slow=False) 
                myobj.save("welcome.mp3")  
                os.system("mpg321 welcome.mp3")
                while(thread1.isAlive()):
                  
                    ret, bullshit, frame = cap.get_frame()
                    if ret == 0:
                        break
                    self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(bullshit))
                    self.canvas.create_image(0, 0, image = self.photo, anchor = Tkinter.NW)
                    self.canvas.update() 
                    
                    cv2.imshow('frame',frame)
                    show = "ANALYZING...."
                    cv2.putText(frame, show, (50, 50), cv2.FONT_HERSHEY_COMPLEX, .8, (255, 50, 0), 2, lineType=cv2.LINE_AA)
                    cv2.imshow('frame',frame)
                    
                    k = cv2.waitKey(30) & 0xff
                    if k == 27:
                        break
                objecte1 = open("Output-Keypoints.txt", "r")
                result = objecte1.read()
                objecte1.close()
                #print result
                result = ast.literal_eval(result)
                last_eval = Compare_Skeletons(self.points_1, result)
                print(last_eval)
                #engine = pyttsx.init()
                #engine.say(last_eval)
                #engine.runAndWait()
                myobj = gTTS(text=last_eval, lang=language, slow=False) 
                myobj.save("welcome.mp3")  
                os.system("mpg321 welcome.mp3")
            else:
                show = "TARGET MOVING / RESTING TIME"
            cv2.putText(f, show, (50, 50), cv2.FONT_HERSHEY_COMPLEX, .8, (255, 50, 0), 2, lineType=cv2.LINE_AA)
            cv2.imshow('frame',f)

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        cv2.destroyAllWindows()
        comm_final = "rm ctrl-socket"
        subprocess.call(comm_final, shell=True)

###
        
    def select(self, v):
        if(self.var.get() == "Archer"):
            self.source = "../OpenPose/images/archery.jpg"
            self.points_1 = archery
        elif(self.var.get() == "Vrkasana"):
            self.source = "../OpenPose/images/vrkasana.jpg"
            self.points_1 = vrksasana
        elif(self.var.get() == "Squats"):
            self.source = "../OpenPose/images/squats.jpg"
            self.points_1 = squats
        self.image2 = PIL.Image.open(self.source)
        self.image = self.image2.resize((320, self.vid.getH() - 30), PIL.Image.ANTIALIAS)
        self.photo = PIL.ImageTk.PhotoImage(self.image)

        self.label.configure(image=self.photo)
        self.label.image = self.photo


    def createWidgets(self, window):
        frametop = Tkinter.Frame(window)
        frametop.pack({"side":"top", "fill":"both", "expand":1})

        self.var = Tkinter.StringVar()
        self.var.set("Select your pose") # initial information
        self.option = Tkinter.OptionMenu(frametop, self.var, "Archer", "Vrkasana", "Squats",  command = self.select)
        self.option.pack({"side": "left"})

#        self.QUIT = Tkinter.Button(window)
#        self.QUIT["text"] = "FINISH"
#        self.QUIT["fg"]   = "red"
#        self.QUIT["command"] =  self.quit

#        self.QUIT.pack({"side": "right"})

        self.START = Tkinter.Button(frametop)
        self.START["text"] = "START"
        self.START["command"] = self.start
        
        self.START.pack({"side": "right"})
              
        self.source = "../OpenPose/images/white.jpg"

        self.image = PIL.Image.open(self.source)
        self.image = self.image.resize((320, self.vid.getH() - 30), PIL.Image.ANTIALIAS)
        self.photo = PIL.ImageTk.PhotoImage(self.image)

        self.label = Tkinter.Label(image=self.photo)
        self.label.image = self.photo
        self.label.pack({"side": "right"})

    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        
        self.vid = MyVideoCapture(video_source)
                # Create a canvas that can fit the above video source size
        self.canvas = Tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack({"side": "right"})
        #Frame.__init__(self, master)
        #self.pack()
        self.createWidgets(window)

                # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        self.window.mainloop()


    def snapshot(self):
        # Get a frame from the video source
        ret, frame, _ = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        ret, frame, _ = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = Tkinter.NW)

        self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)   

    def getH(self):
        return int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), frame)
            else:
                return (ret, None, None)
        else:
            return (ret, None, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Create a window and pass it to the Application object
Application(Tkinter.Tk(), "PoseTrainer")
