import telebot
from telebot import apihelper
from telebot import types

token = "988269188:AAHXhq2vahut1mL4tJ0Ps62GgTMwGG7I4M0"
id = "797137132"
id2 = "1026388950"
site = "https://qiwi.me/oplataneona22"
channel = "@TriPna"
op = "@BitMeb"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
    bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Написал: " + str(message.text))
    bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Написал: " + str(message.text))
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Москва", callback_data="metro")
    button2 = types.InlineKeyboardButton(text="Воронеж", callback_data="button2")
    button3 = types.InlineKeyboardButton(text="Норильск", callback_data="button3")
    button4 = types.InlineKeyboardButton(text="Томск", callback_data="button4")
    button5 = types.InlineKeyboardButton(text="Краснодар", callback_data="button5")
    button6 = types.InlineKeyboardButton(text="Красноярск", callback_data="button6")
    button7 = types.InlineKeyboardButton(text="Иркутск", callback_data="button7")
    button8 = types.InlineKeyboardButton(text="Улан-Удэ", callback_data="button8")
    button9 = types.InlineKeyboardButton(text="Бийск", callback_data="button9")
    button10 = types.InlineKeyboardButton(text="Борисоглебцк", callback_data="button10")
    button11 = types.InlineKeyboardButton(text="Пермь", callback_data="button11")
    button12 = types.InlineKeyboardButton(text="Екатеринбург", callback_data="button12")
    button13 = types.InlineKeyboardButton(text="Сургут", callback_data="button13")
    button14 = types.InlineKeyboardButton(text="Сочи", callback_data="button14")
    button15 = types.InlineKeyboardButton(text="Ханты-Мансийский", callback_data="button15")
    button16 = types.InlineKeyboardButton(text="Абакан", callback_data="button16")
    button17 = types.InlineKeyboardButton(text="Оренбург", callback_data="button17")
    button18 = types.InlineKeyboardButton(text="Нижний Новгород", callback_data="button18")
    keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18)
    bot.send_message(message.chat.id, "Привет, "+str(message.chat.first_name)+".\nДобро пожаловать в наш бот удовольствий.\nИНФ-канал: "+str(channel)+"\nОператор: "+str(op)+"\nПожалуйста, выберите город:", reply_markup=keyboard)


def metro(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="ВДНХ", callback_data="meVDN")
    button2 = types.InlineKeyboardButton(text="Киевская", callback_data="meKIE")
    button3 = types.InlineKeyboardButton(text="Китай-город", callback_data="meKIT")
    button4 = types.InlineKeyboardButton(text="Комсомольская", callback_data="meKOM")
    button5 = types.InlineKeyboardButton(text="Кропоткинская", callback_data="meKRO")
    button6 = types.InlineKeyboardButton(text="Новогиреево", callback_data="meNOV")
    button7 = types.InlineKeyboardButton(text="Новокосино", callback_data="meNOVOK")
    button8 = types.InlineKeyboardButton(text="Новокузнецкая", callback_data="meNOVOKU")
    button9 = types.InlineKeyboardButton(text="Новослободская", callback_data="meNOVOS")
    button10 = types.InlineKeyboardButton(text="Охотный Ряд", callback_data="meOXO")
    button11 = types.InlineKeyboardButton(text="Парк Победы", callback_data="mePAR")
    button12 = types.InlineKeyboardButton(text="Перово", callback_data="mePER")
    button13 = types.InlineKeyboardButton(text="Площадь Революции", callback_data="mePLO")
    button14 = types.InlineKeyboardButton(text="Полянка", callback_data="mePOL")
    button15 = types.InlineKeyboardButton(text="Рижская", callback_data="meRIG")
    button16 = types.InlineKeyboardButton(text="Фрунзенская", callback_data="meFRU")
    button17 = types.InlineKeyboardButton(text="ЦСКА", callback_data="meCSK")
    button18 = types.InlineKeyboardButton(text="Юго-Западная", callback_data="meUGO")
    button19 = types.InlineKeyboardButton(text="Выстовочная", callback_data="meVIST")
    button20 = types.InlineKeyboardButton(text="Ховрино", callback_data="meHOVR")
    button21 = types.InlineKeyboardButton(text="Выхино", callback_data="meVIXI")
    keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18, button19, button20, button21)
    bot.send_message(message.chat.id, "Пожалуйста, выберите метро:", reply_markup=keyboard)

