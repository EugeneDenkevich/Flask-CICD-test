#!/bin/bash
# chmod +x run.sh
sudo docker stop app
sudo docker rm app
sudo docker build -t api .
sudo docker run -d -p 5000:5000 --name app api