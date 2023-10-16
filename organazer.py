from tkinter import ttk
import tkinter as tk
from tkinter.constants import VERTICAL, HORIZONTAL

from datetime import datetime, timedelta

# Логика

    # Часы
def clock():
    date_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    date, time = date_time.split()
    date_label.config(text=date) # 'Сегодня' вписать
    time_label.config(text=time)
    time_label.after(1000, clock)

    # Секундомер
temp = 0
after_id = ""

def tick():
    global temp, after_id
    after_id = stopwatch.after(1,tick)
    f_temp = str(timedelta(milliseconds=temp))[:-4]
    stopwatch.configure(text=f_temp)
    temp +=1

def start_tick():
    stopwatch_start.grid_forget()#кнопка будет скрываться после нажатия на кнопку старт
    stopwatch_stop.grid(column= 1, row=3, columnspan=2, sticky='wsen', padx=2, pady=2) # появляется после нажатия старта
    tick()

def stop_tick():
    stopwatch_stop.grid_forget()
    stopwatch_continue.grid(row=3, column = 1, sticky='wsen', padx=2, pady=2)# появляются после нажатия стоп
    stopwatch_reset.grid(row=3, column = 2, sticky='wsen', padx=2, pady=2)# появляются после нажатия стоп
    stopwatch.after_cancel(after_id)
def continue_tick():
    stopwatch_continue.grid_forget()
    stopwatch_reset.grid_forget()
    stopwatch_stop.grid(column= 1, row=3, columnspan=2, sticky='wsen',padx=2, pady=2) # появляется после нажатия старта
    tick()

def reset_tick():
    global temp
    temp = 0

    stopwatch.config(text="0:00:00.00")
    stopwatch_continue.grid_forget()
    stopwatch_reset.grid_forget()
    stopwatch_start.grid(column= 1, row=2, columnspan=2, sticky='wsen', padx=2, pady=2, ipadx=3)

    # Таймер

def set_timer_run():
    global timer_running
    timer_running = True

def Timer(action=None):
    global timer_running, timer_seconds_overall

    get_timer_entry = timer_entry.get()
    # print('get_timer_entry', get_timer_entry)
    timer.config(text=get_timer_entry) # надпись что таймер идёт

    hours, minutes, seconds = get_timer_entry.split(':')
    # print('hours:', hours, 'minutes:', minutes, 'seconds:', seconds)

    seconds_in_hours = (int(hours) * 60) * 60
    # print('seconds_in_hours:', seconds_in_hours)

    seconds_in_minutes = int(minutes) * 60
    # print('seconds_in_minutes:', seconds_in_minutes)

    seconds_overall = seconds_in_hours + seconds_in_minutes + int(seconds)
    # print('seconds_overall:', seconds_overall)

    if action == 'start':
        set_timer_run()
        timer_seconds_overall = seconds_overall

    if timer_seconds_overall <= 0:
        timer_running = False
        timer_seconds_overall = 0
        timer.config(text='время вышло')
        play_sound()

    if timer_running:
        format_time = str(timedelta(seconds=timer_seconds_overall))
        timer.config(text=format_time)
        timer.after(1000, Timer)
        timer_seconds_overall -= 1


def play_sound():
    import platform
    import os
    import winsound

    if platform.system() == "Windows":
        winsound.Beep(5000, 1000)
    elif platform.system() == "Linux":
        os.system("beep -f 5000")

# window
window = tk.Tk()
window.title('Часики')
window.geometry("850x300")
window.resizable(width = False, height = False)

#widgets описание логики объектов сетки - таблицы
time_signature = ttk.Label(window,text='Текущее время', font='Calibri 15', borderwidth=0, anchor= tk.N)
time_label = ttk.Label(window,name= 'Текущее время' , font='Calibri 50 bold', foreground='black', borderwidth=0,anchor= tk.N )
date_signature = ttk.Label(window, text= 'Сегодня', font='Calibri 15', borderwidth=0)
date_label = ttk.Label(window, font='Calibri 40 bold', foreground='black' , border=0, borderwidth=0)


