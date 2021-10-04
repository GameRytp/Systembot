import telebot
import config
import dbal
from telebot import types

bot = telebot.TeleBot(config.token)
coords=[["Следуйте к месту с координатами 55.733214, 37.626540", "Следуйте к месту с координатами 55.734383, 37.626567", "Следуйте к месту с координатами 55.736162, 37.625754", "Следуйте к месту с координатами 55.738523, 37.626307", "Следуйте к месту с координатами 55.739518, 37.626769", "Следуйте к месту с координатами 55.740650, 37.628030", "Следуйте к месту с координатами 55.738080, 37.629149", "Следуйте к месту с координатами 55.735441, 37.627456", "Следуйте к месту с координатами 55.732474, 37.626338", "Следуйте к месту с координатами 55.731961, 37.625533"],\
["Следуйте к месту с координатами 55.733205, 37.619128", "Следуйте к месту с координатами 55.731576, 37.622997, 37.626567", "Следуйте к месту с координатами 55.732433, 37.624540", "Следуйте к месту с координатами 55.734593, 37.624767", "Следуйте к месту с координатами 55.736551, 37.625081", "Следуйте к месту с координатами где-то 55.738636, 37.624621", "Следуйте к месту с координатами 55.739263, 37.622021", "Следуйте к месту с координатами 55.737835, 37.620433", "Следуйте к месту с координатами 55.736622, 37.619960", "Следуйте к месту с координатами 55.735276, 37.619326"],\
["Следуйте к месту с координатами 55.718887, 37.624521", "Следуйте к месту с координатами 55.717461, 37.623733", "Следуйте к месту с координатами 55.718615, 37.622560", "Следуйте к месту с координатами 55.721053, 37.622622", "Следуйте к месту с координатами 55.722101, 37.621310", "Следуйте к месту с координатами 55.724143, 37.621916, 37.628030", "Следуйте к месту с координатами 55.726016, 37.623931", "Следуйте к месту с координатами 55.724075, 37.625675", "Следуйте к месту с координатами 55.722491, 37.626735", "Следуйте к месту с координатами 55.720763, 37.626504"]]
plot=["🤖", "🤖", "Меня увезли, не дали поговорить с мужем, ничего не объяснили. Я знаю это место, бывала здесь, когда проходила практику – это подвальное помещение, здесь нет окон и только искусственный свет от ламп, которые так противно трещат. Меня подключи к компьютеру с одной стороны, а с другой поставили непонятный аппарат и провода от него тянулись к голове, руке и бедру. Мне задавали вопросы из разных сфер, когда ответ был верен ничего не происходило, но стоило допустить ошибку, как разряды тока пропускали через все тело. Они вели записи и что-то в них помечали. Мне до сих пор ничего не говорят", "🤖", "🤖", "Утром меня повезли в северное крыло нашей лаборатории, я знала, что там находился тренажерный зал. Ко мне опять присоединили датчики, отслеживающие пульс, давление, насыщенность кислородом и тд. Я встала на дорожку и начала бежать. Темп постепенно увеличивался, но я не чувствовала усталости или боли в мышцах, абсолютно ничего. Это продолжалось в течении нескольких часов, когда всё закончилось и ассистентка снимала с меня датчики, я почувствовала странный звон в ушах и в следующую секунду отчетливо услышала, что происходило за закрытыми дверьми. Учёные говорили о том, что мутация проходит успешно, все показатели в норме, а по признакам я всё больше становлюсь роботом. Но у них появилась проблема, теперь меня хотят заполучить другие страны, может начаться борьба за неё. Боже, они говорят, что меня надо будет вывезти в охраняемое место и желательно сделать это без лишних слухов.", "🤖", "https://youtu.be/XHPhVRxCaP0", "Я проснулась посреди ночи от ночного кошмара, голова трещала, но самое страшное было то, что мой сон как будто и не закончился. Я слышу голоса и вижу перед глазами страшные вещи – это какая – то катастрофа, которая ждёт нас в ближайшее время я позвала одного из учёных и молила их, чтобы они остановили это, но в ответ услышал, что это нормально, это моя миссия. Я так больше не могу! Помогите мне скорее!", "🤖"]
answers=["дедлайн","91209760","21381376","красные розы","мир принадлежит терпеливым", "акрополь", "фунты стерлингов", "скорлупка", "39332,33", "164019"]
questions = ["всегда нужно смотреть по сторонам", "2", "1", "Следуйте указаниям актера", "105 100 101 110 116 105 116 121 100 111 99 117 109 101 110 116 40 48 48 48 48 48 48 53 57 53 57 32 102 97 98 114 105 107 97 110 116 110 117 109 109 101 114 41", "cez", "Следуйте указаниям актера" , "10 00 101 111 110 100 01 10 0 1100 01 1000 1011 011 01 0111 1 0 0110 010 111 1111 01 0110 101 001 110011", "цсыъфн овл, прыъуъссдх ся моц, рфольуаът ыр нрмдй ц рмэъм ээрыцт зъоъч чяпамлб", "сегодня; Варфоломеевская ночь" ]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Привет! Я великий бот Systema)")
    bot.send_message(message.from_user.id, "Вот что я умею:")
    bot.send_message(message.from_user.id, "1. Напиши /StartG, чтобы начать игру")
    bot.send_message(message.from_user.id, "2. Напиши /reset, чтобы сбросить весь результат")
    bot.send_message(message.from_user.id, "3. Чтобы узнать об авторах проекта, напиши /authors")
    dbal.set_state(message.chat.id) #Закидываем в БД значение этапа квеста [1];
    dbal.letnext(message.chat.id)
    #bot.send_message(message.from_user.id, dbal.out(message.chat.id))

