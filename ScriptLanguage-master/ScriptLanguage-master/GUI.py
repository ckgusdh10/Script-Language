from tkinter import *
from LoadAPI import *
window = Tk()
window.geometry("730x250")
def process():
    text = str(inputText.get())
    if state == Search.CustNo:
        getInfoDataFromname(text)
    elif state == Search.BasicInfo:
        getInfoFromNum(text)
    elif state == Search.StockIn:
        getStockFromNum(text)
    elif state == Search.FinancialMean:
        getInfoFromKey(text)

class Search(enum.Enum):
    CustNo = 0
    BasicInfo = 1
    FinancialMean = 2
    StockIn = 3
state = Search.CustNo

def IssucoCustno():
    global check
    global searchList1
    global searchList2
    global state
    searchList1.destroy()
    searchList2.destroy()
    searchList1 = Listbox(window, width=20)
    searchList1.place(x=110, y=50)
    searchList2 = Listbox(window, width=20)
    searchList2.place(x=420, y=50)
    state = Search.CustNo


def IssucoBasicInfo():
    global check
    global searchList1
    global searchList2
    global state
    searchList1.destroy()
    searchList2.destroy()
    searchList1 = Listbox(window, width=61)
    searchList1.place(x=110, y=50)
    state = Search.BasicInfo


def FinancialTermMeaning():
    global check
    global searchList1
    global searchList2
    global state
    searchList1.destroy()
    searchList2.destroy()
    searchList1 = Listbox(window, width=30)
    searchList1.place(x=110, y=50)
    searchList2 = Listbox(window, width=20)
    searchList2.place(x=420, y=50)
    state = Search.FinancialMean


def StockInfo():
    global check
    global searchList1
    global searchList2
    global state
    searchList1.destroy()
    searchList2.destroy()
    searchList1 = Listbox(window, width=30)
    searchList1.place(x=110, y=50)
    searchList2 = Listbox(window, width=20)
    searchList2.place(x=420, y=50)
    state = Search.StockIn

def start():
    global  check
    global searchList1
    global searchList2
    global inputText
    searchList1 = Listbox(window, width=42)
    searchList1.place(x=110, y=50)
    searchList2 = Listbox(window, width=42)
    searchList2.place(x=420, y=50)
    button1 = Button(window, text="발행정보\n조회", font = 20,cursor="hand2",command = IssucoCustno)
    button1.place(x=10,y=10)
    button2 = Button(window, text="기업정보\n조회", font = 20,cursor="hand2", command = IssucoBasicInfo)
    button2.place(x=10,y=70)
    button3 = Button(window, text="주식정보\n조회", font = 20,cursor="hand2", command = StockInfo)
    button3.place(x=10,y=130)
    button4 = Button(window, text="금융용어\n조회", font = 20,cursor="hand2", command = FinancialTermMeaning)
    button4.place(x=10,y=190)
    inputText = Entry(window,width = 50,font = 10)
    inputText.place(x = 110, y = 10)
    button5 = Button(window, text="검색", font=20, cursor="hand2", command=process)
    button5.place(x=670,y=10)
    window.mainloop()

check = False




