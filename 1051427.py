# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request, abort
app = Flask(__name__)
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('pUD+ykz0P+H6mQevvJK7mJxstnZAPfpouxGXEjlrNgVlPnvppRfgJxSJ4m2KAIeEiZmd2bhbmt71NCQ5xcmx8Ug+UVKCMEhI9BpdjCdD+DV4B6AKCvw+/O0f/m2pmnuQTWIePF9R51cwrOp+ktSW3QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('696278a5fcd0c4ad4e8e4da7dc14cec5')

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    return 'ok'

@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == '__main__':
    app.run()
