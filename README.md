# cs588_freeway_project

### How to run freeway poc app locally, initial set up (assumes ubuntu enviornment)
1. python virtual environment: virtualenv -p python3 env
2. pip install -r requirements.txt
3. source env/bin/activate
4. cd freeway_poc
5. set environment variable: export MONGO_IP=IP of DB

### After initial set up (if environment reboots will have to reset environ variable above)
run app with: python app.py
