#!/usr/bin/python
# *_* coding:utf-8 *_*

import adb
import cv2
import numpy as np
import math

"""
if you see this code, first you should to kown the img's point in the opencv
and kown the phone's point 
"""

def one_to_two(img):
    left_img = img[0:img.shape[0], 0:img.shape[1] / 2]
    right_img = img[0: img.shape[0], img.shape[1] / 2:img.shape[1]]
    cv2.imshow("left_img", left_img)
    cv2.imshow("right_img", right_img)
    cv2.waitKey()
    print(" ")

def get_aim_img():
    adb.adb("shell screencap -p /sdcard/screen.png")
#     adb.adb("pull /sdcard/DCIM/Camera/2.jpg")
    adb.adb("pull /sdcard/screen.png")

def get_col_img(temp, img, cut, len_lin):
    img = img[0:len_lin, cut[0]:cut[1]]
    
    if img.shape[0] > 0 and img.shape[1] > 0:
        cv2.imwrite("cut_img/" + str(cut[0]) + ".png", img)
#         print(temp[0] + 0, temp[1] + cut[0])
#         cv2.imshow("img", img)
#         cv2.waitKey()
        if need.shape[0] == img.shape[0] and need.shape[1] == img.shape[1]:
            cmd_str = "shell input tap " + str(temp[1] + cut[0] + 20) + " " + str(temp[0] + 0 + 30)
            print(cmd_str)
            for c in range(5):
                adb.adb(cmd_str)
            
        one_cut_img = []
        one_cut_img.append(temp[0] + 0)
        one_cut_img.append(temp[1] + cut[0])
        one_cut_img.append(img)
        one_cut_img.append(img.shape[0])
        one_cut_img.append(img.shape[1])
        
        temp_cut_img.append(one_cut_img)

def get_lin_img(temp, img, cut, len_col):
    img = img[cut[0]:cut[1], 0:len_col]
    
    if img.shape[0] > 0 and img.shape[1] > 0:
        cv2.imwrite("cut_img/" + str(cut[0]) + ".png", img)
        if need.shape[0] == img.shape[0] and need.shape[1] == img.shape[1]:
#             print(temp[0] + cut[0], temp[1] + 0)
#             cv2.imshow("img", img)
#             cv2.waitKey()
            cmd_str = "shell input tap " + str(temp[1] + 0 + 20) + " " + str(temp[0] + cut[0] + 20)
            print(cmd_str)
            for c in range(10):
                adb.adb(cmd_str)
        one_cut_img = []
        one_cut_img.append(temp[0] + cut[0])
        one_cut_img.append(temp[1] + 0)
        one_cut_img.append(img)
        one_cut_img.append(img.shape[0])
        one_cut_img.append(img.shape[1])
        
        temp_cut_img.append(one_cut_img)
    
def how_cut(f, temp, lin, col, img_color):
    cut_one = [0,0]
    is_cut = False
    for x in range(len(lin) - 1):
#         print(x, len(lin) - 1)
        if lin[x] == 0 and lin[x + 1] is not 0:
            cut_one[0] = x + 1
            continue
        if (lin[x] is not 0 and lin[x + 1] == 0):
            cut_one[1] = x
            f(temp, img_color, cut_one, len(col))
#             print(cut_one)
            is_cut = True
            cut_one = [0,0]
        
        if (cut_one[0] is not 0) and x == (len(lin) - 2):
            cut_one[1] = x
            f(temp, img_color, cut_one, len(col))
#             print(cut_one)
            is_cut = True
            cut_one = [0,0]
    return is_cut

def one_cut(img, img_color):
    col = np.sum(img, axis = 0)
    lin = np.sum(img, axis = 1)
#     print(img)
#     print(len(col))
#     print(len(lin))
    temp = temp_cut_img.pop()
#     print(img)
#     input("nihao")
    lin_ok = how_cut(get_lin_img, temp, lin, col, img_color)
    col_ok = how_cut(get_col_img, temp, col, lin, img_color)
    if lin_ok == False and col_ok == False:
        all_cut_img.append(temp)

            
def main(img_color):
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("imgg", img)
#     cv2.waitKey()
    ret, dst = cv2.threshold(img, 180, 255, 1)
#     print(dst)
#     cv2.imshow("new_aim", dst)
#     cv2.waitKey()
    one_cut(dst, img_color)

need = cv2.imread("data/72.png", cv2.IMREAD_GRAYSCALE)
print(need.shape)
all_cut_img = []
temp_cut_img = []
while True:
    get_aim_img()
    img_name = "screen.png"
    one = [0,0]
    img_read = cv2.imread(img_name)
    print(img_read.shape)
    one.append(img_read)
    one.append(img_read.shape[0])
    one.append(img_read.shape[1])
    temp_cut_img.append(one)
    while len(temp_cut_img) is not 0:
        main(temp_cut_img[len(temp_cut_img) - 1][2])
    img_read_c = cv2.imread(img_name)
    j = 0
    f = open("img.txt", "w")
    for i in all_cut_img:
        cv2.rectangle(img_read_c,(i[1],i[0]),(i[1] + i[4],i[0] + i[3]),(0,255,0),3)
        cv2.imwrite("img/" + str(j) + ".png", i[2])
        f.write(str(i[0]) + "    " + str(i[1]) + "    "\
                + str(i[3]) + "    " + str(i[4]) + "\n")
        j +=1
    f.close()
#     cv2.imshow("img_read.png", img_read_c)
#     cv2.waitKey()
    img_read_c = []
    adb.adb("shell input swipe 250 1200 250 800")