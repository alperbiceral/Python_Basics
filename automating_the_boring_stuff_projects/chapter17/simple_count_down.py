#! python3
import time
import subprocess

# this program counts down from 10 to 0 and runs a .wav file (alarm.wav)

def main():
    seconds = 10
    while seconds > 0:
        time.sleep(1)
        print(seconds)
        seconds -= 1

    subprocess.Popen('alarm.wav', shell=True)

if __name__ == '__main__':
    main()
