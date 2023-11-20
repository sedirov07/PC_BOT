from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# Создаем стартовую с выбором действий
b_off_pc = KeyboardButton(text="Выключить компьютер")
b_restart_pc = KeyboardButton(text="Перезагрузить компьютер")
b_move = KeyboardButton(text="Управлять курсором")
b_start = KeyboardButton(text="Запуск программ")
kb_to_do = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_to_do.add(b_off_pc, b_restart_pc, b_move, b_start)


# Создаем клавиатуру для управления курсором
up_button = InlineKeyboardButton('Вверх', callback_data='up')
down_button = InlineKeyboardButton('Вниз', callback_data='down')
right_button = InlineKeyboardButton('Вправо', callback_data='right')
left_button = InlineKeyboardButton('Влево', callback_data='left')
center_button = InlineKeyboardButton('Нажатие', callback_data='center')
exit_button = InlineKeyboardButton('Выход', callback_data='exit')
faster_button = InlineKeyboardButton('Ускорить', callback_data='faster')
lower_button = InlineKeyboardButton('Замедлить', callback_data='lower')
move_keyboard = InlineKeyboardMarkup(row_width=3)
move_keyboard.add(faster_button, lower_button).add(up_button).add(left_button, center_button, right_button).\
    add(down_button).add(exit_button)


b_discord = KeyboardButton(text="Discord")
b_steam = KeyboardButton(text="Steam")
b_yandex = KeyboardButton(text="YandexBrowser")
b_sims = KeyboardButton(text="Sims 4")
b_cs = KeyboardButton(text="CS:GO")
kb_programs = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_programs.add(b_discord, b_steam, b_yandex).add(b_sims, b_cs)
