
Credit:
Base Boilerplate - Jonathan Serrano - https://github.com/jonaths/minimum-python

# Minimum Python project

## Features 
1. Test directory configured to test and read files from the app/ directory
2. File config.py to read environment variables from an.env file in the root 
3. gitignore file
4. Requirements file.txt with rich library (to print in the console) and python-dotenv (to load environment variables from the.env file) 
5. Dockerfile to build a container that installs the necessary libraries using virtualenv 

## Installation 
1. Create virtualenv `virtualenv env --python=python3`
2. Install requirements `pip install -r requirements.txt`
3. Create.env file and add the environment variable `STORAGE_LOG
   `STORAGE_LOGS = '/home/Data/Code/minimum-python/app/common/storage/logs`
   
   
   ## Demo 
   Run the command in app 
   `python cmd_hello_world.py --message "hello world"`

   ## TESTING
   in /test or /
   >>> pytest
