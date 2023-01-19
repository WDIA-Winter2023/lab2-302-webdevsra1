import os
import shutil
if os.path.exists("/home/pi/cst8254"):
    shutil.rmtree("/home/pi/cst8254")

os.mkdir("/home/pi/cst8254")
os.mkdir("/home/pi/cst8254/backup")
os.mkdir("/home/pi/cst8254/linux")
os.mkdir("/home/pi/cst8254/python")

os.mkdir("/home/pi/cst8254/linux/labs")
os.mkdir("/home/pi/cst8254/linux/lectures")

os.mkdir("/home/pi/cst8254/linux/labs/Lab1")
os.mkdir("/home/pi/cst8254/linux/labs/Lab2")
os.mkdir("/home/pi/cst8254/linux/labs/Lab3")

os.mkdir("/home/pi/cst8254/linux/lectures/Week1")
os.mkdir("/home/pi/cst8254/linux/lectures/Week2")
os.mkdir("/home/pi/cst8254/linux/lectures/Week3")

print("Folder Created")