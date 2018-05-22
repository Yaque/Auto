#!/usr/bin/python
# *_* coding:utf-8 *_*
import numpy as np
import cv2

def get_col_img(temp, img, cut, len_lin):
    img = img[0:len_lin, cut[0]:cut[1]]
    
    if img.shape[0] > 0 and img.shape[1] > 0:
        cv2.imwrite("cut_img/" + str(cut[0]) + ".png", img)
        one_cut_img = []
        one_cut_img.append(temp[0] + 0)
        one_cut_img.append(temp[1] + cut[0])
        one_cut_img.append(img)
        one_cut_img.append(img.shape[0])
        one_cut_img.append(img.shape[0])
        
        temp_cut_img.append(one_cut_img)

def get_lin_img(temp, img, cut, len_col):
    img = img[cut[0]:cut[1], 0:len_col]
    
    if img.shape[0] > 0 and img.shape[1] > 0:
        cv2.imwrite("cut_img/" + str(cut[0]) + ".png", img)
        one_cut_img = []
        one_cut_img.append(temp[0] + cut[0])
        one_cut_img.append(temp[1] + 0)
        one_cut_img.append(img)
        one_cut_img.append(img.shape[0])
        one_cut_img.append(img.shape[0])
        
        temp_cut_img.append(one_cut_img)
    
def how_cut(f, temp, lin, col, img_color):
    cut_one = [0,0]
    is_cut = False
    for x in range(len(lin) - 1):
        print(x, len(lin) - 1)
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
    ret, dst = cv2.threshold(img, 200, 255, 1)
#     print(dst)
#     cv2.imshow("new_aim", dst)
#     cv2.waitKey()
    one_cut(dst, img_color)

img_name = "screen.png"
all_cut_img = []
temp_cut_img = []
one = [0,0]
img_read = cv2.imread(img_name)
# print(img_read.shape)
one.append(img_read)
one.append(img_read.shape[0])
one.append(img_read.shape[1])
temp_cut_img.append(one)
while len(temp_cut_img) is not 0:
#     cv2.imshow("1", temp_cut_img[len(temp_cut_img) - 1][2])
#     cv2.waitKey()
    main(temp_cut_img[len(temp_cut_img) - 1][2])
# main("cut_img/966.png")
img_read_c = cv2.imread(img_name)
j = 0
f = open("img.txt", "w")
for i in all_cut_img:
#     print(i)
    cv2.rectangle(img_read_c,(i[1],i[0]),(i[1] + i[4],i[0] + i[3]),(0,255,0),3)
#     cv2.imshow("img_read", img_read_c)
#     cv2.waitKey()
    cv2.imwrite("img/" + str(j) + ".png", i[2])
    f.write(str(i[0]) + "    " + str(i[1]) + "    "\
            + str(i[3]) + "    " + str(i[4]) + "\n")
    j +=1
f.close()
cv2.imshow("img_read.png", img_read_c)
cv2.waitKey()