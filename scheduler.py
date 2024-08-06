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
    subprocess.run(["python","loginAndComment.py"])
    print("Comment was trying to send!")


schedule.every(10).seconds.do(run_login_and_comment_script)
while True:
    schedule.run_pending()
    time.sleep(1)
