# -*- coding: UTF-8 -*-
#!/usr/bin/python

#基本窗口
import math
import Tkinter
root_window = Tkinter.Tk()
# root_window._test()
#居中窗口的函数
def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)

#计算中点，即第一个点
def culcu_middle_point(start_x,start_y,end_x,end_y):
    middle_x = (start_x + end_x)/2
    middle_y = (start_y + end_y)/2
    return (middle_x,middle_y)

#计算两点距离
def culcu_two_point_dis(start_x,start_y,end_x,end_y):
    del_x = end_x - start_x
    del_y = end_y - start_y
    # print math.sqrt(del_x*del_x+del_y*del_y)
    return math.sqrt(del_x*del_x+del_y*del_y)

# culcu_two_point_dis(0,0,3,4)


#按照龙的分形生成一个点,生成在左手边
def generate_point_left(start_x,start_y,end_x,end_y):
    delta_l = culcu_two_point_dis(start_x,start_y,end_x,end_y)
    delta_l = delta_l/2
    delta_x = end_x-start_x
    delta_y = end_y-start_y
    middle_x = (start_x + end_x)/2
    middle_y = (start_y + end_y)/2
    if (start_y == end_y):
        return (middle_x,middle_y-delta_l)
    if (start_x == end_x):
        return (middle_x-delta_l,middle_y)
    k = middle_y/middle_x
    sin_k = k*k/(k*k+1)
    sin_k = math.sqrt(sin_k)
    cos_k = 1/(k*k+1)
    cos_k = math.sqrt(cos_k)
    if (delta_x>0):
        if(delta_y>0):
            middle_x = middle_x-delta_l*sin_k
            middle_y = middle_y+delta_l*cos_k
        elif(delta_y<0):
            middle_x = middle_x+delta_l*sin_k
            middle_y = middle_y+delta_l*cos_k
    elif (delta_x<0):
        if (delta_y>0):
            middle_x = middle_x-delta_l*sin_k
            middle_y = middle_y-delta_l*cos_k
        elif(delta_y<0):
            middle_x = middle_x+delta_l*sin_k
            middle_y = middle_y-delta_l*cos_k
    return middle_x,middle_y


#根据两个点，生成一个点，在右手边
def generate_point_right(start_x,start_y,end_x,end_y):
    delta_l = culcu_two_point_dis(start_x,start_y,end_x,end_y)
    delta_l = delta_l/2
    delta_x = end_x-start_x
    delta_y = end_y-start_y
    middle_x = (start_x + end_x)/2
    middle_y = (start_y + end_y)/2
    if (start_y == end_y):
        return (middle_x,middle_y+delta_l)
    if (start_x == end_x):
        return (middle_x+delta_l,middle_y)
    k = middle_y/middle_x
    sin_k = k*k/(k*k+1)
    sin_k = math.sqrt(sin_k)
    cos_k = 1/(k*k+1)
    cos_k = math.sqrt(cos_k)
    if (delta_x>0):
        if(delta_y>0):
            middle_x = middle_x+delta_l*sin_k
            middle_y = middle_y-delta_l*cos_k
        elif(delta_y<0):
            middle_x = middle_x-delta_l*sin_k
            middle_y = middle_y-delta_l*cos_k
    elif (delta_x<0):
        if (delta_y>0):
            middle_x = middle_x+delta_l*sin_k
            middle_y = middle_y+delta_l*cos_k
        elif(delta_y<0):
            middle_x = middle_x-delta_l*sin_k
            middle_y = middle_y+delta_l*cos_k
    return middle_x,middle_y

# print generate_point_right(0.0,0.0,2.0,0.0)
# print generate_point_right(0.0,0.0,0.0,2.0)
# print generate_point_right(0.0,0.0,2.0,2.0)
# print generate_point_right(0.0,0.0,-2.0,-2.0)
# print generate_point_right(0.0,0.0,-2.0,2.0)
# print generate_point_right(0.0,0.0,2.0,-2.0)
#

# def generate_point(start_x,start_y,end_x,end_y):
#     j

#生成的点加入到列表后面
def add_two_num_to_ori(pt_x,pt_y,ori_l):
    list_len = len(ori_l)
    ori_l.insert(len(ori_l)-2,pt_x)
    ori_l.insert(len(ori_l)-2,pt_y)

#处理一次
def cope_list_once(cope_list):
    # print 'cope once'
    list_lenth = len(cope_list)
    #新建一个数组
    temp_list = []
    i = 0
    left_or_right = 0
    while (i <= list_lenth - 1):
        temp_list.append(cope_list[i])
        temp_list.append(cope_list[i+1])
        #最后两个数不会生成新的点
        if(i < list_lenth - 3):
            if (left_or_right == 0):
                fir,sec = generate_point_left(cope_list[i],cope_list[i+1],cope_list[i+2],cope_list[i+3])
                left_or_right = 1
            elif(left_or_right == 1):
                fir,sec = generate_point_right(cope_list[i],cope_list[i+1],cope_list[i+2],cope_list[i+3])
                left_or_right = 0
            temp_list.append(fir)
            temp_list.append(sec)
        i = i + 2
    return temp_list

#自定义处理次数，把处理结果送到一个新的数组里
def cope_lists(cope_list,cope_n):
    if (cope_n<0):
        return
    recive_list = cope_list
    #n次处理
    while (cope_n > 0):
        # print cope_n
        # t_list = []
        recive_list = cope_list_once(recive_list)
        # recive_list = []
        cope_n = cope_n - 1
    # for i in recive_list:
    #     print i
    return recive_list

ori_list = [100.0,400.0,400.0,100.0]

draw_list = cope_lists(ori_list,20)
# draw_list = cope_lists(ori_list,3)

#创建画布
main_canv = Tkinter.Canvas(root_window,bg="blue",height=600,width=600)
coord = 10, 50, 240, 210
line = main_canv.create_line(draw_list,width=1)
main_canv.pack()
root_window.maxsize(600, 600)
root_window.minsize(600, 600)
center_window(root_window,600,600)
root_window.mainloop()
