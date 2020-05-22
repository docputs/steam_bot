import telebot
import steamweb
import lista_promocoes
from csv import DictWriter

with open('keys.txt', 'r') as keys:
    TOKEN = keys.read().strip()

bot = telebot.TeleBot(TOKEN)

resposta_forcada = telebot.types.ForceReply()


def steamid_message_check(msg):
    msg = msg.text
    msg = msg.split(' ')

    if msg[0] == 'steamid' and msg[1].isnumeric():
        return True
    else:
        return False


@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
    bot.send_message(chat_id=msg.chat.id, text='Olá! Eu posso mostrar as promoções de jogos na Steam.'
                                               ' Para isso, envie-me a mensagem /promocoes')


@bot.message_handler(commands=['meusjogos'])
def send_jogos(msg):
    steamid = steamweb.find_steamid(msg.from_user.id)

    if steamid is not None:
        bot.send_message(chat_id=msg.chat.id, text=steamweb.meusjogos(steamid), parse_mode='HTML')
    else:
        bot.send_message(chat_id=msg.chat.id, text='Steam ID não encontrado :c')


@bot.message_handler(commands=['promocoes'])
def show_specials(msg):
    bot.send_message(chat_id=msg.chat.id, text=lista_promocoes.extrair_promocoes(), parse_mode='HTML')
    print(f'{msg.from_user.first_name} solicitou as promocoes')


@bot.message_handler(commands=['steamid'])
def ask_steamid(msg):
    bot.send_message(chat_id=msg.chat.id, text='Envie-me o seu Steam ID digitando steamid <numero>\n\n'
                                               'Utilize shorturl.at/equxB para encontrar um Steam ID',
                     reply_markup=resposta_forcada)


@bot.message_handler(content_types=['text'], func=steamid_message_check)
def save_steamid(msg):
    with open('database.csv', 'a') as db:
        escritor = DictWriter(f=db, fieldnames=['userid', 'steamid'])

        lista = {'userid': msg.from_user.id, 'steamid': msg.text.split(' ')[1]}
        escritor.writerow(lista)

    bot.send_message(chat_id=msg.chat.id, text=f'Steam ID {msg.text.split(" ")[1]} cadastrado')


bot.polling(timeout=20, none_stop=True)
