import keyboard
import pyperclip
import customtkinter as ctk
import pyauto_desktop
from CTkToolTip import CTkToolTip
from pyexpat.errors import messages

from 函数 import lenn,wbfg,swj
import sys, os

zhuangt = '主界面'
zd = False#置顶
kg = True#读取
txsb = False#图像识别

class setting:

    def __init__(self, name, text, w, h, grid):
        self.name = name
        self.text = text
        self.w = w
        self.h = h
        self.str2 = grid

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(os.path.abspath("."), relative)
   # 打包前后都能用

#读取文本并翻译
with open('设置.txt', 'a+', encoding='utf-8') as f:

    f.seek(0)
    content = f.read()

    if content.strip() == '':
        f.write('起点快捷键:/\n落点快捷键:*\n提交快捷键:-\n置顶开启与关闭(输快捷键):+\n置顶透明度(0-100透明度越来低):70'
                '\n------------以下为调试选项--------------'
                '\n输入框1:1\n输入框2:1\n提交:1\n读取:1\n置顶:1\n文本:1'
                )

    f.seek(0)

    int1 = 0
    listaj = []

    for line in f:
        listaj.append('')
        line1 = line.strip()
        if int1 == 0:#输入框1
            listaj[0]=wbfg(line1,['起点快捷键:'])[0]
        elif int1 == 1:#输入框2
            listaj[1]=wbfg(line1,['落点快捷键:'])[0]
        elif int1 == 2:#提交
            listaj[2]=wbfg(line1,['提交快捷键:'])[0]
        elif int1 == 3:  #置顶快捷键
            listaj[3] = wbfg(line1, ['置顶开启与关闭(输快捷键):'])[0]
        elif int1 == 4:  #透明度
            listaj[4] = wbfg(line1, ['置顶透明度(0-100透明度越来低):'])[0]
        #调试
        elif int1 == 6:
            listaj[6] = wbfg(line1, ['输入框1:'])[0]
        elif int1 == 7:
            listaj[7] = wbfg(line1, ['输入框2:'])[0]
        elif int1 == 8:
            listaj[8] = wbfg(line1, ['提交:'])[0]
        elif int1 == 9:
            listaj[9] = wbfg(line1, ['读取:'])[0]
        elif int1 == 10:
            listaj[10] = wbfg(line1, ['置顶:'])[0]
        elif int1 == 11:
            listaj[11] = wbfg(line1, ['文本:'])[0]

        int1 += 1

    line_count = int1
#------------------------------------------osr----------------------------------------------------

screen0 = pyauto_desktop.Session(
    screen=1,
    source_resolution=(1920, 1080),
    source_dpr=1.0,
    scaling_type="dpr"
)#定义屏幕

region = (81, 194, 119, 29)

#-------------------------------------------------------------------------------------------

#外观
ctk.set_appearance_mode('System')
#主题颜色
ctk.set_default_color_theme('blue')
#窗口设置
root = ctk.CTk()
root.title('迫击炮 @ZhilLw17')
root.iconbitmap(resource_path('1145.ico'))
#限死分辨率
#root.minsize(200, 200)
#root.maxsize(200, 200)

#root.configure(width=200, height=200)
#root.grid_propagate(False)

#计算
def on_click(name):

    global kg,zd,zhuangt,txsb

    if name == '提交':

        text1 = entry1.get()
        text2 = entry2.get()

        if text1.strip() == '' or text2.strip() == '':
            label.configure(text='数据异常')
        else:
            answer1145 = lenn(text1, text2)
            label.configure(text=f'距离{answer1145[0]*100:.2f}米,方位角{answer1145[1]}')

    if name == '读取开关':
        if kg == True:
            label.configure(text='等待输入')
            btn2.configure(text='读取已关闭')
            kg = False
        else:
            label.configure(text=f'{listaj[0]}键为读取起始 {listaj[1]}键为读取目标 \n{listaj[2]}键提交 {listaj[3]}键置顶')
            btn2.configure(text='读取已开启')
            kg = True

    if name == '置顶开关':
        if zd:
            btn3.configure(text='置顶已关闭')
            zd = False
            root.attributes('-topmost', False)
            root.overrideredirect(False)
            root.attributes('-alpha', 1)
            recover_buttons()

        else:
            btn3.configure(text='置顶已开启')
            zd = True
            root.attributes('-topmost', True)
            root.overrideredirect(True)
            root.attributes('-alpha', float(listaj[4])/100)
            remove_buttons()
            if not kg:
                on_click('读取开关')

    if name == '图像识别':

        if txsb:
            txsb = False
            label_st.configure(text='图像识别已关闭')
        else:
            txsb = True
            label_st.configure(text='图像识别已开启')

    if name == '设置':
        zhuangt = '设置'

    if name == '返回':
        zhuangt = '主界面'

    reflash_grid()

#----------------------------------------------------拖动条信息-----------------------------------------------------------------

def slider1_change(value):  # 获取滑块数值填入value
    global listaj

    listaj[4] = value
    tooltip.configure(message=f'置顶透明度为{int(listaj[4])}%')
    label_st.configure(text=f'置顶透明度为{int(listaj[4])}%')

