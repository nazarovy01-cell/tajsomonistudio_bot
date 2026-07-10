import telebot
from telebot import types

TOKEN = "8960499746:AAERgXoStL0xL8PZwQ70pRpCACqZdx0bxrM"

bot = telebot.TeleBot(TOKEN)


# Каналҳои спонсор
SPONSORS = [
    "@TOJISOMON",
    "@TAJSOMONIII"
]


# ID-и видео (аз Telegram гирифта мешавад)
VIDEO_ID = "https://t.me/Abdujabborhd/19817"


# Менюи спонсорҳо
def sponsor_menu():

    markup = types.InlineKeyboardMarkup()

    for channel in SPONSORS:

        button = types.InlineKeyboardButton(
            text="Обунa шудан ✅",
            url="https://t.me/" + channel.replace("@", "")
        )

        markup.add(button)


    check = types.InlineKeyboardButton(
        text="Санҷиши обуна 🔍",
        callback_data="check"
    )

    markup.add(check)

    return markup



# Вақти START
@bot.message_handler(commands=["start"])
def start(message):

    bot.send_message(
        message.chat.id,
        """
Салом 👋

Барои гирифтани кино аввал ба каналҳои спонсор обуна шавед.

Баъд тугмаи «Санҷиши обуна 🔍»-ро пахш кунед.
        """,
        reply_markup=sponsor_menu()
    )



# Санҷиши обуна
@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):

    user_id = call.from_user.id

    ok = True


    for channel in SPONSORS:

        try:

            member = bot.get_chat_member(
                channel,
                user_id
            )

            if member.status not in [
                "member",
                "administrator",
                "creator"
            ]:

                ok = False


        except:

            ok = False



    if ok:

        bot.answer_callback_query(
            call.id,
            "Обуна тасдиқ шуд ✅"
        )

        bot.send_video(
            user_id,
            VIDEO_ID,
            caption="🎬 Ин аст кинои шумо"
        )


    else:

        bot.answer_callback_query(
            call.id,
            "Ҳоло обуна нашудаед ❌"
        )

        bot.send_message(
            user_id,
            """
❌ Шумо ба ҳамаи каналҳои спонсор обуна нашудаед.

Аввал обуна шавед ва боз санҷед.
            """,
            reply_markup=sponsor_menu()
        )



bot.infinity_polling()