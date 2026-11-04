import keyboard
import pyperclip
import customtkinter as ctk

from 函数 import lenn,wbfg
import sys, os

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(os.path.abspath("."), relative)
   # 打包前后都能用

#读取文本
with open('设置.txt', 'a+', encoding='utf-8') as f:

    f.seek(0)
    content = f.read()

    if content.strip() == '':
        f.write('起点快捷键:/\n落点快捷键:*\n提交快捷键:-\n置顶开启与关闭(输快捷键):+\n置顶透明度(0-1透明度越来低):0.7'
                '\n------------以下为调试选项--------------'
                '\n输入框1:1\n输入框2:1\n提交:1\n读取:1\n置顶:1\n文本:1')

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
            listaj[4] = wbfg(line1, ['置顶透明度(0-1透明度越来低):'])[0]
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

#外观
ctk.set_appearance_mode('System')
#主题颜色
ctk.set_default_color_theme('blue')
#窗口设置
root = ctk.CTk()
root.title('迫击炮 @ZhilLw17')
root.iconbitmap(resource_path('1145.ico'))

frame1 = ctk.CTkFrame(root)
frame1.grid(row=0, column=0, sticky='nsew')
frame2 = ctk.CTkFrame(root)
frame2.grid(row=1, column=0, sticky='nsew')
#输入框1
entry1 = ctk.CTkEntry(frame1,width=150,height=40, placeholder_text='起始xy')
entry1.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky='nsew')
entry1.configure(font=('微软雅黑',18,'bold'))
#输入框2
entry2 = ctk.CTkEntry(frame1,width=150,height=40, placeholder_text='目标xy')
entry2.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky='nsew')
entry2.configure(font=('微软雅黑',18,'bold'))
#计算
def on_click(name):

    global kg,zd

    if name == '提交':
        text1 = entry1.get()
        text2 = entry2.get()
        if text1.strip() == '' or text2.strip() == '':
            label.configure(text='数据异常')
        else:
            answer1145 = lenn(text1, text2)
            label.configure(text=f'距离{answer1145[0]*100:.2f}米,方位角{answer1145[1]}')

    elif name == '读取开关':
        if kg == True:
            label.configure(text='等待输入(直接粘贴游戏内坐标)')
            btn2.configure(text='读取已关闭')
            kg = False
        else:
            label.configure(text=f'{listaj[0]}键为读取起始 {listaj[1]}键为读取目标 \n{listaj[2]}键提交 {listaj[3]}键置顶')
            btn2.configure(text='读取已开启')
            kg = True

    elif name == '置顶开关':
        if zd == True:
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
            root.attributes('-alpha', float(listaj[4]))
            remove_buttons()
            if not kg:
                on_click('读取开关')

btn1 = ctk.CTkButton(frame1, text='提交', command=lambda: on_click('提交'),width=230,height=40,font=('微软雅黑',18,'bold'))
btn1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

btn2 = ctk.CTkButton(frame1, text='读取已开启', command=lambda: on_click('读取开关'),width=100,height=30,font=('微软雅黑',15,'bold'))
btn2.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky='nsew')
kg = True

btn3 = ctk.CTkButton(frame1, text='置顶已关闭', command=lambda: on_click('置顶开关'),font=('微软雅黑',15,'bold'))
btn3.grid(row=2, column=1, columnspan=1, padx=10, pady=10, sticky='nsew')
zd = False

#字号的动态适应
def on_resize(event):
    if event.widget != root:#忽略不是窗口拉伸导致的字号调整
        return
    #h = label.winfo_width()
    size = 16
    label.configure(font=('微软雅黑',size,'bold'))

#初始化
label = ctk.CTkLabel(frame2, text=f'{listaj[0]}键为读取起始 {listaj[1]}键为读取目标 \n{listaj[2]}键提交 {listaj[3]}键置顶')
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
size = 16
label.configure(font=('微软雅黑',size,'bold'))

#窗口变化时自动拉伸字体
root.bind('<Configure>', on_resize)

children1 = len(frame1.winfo_children())
children2 = len(frame2.winfo_children())
children_root = len(root.winfo_children())

#拉伸控件
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
#移除区
def remove_buttons():
    btn1.grid_forget()
    reflash_root()
#恢复区
def recover_buttons():
    btn1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
    reflash_root()

def on_key(event):

    if kg:
        if event.name == listaj[0]:
            zt1 = pyperclip.paste()
            entry1.delete(0, 'end')
            entry1.insert(0, f'{zt1}')

        elif event.name == listaj[1]:
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

#调试区
list1 = []
for i in range(6):
    if listaj[i+6] == '1':
        list1.append(False)
    else:
        list1.append(True)
if list1[0]:
    entry1.grid_forget()
if list1[1]:
    entry2.grid_forget()
if list1[2]:
    btn1.grid_forget()
if list1[3]:
    btn2.grid_forget()
if list1[4]:
    btn3.grid_forget()
if list1[5]:
    label.grid_forget()

root.mainloop()