from telegram import Update
from telegram.ext import CallbackContext
from keyboards.language import get_language_keyboard
from keyboards.register import get_register_keyboard


def start(update: Update, context: CallbackContext):
    user = update.effective_user

    update.message.reply_html(
        text=f"Assalomu Alaykum <b>{user.full_name}</b>! Nima Gap Botga hush kelibsiz.",
    )

    update.message.reply_text(
        text=f"Tilni tanlang / Select language",
        reply_markup=get_language_keyboard()
    )

    update.message.reply_text(
        text=f"Ro'yxatdan o'tish",
        reply_markup=get_register_keyboard()
    )


