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
    print("Post2 was trying to send!")

def run_login_and_like():
    subprocess.run(["python3","loginAndLike.py"])
    print("Likes trying to do")

def run_login_and_follow():
    subprocess.run(["python3","loginAndFollow.py"])
    print("Follows was rying to do")

schedule.every(2).minutes.do(run_login_and_post_script)

schedule.every(2).minutes.do(run_login_and_post2_script)

# Schedule the sign-up script to run twice a day (every 12 hours)
schedule.every(10).minutes.do(run_signup_script)

schedule.every(20).minutes.do(run_login_and_bio_script)

schedule.every(2).minutes.do(run_login_and_gif_script)

schedule.every(5).minutes.do(run_login_and_comment_script)
schedule.every(1).minutes.do(run_login_and_like)
schedule.every(5).minutes.do(run_login_and_follow)
while True:
    schedule.run_pending()
    time.sleep(1)
