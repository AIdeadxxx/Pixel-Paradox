import curses
import os
import sys

def main(stdscr):
    curses.curs_set(0)  # Скрыть курсор
    stdscr.clear()  # Очистить экран
    stdscr.nodelay(1)

    x = 10
    y = 9

    while True:
        stdscr.addstr(y, x, "●")
        stdscr.addstr(10, 0, "⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")  # Вывести текст на экран
        stdscr.refresh()  # Обновить экран

        key = stdscr.getch()  # Ожидание нажатия клавиши

        if key == ord('z'):
            break
        elif y != 9: #!
            if key == ord('a') and x > 0: #!
                x -= 1 #!
                stdscr.clear() #!
            continue #!
                
        elif key == ord('d') and x < 119:
            x += 1
            stdscr.clear()
        elif key == ord('s') and y < 20:
            y += 1
            stdscr.clear()
        elif key == ord('w') and y >= 9:
            y -= 1
            stdscr.clear()
    
        curses.napms(20)


    
if "CHILD_PROCESS" not in os.environ:
    os.environ["CHILD_PROCESS"] = "1"
    os.system("start cmd /k python Main.py")
    sys.exit()  # Выход из основного скрипта


curses.wrapper(main)  # Запуск программы

    # # stdscr.addstr(7, 10, f"Ты нажал: {chr(key)}")  # Вывести, какую клавишу нажал пользователь
    # stdscr.refresh()
    # stdscr.getch()  # Ждать ещё одно нажатие перед выходом