import tkinter as tk
import os
import sys
import main.py

cwhite="#fff"
cblack="#000"
cframe="#DDE6F1"
cbut="#6E8FFA"

#вызываем 1 вопрос с главного окна
def ans1(event):
    global answer1
    answer1=0
    #Стираем ненужное
    label0.pack_forget()
    text0.pack_forget()
    but0.pack_forget()
    label2_1.pack_forget()
    label2_2.pack_forget()
    spin2q.pack_forget()
    but2answ.pack_forget()
    but2_2.pack_forget()
    but2_3.pack_forget()
    labelstudent.pack_forget()
    labelcount.pack_forget()
    labelmark.pack_forget()
    butstart.pack_forget()
    butstop.pack_forget()
    #Рисуем нужное 1 блок
    root.title("Первый вопрос")
    root.geometry('900x450')
    label1_1.pack(side=tk.TOP, expand=True)
    spin1q.pack(expand=True)
    but1answ.pack(expand=True)
    but1_2.pack(side=tk.BOTTOM, anchor='e')

#отвечаем на 1 вопрос и сохраняем ответ
def ans1_2(event):
    global answer1
    q = spin1q.get()
    if str(q) == 'Вариант 2':
        label1_2["text"] = "Правильно"
        label1_2.config(fg='#1FDE31')
        label1_2.pack(padx=5, pady=5, anchor='center', expand=True)
        answer1 = 1
    else:
        label1_2["text"] = "Неправильно"
        label1_2.config(fg='#DE1F43')
        label1_2.pack(padx=5, pady=5, anchor='center', expand=True)
        answer1 = 0

#вызываем 2 вопрос с окна 1 или 3 вопроса
def ans2(event):
    global answer2
    answer2 = 0
    label1_1.pack_forget()
    spin1q.pack_forget()
    but1answ.pack_forget()
    label1_2.pack_forget()
    but1_2.pack_forget()
    label3_1.pack_forget()
    spin3q.pack_forget()
    but3answ.pack_forget()
    label3_2.pack_forget()
    but3_2.pack_forget()
    but3_3.pack_forget()
    root.title("Второй вопрос")
    root.geometry('900x450')
    label2_1.pack(padx=5, pady=5, side=tk.TOP, expand=True)
    spin2q.pack(padx=5, pady=5, expand=True)
    but2answ.pack(padx=5, pady=5, expand=True)
    but2_2.pack(side='right', anchor='s')
    but2_3.pack(side='left', anchor='s')

#отвечаем на 2 вопрос и сохраняем ответ
def ans2_2(event):
    global answer2
    q = spin2q.get()
    if str(q) == 'Вариант 1':
        label2_2["text"] = "Правильно"
        label2_2.config(fg='#1FDE31')
        label2_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer2 = 1
    else:
        label2_2["text"] = "Неправильно"
        label2_2.config(fg='#DE1F43')
        label2_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer2 = 0

#вызываем 3 вопрос с окна 2 или 4 вопроса
def ans3(event):
    global answer3
    answer3 = 0
    label2_1.pack_forget()
    spin2q.pack_forget()
    but2answ.pack_forget()
    label2_2.pack_forget()
    but2_2.pack_forget()
    but2_3.pack_forget()
    label4_1.pack_forget()
    spin4q.pack_forget()
    but4answ.pack_forget()
    label4_2.pack_forget()
    but4_2.pack_forget()
    but4_3.pack_forget()
    root.title("Третий вопрос")
    root.geometry('900x450')
    label3_1.pack(padx=5, pady=5, side=tk.TOP, expand=True)
    spin3q.pack(padx=5, pady=5, expand=True)
    but3answ.pack(padx=5, pady=5, expand=True)
    but3_2.pack(side='right', anchor='s')
    but3_3.pack(side='left', anchor='s')

# отвечаем на 3 вопрос и сохраняем ответ
def ans3_2(event):
    global answer3
    q = spin3q.get()
    if str(q) == 'Вариант 4':
        label3_2["text"] = "Правильно"
        label3_2.config(fg='#1FDE31')
        label3_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer3 = 1
    else:
        label3_2["text"] = "Неправильно"
        label3_2.config(fg='#DE1F43')
        label3_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer3 = 0

