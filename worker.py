
import filmriader
import telebot
from time import sleep

bot = telebot.TeleBot('1945439245:AAG7UfIqmfdZDQALLtiyf9fntaFaL6lD1oo')

def SendVideo():
    film = filmriader.getFilm()

    text = f"\n{film['ru_name']}\n{film['cuntry']}\n{film['genre']}\n{film['youtubeLink']}"
    #bot.send_media_group(-1001650547543,[InputMediaVideo(f,caption="https://t.me/ToKTokVideos")])
    bot.send_message(-1001740715979,text)


while True:
    SendVideo()
    #sleep(9000)
    #sleep(10)
