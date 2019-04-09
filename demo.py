#!/usr/bin/env python
# encoding: utf-8
'''
@author: tianxiaomo
@license: (C) Apache.
@contact: huguanghao520@gmail.com
@software: 
@file: demo.py
@time: 2019/3/19 16:24
@desc:
'''
from PIL import Image,ImageFont,ImageDraw
import random
import os
import math
import numpy as np
import cv2


class Paper:
    def __init__(self,w,h,path,color=0xffffff):
        bg_list = os.listdir(path)
        img_path = os.path.join(path,random.sample(bg_list,1)[0])
        img = Image.open(img_path)
        i_w,i_h = img.size
        c_w = random.randint(0,i_w-w)
        c_h = random.randint(0,i_h-h)
        self.img = img.crop((c_w, c_h,c_w+w,c_h+h))

        self.img = Image.new('RGB',[w,h],color)

        self.draw = ImageDraw.Draw(self.img)

    def write(self,point,words,font_path,font_size,color=0):
        '''
        draw text,one by one character
        :param point:[left,right,up,down]
        :param words:
        :param font_path:
        :param font_size:
        :param color: 0x000000 white ,0xffffff black
        :return:
        '''
        l,r,u,d = point
        font = ImageFont.truetype(font=font_path, size=font_size)
        w_w = (r - l) / len(words)
        for i, t in enumerate(words):
            self.draw.text([int(0.5 + l + w_w * i), u], t, fill=color, font=font)
        text_height = max([font.getsize(w)[1] for w in words])
        d = u + text_height
        return self.img,[l,u,r,u,r,d,l,d],words

    def writeW(self,point,words,font_path,font_size,color=0):
        '''
        draw text,one word
        :param point:
        :param words:
        :param font_path:
        :param font_size:
        :param color:
        :return:
        '''
        l,r,u,d = point
        font = ImageFont.truetype(font=font_path, size=font_size)
        space_width = font.getsize(' ')[0] * 1
        words_width = [font.getsize(w)[0] for w in words]
        text_width = sum(words_width)
        text_height = max([font.getsize(w)[1] for w in words])
        r = l+text_width
        d = u+text_height
        self.draw.text([l, u],words, fill=color, font=font)
        return self.img,[l,u,r,u,r,d,l,d],words

    def writeR(self,point,words,font_path,font_size,color=0,c_w=None):
        '''
        draw text,one by one character,from right
        :param point:
        :param words:
        :param font_path:
        :param font_size:
        :param color:
        :return:
        '''
        l,r,u,d = point
        font = ImageFont.truetype(font=font_path, size=font_size)
        if c_w is None:c_w = (r - l) / len(words)
        for i, t in enumerate(words):
            self.draw.text([int(0.5 + r - c_w * i), u], words[len(words)-i-1], fill=color, font=font)
        r +=c_w
        l = r - c_w*(len(words)+0.2)
        text_height = max([font.getsize(w)[1] for w in words])
        d = u + text_height*1.1
        u += text_height*0.1
        return self.img,[l,u,r,u,r,d,l,d],words

    def write_direction(self,point,words,font_path,font_size,color=0,direction=None):
        '''
        draw text,one by one character
        :param point:[left,right,up,down]
        :param words:
        :param font_path:
        :param font_size:
        :param color: 0x000000 white ,0xffffff black
        :param direction: 方向 度数
        :return:
        '''
        l,r,u,d = point
        font = ImageFont.truetype(font=font_path, size=font_size)
        w_w = (r - l) / len(words)

        color = color+0xff000000

        for i, t in enumerate(words):
            s = font.getsize(t)
            img_w = Image.new('RGBA',(s),0x00000000)
            draw_w = ImageDraw.Draw(img_w)
            draw_w.text([0,0],t, fill=color, font=font)
            img_w = img_w.rotate(direction,expand=1)
            self.img.paste(img_w,[int(0.5 + l + w_w * i), u], img_w)
            # self.draw.text([int(0.5 + l + w_w * i), u], t, fill=color, font=font)
        text_height = max([font.getsize(w)[1] for w in words])
        d = u + text_height
        return self.img,[l,u,r,u,r,d,l,d],words

    def get_num(self,size):
        if size == 1:
            return str(random.randint(1,9))
        elif size == 2:
            return str(random.randint(10,99))
        elif size == 3:
            return str(random.randint(100,999))
        elif size == 4:
            return str(random.randint(1000, 9999))
        elif size == 5:
            return str(random.randint(10000, 99999))
        elif size == 6:
            return str(random.randint(100000, 999999))
        elif size == 7:
            return str(random.randint(1000000, 9999999))
        elif size == 8:
            return str(random.randint(10000000, 99999999))
        elif size == 9:
            return str(random.randint(100000000, 999999999))
        elif size == 10:
            return str(random.randint(1000000000, 9999999999))
        elif size == 11:
            return str(random.randint(10000000000, 99999999999))
        elif size == 12:
            return str(random.randint(100000000000, 999999999999))
        elif size == 13:
            return str(random.randint(1000000000000, 9999999999999))
        elif size == 15:
            return str(random.randint(10000000000000, 99999999999999))

