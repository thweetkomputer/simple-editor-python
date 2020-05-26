import tkinter.filedialog
import tkinter.messagebox
from tkinter import *
import numpy as np
#import matplotlib.pyplot as plt
import re
fileName = ''#初始化文件名
content_in_text = ''#初始化文本框内变量
content_of_file = ''#初始化
content_used = ''
#建立停用词表
del_content = open('停用词表.txt','r')
del_word=del_content.read()
delList = del_word.split()
#1
root = Tk() #建立窗口
root.title("editor1.0")

text = Text(root,width = 30, height = 10)
scroll = Scrollbar()
# side放到窗体的哪一侧,  fill填充
scroll.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT, fill=Y)
# 关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
#设计带滚轮的文本框
text.pack()
#2
FileButton = Button(root,text='openfile',command = lambda:callback())
FileButton.pack()
def callback():
    global fileName,content_of_file,content_used
    fileName =filedialog.askopenfilename(filetypes=[("Text",".txt")])
    content_of_file = open(fileName)
    content_used = content_of_file.read()
    text.delete("1.0",END)
    text.insert(INSERT,content_used)#将文件内容加入到文本框中
def callback2(self):
    global fileName,content_of_file,content_used
    fileName =filedialog.askopenfilename(filetypes=[("Text",".txt")])
    content_of_file = open(fileName)
    content_used = content_of_file.read()
    text.delete("1.0",END)
    text.insert(INSERT,content_used)#将文件内容加入到文本框中
FileButton.bind_all('<Control-o>',callback2)
#获得文件名
#3
ReturnButton = Button(root,text='show text',command = lambda:ReturnText())
ReturnButton.pack()
def ReturnText():
    text.delete("1.0",END)
    text.insert(INSERT,content_used)
#4
countButton = Button(root,text = 'count words',command = lambda:count_word())
countButton.pack()
def count_word():
    content_in_text = text.get("1.0",END)
    word_list = re.findall('[a-zA-Z]+',content_in_text)
    word_dict = {}
    for i in range(len(word_list)):
        word = word_list[i].lower()
        if not word_dict.get(word,0):
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    count_list = []
    for i in word_dict:
        if i not in delList:
            count_list.append([i,word_dict[i]])
    count_list_2 = sorted(count_list,key = by)
    count_list_2.reverse()
    text.delete("1.0",END)
    text.insert(INSERT,"total:"+str(len(word_list))+"\n")
    text.insert(INSERT,"number of words:"+str(len(count_list_2))+"\n")
    for i in range(len(count_list_2)):
        text.insert(INSERT,str(count_list_2[i][0])+':'+str(count_list_2[i][1])+'\n')
    import matplotlib.pyplot as plt

    x_list = [word[0] for word in count_list_2]
    y_list = [word[1] for word in count_list_2]
    plt.barh(range(len(y_list)), y_list,color = 'rgb',tick_label=x_list)
    plt.show()
def by(t):
    return t[1]
#5
InfoButton = Button(root,text = 'keyword',command = lambda:showInfo())
InfoButton.pack()
def showInfo():
    content_in_text = text.get("1.0",END)
    word_list = re.findall('[a-zA-Z]+',content_in_text)
    word_dict = {}
    for i in range(len(word_list)):
        word = word_list[i].lower()
        if not word_dict.get(word,0):
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    count_list = []
    for i in word_dict:
        if i not in delList:
            count_list.append([i,word_dict[i]])
    count_list_2 = sorted(count_list,key = by)
    count_list_2.reverse()
    text.delete("1.0",END)
    for i in range(6):
        text.insert(INSERT,str(i+1)+':'+str(count_list_2[i][0])+':'+str(count_list_2[i][1])+'\n')
#6
FindButton = Button(root,text='find',command=lambda:findword())
FindButton.pack()
def findword():
    win = Tk()
    win.title("find")
    Label2=Label(win,text='find：')
    Label2.pack()
    entry3=Entry(win,width=10)
    entry3.pack()
    OKButton3 = Button(win,text='OK',command=lambda:fin(entry3,win))
    OKButton3.pack()
def findword2(self):
    win = Tk()
    win.title("find")
    Label2=Label(win,text='find：')
    Label2.pack()
    entry3=Entry(win,width=10)
    entry3.pack()
    OKButton3 = Button(win,text='OK',command=lambda:fin(entry3,win))
    OKButton3.pack()
FindButton.bind_all('<Control-f>',findword2)

def fin(entry3,win):
    global text
    text.tag_config('tag1', foreground='green')
    word3 = entry3.get()
    Len = len(word3)
    win.destroy()
    content = text.get("1.0",END)
    cnt = 0
    ibox = [-9999]
    for i in range(len(content)-Len):
        if content[i:i+Len]==word3 and i-ibox[-1]>=Len:#通过判断字符串的方法进行替换，注意定义遍历的范围防止越界报错
            ibox.append(i)
            cnt+=1
    if cnt==0:
        messagebox.showerror('fail','fail')
    else:
        messagebox.showinfo('success','find'+str(cnt))
    if cnt!=0:
        text.delete("1.0",END)
        text.insert(INSERT,content[:ibox[1]])
        text.insert(INSERT,word3,'tag1')
        if cnt>1:
            for j in range(2,len(ibox)):
                text.insert(INSERT,content[ibox[j-1]+Len:ibox[j]])
                text.insert(INSERT,word3,'tag1')
        text.insert(INSERT,content[ibox[-1]+Len:])