stopwatch_signature = ttk.Label(window,text= "Секундомер", font='Calibri 15')
stopwatch = ttk.Label(window,text='0:00:00.00', font='Calibri 45 bold')  # label1
stopwatch_start = ttk.Button(window,text= "Старт",width= 15, command = start_tick )
stopwatch_stop = ttk.Button(window,text= "Стоп",width= 15, command = stop_tick)
stopwatch_continue = ttk.Button(window,text= "Продолжить", width= 15, command = continue_tick)
stopwatch_reset = ttk.Button(window,text= "Сброс", width= 15, command = reset_tick)


timer_signature = ttk.Label(window,text= "Таймер", font='Calibri 15')
timer = ttk.Label(window, font='Calibri 40 bold', foreground='black')
timer.config(text='0:00:00')

timer_hints = ttk.Label(window, font='Calibri 16', foreground='black')
timer_hints.config(text='Часы:Минуты:Секунды')

entry_text = tk.StringVar()
timer_entry = ttk.Entry(window, font='Calibri 22', textvariable=entry_text)
entry_text.set('0:00:00')

timer_start = ttk.Button(window, text='Start', command=lambda : Timer('start'))
# stopwatch_stop = ttk.Button(window, text= 'Button1')
# stopwatch_continue = ttk.Button(window, text= 'Button2')
# stopwatch_reset = ttk.Button(window, text= 'Button1')


alarm_clock = ttk.Label(window,text= "Будильник", font='Calibri 15')


sep = ttk.Separator(window, orient=VERTICAL)
sep1 = ttk.Separator(window, orient=VERTICAL)
sep2 = ttk.Separator(window, orient=HORIZONTAL)


# определить сетку -minsize, -pad, -uniform, or -weight
window.columnconfigure(0, weight=2)# три ряда ровных было основных
window.columnconfigure(1, weight=1)# три ряда ровных было основных
window.columnconfigure(2, weight=1)# три ряда ровных было основных
window.columnconfigure(3, weight=2)# средний столбец раздел1н на 2 столбца
window.rowconfigure(0, weight=1)# строки
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)# строки
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)


# получить виджет - расположение
time_signature.grid(row=0, column= 0, sticky='w', ipady=0)# первый столбик 1 строка
time_label.grid(row=1, column= 0, sticky='n',rowspan=2 , ipady=0)# первый столбик 2 строка
date_signature.grid(row=2, column= 0, sticky='w')# первый столбик 3 строка
date_label.grid(row=3, column= 0, rowspan=2 , sticky='wn')# первый столбик 4 строка

stopwatch_signature.grid(row=0, column= 1, columnspan=2, sticky='w')# второй столбик, название таймера соеденены 2 строки
stopwatch.grid(row=0, column= 1, sticky='ws', rowspan=2, columnspan=2, ipady=0)# цифры таймера label1.grid()
stopwatch_start.grid(column= 1, row=2, columnspan=2, sticky='wsen', padx=2, pady=2, ipadx=3) #  первая неоходимая кнопка

timer_signature.grid(row=0, column= 3, sticky='w')
timer.grid(row=1, column= 3)
timer_hints.grid(row=2, column= 3, sticky= "wn")
timer_entry.grid(row=3, column= 3, sticky= "wn")
timer_start.grid(column=3, row=4, sticky= "wens")

# label3.grid(row=0, column= 3, sticky='wnes', rowspan=3, pady=5, padx=5)
alarm_clock.grid(row=5, sticky="wens", columnspan=4, rowspan=1)


sep.grid(row=0, column=0, rowspan=5, sticky='nse')
sep1.grid(row=0, column=2, rowspan=5, sticky='nse')
sep2.grid(row=5, column=0, columnspan=4, sticky='wen')

# stopwatch_stop = ttk.Button(window, text= 'Button1')
# stopwatch_continue = ttk.Button(window, text= 'Button2')
# stopwatch_reset = ttk.Button(window, text= 'Button1')


clock()
# run
window.mainloop()
