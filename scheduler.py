import schedule
import time
import subprocess

def run_login_and_post_script():
    subprocess.run(["python3", "loginAndPost.py"])

def run_signup_script():
    subprocess.run(["python3", "signUp.py"])

schedule.every(10).minutes.do(run_login_and_post_script)

# Schedule the sign-up script to run twice a day (every 12 hours)
schedule.every(10).minutes.do(run_signup_script)

while True:
    schedule.run_pending()
    time.sleep(1)
