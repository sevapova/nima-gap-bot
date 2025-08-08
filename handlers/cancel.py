from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler


def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    update.message.reply_text(
        'Bye! I hope we can talk again some day.',
    )

    return ConversationHandler.END

