# cs588_freeway_project

### How to run freeway poc app locally, initial set up (assumes ubuntu enviornment)
1. python virtual environment: virtualenv -p python3 env
2. source evn/bin/activate
3. cd freeway_poc
4. set environment variable: export MONGO_IP=IP of DB

### After initial set up (if environment reboots will have to reset environ variable above)
run app with: python app.py
