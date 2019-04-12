sshpass -p Avalls2018bcn ssh  Avalls2018bcn@azure.rabbyte.club -t 'cd perceive2perfect/OpenPose/ && python OpenPoseImage.py > Output-Keypoints.txt'
sshpass -p Avalls2018bcn scp  Avalls2018bcn@azure.rabbyte.club:~/perceive2perfect/OpenPose/Output-Keypoints.txt . 
