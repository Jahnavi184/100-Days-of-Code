import time
countDownTime=int(input("Enter the time in seconds:"))
while countDownTime>0:
    print(countDownTime, end="\r", flush=True)
    time.sleep(1)
    countDownTime-=1
print("Time's up!")
