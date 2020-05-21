import telebot
import steamweb
import lista_promocoes

bot = telebot.TeleBot('1148615135:AAE3Gtp3EOSgc0uMp2KRpomdyFgNS5J4hRQ')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
    bot.send_message(chat_id=msg.chat.id, text='Olá! Eu posso mostrar as promoções de jogos na Steam.'
                                               ' Para isso, envie-me a mensagem /promocoes')


@bot.message_handler(commands=['meusjogos'])
def send_jogos(msg):
    bot.send_message(chat_id=msg.chat.id, text=steamweb.meusjogos(76561198067139679))


@bot.message_handler(commands=['promocoes'])
def show_specials(msg):
    bot.send_message(chat_id=msg.chat.id, text=lista_promocoes.extrair_promocoes(), parse_mode='HTML')
    print(f'{msg.from_user.first_name} solicitou as promocoes')


bot.polling()
