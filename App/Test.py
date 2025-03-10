import curses

def main(stdscr):
    curses.curs_set(0)  # Скрываем курсор
    stdscr.nodelay(1)  # Не ждёт нажатия, чтобы не тормозить цикл
    stdscr.keypad(True)  # Позволяет использовать специальные клавиши
    stdscr.clear()

    x = 10  # Начальная позиция по X
    y = 5   # Фиксированная позиция по Y

    while True:
        stdscr.clear()  # Очищаем экран перед перерисовкой
        stdscr.addstr(y, x, "🚀")  # Рисуем объект
        stdscr.refresh()

        key = stdscr.getch()  # Ждём нажатие клавиши

        if key == ord('q'):  # Выход из игры по 'q'
            break
        elif key == ord('a') and x > 0:  # Двигаем влево (ограничение, чтобы не уйти в -)
            x -= 1
        elif key == ord('d') and x < curses.COLS - 1:  # Двигаем вправо (предел по ширине экрана)
            x += 1

        curses.napms(20)  # Задержка для плавности

curses.wrapper(main)