#вызываем 4 вопрос с окна 3 или 5 вопроса
def ans4(event):
    global answer4
    answer4 = 0
    label3_1.pack_forget()
    spin3q.pack_forget()
    but3answ.pack_forget()
    label3_2.pack_forget()
    but3_2.pack_forget()
    but3_3.pack_forget()
    label5_1.pack_forget()
    spin5q.pack_forget()
    but5answ.pack_forget()
    label5_2.pack_forget()
    but5_2.pack_forget()
    but5_3.pack_forget()
    root.title("Четвёртый вопрос")
    root.geometry('900x450')
    label4_1.pack(padx=5, pady=5, side=tk.TOP, expand=True)
    spin4q.pack(padx=5, pady=5, expand=True)
    but4answ.pack(padx=5, pady=5, expand=True)
    but4_2.pack(side='right', anchor='s')
    but4_3.pack(side='left', anchor='s')

# отвечаем на 4 вопрос и сохраняем ответ
def ans4_2(event):
    global answer4
    q = spin4q.get()
    if str(q) == 'Вариант 1':
        label4_2["text"] = "Правильно"
        label4_2.config(fg='#1FDE31')
        label4_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer4 = 1
    else:
        label4_2["text"] = "Неправильно"
        label4_2.config(fg='#DE1F43')
        label4_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer4 = 0

#вызываем 5 вопрос с окна 4 или 6 вопроса
def ans5(event):
    global answer5
    answer5 = 0
    label4_1.pack_forget()
    spin4q.pack_forget()
    but4answ.pack_forget()
    label4_2.pack_forget()
    but4_2.pack_forget()
    but4_3.pack_forget()
    label6_1.pack_forget()
    spin6q.pack_forget()
    but6answ.pack_forget()
    label6_2.pack_forget()
    but6_2.pack_forget()
    but6_3.pack_forget()
    root.title("Пятый вопрос")
    root.geometry('900x450')
    label5_1.pack(padx=5, pady=5, side=tk.TOP, expand=True)
    spin5q.pack(padx=5, pady=5, expand=True)
    but5answ.pack(padx=5, pady=5, expand=True)
    but5_2.pack(side='right', anchor='s')
    but5_3.pack(side='left', anchor='s')

# отвечаем на 5 вопрос и сохраняем ответ
def ans5_2(event):
    global answer5
    q = spin5q.get()
    if str(q) == 'Вариант 2':
        label5_2["text"] = "Правильно"
        label5_2.config(fg='#1FDE31')
        label5_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer5 = 1
    else:
        label5_2["text"] = "Неправильно"
        label5_2.config(fg='#DE1F43')
        label5_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer5 = 0

#вызываем 6 вопрос с окна 5 или 7 вопроса
def ans6(event):
    global answer6
    answer6 = 0
    label5_1.pack_forget()
    spin5q.pack_forget()
    but5answ.pack_forget()
    label5_2.pack_forget()
    but5_2.pack_forget()
    but5_3.pack_forget()
    label7_1.pack_forget()
    spin7q.pack_forget()
    but7answ.pack_forget()
    label7_2.pack_forget()
    but7_2.pack_forget()
    but7_3.pack_forget()
    root.title("Шестой вопрос")
    root.geometry('900x450')
    label6_1.pack(padx=5, pady=5, side=tk.TOP, expand=True)
    spin6q.pack(padx=5, pady=5, expand=True)
    but6answ.pack(padx=5, pady=5, expand=True)
    but6_2.pack(side='right', anchor='s')
    but6_3.pack(side='left', anchor='s')

# отвечаем на 6 вопрос и сохраняем ответ
def ans6_2(event):
    global answer6
    q = spin6q.get()
    if str(q) == 'Вариант 1':
        label6_2["text"] = "Правильно"
        label6_2.config(fg='#1FDE31')
        label6_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer6 = 1
    else:
        label6_2["text"] = "Неправильно"
        label6_2.config(fg='#DE1F43')
        label6_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer6 = 0

