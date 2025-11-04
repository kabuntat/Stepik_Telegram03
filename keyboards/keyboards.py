from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    WebAppInfo,
    KeyboardButtonPollType,
    KeyboardButtonRequestUser,
    KeyboardButtonRequestUsers,
    KeyboardButtonRequestChat,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.enums import PollType
from lexicon.lexicon import LEXICON_RU



# Инициализируем билдеры
kb_start_builder = ReplyKeyboardBuilder()
kb_game_builder = ReplyKeyboardBuilder()

# Создаем кнопки
stone_btn = KeyboardButton(text="✊")
scissors_btn = KeyboardButton(text="✌️")
paper_btn = KeyboardButton(text="✋")
game_yes_btn  = KeyboardButton(text=LEXICON_RU['game_yes'])
game_no_btn  = KeyboardButton(text=LEXICON_RU['game_no'])

# Добавляем кнопки в билдеры
kb_start_builder.row(game_yes_btn, game_no_btn)
kb_game_builder.row(stone_btn, scissors_btn, paper_btn)

# Создаем объекты клавиатур
my_keyboard_start: ReplyKeyboardMarkup = kb_start_builder.as_markup(
    input_field_placeholder='Ничего не надо вводить, просто выбери кнопку',
    resize_keyboard=True,
    one_time_keyboard=True

)
my_keyboard_game: ReplyKeyboardMarkup = kb_game_builder.as_markup(
    input_field_placeholder='Ничего не надо вводить, просто выбери кнопку',
    resize_keyboard=True,
    one_time_keyboard=True
)

