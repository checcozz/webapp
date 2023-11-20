from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import funzioni

Token: Final = "6894902197:AAFsiZxidwTGf1iPtkNHPZm5GS6dIpmOaTY"
Bot_username: Final = "@WhatACatchBot"


# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('benvenuto nel club esclusivo!')


async def estrai_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(funzioni.estrazione())

def handle_responses(text):

    if 'hello' in text:
        return 'ciao'
    if 'spiegami' in text:
        return 'sono un bot'

    return 'non ho capito'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

#controlla se il bot è in una chat privata o un gruppo

    if message_type == 'group':
        if Bot_username in text:
            new_text = text.replace(Bot_username,'').strip()
            response = handle_responses(new_text)
        else:
            return
    else:
        response = handle_responses(text)

    print('Bot', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update{update} caused error {context.error}')



if __name__ == '__main__':

    print('starting bot')
    app = Application.builder().token(Token).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('estrai', estrai_command))

    #messages

    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #error

    app.add_error_handler(error)

    print('polling...')
    app.run_polling(poll_interval=3)