#вызываем 7 вопрос с окна 6 или 8 вопроса
def ans7(event):
    global answer7
    answer7 = 0
    label6_1.pack_forget()
    spin6q.pack_forget()
    but6answ.pack_forget()
    label6_2.pack_forget()
    but6_2.pack_forget()
    but6_3.pack_forget()
    label8_1.pack_forget()
    spin8q.pack_forget()
    but8answ.pack_forget()
    label8_2.pack_forget()
    but8_2.pack_forget()
    but8_3.pack_forget()
    root.title("Седьмой вопрос")
    root.geometry('900x450')
    label7_1.pack(padx=5, pady=5, side=tk.TOP, expand=True)
    spin7q.pack(padx=5, pady=5, expand=True)
    but7answ.pack(padx=5, pady=5, expand=True)
    but7_2.pack(side='right', anchor='s')
    but7_3.pack(side='left', anchor='s')

# отвечаем на 7 вопрос и сохраняем ответ
def ans7_2(event):
    global answer7
    q = spin7q.get()
    if str(q) == 'Вариант 4':
        label7_2["text"] = "Правильно"
        label7_2.config(fg='#1FDE31')
        label7_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer7 = 1
    else:
        label7_2["text"] = "Неправильно"
        label7_2.config(fg='#DE1F43')
        label7_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer7 = 0

#вызываем 8 вопрос с окна 7 или 9 вопроса
def ans8(event):
    global answer8
    answer8 = 0
    label7_1.pack_forget()
    spin7q.pack_forget()
    but7answ.pack_forget()
    label7_2.pack_forget()
    but7_2.pack_forget()
    but7_3.pack_forget()
    label9_1.pack_forget()
    spin9q.pack_forget()
    but9answ.pack_forget()
    label9_2.pack_forget()
    but9_2.pack_forget()
    but9_3.pack_forget()
    root.title("Восьмой вопрос")
    root.geometry('900x450')
    label8_1.pack(padx=5, pady=5, side=tk.TOP, expand=True)
    spin8q.pack(padx=5, pady=5, expand=True)
    but8answ.pack(padx=5, pady=5, expand=True)
    but8_2.pack(side='right', anchor='s')
    but8_3.pack(side='left', anchor='s')

# отвечаем на 8 вопрос и сохраняем ответ
def ans8_2(event):
    global answer8
    q = spin8q.get()
    if str(q) == 'Вариант 3':
        label8_2["text"] = "Правильно"
        label8_2.config(fg='#1FDE31')
        label8_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer8 = 1
    else:
        label8_2["text"] = "Неправильно"
        label8_2.config(fg='#DE1F43')
        label8_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer8 = 0

#вызываем 9 вопрос с окна 8 или 10 вопроса
def ans9(event):
    global answer9
    answer9 = 0
    label8_1.pack_forget()
    spin8q.pack_forget()
    but8answ.pack_forget()
    label8_2.pack_forget()
    but8_2.pack_forget()
    but8_3.pack_forget()
    label10_1.pack_forget()
    spin10q.pack_forget()
    but10answ.pack_forget()
    label10_2.pack_forget()
    but10_2.pack_forget()
    but10_3.pack_forget()
    root.title("Девятый вопрос")
    root.geometry('900x450')
    label9_1.pack(padx=5, pady=5, side=tk.TOP, expand=True)
    spin9q.pack(padx=5, pady=5, expand=True)
    but9answ.pack(padx=5, pady=5, expand=True)
    but9_2.pack(side='right', anchor='s')
    but9_3.pack(side='left', anchor='s')

# отвечаем на 9 вопрос и сохраняем ответ
def ans9_2(event):
    global answer9
    q = spin9q.get()
    if str(q) == 'Вариант 5':
        label9_2["text"] = "Правильно"
        label9_2.config(fg='#1FDE31')
        label9_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer9 = 1
    else:
        label9_2["text"] = "Неправильно"
        label9_2.config(fg='#DE1F43')
        label9_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer9 = 0

