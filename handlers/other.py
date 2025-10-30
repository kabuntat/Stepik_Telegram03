import logging

from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from aiogram import Router

# Инициализируем роутер уровня модуля
router_other = Router()


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router_other.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        logging.debug("Copy was sent")
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])

