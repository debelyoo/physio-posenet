import numpy as np
import random
import cv2
import os
import subprocess
#from subprocess import run
#cap = cv2.VideoCapture(2)

comm = "sshpass -p Avalls2018bcn ssh -M -S ctrl-socket -fnNT Avalls2018bcn@azure.rabbyte.club " 
subprocess.call(comm, shell=True)

fgbg = cv2.createBackgroundSubtractorMOG2()
i = 0
maxsum = 0

while(i==0):
    frame = cv2.imread("single.jpeg")
    i=i+1
    fgmask = fgbg.apply(frame)
    currentsum = fgmask.sum()
    if(currentsum > maxsum and i!=1):
        maxsum = currentsum
        print('Nova suma maxima ')
        print(maxsum)
    print('La suma es ')
    print(currentsum)
    if(currentsum>maxsum/5.36):
        print('--------------------- \n esta en moviment \n---------------------')
    
    comm = "sshpass -p Avalls2018bcn ssh  Avalls2018bcn@azure.rabbyte.club -t 'cd perceive2perfect/OpenPose/ && python OpenPoseImage.py > Output-Keypoints.txt && cat Output-Keypoints.txt | sed -sn 2p' < echo "

        #result = subprocess.check_output(comm, shell=True)
    #print result 
    
    #os.system('./test.sh')
    #os.system("sshpass -p Avalls2018bcn ssh  Avalls2018bcn@azure.rabbyte.club -t 'cd perceive2perfect/OpenPose/ && python OpenPoseImage.py > Output-Keypoints.txt && cat Output-Keypoints.txt | sed -n 2p' < echo ")
    
    #os.system("sshpass -p Avalls2018bcn scp  Avalls2018bcn@azure.rabbyte.club:~/perceive2perfect/OpenPose/Output-Keypoints.txt .")
    #comma="ssh -S ctrl-socket Avalls2018bcn@azure.rabbyte.club -t 'cd perceive2perfect/OpenPose/ && python OpenPoseImage.py > Output-Keypoints.txt && cat Output-Keypoints.txt | sed -n 2p' < echo"
    
    comma="ssh -S ctrl-socket Avalls2018bcn@azure.rabbyte.club -t 'cd perceive2perfect/OpenPose/ && python OpenPoseImage.py > Output-Keypoints.txt && cat Output-Keypoints.txt' < echo"
    result = subprocess.check_output(comma, shell=True)
    print result

    #pro0 = subprocess.Popen(["bash","./test.sh"])
    #pro0.wait()
    #pro = subprocess.Popen(["bash", "sshpass -p Avalls2018bcn ssh  Avalls2018bcn@azure.rabbyte.club -t 'cd perceive2perfect/OpenPose/ && python OpenPoseImage.py > Output-Keypoints.txt'"])
    #pro.wait()
    #pro1 = subprocess.Popen(["bash","sshpass -p Avalls2018bcn scp  Avalls2018bcn@azure.rabbyte.club:~/perceive2perfect/OpenPose/Output-Keypoints.txt ."])
    #pro1.wait()
   
    

     
    cv2.imshow('frame',fgmask)
    previousframe = frame
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#cap.release()
#cv2.destroyAllWindows()