#вызываем 10 вопрос с окна 9 вопроса
def ans10(event):
    global answer10
    answer10 = 0
    label10_1.pack_forget()
    spin10q.pack_forget()
    but10answ.pack_forget()
    label10_2.pack_forget()
    but10_2.pack_forget()
    but10_3.pack_forget()
    label9_1.pack_forget()
    spin9q.pack_forget()
    but9answ.pack_forget()
    label9_2.pack_forget()
    but9_2.pack_forget()
    but9_3.pack_forget()
    root.title("Десятый вопрос")
    root.geometry('900x450')
    label10_1.pack(padx=5, pady=5, side=tk.TOP, expand=True)
    spin10q.pack(padx=5, pady=5, expand=True)
    but10answ.pack(padx=5, pady=5, expand=True)
    but10_2.pack(side='right', anchor='s')
    but10_3.pack(side='left', anchor='s')

# отвечаем на 10 вопрос и сохраняем ответ
def ans10_2(event):
    global answer10
    q = spin10q.get()
    if str(q) == 'Вариант 3':
        label10_2["text"] = "Правильно"
        label10_2.config(fg='#1FDE31')
        label10_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer10 = 1
    else:
        label10_2["text"] = "Неправильно"
        label10_2.config(fg='#DE1F43')
        label10_2.pack(padx=5, pady=5, side=tk.BOTTOM, expand=True)
        answer10 = 0

def destr(event):
    root.destroy()

def count(event):
    label10_1.pack_forget()
    spin10q.pack_forget()
    but10answ.pack_forget()
    label10_2.pack_forget()
    but10_2.pack_forget()
    but10_3.pack_forget()
    root.title('Результат')
    root.geometry('400x180')
    if text0.get('1.0', 'end-1c') == '':
        labelstudent.config(text='Незнакомец')
    else:
        labelstudent.config(text=text0.get('1.0', 'end-1c'))
    labelstudent.pack(side='top', anchor='nw')
    labelmark.pack(side='top', anchor='nw')
    mark=answer1*0.45+answer2*0.45+answer3*0.45+answer4*0.5+answer5*0.5+answer6*0.5+answer7*0.5+answer8*0.55+answer9*0.55+answer10*0.55+0.2
    if mark >= 4.2:
        labelcount["text"]=('Оценка "5" баллов')
        labelcount.config(fg='#208815')
    elif mark >= 3.2:
        labelcount["text"]=('Оценка "4" балла')
        labelcount.config(fg='#2BF116')
    elif mark >= 2.2:
        labelcount["text"]=('Оценка "3" балла')
        labelcount.config(fg='#DD9816')
    elif mark >= 1.2:
        labelcount["text"]=('Оценка "2" балла')
        labelcount.config(fg='#FA820E')
    else:
        labelcount["text"]=('Оценка "1" балл')
        labelcount.config(fg='#FA0E0E')
    labelcount.pack(padx=2, pady=2,side='top', anchor='w')
    butstart.pack(side='left', anchor='s')
    butstop.pack(side='right', anchor='s')

def mainwin(event):
    labelcount.pack_forget()
    butstop.pack_forget()
    butstart.pack_forget()
    labelmark.pack_forget()
    labelstudent.pack_forget()
    root.geometry('500x250')
    root.title("Программа тестирования студентов")
    #label0 = tk.Label(frame, text='Введите вашу Фамилию и инициалы:', fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
    label0.pack(padx=2, pady=2, side=tk.TOP, expand=True)
    #text0 = tk.Text(frame, height=1.5, width=20, wrap=tk.WORD)
    text0.pack(padx=2, pady=2, expand=True)
    #but0 = tk.Button(frame, text='Начать тестирование', bg=cbut, fg=cwhite, bd=3)
    #but0.bind("<ButtonRelease-1>", ans1)
    but0.pack(padx=5, pady=5, expand=True)

