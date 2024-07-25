import schedule
import time
import subprocess

def run_script():
    subprocess.run(["python", "loginAndPost.py"])

# Schedule the script to run every 4 hours
schedule.every(4).hours.do(run_script)

while True:
    schedule.run_pending()
    time.sleep(1)