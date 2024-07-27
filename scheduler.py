import schedule
import time
import subprocess

def run_login_and_post_script():
    subprocess.run(["python3", "loginAndPost.py"])
    print("Login and Post ended!")
	
def run_signup_script():
    subprocess.run(["python3", "signUp.py"])
    print("New bot created!")
def run_login_and_bio_script():
    subprocess.run(["python3","loginAndBio.py"])
    print("Bio was trying to change")


schedule.every(1).minutes.do(run_login_and_post_script)

# Schedule the sign-up script to run twice a day (every 12 hours)
schedule.every(1).hours.do(run_signup_script)

schedule.every(1).minutes.do(run_login_and_bio_script)

while True:
    schedule.run_pending()
    time.sleep(1)
