import sys
import time
import telepot
import argparse

from telepot.loop import MessageLoop

bot_introduction_message = "Welcome to the telegram forwarder bot. Just type something, attach any supported media and bot will do all the background work to deliver it to the necessary chats."
salutation = "Mr/Mrs"
type_not_supported_message = "This type cannot be send, as it doesn't supported"


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(msg)
    target_id = sys.argv[2]
    first_name = msg["from"]["first_name"]
    last_name = msg["from"]["last_name"]
    caption1 = "<b>" + first_name + " " + last_name + "</b>"
    if content_type == "photo":
        photo4 = msg["photo"][1]["file_id"]
        if "caption" in msg:
            photo_caption = "<b>" + first_name + " " + \
                last_name + " - </b>" + msg["caption"]
        else:
            photo_caption = "<b>" + first_name + " " + last_name + "</b>"
        bot.sendPhoto(chat_id=target_id, photo=photo4,
                      caption=photo_caption, parse_mode="HTML")
    elif content_type == "text" and msg["text"] == "/start":
        bot.sendMessage(chat_id=chat_id, text=salutation + " " +
                        first_name + " " + last_name + ", bot_introduction_message")
    elif content_type == "text":
        message_text = "<b>" + first_name + " " + \
            last_name + "</b>" + '\n' + msg["text"]
        bot.sendMessage(target_id, message_text, parse_mode="HTML")
    elif content_type == "video":
        video = msg["video"]["file_id"]
        if "caption" in msg:
            video_caption = "<b>" + first_name + " " + \
                last_name + " - </b>" + msg["caption"]
        else:
            video_caption = "<b>" + first_name + " " + last_name + "</b>"
        bot.sendVideo(chat_id=target_id, video=video,
                      caption=video_caption, parse_mode="HTML")
    else:
        bot.sendMessage(chat_id=chat_id, text=first_name + " " + last_name + type_not_supported_message)


TOKEN = sys.argv[1]
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