root = tk.Tk()
root.title("Программа тестирования студентов")
#root.iconbitmap(default="pen.ico")
root.config(bg='#f5f5f5')
root.geometry('500x250')
frame = tk.Frame(root, bg=cframe,  bd=5)
frame.place(relx=0.5, rely=0.5, relwidth=0.85, relheight=0.80, anchor='center')
label0 = tk.Label(frame, text='Введите вашу Фамилию и инициалы:', fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
label0.pack(padx=2, pady=2, side=tk.TOP, expand=True)
text0 = tk.Text(frame, height=1.5, width=20, wrap=tk.WORD)
text0.pack(padx=2, pady=2, expand=True)
but0 = tk.Button(frame, text='Начать тестирование', bg=cbut, fg=cwhite, bd=3)
but0.bind("<ButtonRelease-1>", ans1)
but0.pack(padx=5, pady=5, expand=True)

#start Блок 1 вопроса
label1_1 = tk.Label(frame, text='Вопрос №1\nТекст вопроса\n\nВариант 1\nВариант 2\nВариант 3\n', fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
spin1q = tk.Spinbox(frame, width=10, values=('Вариант 1', 'Вариант 2', 'Вариант 3'), bg=cframe, font=('Times', 10, 'bold'))
but1answ = tk.Button(frame, text='Ответить на вопрос №1\n( правильный 2)', bg=cbut, fg=cwhite, bd=3)
but1answ.bind("<ButtonRelease-1>", ans1_2)
label1_2 = tk.Label(frame, text='Проверка ответа',width=12, height=2, bd=5, fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
but1_2 = tk.Button(frame, text='Следующий вопрос', bg=cbut, fg=cwhite, bd=3)
but1_2.bind("<ButtonRelease-1>", ans2)
#end Блок 1 вопроса

#start Блок 2 вопроса
label2_1=tk.Label(frame, text='Вопрос №2\n\nТекст вопроса\n\nВариант 1\nВариант 2\nВариант 3', fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
spin2q=tk.Spinbox(frame, width=10, values=('Вариант 1','Вариант 2','Вариант 3'), bg=cframe, font=('Times', 10, 'bold'))
but2answ=tk.Button(frame, text='Ответить на вопрос №2\n( правильный 1)', bg=cbut, fg=cwhite, bd=3)
but2answ.bind("<ButtonRelease-1>", ans2_2)
label2_2=tk.Label(frame, text='Проверка ответа', width=12, height=2, fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
but2_2=tk.Button(frame, text='Следующий вопрос', bg=cbut, fg=cwhite, bd=3)
but2_2.bind("<ButtonRelease-1>", ans3)
but2_3=tk.Button(frame, text='Предыдущий вопрос', bg=cbut, fg=cwhite, bd=3)
but2_3.bind("<ButtonRelease-1>", ans1)
#/end Блок 2 вопроса

#start Блок 3 вопроса
label3_1=tk.Label(frame, text='Вопрос №3\n\nТекст вопроса\n\nВариант 1\nВариант 2\nВариант 3\nВариант 4', fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
spin3q=tk.Spinbox(frame, width=10, values=('Вариант 1','Вариант 2','Вариант 3', 'Вариант 4'), bg=cframe, font=('Times', 10, 'bold'))
but3answ=tk.Button(frame, text='Ответить на вопрос №3\n( правильный 4)', bg=cbut, fg=cwhite, bd=3)
but3answ.bind("<ButtonRelease-1>", ans3_2)
label3_2=tk.Label(frame, text='Проверка ответа', width=12, height=2, fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
but3_2=tk.Button(frame, text='Следующий вопрос', bg=cbut, fg=cwhite, bd=3)
but3_2.bind("<ButtonRelease-1>", ans4)
but3_3=tk.Button(frame, text='Предыдущий вопрос', bg=cbut, fg=cwhite, bd=3)
but3_3.bind("<ButtonRelease-1>", ans2)
#/end Блок 3 вопроса

#start Блок 4 вопроса
label4_1=tk.Label(frame, text='Вопрос №4\n\nТекст вопроса\n\nВариант 1\nВариант 2\nВариант 3\nВариант 4', fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
spin4q=tk.Spinbox(frame, width=10, values=('Вариант 1','Вариант 2','Вариант 3', 'Вариант 4'), bg=cframe, font=('Times', 10, 'bold'))
but4answ=tk.Button(frame, text='Ответить на вопрос №4\n( правильный 1)', bg=cbut, fg=cwhite, bd=3)
but4answ.bind("<ButtonRelease-1>", ans4_2)
label4_2=tk.Label(frame, text='Проверка ответа', width=12, height=2, fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
but4_2=tk.Button(frame, text='Следующий вопрос', bg=cbut, fg=cwhite, bd=3)
but4_2.bind("<ButtonRelease-1>", ans5)
but4_3=tk.Button(frame, text='Предыдущий вопрос', bg=cbut, fg=cwhite, bd=3)
but4_3.bind("<ButtonRelease-1>", ans3)
#/end Блок 4 вопроса

#start Блок 5 вопроса
label5_1=tk.Label(frame, text='Вопрос №5\n\nТекст вопроса\n\nВариант 1\nВариант 2\nВариант 3\nВариант 4\nВариант 5', fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
spin5q=tk.Spinbox(frame, width=10, values=('Вариант 1','Вариант 2','Вариант 3', 'Вариант 4', 'Вариант 5'), bg=cframe, font=('Times', 10, 'bold'))
but5answ=tk.Button(frame, text='Ответить на вопрос №5\n( правильный 2)', bg=cbut, fg=cwhite, bd=3)
but5answ.bind("<ButtonRelease-1>", ans5_2)
label5_2=tk.Label(frame, text='Проверка ответа', width=12, height=2, fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
but5_2=tk.Button(frame, text='Следующий вопрос', bg=cbut, fg=cwhite, bd=3)
but5_2.bind("<ButtonRelease-1>", ans6)
but5_3=tk.Button(frame, text='Предыдущий вопрос', bg=cbut, fg=cwhite, bd=3)
but5_3.bind("<ButtonRelease-1>", ans4)
#/end Блок 5 вопроса

#start Блок 6 вопроса
label6_1=tk.Label(frame, text='Вопрос №6\n\nТекст вопроса\n\nВариант 1\nВариант 2\nВариант 3',  fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
spin6q=tk.Spinbox(frame, width=10, values=('Вариант 1','Вариант 2','Вариант 3'), bg=cframe, font=('Times', 10, 'bold'))
but6answ=tk.Button(frame, text='Ответить на вопрос №6\n( правильный 1)', bg=cbut, fg=cwhite, bd=3)
but6answ.bind("<ButtonRelease-1>", ans6_2)
label6_2=tk.Label(frame, text='Проверка ответа', width=12, height=2, fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
but6_2=tk.Button(frame, text='Следующий вопрос', bg=cbut, fg=cwhite, bd=3)
but6_2.bind("<ButtonRelease-1>", ans7)
but6_3=tk.Button(frame, text='Предыдущий вопрос', bg=cbut, fg=cwhite, bd=3)
but6_3.bind("<ButtonRelease-1>", ans5)
#/end Блок 6 вопроса

#start Блок 7 вопроса
label7_1=tk.Label(frame, text='Вопрос №7\n\nТекст вопроса\n\nВариант 1\nВариант 2\nВариант 3\nВариант 4', fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
spin7q=tk.Spinbox(frame, width=10, values=('Вариант 1','Вариант 2','Вариант 3', 'Вариант 4'), bg=cframe, font=('Times', 10, 'bold'))
but7answ=tk.Button(frame, text='Ответить на вопрос №7\n( правильный 4)', bg=cbut, fg=cwhite, bd=3)
but7answ.bind("<ButtonRelease-1>", ans7_2)
label7_2=tk.Label(frame, text='Проверка ответа', width=12, height=2, fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
but7_2=tk.Button(frame, text='Следующий вопрос', bg=cbut, fg=cwhite, bd=3)
but7_2.bind("<ButtonRelease-1>", ans8)
but7_3=tk.Button(frame, text='Предыдущий вопрос', bg=cbut, fg=cwhite, bd=3)
but7_3.bind("<ButtonRelease-1>", ans6)
#/end Блок 7 вопроса

#start Блок 8 вопроса
label8_1=tk.Label(frame, text='Вопрос №8\n\nТекст вопроса\n\nВариант 1\nВариант 2\nВариант 3\nВариант 4', fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
spin8q=tk.Spinbox(frame, width=10, values=('Вариант 1','Вариант 2','Вариант 3', 'Вариант 4'), bg=cframe, font=('Times', 10, 'bold'))
but8answ=tk.Button(frame, text='Ответить на вопрос №8\n( правильный 3)', bg=cbut, fg=cwhite, bd=3)
but8answ.bind("<ButtonRelease-1>", ans8_2)
label8_2=tk.Label(frame, text='Проверка ответа', width=12, height=2, fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
but8_2=tk.Button(frame, text='Следующий вопрос', bg=cbut, fg=cwhite, bd=3)
but8_2.bind("<ButtonRelease-1>", ans9)
but8_3=tk.Button(frame, text='Предыдущий вопрос', bg=cbut, fg=cwhite, bd=3)
but8_3.bind("<ButtonRelease-1>", ans7)
#/end Блок 8 вопроса

#start Блок 9 вопроса
label9_1=tk.Label(frame, text='Вопрос №9\n\nТекст вопроса\n\nВариант 1\nВариант 2\nВариант 3\nВариант 4\nВариант 5', fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
spin9q=tk.Spinbox(frame, width=10, values=('Вариант 1','Вариант 2','Вариант 3', 'Вариант 4', 'Вариант 5'), bg=cframe, font=('Times', 10, 'bold'))
but9answ=tk.Button(frame, text='Ответить на вопрос №9\n( правильный 5)', bg=cbut, fg=cwhite, bd=3)
but9answ.bind("<ButtonRelease-1>", ans9_2)
label9_2=tk.Label(frame, text='Проверка ответа', width=12, height=2, fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
but9_2=tk.Button(frame, text='Следующий вопрос', bg=cbut, fg=cwhite, bd=3)
but9_2.bind("<ButtonRelease-1>", ans10)
but9_3=tk.Button(frame, text='Предыдущий вопрос', bg=cbut, fg=cwhite, bd=3)
but9_3.bind("<ButtonRelease-1>", ans8)
#/end Блок 9 вопроса

#start Блок 10 вопроса
label10_1=tk.Label(frame, text='Вопрос №10\n\nТекст вопроса\n\nВариант 1\nВариант 2\nВариант 3\nВариант 4', fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
spin10q=tk.Spinbox(frame, width=10, values=('Вариант 1','Вариант 2','Вариант 3', 'Вариант 4'), bg=cframe, font=('Times', 10, 'bold'))
but10answ=tk.Button(frame, text='Ответить на вопрос №9\n( правильный 3)', bg=cbut, fg=cwhite, bd=3)
but10answ.bind("<ButtonRelease-1>", ans10_2)
label10_2=tk.Label(frame, text='Проверка ответа', width=12, height=2, fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
but10_2=tk.Button(frame, text='Узнать оценку', bg=cbut, fg=cwhite, bd=3)
but10_2.bind("<ButtonRelease-1>", count)
but10_3=tk.Button(frame, text='Предыдущий вопрос', bg=cbut, fg=cwhite, bd=3)
but10_3.bind("<ButtonRelease-1>", ans9)
#/end Блок 10 вопроса

#start Блок выставления оценки
labelstudent=tk.Label(frame, fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
labelmark=tk.Label(frame, text='Ваш результат тестирования:', fg=cblack, bg=cframe, font=('Times', 14, 'bold'))
labelcount=tk.Label(frame, fg=cblack, bg=cwhite, font=('Times', 14, 'bold'))
butstart=tk.Button(frame, text='Начать заново?', bg=cbut, fg=cwhite, bd=3)
butstart.bind("<ButtonRelease-1>", mainwin)
butstop=tk.Button(frame, text='Выйти', bg=cbut, fg=cwhite, bd=3)
butstop.bind("<ButtonRelease-1>", destr)
#end Блок выставления оценки

root.mainloop()