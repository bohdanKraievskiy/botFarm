import schedule
import time
import subprocess

def run_login_and_post_script():
    subprocess.run(["python3", "loginAndPost.py"])
    print("Login and Post ended!")
	
def run_signup_script():
    subprocess.run(["python3", "signUp.py"])

schedule.every(1).minutes.do(run_login_and_post_script)

# Schedule the sign-up script to run twice a day (every 12 hours)
schedule.every(12).hours.do(run_signup_script)

while True:
    schedule.run_pending()
    time.sleep(1)
