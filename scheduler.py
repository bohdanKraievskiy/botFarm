import schedule
import time
import subprocess

def run_login_and_post_script():
    subprocess.run(["python", "loginAndPost.py"])

def run_signup_script():
    subprocess.run(["python", "signUp.py"])

# Schedule the login and post script to run every 4 hours
schedule.every(4).hours.do(run_login_and_post_script)

# Schedule the sign-up script to run every 6 hours
schedule.every(6).hours.do(run_signup_script)

while True:
    schedule.run_pending()
    time.sleep(1)
