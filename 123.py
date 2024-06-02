import schedule
import time
import asyncio
from pyrogram import Client, filters
from datetime import date
import telebot




today = date.today()
d1 = today.strftime("%d")

def job():
    app = Client("client1")
    with app:



        app.send_photo("me", d1 + ".jpg")#







schedule.every().day.at("13:17:40").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)