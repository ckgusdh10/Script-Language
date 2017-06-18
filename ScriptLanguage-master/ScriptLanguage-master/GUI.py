from tkinter import *
from LoadAPI import *
import pygame
pygame.mixer.init()
window = Tk()
cSound = pygame.mixer.Sound("click.wav")

def process():
    global dic
    global cSound
    cSound.play()
    text = str(inputText.get())
    if state == Search.CustNo:
        dic = getInfoDataFromname(text)
    elif state == Search.BasicInfo:
        dic = getInfoFromNum(text)
    elif state == Search.StockIn:
        dic = getStockFromNum(text)
    elif state == Search.FinancialMean:
        dic = getInfoFromKey(text)
    insertList()
def select():
    global searchList1
    global searchList2
    global dic
    global cSound
    cSound.play()
    searchList2.configure(state='normal')
    searchList2.delete(1.0,END)
    searchList2.insert(INSERT,dic[searchList1.get(searchList1.curselection()[0])])
    searchList2.configure(state='disabled')

class Search(enum.Enum):
    CustNo = 0
    BasicInfo = 1
    FinancialMean = 2
    StockIn = 3
state = Search.CustNo

def IssucoCustno():
    global searchList1
    global searchList2
    global state
    global cSound
    cSound.play()
    searchList1.destroy()
    searchList2.destroy()
    searchList1 = Listbox(window, width=38, height=11)
    searchList1.place(x=110, y=50.5)
    searchList2 = Text(window, width=38, height=14)
    searchList2.place(x=452, y=50)
    state = Search.CustNo


def IssucoBasicInfo():
    global searchList1
    global state
    global cSound
    cSound.play()
    searchList1.destroy()
    searchList2.destroy()
    searchList1 = Text(window, width=87,height = 14)
    searchList1.place(x=110, y=50)
    state = Search.BasicInfo


def FinancialTermMeaning():
    global searchList1
    global searchList2
    global state
    global cSound
    cSound.play()
    searchList1.destroy()
    searchList2.destroy()
    searchList1 = Listbox(window, width=38,height = 11)
    searchList1.place(x=110, y=50.5)
    searchList2 = Text(window, width=38,height = 14)
    searchList2.place(x=452, y=50)
    state = Search.FinancialMean
def insertList():
    global dic
    global searchList1
    global searchList2
    if state == Search.CustNo or state == Search.FinancialMean:
        searchList1.destroy()
        searchList1 = Listbox(window, width=38, height=11)
        searchList1.place(x=110, y=50.5)
        for d in dic.keys():
            searchList1.insert(END,d);
    else:
        searchList1.destroy()
        searchList1 = Text(window, width=87,height = 14)
        searchList1.place(x=110, y=50)
        searchList1.configure(state='normal')
        for d in dic.keys():
            searchList1.insert(END, d + " : " + dic[d]+"\n");
        searchList1.configure(state='disable')

def send_mail():
    #현재 내용을 메일로 전송한다.
    global cSound
    cSound.play()
    import smtplib
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    global state
    global searchList1
    global searchList2
    global dic

    # global value
    host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
    port = "587"
    htmlFileName = "book.xml"

    senderAddr = "pkekzm6239@gmail.com" # 보내는 사람 email 주소.
    recipientAddr = "pkekzm6239@naver.com"  # 받는 사람 email 주소.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "Test email in Python 3.5"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    #htmlFD = open(htmlFileName, 'rb')
    if state == Search.CustNo:
        info1 = MIMEText(searchList1.get(searchList1.curselection()[0]), 'html', _charset='UTF-8')
        msg.attach(info1)
        info2 = MIMEText(dic[searchList1.get(searchList1.curselection()[0])], 'html', _charset='UTF-8')
        msg.attach(info2)
    elif state == Search.BasicInfo:
        info2 = MIMEText(searchList1.get(1.0,END), 'html', _charset='UTF-8')
        msg.attach(info2)
    elif state == Search.FinancialMean:
        info2 = MIMEText(dic[searchList1.get(searchList1.curselection()[0])], 'html', _charset='UTF-8')
        msg.attach(info2)

    # 메일을 발송한다.
    s = smtplib.SMTP(host, port)
    # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("pkekzm6239@gmail.com","vosalxld!0625")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

def start2():
    window.geometry("730x250")
    global check
    global searchList1
    global searchList2
    global inputText
    global TitleLabel
    global intoApp
    global cSound
    cSound.play()
    TitleLabel.destroy()
    intoApp.destroy()
    searchList1 = Listbox(window, width=38, height=11)
    searchList1.place(x=110, y=50.5)
    searchList2 = Text(window, width=38, height=14)
    searchList2.place(x=452, y=50)
    button1 = Button(window, text="발행번호\n조회", font = 20,cursor="hand2",command = IssucoCustno)
    button1.place(x=10,y=10)
    button2 = Button(window, text="기업정보\n조회", font = 20,cursor="hand2", command = IssucoBasicInfo)
    button2.place(x=10,y=70)
    button4 = Button(window, text="금융용어\n조회", font = 20,cursor="hand2", command = FinancialTermMeaning)
    button4.place(x=10,y=130)
    button3 = Button(window, text="G - Mail \n전송", font = 20,cursor="hand2", command = send_mail)
    button3.place(x=10,y=190)
    #button7 = Button(window, text="aaa", font=20, cursor="hand2", command=send_mail)
    #button7.place(x=80, y=190)
    buttonS = Button(window, text="Select", font=5, cursor="hand2", command=select)
    buttonS.place(x=380, y=125)
    inputText = Entry(window,width = 50,font = 10)
    inputText.place(x = 110, y = 10)
    button5 = Button(window, text="검색", font=20, cursor="hand2", command=process)
    button5.place(x=670,y=10)
def start():
    global TitleLabel
    global intoApp
    photo = PhotoImage(file="Title.gif")  # 디폴트 이미지 파일

    TitleLabel = Label(window, image=photo)
    TitleLabel.pack()
    intoApp = Button(window, text='클릭', command=start2)
    intoApp.pack()
    window.mainloop()

check = False