def get_Invoice():
    boxes = []
    words_list = []
    Invoice = Paper(350,1060,'invoice_bg')
    
    # Invoice.draw.ellipse((50, 153, 290, 313),fill=0xa493d7)
    # Invoice.draw.ellipse((57, 160, 283, 306),fill="white")
    # Invoice.draw.ellipse((61, 166, 279, 300),fill=0xa190e4)
    # Invoice.draw.ellipse((62, 167, 278, 299),fill='white')
    # boxes.append(box)
    # _, box, word = Invoice.write([74,266,177,232],'全国统一发票监制章','fonts/fonts/simsun.ttc',22,0xa493d7)
    # boxes.append(box)

    seal = Image.open('seal/seal_1_1.png')
    seal = seal.resize([250,170])
    Invoice.img.paste(seal, (47, 150),seal)
    
    seal = Image.open('seal/seal_2_1.png')
    seal = seal.resize([220,160])
    Invoice.img.paste(seal, (70,830),seal)

    color = 0xffffff - 0xc29874
    Invoice.write_direction([4, 30, 20, 44], '存', 'fonts/simsun.ttc', 26, color,90)

    # _, box, word = Invoice.write([4, 30, 20, 44], '存', 'fonts/simsun.ttc', 26, color)
    #    boxes.append(box)
    _, box, word = Invoice.write([4, 30, 86, 110], '根', 'fonts/simsun.ttc', 26, color)
    #    boxes.append(box)
    _, box, word = Invoice.write([50, 300, 190, 214], '北京市出租汽车专用发票', 'fonts/simsun.ttc', 22, color)
    #    boxes.append(box)
    _, box, word = Invoice.write([58, 293, 222, 240], 'BEIJING TAXI SPECIAL INVOICE', 'fonts/simhei.ttf', 20, color)
    #    boxes.append(box)
    _, box, word = Invoice.write([137, 207, 260, 285], '发票联', 'fonts/simhei.ttf', 24, color)
    #    boxes.append(box)
    _, box, word = Invoice.write([131, 214, 293, 311], 'INVOICE', 'fonts/simhei.ttf', 22, color)
    #    boxes.append(box)

    h_h = (101 - 27) / 4
    _, box, word = Invoice.write([30, 44, 27, 44], 'S', 'fonts/simsun.ttc', 20, color)
    #    boxes.append(box)
    _, box, word = Invoice.write([30, 44, int(0.5 + 27 + 1 * h_h), 44], 'T', 'fonts/simsun.ttc', 20, color)
    #    boxes.append(box)
    _, box, word = Invoice.write([30, 44, int(0.5 + 27 + 2 * h_h), 44], 'U', 'fonts/simsun.ttc', 20, color)
    #    boxes.append(box)
    _, box, word = Invoice.write([30, 44, int(0.5 + 27 + 3 * h_h), 44], 'B', 'fonts/simsun.ttc', 20, color)
    #    boxes.append(box)

    size = 16
    color = 0xffffff - 0x846536
    font = 'fonts/simhei.ttf'
    l_h = (529 - 387) / 8
    _, box, word = Invoice.writeW([58, 92, 387, 404], '单位', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 387 + l_h * 1), 404], 'Company', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 387 + l_h * 2), 404], '电话', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 387 + l_h * 3), 404], 'Tel', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([77, 92, int(0.5 + 387 + l_h * 4), 404], '车号   京', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([77, 92, int(0.5 + 387 + l_h * 5), 404], 'Taxi No.', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([80, 92, int(0.5 + 387 + l_h * 6), 404], '证号', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([80, 92, int(0.5 + 387 + l_h * 7), 404], 'Certificate No.', font, size, color)
    #    boxes.append(box)

    l_h = (1000 - 540) / 26
    _, box, word = Invoice.writeW([58, 92, 540, 404], '日期', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 1), 404], 'Data', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 2), 404], '时间', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 3), 404], 'Time', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 4), 404], '单价', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 5), 404], 'Price cer km', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 6), 404], '里程', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 7), 404], 'Distance', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 8), 404], '等候', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 9), 404], 'Waiting time', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 10), 404], '状态', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 11), 404], 'State', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 12), 404], '金额', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 13), 404], 'Fare', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 14), 404], '燃油附加费', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 15), 404], 'Fuel oil surcharge', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 16), 404], '预约叫车服务费', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 17), 404], 'Call service surcharge', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 18), 404], '实收金额', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 19), 404], 'Total', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 20), 404], '卡号', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 21), 404], 'Card No.', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 22), 404], '卡原额', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 23), 404], 'Previous Card Balance', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 24), 404], '卡余额', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([58, 92, int(0.5 + 540 + l_h * 25), 404], 'Card Balance', font, size, color)
    #    boxes.append(box)

    _, box, word = Invoice.write([9, 27, 1001, 1020], '密', font, 18, color)
    #    boxes.append(box)
    _, box, word = Invoice.write([63, 82, 1001, 1020], '码', font, 18, color)
    #    boxes.append(box)
    _, box, word = Invoice.write([9, 66, 1024, 1035], 'Password', font, 18, color)
    #    boxes.append(box)

    size = 20
    font = 'fonts/simsun.ttc'
    l_h = (634 - 555) / 4
    Invoice.draw.rectangle((13, 547, 44, 727), None, color, width=2)
    _, box, word = Invoice.writeW([18, 92, 555, 404], '机', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([18, 92, int(0.5 + 555 + l_h * 1), 404], '打', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([18, 92, int(0.5 + 555 + l_h * 2), 404], '发', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([18, 92, int(0.5 + 555 + l_h * 3), 404], '票', font, size, color)
    #    boxes.append(box)

    l_h = (723 - 645) / 4
    _, box, word = Invoice.writeW([18, 92, 645, 404], '手', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([18, 92, int(0.5 + 645 + l_h * 1), 404], '写', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([18, 92, int(0.5 + 645 + l_h * 2), 404], '无', font, size, color)
    #    boxes.append(box)
    _, box, word = Invoice.writeW([18, 92, int(0.5 + 645 + l_h * 3), 404], '效', font, size, color)
    #    boxes.append(box)

    Invoice.draw.rectangle((270, 146, 350, 186), 0x101010)
    Invoice.draw.rectangle((0, 495, 77, 534), 0x101010)
    Invoice.draw.rectangle((96, 999, 237, 1045), 0x8d8b83, 0xd3d9d7, width=3)

    # 发票号
    color = 0x434343
    invoice_1 = Invoice.get_num(12)
    _, box, word = Invoice.write([20, 285, 314, 347], invoice_1, 'fonts/Deng.ttf', 34, color)
    boxes.append(box)
    words_list.append(word)
    invoice_2 = Invoice.get_num(8)
    _, box, word = Invoice.write([20, 194, 354, 381], invoice_2, 'fonts/Deng.ttf', 34, color)
    boxes.append(box)
    words_list.append(word)


    # 出租车打印信息
    print_color = [0x666666,0x782c31,0x782c31,0x782c31,0x782c31]
    print_color = random.sample(print_color,1)[0]
    print_color = (print_color//0xffff + random.randint(-10,10))*0xffff + (print_color%0xffff // 0xff + random.randint(-10,10))*0xff + (print_color % 0xff + random.randint(-10,10))
    font = ['dianzhen1.ttf','dianzhen1.ttf','dianzhen1.ttf','dianzhen1.ttf','dianzhen1.ttf','dianzhen1.ttf','ProggyClenSZ-1.ttf','ProggyCleanSZBP-2.ttf','ProggySquareSZ-3.ttf']
    size = 36
    font = os.path.join('fonts',random.sample(font,1)[0])
    w_w = (314 - 50) / 16
    l_h = (142 - 16) / 3
    _, box, word = Invoice.writeR([50, 314, 16, 66], '----', font, size, print_color, w_w)
    # boxes.append(box)
    _, box, word = Invoice.writeR([50, 314, 41, 66], 'PSAM200160000823', font, size, print_color, w_w)
    # boxes.append(box)
    _, box, word = Invoice.writeR([50, 314, int(16 + l_h + 0.5), 66], '----', font, size, print_color, w_w)
    # boxes.append(box)
    _, box, word = Invoice.writeR([50, 118, 92, 117], 'CCBH', font, size, print_color, w_w)
    # boxes.append(box)
    _, box, word = Invoice.writeR([150, 314, 92, 117], '0201423223',font, size, print_color, w_w)
    # boxes.append(box)
    _, box, word = Invoice.writeR([50, 314, int(16 + l_h * 2 + 0.5), 66], '----', font, size, print_color, w_w)
    # boxes.append(box)

    w_w = (314-113)/11
    l_h = (1008-384)/17
    company = Invoice.get_num(4)
    _, box, word = Invoice.writeR([113,314,384,404],company,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)

    tel = Invoice.get_num(8)
    _, box, word = Invoice.writeR([113,314,384+l_h*1,404],tel,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    taxi_no = Invoice.get_num(7)
    _, box, word = Invoice.writeR([113,314,384+l_h*2,404],taxi_no,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    cer_no = Invoice.get_num(6)
    _, box, word = Invoice.writeR([113,314,384+l_h*3,404],cer_no,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    data = '20{0}_{1:02d}_{2:02d}'.format(random.randint(10,99),random.randint(1,12),random.randint(1,31))
    _, box, word = Invoice.writeR([113,314,384+l_h*4,404],data,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    time = '{0:02d}:{1:02d}-{2:02d}:{3:02d}'.format(random.randint(0,24), random.randint(0,59), random.randint(0,24),random.randint(0,59))
    _, box, word = Invoice.writeR([113,314,384+l_h*5,404],time,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    price = Invoice.get_num(1)+'.'+Invoice.get_num(2)
    _, box, word = Invoice.writeR([113,314,384+l_h*6,404],price,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    distance = Invoice.get_num(2)+'.'+Invoice.get_num(1)
    _, box, word = Invoice.writeR([113,314,384+l_h*7,404],distance,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    wait = '{0:02d}:{1:02d}:{2:02d}'.format(0,random.randint(0,30),random.randint(0,59))
    _, box, word = Invoice.writeR([113,314,384+l_h*8,404],wait,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    state = Invoice.get_num(1)
    _, box, word = Invoice.writeR([113,314,384+l_h*9,404],state,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    fare = '¥'+Invoice.get_num(2)+'.'+Invoice.get_num(2)
    _, box, word = Invoice.writeR([113,314,384+l_h*10,404],fare,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    oil_fare = '¥'+Invoice.get_num(2)+'.'+Invoice.get_num(2)
    _, box, word = Invoice.writeR([113,314,384+l_h*11,404],oil_fare,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    ser_fare = '¥' + Invoice.get_num(2) + '.' + Invoice.get_num(2)
    _, box, word = Invoice.writeR([113,314,384+l_h*12,404],ser_fare,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    total = '¥' + str(random.randint(20,999)) + '.' + Invoice.get_num(2)
    _, box, word = Invoice.writeR([113,314,384+l_h*13,404],total,font,size,print_color,w_w)
    boxes.append(box)
    words_list.append(word)
    _, box, word = Invoice.writeR([113,314,384+l_h*14,404],'----',font,size,print_color,w_w)
    # boxes.append(box)
    _, box, word = Invoice.writeR([113,314,384+l_h*15,404],'----',font,size,print_color,w_w)
    # boxes.append(box)
    _, box, word = Invoice.writeR([113,314,384+l_h*16,404],'----',font,size,print_color,w_w)
    # boxes.append(box)

    # Invoice.img.show()
    return Invoice.img,boxes,words_list

def blur_A(img,a):
    if isinstance(a,tuple):
        a = int(random.uniform(a[0],a[1]))
    img = cv2.blur(img,(a,a))
    return img

def color_jitter(img):
    #hue
    img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    hue_add = random.uniform(-10,10)
    img[:,:,0] = img[:,:,0]+hue_add
    img = cv2.cvtColor(img,cv2.COLOR_HSV2RGB)
    return img

def copy_img(background,img,bbox_list,words_list):
    alpha = random.randint(-20,20)

    h, w = img.shape[:2]

    img = Image.fromarray(img)
    img = img.rotate(alpha, expand=True)
    img = np.asarray(img)

    h_t,w_t = img.shape[:2]

    b_h,b_w = background.shape[:2]

    put_h = random.randint(0,b_h-h_t)
    put_w = random.randint(0,b_w-w_t)

    roi = background[put_h:put_h+h_t,put_w:put_w+w_t]

    # 创建掩膜
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # 保留除logo外的背景
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    dst = cv2.add(img1_bg, img)  # 进行融合
    background[put_h:put_h + h_t, put_w:put_w + w_t] = dst  # 融合后放在原图上

    bbox = np.asarray(bbox_list)
    bbox = np.reshape(bbox,[-1,2])
    s = math.sin(math.radians(-alpha))
    c = math.cos(math.radians(-alpha))
    t = np.asarray([[c, s], [-s, c]])

    bbox[:,0] = bbox[:,0] - w//2
    bbox[:,1] = bbox[:,1] - h//2
    bbox = np.dot(bbox,t)
    bbox[:,0] = bbox[:,0] + w_t//2
    bbox[:,1] = bbox[:,1] + h_t//2
    bbox = np.reshape(bbox,[-1,4,2])
    bbox = bbox.astype('int32')

    bbox[:, :, 0] = bbox[:,:,0] + put_w
    bbox[:, :, 1] = bbox[:,:,1] + put_h
    bbox = bbox.astype('int32')

    d = random.randint(0,put_h)
    u = random.randint(put_h+h_t,b_h)
    l = random.randint(0,put_w)
    r = random.randint(put_w+w_t,b_w)

    background = background[d:u,l:r]
    bbox[:,:,0] = bbox[:,:,0] - l
    bbox[:,:,1] = bbox[:,:,1] - d

    return background,bbox,words_list

def get_pic(bg_dir,out_dir,id):
    try:
        img, boxes,words = get_Invoice()
        # img.show()
        bg_list = os.listdir(bg_dir)
        bg_path = os.path.join(bg_dir,random.sample(bg_list,1)[0])
        bg = Image.open(bg_path)
        img = np.asarray(img).copy()
        bg = np.asarray(bg).copy()

        img,boxes,words = copy_img(bg,img,boxes,words)
        img = Image.fromarray(img)
        img.save(os.path.join(out_dir,'train_img/img_'+str(id)+'_.jpg'))

        with open(os.path.join(out_dir,'train_gt/gt_img_'+str(id)+'_.txt'), 'w', encoding='utf-8') as txt:
            for box, w in zip(boxes, words):
                box.reshape(-1)
                a = ''.join(str(i) + ',' for i in box.reshape(-1))
                a = a + w + '\n'
                txt.write(a)
    except BaseException as e:
        print(id,e)

if __name__ == '__main__':
    get_pic('bg','out',1)
    for i in range(10):
        get_pic('bg', 'out', i)
    #
    # bg_dir = '/home/huguanghao2/Data/DIV2K/DIV2K_valid_HR'
    # out_dir = '/home/huguanghao2/Data/Invoice'
    # from tqdm import tqdm
    # import multiprocessing as mlp
    # from multiprocessing import Pool
    #
    # # 任务数量
    # num = 10000
    #
    # # # 子任务
    # def task(a, b):
    #     print('sub task')
    #     for index in tqdm(range(a,b)):
    #         get_pic(bg_dir,out_dir,index)
    #
    # # 线程池
    # p = Pool()
    # n_cpu = mlp.cpu_count()
    # split = num // n_cpu
    #
    # for i in range(n_cpu):
    #     a = split * i
    #     if i == n_cpu - 1:
    #         b = num
    #     else:
    #         b = split * (i + 1)
    #     p.apply_async(task, args=(a, b))
    #
    # p.close()
    # p.join()