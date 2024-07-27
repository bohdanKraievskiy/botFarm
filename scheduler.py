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
def run_login_and_gif_script():
    subprocess.run(["python3","loginAndGif.py"])
    print("Gif was trying to send!")


schedule.every(20).minutes.do(run_login_and_post_script)

# Schedule the sign-up script to run twice a day (every 12 hours)
schedule.every(12).hours.do(run_signup_script)

schedule.every(20).minutes.do(run_login_and_bio_script)

schedule.every(30).minutes.do(run_login_and_gif_script)
while True:
    schedule.run_pending()
    time.sleep(1)
