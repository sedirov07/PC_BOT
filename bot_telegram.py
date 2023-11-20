import logging
from aiogram.utils import executor
from create_bot import dispatcher
from handlers import admin


# Оповещение в терминале о запуске бота
async def on_startup(_):
    print("Бот 'PC' онлайн")


# Регистрация хендлеров
admin.register_handlers_admin(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True, on_startup=on_startup)
    logging.basicConfig(level=logging.INFO)
