from aiogram import types
from aiogram.types import ParseMode,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils import executor

from config import bot, dp
import logging

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(f"Hello {message.from_user.full_name}!")

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_1',
    )
    markup.add(button_call_1)

    question = 'Чему равно число пи?'
    answers = [
        '3.15', '4.35', '3.14', '3.13'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call:call.data=="button_call_1")
async def quiz_2(call:types.CallbackQuery):
    question = 'Самая большая страна в мире?'
    answers = [
        'Канада', 'Россия', 'Китай', 'Австралия'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Изи же",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )


@dp.message_handler(commands=["Mem"])
async def mem(message: types.Message):
    photo=open("media/download.jpg" , 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    x = message.text
    try:
        x = int(x)
        c = 1
    except:
        pass
        c = 0
    if c == 1:
        await bot.send_message(message.chat.id, f"{x*x}")
    elif c == 0:
        await bot.send_message(message.chat.id, x)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
