import logging
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from aiogram import Router

# Инициализируем роутер уровня модуля
router_other = Router()


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router_other.message()
async def answer_to_unknown_message(message: Message):
    try:
        await message.answer(text='Не понимаю')
        logging.debug("unknown message")
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])