def button(message, city, metr="Нету"):
    keyboard1 = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="МЕФ", callback_data="ME")
    button2 = types.InlineKeyboardButton(text="СОЛЬ", callback_data="SO")
    button3 = types.InlineKeyboardButton(text="ГАШИШ", callback_data="GA")
    button4 = types.InlineKeyboardButton(text="ЛСД", callback_data="LS")
    button5 = types.InlineKeyboardButton(text="ТРАВА", callback_data="TR")
    button6 = types.InlineKeyboardButton(text="КОКАИН", callback_data="CO")
    button7 = types.InlineKeyboardButton(text="АМФЕТАМИН", callback_data="AM")
    bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Выбрал: " + str(city))
    bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(city))
    if metr!="Нету":
        bot.send_message(id, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(metr))
        bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(metr))
    keyboard1.add(button1)
    keyboard1.add(button2)
    keyboard1.add(button3)
    keyboard1.add(button4)
    keyboard1.add(button5)
    keyboard1.add(button6)
    keyboard1.add(button7)
    bot.send_message(message.chat.id, "Вы выбрали город "+str(city)+".\nМетро: "+str(metr)+ "\nТеперь выберите товар:", reply_markup=keyboard1)

def ME(message, name):
    keyboard2 = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="0.5г - 900р", callback_data="M05")
    button2 = types.InlineKeyboardButton(text="1г - 1500р", callback_data="M1")
    button3 = types.InlineKeyboardButton(text="2г - 2000р", callback_data="M2")
    bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Выбрал: " + str(name))
    bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(name))
    keyboard2.add(button1)
    keyboard2.add(button2)
    keyboard2.add(button3)
    bot.send_message(message.chat.id, "Вы выбрали "+str(name)+".\nТеперь выберите количество:", reply_markup=keyboard2)

def SO(message, name):
    keyboard2 = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="1г - 1100р", callback_data="S1")
    button2 = types.InlineKeyboardButton(text="2г - 1900р", callback_data="S2")
    bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Выбрал: " + str(name))
    bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(name))
    keyboard2.add(button1)
    keyboard2.add(button2)
    bot.send_message(message.chat.id, "Вы выбрали "+str(name)+".\nТеперь выберите количество:", reply_markup=keyboard2)

def GA(message, name):
    keyboard2 = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton(text="1г - 950р", callback_data="G1")
    button3 = types.InlineKeyboardButton(text="2г - 1550р", callback_data="G2")
    bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Выбрал: " + str(name))
    bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(name))
    keyboard2.add(button2)
    keyboard2.add(button3)
    bot.send_message(message.chat.id, "Вы выбрали "+str(name)+".\nТеперь выберите количество:", reply_markup=keyboard2)

def LS(message, name):
    keyboard2 = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton(text="1шт - 950р", callback_data="L1")
    button3 = types.InlineKeyboardButton(text="2шт - 1650р", callback_data="L2")
    bot.send_message(id, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(name))
    bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(name))
    keyboard2.add(button2)
    keyboard2.add(button3)
    bot.send_message(message.chat.id, "Вы выбрали " + str(name) + ".\nТеперь выберите количество:",
                     reply_markup=keyboard2)

def TR(message, name):
    keyboard2 = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton(text="1г - 1500р", callback_data="T1")
    button3 = types.InlineKeyboardButton(text="2г - 2000р", callback_data="T2")
    bot.send_message(id, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(name))
    bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(name))
    keyboard2.add(button2)
    keyboard2.add(button3)
    bot.send_message(message.chat.id, "Вы выбрали " + str(name) + ".\nТеперь выберите количество:",
                     reply_markup=keyboard2)

def CO(message, name):
    keyboard2 = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton(text="0.5г - 5000р", callback_data="C05")
    button3 = types.InlineKeyboardButton(text="1г - 9000р", callback_data="C1")
    bot.send_message(id, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(name))
    bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(name))
    keyboard2.add(button2)
    keyboard2.add(button3)
    bot.send_message(message.chat.id, "Вы выбрали " + str(name) + ".\nТеперь выберите количество:",
                     reply_markup=keyboard2)

