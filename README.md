# Setup

1. `git clone https://github.com/SIG-IR/flask_demo.git && cd flask_demo`
2. Make sure pip is installed -> see the setup script https://github.com/sameetandpotatoes/Enviguration
3. `pip install virtualenv`
4. `virtualenv .venv`
5. `source .venv/bin/activate`
6. `cp twitter_authentication.py.example twitter_authentication.py`
7. `pip install -r requirements.txt`
8. (optional) Get valid twitter API credentials from https://dev.twitter.com . Note that you need to have a valid Twitter account, and a phone number registered under your Twitter account to obtain valid credentials. Then, populate `twitter_authentication.py` with the credentials you got from Twitter

Note: Step 5 (`source .venv/bin/activate` activates the virtual environment that you just created (named .venv), and this needs to be done every time you work on this project). See below for more information on virtual environments.

## Start the Server

    python app.py

## Virtual Environments

From the Python official docs:

> A Virtual Environment is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.
