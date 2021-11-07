# 창 만들기

from tkinter import *

win = Tk()  # 창 생성

win.geometry('500x500')     # 창 크기 설정
win.title('temp')   # 창 이름 설정
win.option_add('*Font', '맑은고딕 25')    # 폰트 설정
win.configure(bg="red")

btn = Button(win, text="버튼")
btn.pack()

win.mainloop()  # 창 실행
