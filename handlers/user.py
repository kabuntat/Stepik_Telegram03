import logging
from aiogram.types import Message, PollAnswer, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from aiogram import Router, F
from keyboards import my_keyboard_game, my_keyboard_start
from aiogram.enums import PollType
import random

# Инициализируем роутер уровня модуля
router_user = Router()

# Этот хэндлер срабатывает на команду /start
@router_user.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=my_keyboard_start
    )

# Этот хэндлер срабатывает на кнопку "Давай!"
@router_user.message(F.text==LEXICON_RU['game_yes'])
async def process_game_command(message: Message):
    await message.answer(
        text='Отлично! Делай свой выбор!',
        reply_markup=my_keyboard_game
    )

# Этот хэндлер будет срабатывать на нажатие одной из кнопок(✊ ✌️ ✋)
@router_user.message(F.text.in_("✊ ✌️ ✋"))
async def process_game(message: Message):
    hand = random.choice(['✊','✌️','✋'])
    await message.answer(text=hand)
    if message.text == hand:
        await message.answer(text=LEXICON_RU['Draw'])
    elif (message.text == "✊" and hand == '✋' or
          message.text == '✌️' and hand == '✊' or
          message.text == '✋' and hand == '✌️'):
        await message.answer(text=LEXICON_RU['You lose'])
    else:
        await message.answer(text=LEXICON_RU['You win'], message_effect_id='5046509860389126442')
    await message.answer(
        text='Сыграем еще?!',
        reply_markup=my_keyboard_start
    )

@router_user.message(F.text==LEXICON_RU['game_no'])
async def refuse_to_play(message: Message):
    await message.answer(text='Хорошо. Если, вдруг, захочешь сыграть - открой клавиатуру и нажми "Давай!')

# Этот хэндлер срабатывает на команду /help
@router_user.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
