from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from config import states
from keyboards.location import get_location_keyboard
from keyboards.contact import get_contact_keyboard
from keyboards.gender import get_gender_keyboard


def start_register(update: Update, context: CallbackContext):
    update.message.reply_text("Ro'yxatdan o'tish uchun quyidagi malumotlaringizni yuboring.")
    update.message.reply_text("name yuboring")
    return states.NAME


def set_name(update: Update, context: CallbackContext):
    name = update.message.text
    context.user_data['name'] = name

    update.message.reply_text("name qabul qilindi")
    update.message.reply_text(
        "gender yuboring",
        reply_markup=get_gender_keyboard()
    )
    return states.GENDER


def set_gender(update: Update, context: CallbackContext):
    gender = update.message.text
    context.user_data['gender'] = gender

    update.message.reply_text("gender qabul qilindi")
    update.message.reply_text(
        "location yuboring",
        reply_markup=get_location_keyboard()
    )
    return states.LOCATION


def set_location(update: Update, context: CallbackContext):
    location = update.message.location
    context.user_data['location'] = {'latitude': location.latitude, 'longitude': location.longitude}

    update.message.reply_text("location qabul qilindi")
    update.message.reply_text(
        "Contact yuboring",
        reply_markup=get_contact_keyboard()
    )
    return states.NUMBER


def set_number(update: Update, context: CallbackContext):
    contact = update.message.contact

    context.user_data['number'] = contact.phone_number

    print(context.user_data)

    update.message.reply_text("contact qabul qilindi")

    # save a new user into database

    update.message.reply_text("Register qilindingiz.")
    return ConversationHandler.END