@bot.message_handler(commands=['StartG'])
def stg(message):
    bot.send_message(message.from_user.id, "Выбери номер линии. Напиши /1, /2 или /3")





@bot.message_handler(commands=['StartGame'])
def plott(message):
	if dbal.checknext(message.chat.id):
		if int(dbal.out(message.chat.id))<=9:
			bot.send_message(message.from_user.id, plot[int(dbal.out(message.chat.id))] )
			dbal.plusState(message.chat.id)
			keyboard = types.InlineKeyboardMarkup()
			key_one = types.InlineKeyboardButton(text="1", callback_data="1")
			keyboard.add(key_one)
			key_two = types.InlineKeyboardButton(text='2', callback_data='2')
			keyboard.add(key_two)
			key_three = types.InlineKeyboardButton(text='3', callback_data='3')
			keyboard.add(key_three)
			key_four = types.InlineKeyboardButton(text='4', callback_data='4')
			keyboard.add(key_four)
			key_five = types.InlineKeyboardButton(text='5', callback_data='5')
			keyboard.add(key_five)
			key_six = types.InlineKeyboardButton(text='6', callback_data='6')
			keyboard.add(key_six)
			key_seven = types.InlineKeyboardButton(text='7', callback_data='7')
			keyboard.add(key_seven)
			key_eight = types.InlineKeyboardButton(text='8', callback_data='8')
			keyboard.add(key_eight)
			key_nine = types.InlineKeyboardButton(text='9', callback_data='9')
			keyboard.add(key_nine)
			key_ten = types.InlineKeyboardButton(text='10', callback_data='10')
			keyboard.add(key_ten)
			bot.send_message(message.from_user.id, text='Выбери номер станции', reply_markup=keyboard)
			dbal.nonext(message.chat.id)			
		else:
			bot.send_message(message.from_user.id, text='Ты закончил квест, осталось решить судьбу Марты. Напиши /becomebot, чтобы она стала роботом и /human, чтобы она осталась человеком')
	else:
		bot.send_message(message.from_user.id, "Прости, но ты не решил задачу, чтобы перейти на новый уровень")
 
@bot.message_handler(commands=['1'])
def one(message):
    dbal.setline(message.chat.id, 0)
    bot.send_message(message.from_user.id, "Данные приняты. Напиши /StartGame, чтобы начать квест")

@bot.message_handler(commands=['2'])
def two(message):
    dbal.setline(message.chat.id, 1)
    bot.send_message(message.from_user.id, "Данные приняты. Напиши /StartGame, чтобы начать квест")

@bot.message_handler(commands=['3'])
def three(message):
    dbal.setline(message.chat.id, 2)
    bot.send_message(message.from_user.id, "Данные приняты. Напиши /StartGame, чтобы начать квест")
        
