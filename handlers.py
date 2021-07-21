import os
from telegram.ext import CommandHandler, MessageHandler, Filters

from settings import WELCOME_MESSAGE, TELEGRAM_SUPPORT_CHAT_ID

def start(update, context):
    update.message.reply_text(WELCOME_MESSAGE)

    user_info = update.message.from_user.to_dict()

    context.bot.send_message(
        chat_id=TELEGRAM_SUPPORT_CHAT_ID,
        text=f"""
📞 Connected {user_info}.
        """,
    )


def forward_to_chat(update, context):
    """{ 
        'message_id': 716862, 
        'date': 1626874206, 
        'chat': {'id': 1309138849, 'type': 'private', 'username': 'mummicoffee', 'first_name': 'Mummi', 'last_name': 'Coffee'}, 
        'text': 'G', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
        'from': {'id': 1309138849, 'first_name': 'Mummi', 'is_bot': False, 'last_name': 'Coffee', 'username': 'mummicoffee', 'language_code': 'ru'}
    }"""
    update.message.forward(chat_id=TELEGRAM_SUPPORT_CHAT_ID)


def forward_to_user(update, context):
    """{
        'message_id': 716856, 'date': 1626874043, 
        'chat': {'id': -460338920, 'type': 'group', 'title': 'support', 'all_members_are_administrators': True}, 
        'reply_to_message': {
            'message_id': 9, 'date': 1605106659, 
            'chat': {'id': -460338920, 'type': 'group', 'title': 'support', 'all_members_are_administrators': True}, 
            'forward_from': {'id': 1309138849, 'first_name': 'Mummi', 'is_bot': False, 'last_name': 'Coffee', 'mummicoffee': 'Mummi', 'language_code': 'ru'}, 
            'forward_date': 1605106659, 
            'text': 'g', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 
            'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
            'from': {'id': 1949519631, 'first_name': 'Mummi Coffee', 'is_bot': True, 'username': 'mom_coffee_bot'}
        }, 
        'text': 'ggg', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 
        'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
        'from': {'id': 1309138849, 'first_name': 'Mummi', 'is_bot': False, 'last_name': 'Coffee', 'username': 'mummicoffee', 'language_code': 'ru'}
    }"""
    user_id = update.message.reply_to_message.forward_from.id
    context.bot.copy_message(
        message_id=update.message.message_id,
        chat_id=user_id,
        from_chat_id=update.message.chat_id
    )


def setup_dispatcher(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.chat_type.private, forward_to_chat))
    dp.add_handler(MessageHandler(Filters.chat(TELEGRAM_SUPPORT_CHAT_ID) & Filters.reply, forward_to_user))
    return dp
