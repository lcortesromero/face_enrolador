ls
ls#! /bin/bash

clear
echo "the script starts now"

xhost local:root

#sudo docker run -v /home/miller/Documents/face_course:/root/face_course/ -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY  -t -i camilol/opencv:v11 /bin/bash

#sudo docker run -it --privileged -v /home/miller/Documents/face_course:/root/face_course/ -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY camilol/opencv:v11 /bin/bash

#--add-host="localhost:192.168.56.108" \
#--net="host"\

#face_camara = "/root/openface/demos/web/project/face_video/face_start_script_within_docker.sh " + $1

sudo docker run -it \
  --net="host"\
  --privileged \
  --rm \
  -e DISPLAY=unix$DISPLAY \
  --env="QT_X11_NO_MITSHM=1" \
  --privileged -v /dev/video0:/dev/video0 \
  --privileged -v /dev/video1:/dev/video1 \
  --privileged -v /dev/video2:/dev/video2 \
  --privileged -v /dev/video3:/dev/video3 \
  --privileged -v /tmp/.X11-unix:/tmp/.X11-unix:ro  \
  --device /dev/video0 \
  --device /dev/video1 \
  --device /dev/video2 \
  --device /dev/video3 \
  -v /home/lcortes/Documentos/face_enrolador:/home/face_enrolador \
  camilol/opencv:latest /bin/bash #-l -c "/root/openface/demos/web/project/face_video/face_start_script_within_docker.sh $1" 

# cd /home/face_enrolador
# workon facecourse-py2
# python 
# sudo docker pull camilol/opencv:latest
# sudo docker images


		

#export containerId=$(docker ps -l -q)



#sudo docker commit 50dfef3fd41b  camilol/openface_ubuntu:face_course 
#sudo docker push camilol/openface_ubuntu:face_course