def AM(message, name):
    keyboard2 = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton(text="1г - 950р", callback_data="A1")
    button3 = types.InlineKeyboardButton(text="2г - 1350р", callback_data="A2")
    bot.send_message(id, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(name))
    bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Выбрал: " + str(name))
    keyboard2.add(button2)
    keyboard2.add(button3)
    bot.send_message(message.chat.id, "Вы выбрали " + str(name) + ".\nТеперь выберите количество:",
                     reply_markup=keyboard2)

def buy(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Оплатить",url=site, callback_data="by")
    keyboard.add(button1)
    bot.send_message(message.chat.id, "Для оплаты нажмите на кнопку:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    message = call.message
    if call.message:
        if call.data == "button1":
            button(call.message, "Москва")
        elif call.data == "button2":
            button(call.message, "Воронеж")
        elif call.data == "button3":
            button(call.message, "Норильск")
        elif call.data == "button4":
            button(call.message, "Томск")
        elif call.data == "button5":
            button(call.message, "Краснодар")
        elif call.data == "button6":
            button(call.message, "Красноярск")
        elif call.data == "button7":
            button(call.message, "Иркутск")
        elif call.data == "button8":
            button(call.message, "Улан-Удэ")
        elif call.data == "button9":
            button(call.message, "Бийск")
        elif call.data == "button10":
            button(call.message, "Борисоглебцк")
        elif call.data == "button11":
            button(call.message, "Пермь")
        elif call.data == "button12":
            button(call.message, "Екатеринбург")
        elif call.data == "button13":
            button(call.message, "Сургут")
        elif call.data == "button14":
            button(call.message, "Сочи")
        elif call.data == "button15":
            button(call.message, "Ханты-Мансийский")
        elif call.data == "button16":
            button(call.message, "Абакан")
        elif call.data == "button17":
            button(call.message, "Оренбург")
        elif call.data == "button18":
            button(call.message, "Нижний Новгород")
        elif call.data == "ME":
            ME(call.message, "МЕФ")
        elif call.data == "SO":
            SO(call.message, "СОЛЬ")
        elif call.data == "GA":
            GA(call.message, "ГАШИШ")
        elif call.data == "LS":
            LS(call.message, "ЛСД")
        elif call.data == "TR":
            TR(call.message, "ТРАВА")
        elif call.data == "CO":
            CO(call.message, "КОКАИН")
        elif call.data == "AM":
            AM(call.message, "АМФЕТАМН")


        elif call.data == "metro":
            metro(call.message)

        elif call.data == "meVDN":
            button(call.message, "Москва" , "ВДНХ")
        elif call.data == "meKIE":
            button(call.message, "Москва" , "Киевская")
        elif call.data == "meKIT":
            button(call.message, "Москва" , "Китай-город")
        elif call.data == "meKOM":
            button(call.message, "Москва" , "Комсомольская")
        elif call.data == "meKRO":
            button(call.message, "Москва" , "Кропоткинская")
        elif call.data == "meNOV":
            button(call.message, "Москва" , "Новогиреево")
        elif call.data == "meNOVOK":
            button(call.message, "Москва" , "Новокосино")
        elif call.data == "meNOVOKU":
            button(call.message, "Москва" , "Новокузнецкая")
        elif call.data == "meNOVOS":
            button(call.message, "Москва" , "Новослободская")
        elif call.data == "meOXO":
            button(call.message, "Москва" , "Охотный Ряд")
        elif call.data == "mePAR":
            button(call.message, "Москва" , "Парк Победы")
        elif call.data == "mePER":
            button(call.message, "Москва" , "Перово")
        elif call.data == "mePLO":
            button(call.message, "Москва" , "Площадь Революции")
        elif call.data == "mePOL":
            button(call.message, "Москва" , "Полянка")
        elif call.data == "meRIG":
            button(call.message, "Москва" , "Рижская")
        elif call.data == "meFRU":
            button(call.message, "Москва" , "Фрунзенская")
        elif call.data == "meCSK":
            button(call.message, "Москва" , "ЦСКА")
        elif call.data == "meUGO":
            button(call.message, "Москва" , "Юго-Западная")
        elif call.data == "meVIST":
            button(call.message, "Москва" , "Выстовочная")
        elif call.data == "meHOVR":
            button(call.message, "Москва" , "Ховрино")
        elif call.data == "meVIXI":
            button(call.message, "Москва" , "Выхино")


        elif call.data == "M05":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | МЕФ 0.5г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | МЕФ 0.5г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали МЕФ 0.3г\nК оплате: 900р.\nКоментарий: "+str(message.chat.id))
            buy(message)
        elif call.data == "M1":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: МЕФ 1г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: МЕФ 1г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали МЕФ 1г\nК оплате: 1500р.\nКоментарий: "+str(message.chat.id))
            buy(message)
        elif call.data == "M2":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: МЕФ 2г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: МЕФ 2г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали МЕФ 2г\nК оплате: 2000р.\nКоментарий: "+str(message.chat.id))
            buy(message)

        elif call.data == "S1":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: СОЛЬ 1г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: СОЛЬ 1г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали СОЛЬ 1г\nК оплате: 1100р.\nКоментарий: "+str(message.chat.id))
            buy(message)
        elif call.data == "S2":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: СОЛЬ 2г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: СОЛЬ 2г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали СОЛЬ 2г\nК оплате: 1900р.\nКоментарий: "+str(message.chat.id))
            buy(message)

        elif call.data == "G1":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: ГАШИШ 1г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: ГАШИШ 1г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали ГАШИШ 1г\nК оплате: 950р.\nКоментарий: "+str(message.chat.id))
            buy(message)
        elif call.data == "G2":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: ГГАШИШ 2г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: ГГАШИШ 2г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали ГАШИШ 2г\nК оплате: 1550р.\nКоментарий: "+str(message.chat.id))
            buy(message)

        elif call.data == "L1":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: ЛСД 1шт")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: ЛСД 1шт")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали ЛСД 1шт\nК оплате: 950р.\nКоментарий: "+str(message.chat.id))
            buy(message)
        elif call.data == "L2":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: Гашиш на реагенте 2шт")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: Гашиш на реагенте 2шт")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали ЛСД 2шт\nК оплате: 1650р.\nКоментарий: "+str(message.chat.id))
            buy(message)

        elif call.data == "T1":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: ТРАВА 1г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: ТРАВА 1г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали ТРАВА 1г\nК оплате: 1500р.\nКоментарий: "+str(message.chat.id))
            buy(message)
        elif call.data == "T2":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: ТРАВА 2г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: ТРАВА 2г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали ТРАВА 2г\nК оплате: 2000р.\nКоментарий: "+str(message.chat.id))
            buy(message)

        elif call.data == "C05":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: КОКАИН 0.5г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: КОКАИН 0.5г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали КОКАИН 0.5г\nК оплате: 5000р.\nКоментарий: "+str(message.chat.id))
            buy(message)
        elif call.data == "C1":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: КОКАИН 1г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: КОКАИН 1г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали КОКАИН 1г\nК оплате: 9000р.\nКоментарий: "+str(message.chat.id))
            buy(message)

        elif call.data == "A1":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: АМФЕТАМИН 1г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: АМФЕТАМИН 1г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали АМФЕТАМИН 1г\nК оплате: 950р.\nКоментарий: "+str(message.chat.id))
            buy(message)
        elif call.data == "A2":
            bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Оплачивает: АМФЕТАМИН 2г")
            bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Оплачивает: АМФЕТАМИН 2г")
            bot.send_message(message.chat.id, "QIWI\nВы выбрали ГАМФЕТАМИН 2г\nК оплате: 1350р.\nКоментарий: "+str(message.chat.id))
            buy(message)

@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.send_message(id, str(message.chat.first_name) + " [ "+ str(message.chat.id)+" ] | Написал: " + str(message.text))
    bot.send_message(id2, str(message.chat.first_name) + " [ " + str(message.chat.id) + " ] | Написал: " + str(message.text))
    bot.send_message(message.chat.id, "Вы что-то делаете не так, пожалуйста нажмите -  /start")

while True:
    bot.polling(none_stop=True)
