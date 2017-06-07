from tkinter import *

def start():
    window = Tk()
    window.geometry("730x250")
    button1 = Button(window, text="발행정보\n조회", font = 20,cursor="hand2")
    button1.place(x=10,y=10)
    button2 = Button(window, text="기업정보\n조회", font = 20,cursor="hand2")
    button2.place(x=10,y=70)
    button3 = Button(window, text="주식정보\n조회", font = 20,cursor="hand2")
    button3.place(x=10,y=130)
    button4 = Button(window, text="금융용어\n조회", font = 20,cursor="hand2")
    button4.place(x=10,y=190)
    inputText = Entry(window,width = 50,font = 10)
    inputText.place(x = 110, y = 10)
    button5 = Button(window, text = "검색",font = 20, cursor = "hand2")
    button5.place(x=670,y=10)
    searchList1 = Listbox(window, width=42)
    searchList1.place(x=110, y=50)
    searchList2 = Listbox(window, width=42)
    searchList2.place(x=420, y=50)


    window.mainloop()