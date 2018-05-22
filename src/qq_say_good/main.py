#!/usr/bin/python
# *_* coding:utf-8 *_*
import adb.adb

out = adb.adb.adb("devices")
adb.adb.adb("devices")
adb.adb.adb("shell wm size")
adb.adb.adb("shell screencap -p /sdcard/screen.png")
adb.adb.adb("pull /sdcard/screen.png")
print(type(out), len(out))