#-------------------------------------------------获取窗口状态-----------------------------------------------------------------

def get_windows():#拿实际分辨率
    window_w = root.winfo_width()
    window_h = root.winfo_height()
    return window_w, window_h


#-------------------------------------------------控件的位置排列,出现与否--------------------------------------------------------

def u_ety(name,act):#输入框

    if name == 0:#起始输入框
        if act:
            entry1.grid()
        else:
            entry1.grid_remove()
    if name == 1:#目标输入框
        if act:
            entry2.grid()
        else:
            entry2.grid_remove()

def u_btn(name,act):#按钮
    global zd,kg,zhuangt

    if name == 0:#提交
        if act:
            btn1.grid()
        else:
            btn1.grid_remove()

    if name == 1:#读取
        if act:
            btn2.grid()
        else:
            btn2.grid_remove()

    if name == 2:#置顶
        if act:
            btn3.grid()
        else:
            btn3.grid_remove()

    if name == 3:#设置
        if act:
            btn4.grid()
        else:
            btn4.grid_remove()

    if name == 4:#返回
        if act:
            btn5.grid()
        else:
            btn5.grid_remove()

    if name == 5:#图像识别
        if act:
            btn6.grid()
        else:
            btn6.grid_remove()

def u_lbl(name,act):

    if name == 0:#label
        if act:
            label.grid()
        else:
            label.grid_remove()

    if name == 1:#设置界面活动提示
        if act:
            label_st.grid()
        else:
            label_st.grid_remove()

def u_fme(name,act):

    if name == 0:#f1
        if act:
            frame1.grid()
        else:
            frame1.grid_remove()
    if name == 1:#f2
        if act:
            frame2.grid()
        else:
            frame2.grid_remove()
    if name == 2:#f3
        if act:
            frame3.grid()
        else:
            frame3.grid_remove()

#--------------------------------------------------------------定义控件-----------------------------------------------------------------

#控件组
frame1 = ctk.CTkFrame(root)#主界面控件
frame2 = ctk.CTkFrame(root)#主界面文本
frame3 = ctk.CTkFrame(root)#设置
frame1.grid(row=0, column=0, sticky='nsew')
frame2.grid(row=1, column=0, sticky='nsew')
frame3.grid(row=0, column=0, sticky='nsew')

#输入框
entry1 = ctk.CTkEntry(frame1,width=150,height=40, placeholder_text='起始xy',font=('微软雅黑',18,'bold'))
entry2 = ctk.CTkEntry(frame1,width=150,height=40, placeholder_text='目标xy',font=('微软雅黑',18,'bold'))
entry1.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky='nsew')
entry2.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky='nsew')

#按钮
btn1 = ctk.CTkButton(frame1, text='提交', command=lambda: on_click('提交'),width=150,height=30,font=('微软雅黑',18,'bold'))
btn4 = ctk.CTkButton(frame1, text='设置', command=lambda: on_click('设置'),width=150,height=30,font=('微软雅黑',18,'bold'))
btn2 = ctk.CTkButton(frame1, text='读取已开启', command=lambda: on_click('读取开关'),width=100,height=30,font=('微软雅黑',15,'bold'))#默认开启
btn3 = ctk.CTkButton(frame1, text='置顶已关闭', command=lambda: on_click('置顶开关'),width=100,height=30,font=('微软雅黑',15,'bold'))#默认关闭
btn5 = ctk.CTkButton(frame3, text='返回', command=lambda: on_click('返回'),width=150,height=30,font=('微软雅黑',15,'bold'))
btn6 = ctk.CTkButton(frame3, text='图像识别(实验性)', command=lambda: on_click('图像识别'),width=150,height=30,font=('微软雅黑',13,'bold'))#默认关闭
btn1.grid(row=1, column=0, columnspan=1, padx=10, pady=5, sticky='nsew')
btn4.grid(row=1, column=1, columnspan=1, padx=10, pady=5, sticky='nsew')
btn2.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky='nsew')
btn3.grid(row=2, column=1, columnspan=1, padx=10, pady=10, sticky='nsew')
btn5.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky='nsew')
btn6.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky='nsew')

#文本
label = ctk.CTkLabel(frame2, text=f'{listaj[0]}键为读取起始 {listaj[1]}键为读取目标 \n{listaj[2]}键提交 {listaj[3]}键置顶',font=('微软雅黑',16,'bold'))
label_st = ctk.CTkLabel(frame3, text='---',font=('微软雅黑',16,'bold'))
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
label_st.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

#滑块
slider_tmd = ctk.CTkSlider(frame3, from_=0, to=100, number_of_steps=100, command=slider1_change)
slider_tmd.set(float(listaj[4]))
slider_tmd.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
#绑定tooltip到滑块
tooltip = CTkToolTip(slider_tmd, message=f'置顶透明度是{int(listaj[4])}%')