@bot.message_handler(commands=['becomebot'])
def human(message):
    bot.send_message(message.from_user.id, "https://youtu.be/a-n4Cu-weik ")
    bot.send_message(message.from_user.id, "Мы рады тебе сообщить, что ваша команда попала в топ проекта 'Система', но какое место заняла ваша команда вы узнаете на вечерке. Следи за информацией в группе")
    
@bot.message_handler(commands=['human'])
def human(message):
    bot.send_message(message.from_user.id, "https://youtu.be/6hyQkGq4rOM")  
    bot.send_message(message.from_user.id, "Мы рады тебе сообщить, что ваша команда попала в топ проекта 'Система', но какое место заняла ваша команда вы узнаете на вечерке. Следи за информацией в группе")
    
@bot.message_handler(commands=['reset'])
def res(message):
    dbal.set_state(message.chat.id)
    dbal.letnext(message.chat.id)
    dbal.setStation(message.chat.id, -1)
    bot.send_message(message.from_user.id, "Данные успешно сброшены")


@bot.message_handler(commands=['authors'])
def res(message):
    bot.send_message(message.from_user.id, "Полина Петрова – менеджер проекта🐥")
    bot.send_photo(message.chat.id, open("polina.jpg", "rb"))
    bot.send_message(message.from_user.id, "Ксюша Лисина – ответственная за кураторов команд💬")
    bot.send_photo(message.chat.id, open("ksysha.jpg", "rb"))
    bot.send_message(message.from_user.id, "Маша Крестова – ответственная за направления SMM, дизайн и продвижение проекта🗣")
    bot.send_photo(message.chat.id, open("masha.jpg", "rb"))
    bot.send_message(message.from_user.id, "Загир Чурагулов – ответственный за разработку головоломок и задач на проекте🧩")
    bot.send_photo(message.chat.id, open("zagir.jpg", "rb"))
    bot.send_message(message.from_user.id, "Лиза Шаганова – ответственная за фото на проекте📸")
    bot.send_photo(message.chat.id, open("liza.jpg", "rb"))
    bot.send_message(message.from_user.id, "Юля Вахрушева – ответственная за видео, благодаря которым мы запомним это проект надолго🎬")
    bot.send_photo(message.chat.id, open("july.jpg", "rb"))
    bot.send_message(message.from_user.id, "Надя Чернюк – ответственная за программу и сценарий проекта📝")
    bot.send_photo(message.chat.id, open("nadia.jpg", "rb"))
    bot.send_message(message.from_user.id, "Катя Василенко – ответственная за программу и сценарий проекта📝")
    bot.send_photo(message.chat.id, open("kate.jpg", "rb"))
    bot.send_message(message.from_user.id, "Костя Долгополов – ответственный за разработку и поддержку Telegram-бота📲")
    bot.send_photo(message.chat.id, open("kostya.png", "rb"))


@bot.callback_query_handler(func=lambda call: True)
def check(call):
    if int(call.data)==2 or int(call.data)==3 or int(call.data)==6:
        if int(call.data)==2:
            bot.send_photo(call.message.chat.id, open("frame.png", "rb"))
        elif int(call.data)==6:
            bot.send_photo(call.message.chat.id, open("4.jpg", "rb"))
        elif int(call.data)==3 and int(dbal.outline(call.message.chat.id))==0:
            bot.send_photo(call.message.chat.id, open("1.jpg", "rb"))
        elif int(call.data)==3 and int(dbal.outline(call.message.chat.id))==1:
            bot.send_photo(call.message.chat.id, open("2.jpg", "rb"))
        else:
            bot.send_photo(call.message.chat.id, open("3.jpg", "rb"))
    else:bot.send_message(call.message.chat.id, questions[int(call.data)-1])
    dbal.setStation(call.message.chat.id, int(call.data)-1)
    


@bot.message_handler(content_types=['text'])
def get_text_messages(message):  
    if answers[int( dbal.outStation(message.chat.id))] == message.text:
       bot.send_message(message.from_user.id, 'Молодец! Ты прав')
       bot.send_message(message.from_user.id, coords[int(dbal.outline(message.chat.id))][int(dbal.outStation(message.chat.id))])
       dbal.letnext(message.chat.id)
       plott(message)
    else:
        bot.send_message(message.chat.id, "К сожалению, ответ неверный, попробуй еще)")
        return

bot.polling(none_stop=True)
