import json
import daterime
file = open('info.json', 'r')
info = json.load(file)

from linebot import LineBotApi
from linebot.models import TextSendMessage

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

a = datetime.datetime.now()

def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text = "ぽぽぽぽ", a)
    line_bot_api.push_message(USER_ID, messages=messages)

if __name__ == "__main__":
    main()