#-----------------------------------------------------------控件实时刷新区-----------------------------------------------------------------------
def remove_allgrid():

    a = False

    u_ety(0, a)  # et1
    u_ety(1, a)  # et2
    u_btn(0, a)  # bt1
    u_btn(1, a)  # bt2
    u_btn(2, a)  # bt3
    u_lbl(0, a)  # label
    u_fme(0, a)  # frame1
    u_fme(1, a)  # frame2
    u_fme(2, a)  # frame3
    u_btn(3, a)  # 设置

    root.update_idletasks()
    reflash_root()

def reflash_grid():
    global zhuangt

    list1 = []
    remove_allgrid()

    # 界面控件出现与消失
    if zhuangt == '主界面':

        for i in range(line_count - 6):
            if listaj[i + 6] == '1':
                list1.append(True)
            else:
                list1.append(False)

        u_ety(0, list1[0])  # et1
        u_ety(1, list1[1])  # et2
        u_btn(0, list1[2])  # bt1
        u_btn(1, list1[3])  # bt2
        u_btn(2, list1[4])  # bt3
        u_lbl(0, list1[5])  # label
        u_fme(0, True) # frame1
        u_fme(1, True) # frame2
        u_btn(3, True) # 设置

    elif zhuangt == '设置':
        u_btn(4, True)
        u_btn(5, True)
        u_lbl(1, True)
        u_fme(2, True)

    root.update_idletasks()
    reflash_root()
#------------------------------------------------------------------------------------------------------------------------------------------
#字号的动态适应
#def on_resize(event):
    #if event.widget != root:#忽略不是窗口拉伸导致的字号调整
        #return
    #h = label.winfo_width()
    #size = 16
    #label.configure(font=('微软雅黑',size,'bold'))

#窗口变化时自动拉伸字体
#root.bind('<Configure>', on_resize)

children1 = len(frame1.winfo_children())#计算f1中控件的数量,frame1.winfo_children()是返回包含控件的列表
children2 = len(frame2.winfo_children())
children_root = len(root.winfo_children())

#拉伸控件组
for i in range(children1):
    frame1.grid_columnconfigure(i, weight=1)
    frame1.grid_rowconfigure(i, weight=1)
for i in range(children2):
    frame2.grid_columnconfigure(i, weight=1)
    frame2.grid_rowconfigure(i, weight=1)
for i in range(children_root):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

#动态刷新窗口尺寸

def reflash_root():
    x = root.winfo_x()
    y = root.winfo_y()
    root.update_idletasks()
    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    root.geometry(f'{w}x{h}+{x}+{y}')

#置顶移除区
def remove_buttons():
    u_btn(0, False)
    root.update_idletasks()
    reflash_root()
#置顶恢复区
def recover_buttons():
    u_btn(0, True)
    root.update_idletasks()
    reflash_root()

def on_key(event):

    global txsb

    if kg:
        if event.name == listaj[0]:
            if txsb:
                # 图像识别
                text = screen0.read_text(region=region, mode='restore', use_det=True)
                #删冗余词汇
                str1 = wbfg(text[0], ['x', 'X', ','])[0]
                if str1[len(str1) - 1] == '.' or str1[len(str1) - 1] == ',':
                    str1 = swj(str1, 1, 'r')
                str2 = wbfg(text[1], ['y', 'Y', ',', '|', listaj[0], listaj[1], listaj[2]])[0]
                if str2[len(str2) - 1] == '.' or str2[len(str2) - 1] == ',':
                    str2 = swj(str2, 1, 'r')

                zt1 = f'x{str1},y{str2}'
            else:
                zt1 = pyperclip.paste()

            entry1.delete(0, 'end')
            entry1.insert(0, f'{zt1}')

        elif event.name == listaj[1]:

            if txsb:

                text = screen0.read_text(region=region, mode='restore', use_det=True)

                str1 = wbfg(text[0],['x','X',','])[0]
                if str1[len(str1)-1] == '.' or str1[len(str1)-1] == ',':
                    str1 = swj(str1, 1, 'r')
                str2 = wbfg(text[1],['y','Y',',','|', listaj[0], listaj[1], listaj[2]])[0]
                if str2[len(str2) - 1] == '.' or str2[len(str2) - 1] == ',':
                    str2 = swj(str2, 1, 'r')

                zt2 = f'x{str1},y{str2}'

            else:
                zt2 = pyperclip.paste()

            entry2.delete(0, 'end')
            entry2.insert(0, f'{zt2}')

        elif event.name == listaj[2]:
            on_click('提交')

        elif event.name == listaj[3]:
            on_click('置顶开关')

    else:
        pass

keyboard.on_press(on_key)

def on_closing():
    keyboard.unhook_all()
    root.destroy()

#将点X的行为改成on_closing
root.protocol('WM_DELETE_WINDOW', on_closing)
root.resizable(False, False)

#拖动窗口
def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    x = root.winfo_x() + (event.x - root.x)
    y = root.winfo_y() + (event.y - root.y)
    root.geometry(f'+{x}+{y}')

#绑定拖动区
frame1.bind('<Button-1>', start_move)
frame1.bind('<B1-Motion>', do_move)
frame2.bind('<Button-1>', start_move)
frame2.bind('<B1-Motion>', do_move)
label.bind('<Button-1>', start_move)
label.bind('<B1-Motion>', do_move)

reflash_grid()

root.mainloop()