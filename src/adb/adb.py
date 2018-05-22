#!/usr/bin/python
# *_* coding:utf-8 *_*

import os
        
def adb(one_command):
    """
    use the command to control you phone by android adb tools
    """
    one_command = "adb " + one_command
    os.system(one_command)
    out = os.popen(one_command).read()
    return out

# adb("devices")
# adb("shell wm size")
# adb("shell screencap -p /sdcard/screen.png")
# like print screen and save on /roo/ the name is screen.png
# adb("pull /sdcard/screen.png")
# uploading the picture
# adb("shell input swipe 250 1200 250 800")
# something that use for swipe or said slide 
"""
 x is 1200 y is 250 
 and (1200, 250) --> (800, 250)
 like dwon sliding 
"""
# for i in range(5):
#     adb("shell input tap 1841 1001")
# like click one time use your finger
#     adb("shell input tap 1583 1001")
#     adb("shell input tap 1005 1327")
