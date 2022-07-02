from config import bot, dp
from aiogram import types, Dispatcher


async def echo_and_ban(message: types.Message):
    bad_words = ['тупой', 'лох', 'дурак', 'придурок']
    for word in bad_words:
        if word in message.text.lower():
            await bot.send_message(message.chat.id, f'Не матерись!')
            await bot.delete_message(message.chat.id, message.message_id)
    if message.text.startswith('pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text.lower() == 'dice':
        await bot.send_dice(message.chat.id, emoji='⚽')


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_and_ban)
