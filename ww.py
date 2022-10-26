import telebot
from telebot import types
import yaml
import time

with open("s.yaml", "r", -1, 'utf-8') as stream:
    try:
        www = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)





def yt(message,uuu):
    if www['ведение журнала'] == 'да':
        file = open('все запросы.txt', 'a', -1, 'utf-8')
        a = time.ctime()
        a = a.split()
        file.write('['+str(a[1]+'/'+a[2]+'/'+a[3]+'/'+a[4])+'] '+"{0.first_name}".format(message.from_user)+' > '+str(uuu)+'\n')
        file.close()
    if str(uuu) in www:#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        www1 = www[uuu]
        if www1['тип'] == 'text':
            bot.reply_to(message, www1['text'])
        elif www1['тип'] == 'survey':
            bot.send_poll(message.chat.id, question=www1['опрос'], options=www1['выбор'])
        elif www1['тип'] == 'paintings_text':
            img = open('картины/{}'.format(www1['изображение']), 'rb')
            bot.send_photo(message.chat.id, img, www1['text'])

        if 'следующее_событие' in www1:
            if 'задержка' in www1:
                time.sleep(www1['задержка'])
            yt(message,www1['следующее_событие'])
        if 'вывести_в_консоль' in www1:
            print(www1['вывести_в_консоль'])
        if 'python' in www1:
            uyt = 0
            sggfe = ''
            ytr = www1['python']
            while uyt < len(www1['python']):
                sggfe = sggfe+ytr[uyt]+'\n'
                uyt = uyt+1
            exec(sggfe)
            


print('сервер запущен')
if __name__ == '__main__':
    bot = telebot.TeleBot(www['HTTP_API'], parse_mode=None)

    @bot.message_handler(commands=['start'])
    def start(message):
        yt(message,'start')
    @bot.message_handler(commands=['we'])
    def start(message):
        global www
        with open("s.yaml", "r", -1, 'utf-8') as stream:
            try:
                www = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        bot.reply_to(message, 'сервер обновлен')


    @bot.message_handler(content_types=['text'])
    def bot_message(message):
        if message.chat.type == 'private':
            gr = message.text.split('#')
            if len(gr) == 1:
                yt(message,message.text)
            

    bot.infinity_polling()