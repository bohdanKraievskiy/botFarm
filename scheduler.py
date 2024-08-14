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
def run_login_and_comment_script():
    subprocess.run(["python3","loginAndComment.py"])
    print("Comment was trying to send!")

def run_login_and_post2_script():
    subprocess.run(["python3","loginAndPost2.py"])
    print("Comment was trying to send!")


schedule.every(2).minutes.do(run_login_and_post_script)

schedule.every(2).minutes.do(run_login_and_post2_script)

# Schedule the sign-up script to run twice a day (every 12 hours)
schedule.every(12).hours.do(run_signup_script)

schedule.every(20).minutes.do(run_login_and_bio_script)

schedule.every(10).minutes.do(run_login_and_gif_script)

schedule.every(1).minutes.do(run_login_and_comment_script)

while True:
    schedule.run_pending()
    time.sleep(1)
