import requests as r
from tkinter import*
import re
h = {
    'Uaer-Agent':'wswp'
}
htmlcode = r.get('https://blog.csdn.net/s/sitemap_index/index_site_map.xml',headers=h)
htmlcode = htmlcode.content.decode('UTF-8')

code = re.findall('<loc>(.*?)</loc>', htmlcode)
# print(code)
# code = '网页：' + code
# print(htmlcode)
# print(code)
c=0


root = Tk()
root.geometry('400x500')
# w = Label(root,text=code,wraplength=800)
# w.pack()

s = Scrollbar(root)
s.pack(side=RIGHT,fill=Y)

lb=Listbox(root,yscrollcommand=s.set)

for i in code:
    # code1 = code[c]
    lb.insert(END,code[c])
    c+=1
lb.pack(side=LEFT,fill=BOTH,expand=True)
s.config(command=lb.yview)
root.mainloop()