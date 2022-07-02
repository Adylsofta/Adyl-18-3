from config import bot, dp
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram import types, Dispatcher


#@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call:types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('NEXT', callback_data='button_call_2')

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


async def quiz_3(call:types.CallbackQuery):
    question = 'Какой напиток первым был взят в космос?'
    answers = [
        'Пепси', 'Фанта', 'Кола', 'Фрешбар'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Как так!",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')


