import os
import pyautogui as pg
from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery
from create_bot import bot, ADMIN_ID
from keyboards import kb_to_do, move_keyboard, kb_programs


async def command_start(message: types.Message):
    await message.answer("Выберите:", reply_markup=kb_to_do)


async def computer_shutdown(message: types.Message):
    if message.text == "Выключить компьютер":
        await bot.send_message(ADMIN_ID, "Выключение компьютера")
        os.system("shutdown /s /t 1")
    elif message.text == "Перезагрузить компьютер":
        await bot.send_message(ADMIN_ID, "Перезагрузка компьютера")
        os.system("shutdown /r /t 1")
    else:
        await message.answer("Выберите:", reply_markup=kb_to_do)


async def move(message: types.Message):
    await message.answer("Выберите:", reply_markup=move_keyboard)


async def chose_program(message: types.Message):
    await message.answer("Выберите программу для запуска:", reply_markup=kb_programs)


async def start_program(message: types.Message):
    discord_path = r"C:\Users\Арсен\AppData\Local\Discord\app-1.0.9013\Discord.exe"
    steam_path = r"D:\Steam\steam.exe"
    yandex_browser_path = r"C:\Users\Администратор\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    sims4_path = r"D:\Games\The Sims 4\Launcher.exe"
    csgo_path = r"D:\Steam\steamapps\common\Counter-Strike Global Offensive\csgo.exe"

    if message.text == "Discord":
        os.startfile(discord_path)
    elif message.text == "Steam":
        os.startfile(steam_path)
    elif message.text == "YandexBrowser":
        os.startfile(yandex_browser_path)
    elif message.text == "Sims 4":
        os.startfile(sims4_path)
    elif message.text == "CS:GO":
        os.startfile(csgo_path)
    else:
        await message.answer("Выберите из предложенных программ!", reply_markup=kb_programs)
    await message.answer("Выберите:", reply_markup=kb_to_do)


async def button_handler(callback_query: CallbackQuery):
    chosen_buttons = callback_query.data.split(',')
    delta = 50
    global previous_pos
    global delt
    for button in chosen_buttons:
        if button == "faster":
            delta = delt + 50
        elif button == "slower":
            delta = delt - 50
        elif button == "up":
            current_pos = pg.position()  # Сохраняем текущее положение курсора
            pg.moveTo(current_pos[0], current_pos[1] - delt, 0.5)
            previous_pos = current_pos  # Обновляем предыдущее положение курсора
        elif button == "down":
            current_pos = pg.position()
            pg.moveTo(current_pos[0], current_pos[1] + delt, 0.5)
            previous_pos = current_pos
        elif button == "right":
            current_pos = pg.position()
            pg.moveTo(current_pos[0] + delta, current_pos[1], 0.5)
            previous_pos = current_pos
        elif button == "left":
            current_pos = pg.position()
            pg.moveTo(current_pos[0] - delta, current_pos[1], 0.5)
            previous_pos = current_pos
        elif button == "center":
            previous_pos = pg.position()  # Используем текущее положение курсора
            pg.click(previous_pos)  # Используем сохраненное предыдущее положение курсора
        else:
            await callback_query.message.edit_reply_markup(reply_markup=None)
            await bot.send_message(ADMIN_ID, "Выберите:", reply_markup=kb_to_do)
            break
    await callback_query.answer()  # Отправляем ответ, чтобы закрыть всплывающее окно с кнопками


def register_handlers_admin(dispatcher: Dispatcher):
    dispatcher.register_message_handler(command_start, commands=["start"])
    dispatcher.register_message_handler(computer_shutdown, lambda message: message.text in "Выключить компьютер"
                                                                                           "Перезагрузить компьютер",
                                        user_id=ADMIN_ID)
    dispatcher.register_message_handler(move, lambda message: message.text == "Управлять курсором",
                                        user_id=ADMIN_ID)
    dispatcher.register_callback_query_handler(
        button_handler,
        lambda callback_query: callback_query.data in ('up', 'down', 'left', 'right', 'center',
                                                       'exit', 'faster', 'lower')
    )
    dispatcher.register_message_handler(chose_program, lambda message: message.text == "Запуск программ",
                                        user_id=ADMIN_ID)
    dispatcher.register_message_handler(start_program,
                                        lambda message: message.text in "Discord, Steam, YandexBrowser, Sims 4, CS:GO",
                                        user_id=ADMIN_ID)
