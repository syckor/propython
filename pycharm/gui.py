import tkinter as tk
from tkinter import *
from tkinter import messagebox


price = {'아메리카노':3500, '그린티':4000, '카페라떼':4000, '카페모카':4500, '얼그레이':3500, '애플시나몬티':4000,
         '청포도에이드':4000,'타로티':4000, '카라멜마키아또':4500}
order=[]
orderlist=[]
sum = 0
count = 0


#원하는 메뉴 클릭시 textarea에 목록추가
def add(item):
    global sum
    global count

    #텍스트에리아를 리셋시킴
    textarea.delete('1.0', END)

    for i, name in enumerate(orderlist):
        if item in name:
            del orderlist[i]

    count += 1
    this_price = price[item]
    sum += this_price

    orderlist.append()


    #order.append(item)
    textarea.insert(tk.INSERT, orderlist)
    label1['text'] = '금액: ' + str(sum) + "원"


#결제하기 버튼을 눌렀을때 나가진다
def btn_pay():
     msgbox = tk.messagebox.askquestion("확인", '주문을 하시겠습니까?')
     if msgbox == 'yes':
         exit()


window = tk.Tk()
window.title('cafe')
window.geometry('750x600')

frame1=tk.Frame(window)
frame1.pack(side="left")

frame2=tk.Frame(window)
frame2.pack(side="right")

frame3=tk.Frame(frame2)
frame3.pack(side="bottom")
#이미지작업

img0 = PhotoImage(file="./caffemenu/americano.PNG")
img1 = PhotoImage(file="./caffemenu/greentea.PNG")
img2 = PhotoImage(file="./caffemenu/latte.PNG")
img3 = PhotoImage(file="./caffemenu/moca.PNG")
img4 = PhotoImage(file="./caffemenu/muscataid.PNG")
img5 = PhotoImage(file="./caffemenu/apple.PNG")
img6 = PhotoImage(file="./caffemenu/earlgrey.PNG")
img7 = PhotoImage(file="./caffemenu/tarotea.PNG")
img8 = PhotoImage(file="./caffemenu/caramel.PNG")

#메뉴버튼 생성
tk.Button(frame1, image=img0, overrelief='ridge', command=lambda : add('아메리카노')).grid(row=0, column=0)
tk.Button(frame1, image=img1, overrelief='ridge', text='그린티', command=lambda : add('그린티')).grid(row=0, column=1)
tk.Button(frame1, image=img2, overrelief='ridge', text='카페라떼', command=lambda : add('카페라떼')).grid(row=0, column=2)
tk.Button(frame1, image=img3, overrelief='ridge', text='카페모카', command=lambda : add('카페모카')).grid(row=1, column=0)
tk.Button(frame1, image=img4, overrelief='ridge', text='청포도에이드', command=lambda : add('청포도에이드')).grid(row=1, column=1)
tk.Button(frame1, image=img5, overrelief='ridge', text='애플시나몬티', command=lambda : add('애플시나몬티')).grid(row=1, column=2)
tk.Button(frame1, image=img6, overrelief='ridge', text='얼그레이', command=lambda : add('얼그레이')).grid(row=2, column=0)
tk.Button(frame1, image=img7, overrelief='ridge', text='타로티', command=lambda : add('타로티')).grid(row=2, column=1)
tk.Button(frame1, image=img8, overrelief='ridge', text='카라멜마키아또', command=lambda : add('카라멜마키아또')).grid(row=2, column=2)
#tk.Button(frame1, text='exit', command=btn_exit, width=10, height=2).grid(row=4, column=0)

textarea = tk.Text(frame2, width=80)
textarea.pack(side="top")

label1 = tk.Label(frame2, text="금액 : 0원", width=80, height=7, fg="blue")
label1.pack()
tk.Button(frame3, overrelief='ridge', text='취소하기', command=lambda :btn_pay(), width=8, height=3, bg='white').grid(row=0, column=0)
tk.Button(frame3, overrelief='ridge', text='전체취소', command=lambda :textarea.delete('1.0', END),width=8, height=3).grid(row=0, column=1)
tk.Button(frame3, overrelief='ridge', text='결제하기', command=lambda :btn_pay(), width=8, height=3).grid(row=0, column=2)
window.mainloop()
