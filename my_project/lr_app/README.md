

**Instructions**
In this README file I am listing the instructions to run this code. 


**For Linux systems**
- First you need to create your environment using:

export FLASK_APP=server.py

-Then you run it using: 
python3 -m flask run

**For Windows**
-Create environment: 

set FLASK_APP=server.py

-Run it: 
python -m flask run

**Instructions to build and run docker image**

docker build . -t lr_app-image

docker run --name lr_app-container -d -p 5000:5000 lr_app-image