#7
ReplaceButton = Button(root,text='replace',command=lambda:replace())
ReplaceButton.pack()
def replace():
    win = Tk()
    win.title("replace")#定义替换界面
    entry1=Entry(win,width=10)
    entry1.pack()
    Label1=Label(win,text='replace with:')
    Label1.pack()
    entry2=Entry(win,width=10)
    entry2.pack()#设置两个Entry用于读入进行操作的参数
    OKButton2 = Button(win,text='OK',command=lambda:change(entry1,entry2,win))
    OKButton2.pack()
    win.mainloop()
def replace2(self):
    win = Tk()
    win.title("replace")#定义替换界面
    entry1=Entry(win,width=10)
    entry1.pack()
    Label1=Label(win,text='replace with:')
    Label1.pack()
    entry2=Entry(win,width=10)
    entry2.pack()#设置两个Entry用于读入进行操作的参数
    OKButton2 = Button(win,text='OK',command=lambda:change(entry1,entry2,win))
    OKButton2.pack()
    win.mainloop()
ReplaceButton.bind_all('<Control-r>',replace2)

def change(entry1,entry2,win):
    word1 = entry1.get()
    word2 = entry2.get()
    Len = len(word1)
    win.destroy()
    content = text.get("1.0",END)
    for i in range(len(content)-Len):
        if content[i:i+Len]==word1:#通过判断字符串的方法进行替换，注意定义遍历的范围防止越界报错
            content1=content[:i]
            content3=content[i+Len:]
            content=content1+word2+content3
    text.delete("1.0",END)
    text.insert(INSERT,content)
#8
DeleteButton = Button(root,text='delete',command=lambda:Delete())
DeleteButton.pack()
def Delete():
    win = Tk()
    win.title("delete")
    Label2=Label(win,text='delete:')
    Label2.pack()
    entry3=Entry(win,width=10)
    entry3.pack()
    OKButton3 = Button(win,text='OK',command=lambda:Del(entry3,win))
    OKButton3.pack()
def Delete2(self):
    win = Tk()
    win.title("delete")
    Label2=Label(win,text='delete：')
    Label2.pack()
    entry3=Entry(win,width=10)
    entry3.pack()
    OKButton3 = Button(win,text='OK',command=lambda:Del(entry3,win))
    OKButton3.pack()
DeleteButton.bind_all('<Control-d>',Delete2)

def Del(entry3,win):
    word3 = entry3.get()
    Len = len(word3)
    win.destroy()
    content = text.get("1.0",END)
    for i in range(len(content)-Len):
        if content[i:i+Len]==word3:#通过判断字符串的方法进行替换，注意定义遍历的范围防止越界报错
            content1=content[:i]
            content2=content[i+Len:]
            content=content1+content2
    text.delete("1.0",END)
    text.insert(INSERT,content)

#9
ListButton = Button(root,text = 'stopwords',command = lambda:showList())
ListButton.pack()
def showList():
    text.delete("1.0",END)
    del_content = open('stopwords.txt','r')
    global del_word
    del_word=del_content.read()
    delList = del_word.split()
    text.insert(INSERT,del_word)
#10
SaveListButton = Button(root,text = 'savestopwords',command = lambda:saveList())
SaveListButton.pack()
def saveList():
    Content = text.get("1.0",END)
    File = open("stopwords.txt",'w')
    File.write(Content)
    File.close()
#11
SaveButton = Button(root,text='save',command = lambda:save())
SaveButton.pack()
def save():
    content = text.get("1.0",END)
    File = open(fileName,'w')
    File.write(content)
    File.close()#修改文件
def save2(self):
    content = text.get("1.0",END)
    File = open(fileName,'w')
    File.write(content)
    File.close()#修改文件
    SaveButton.bind_all('<Control-s>',save2)

#12
ExitButton = Button(root,text = 'exit',command=lambda:Exit())
ExitButton.pack()
def Exit():
    if fileName=='':
        root.destroy()
        return 
    File = open(fileName,'r')
    Content=File.read()#获得当前文件实际内容
    NOW = text.get("1.0",END)#获得文本框内容
    if NOW==Content:#判断是否提醒
        root.destroy()
    else:#如果当前文本框的内容和实际内容不同
        global win2
        win2 = Tk()
        win2.title("EXIT")
        label = Label(win2,text='do you save it?')
        label.pack()
        ButtonSave = Button(win2,text='Save',command=lambda:save2())
        ButtonSave.pack()
        ButtonExit = Button(win2,text='No',command=lambda:exit2())
        ButtonExit.pack()
def save2():
    win2.destroy()
    save()
    root.destroy()
def exit2():
    win2.destroy()
    root.destroy()

root.mainloop()
