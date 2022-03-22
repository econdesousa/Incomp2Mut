import time
for x in range (0,50):  
    if not x % 3:
        b = "Loading" + "." * x
        print (b, end="\r")
    time.sleep(1)