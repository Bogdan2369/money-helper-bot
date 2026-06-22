import telebot

TOKEN = "8583888651:AAEZI8WL3EGSuZISH2yVCP4SJUvKVQiaX3o"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Привіт!\n\nЯ Money Helper.\nНадішли суму в гривнях, і я переведу її в долари."
    )


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "📖 Приклад використання:\n\n100\n420\n1000\n\nЯ покажу приблизну суму в доларах."
    )


@bot.message_handler(func=lambda message: True)
def money(message):
    try:
        amount = float(message.text.replace(",", "."))

        usd = amount / 42

        bot.send_message(
            message.chat.id,
            f"💰 {amount:.2f} грн ≈ ${usd:.2f}"
        )

    except ValueError:
        bot.send_message(
            message.chat.id,
            "❌ Будь ласка, надішли тільки число.\n\nНаприклад:\n100\n420\n1000"
        )


print("Бот запущений...")
bot.infinity_polling()