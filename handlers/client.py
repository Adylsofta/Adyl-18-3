from config import bot, dp, Dispatcher
from aiogram.types import ParseMode,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram import types
from keyboards.client_kb import start_markup

async def start_command(message: types.Message):
    await message.reply(f"Hello {message.from_user.full_name}!", reply_markup=start_markup)



async def mem(message: types.Message):
    photo =open("media/download.jpg" , 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_1',
    )
    markup.add(button_call_1)

    question = 'Чему равна число пи?'
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


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])

    dp.register_message_handler(mem, commands=["mem"])

    dp.register_message_handler(quiz_1, commands=["quiz"])

