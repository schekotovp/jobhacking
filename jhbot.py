# -*- coding: utf-8 -*-
import telebot
from telebot import types

token = '1241832800:AAE3eEk5Z3cuF2S8lRNZLvy7Wqxt8uzyFhM'


vacname = ''
companyname = ''
reqs = []
resps = []
terms = []
salary = ''

explanations = 'Отлично 👍\n\nПеред тем, как мы начнём, обрати внимание на пояснения ниже:\n\n📍Требования - навыки, опыт, возраст, местоположение и тд\n\n📍Обязанности - что должен делать сотрудник на этой должности\n\n📍Условия - график, занятость, офис и тд\n\n❗️всего доступно до 5 пунктов каждого элемента, выделяй самое важное❗️\n\n📍Зарплата - отдельный пункт (не указывается в условиях!)'
employer = "<b>Кто работодатель?</b>\n(если компания - укажите название/если блогер - укажите аккаунт)"
req01 = "<b>️Начнём с требований</b>❗\n\n📍<b>Какой требуется опыт?</b>\n(кол-во лет либо «не требуется»)"
req02 = "📍<b>Какими программами должен владеть кандидат?</b>\n(перечислите названия)"
req03 = "📍<b>Где должен проживать кандидат?</b>\n(город/неважно)"
req04 = "📍<b>Какими еще навыками должен обладать кандидат?</b>"
req05 = "📍<b>Что-то ещё?</b>\n(если что-то упустили - допишите здесь, в противном случае пропустите шаг с помощью кнопки под строкой ввода)"

term01 = "<b>Завершим условиями</b>❗️\n\n📍<b>Введите график работы</b>\n(свободный, 5/2 и т.п.)"
term02 = "📍<b>Работа удалённая или в офисе?</b>\n(если в офисе, не забудьте указать его адрес)"
term03 = "📍<b>Что-то ещё?</b>\n(если что-то упустили - допишите здесь, в противном случае, пропустите шаг с помощью кнопки под строкой ввода)"
salarytext = "📍<b>Заработная плата</b>\n(укажите зарплату в месяц или размер сдельной оплаты)"
bot = telebot.TeleBot(token)


# клавиатура для вакансий
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item1 = types.KeyboardButton("Добавить вакансию")
# item2 = types.KeyboardButton("Резюме")
markup.add(item1)


markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
item11 = types.KeyboardButton("Следующий шаг")
item12 = types.KeyboardButton("Отменить")
item13 = types.KeyboardButton("Перезапустить")
markup1.add(item11, item12, item13)


markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item21 = types.KeyboardButton("Тариф 1")
item22 = types.KeyboardButton("Тариф 2")
item23 = types.KeyboardButton("Тариф 3")
markup2.add(item21, item22, item23)


markuppp = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
item32 = types.KeyboardButton("Отменить")
item33 = types.KeyboardButton("Перезапустить")
markuppp.add(item32, item33)

markupexp = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
itemexp = types.KeyboardButton("Понятно")
markupexp.add(itemexp)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(message.from_user,
                                                                                                    bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def ans(message):
    global explanations
    textus = message.text
    if textus == 'Добавить вакансию':
        msg = bot.send_message(message.chat.id, explanations, parse_mode='html', reply_markup=markupexp)
        bot.register_next_step_handler(msg, expl)
#    elif textus == 'Резюме':
#       bot.send_message(message.chat.id, 'Введите ФИО', reply_markup=markup1)
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю', reply_markup=markup)


def expl(message):
    textus = message.text
    if textus == 'Понятно':
        msg = bot.send_message(message.chat.id, 'Введите название вакансии', reply_markup=markuppp)
        bot.register_next_step_handler(msg, vac)
    else:
        msg1 = bot.send_message(message.chat.id, 'Я вас не понимаю', reply_markup=markupexp)
        bot.register_next_step_handler(msg1, expl)



def vac(message):
    global employer
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, employer, parse_mode='html', reply_markup=markuppp)
        bot.register_next_step_handler(msg, company)
    elif textus == "Отменить":
        msg1 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg1, ans)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        global vacname
        vacname = textus
        msg = bot.send_message(message.chat.id, employer, parse_mode='html', reply_markup=markuppp)
        bot.register_next_step_handler(msg, company)


def company(message):
    global req01
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, req01, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, req1)
    elif textus == "Отменить":
        msg1 = bot.send_message(message.chat.id, 'Введите название вакансии', reply_markup=markup1)
        bot.register_next_step_handler(msg1, vac)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        global companyname
        companyname = textus
        msg = bot.send_message(message.chat.id, req01, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, req1)



def req1(message):
    global req02
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, '<b>️Перейдём к обязанностям</b>❗\n(1 сообщение = 1 обязанность, всего до 5 штук)\n\n📍Введите <b>первую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, resp1)
    elif textus == "Отменить":
        msg1 = bot.send_message(message.chat.id, employer, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, company)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        global reqs
        reqs.append(textus)
        msg = bot.send_message(message.chat.id, req02, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, req2)


def req2(message):
    global req01
    global req03
    global reqs
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, '<b>️Перейдём к обязанностям</b>❗\n(1 сообщение = 1 обязанность, всего до 5 штук)\n\n📍Введите <b>первую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, resp1)
    elif textus == "Отменить":
        if len(reqs) != 0:
            del reqs[len(reqs) - 1]
        msg1 = bot.send_message(message.chat.id, req01, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, req1)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        reqs.append(textus)
        msg = bot.send_message(message.chat.id, req03, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, req3)


def req3(message):
    global req02
    global req04
    global reqs
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, '<b>️Перейдём к обязанностям</b>❗\n(1 сообщение = 1 обязанность, всего до 5 штук)\n\n📍Введите <b>первую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, resp1)
    elif textus == "Отменить":
        if len(reqs) != 0:
            del reqs[len(reqs) - 1]
        msg1 = bot.send_message(message.chat.id, req02, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, req2)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        reqs.append(textus)
        msg = bot.send_message(message.chat.id, req04, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, req4)


def req4(message):
    global req03
    global req05
    global reqs
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, '<b>️Перейдём к обязанностям</b>❗\n(1 сообщение = 1 обязанность, всего до 5 штук)\n\n📍Введите <b>первую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, resp1)
    elif textus == "Отменить":
        if len(reqs) != 0:
            del reqs[len(reqs) - 1]
        msg1 = bot.send_message(message.chat.id, req03, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, req3)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        reqs.append(textus)
        msg = bot.send_message(message.chat.id, req05, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, req5)


def req5(message):
    global req04
    global reqs
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, '<b>️Перейдём к обязанностям</b>❗\n(1 сообщение = 1 обязанность, всего до 5 штук)\n\n📍Введите <b>первую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, resp1)
    elif textus == "Отменить":
        if len(reqs) != 0:
            del reqs[len(reqs) - 1]
        msg1 = bot.send_message(message.chat.id, req04, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, req4)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        reqs.append(textus)
        msg = bot.send_message(message.chat.id, '<b>️Перейдём к обязанностям</b>❗\n(1 сообщение = 1 обязанность, всего до 5 штук)\n\n📍Введите <b>первую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, resp1)


def resp1(message):
    global term01
    global req05
    global reqs
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, term01, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, term1)
    elif textus == "Отменить":
        if len(reqs) != 0:
            del reqs[len(reqs) - 1]
        msg1 = bot.send_message(message.chat.id, req05, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, req5)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        global resps
        resps.append(textus)
        msg = bot.send_message(message.chat.id, '📍Введите <b>вторую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, resp2)


def resp2(message):
    global term01
    global resps
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, term01, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, term1)
    elif textus == "Отменить":
        if len(resps) != 0:
            del resps[len(resps) - 1]
        msg1 = bot.send_message(message.chat.id, '<b>️Перейдём к обязанностям</b>❗\n(1 сообщение = 1 обязанность, всего до 5 штук)\n\n📍Введите <b>первую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, resp1)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        resps.append(textus)
        msg = bot.send_message(message.chat.id, '📍Введите <b>третью обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, resp3)


def resp3(message):
    global term01
    global resps
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, term01, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, term1)
    elif textus == "Отменить":
        if len(resps) != 0:
            del resps[len(resps) - 1]
        msg1 = bot.send_message(message.chat.id, '📍Введите <b>вторую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, resp2)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        resps.append(textus)
        msg = bot.send_message(message.chat.id, '📍Введите <b>четвёртую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, resp4)


def resp4(message):
    global term01
    global resps
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, term01, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, term1)
    elif textus == "Отменить":
        if len(resps) != 0:
            del resps[len(resps) - 1]
        msg1 = bot.send_message(message.chat.id, '📍Введите <b>третью обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, resp3)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        resps.append(textus)
        msg = bot.send_message(message.chat.id, '📍Введите <b>пятую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, resp5)


def resp5(message):
    global term01
    global resps
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, term01, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, term1)
    elif textus == "Отменить":
        if len(resps) != 0:
            del resps[len(resps) - 1]
        msg1 = bot.send_message(message.chat.id, '📍Введите <b>четвёртую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, resp4)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        resps.append(textus)
        msg = bot.send_message(message.chat.id, term01, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, term1)


def term1(message):
    global term02
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, salarytext, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, sala)
    elif textus == "Отменить":
        global resps
        if len(resps) != 0:
            del resps[len(resps) - 1]
        msg1 = bot.send_message(message.chat.id, '📍Введите <b>пятую обязанность</b> (что должен делать сотрудник)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, resp5)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        global terms
        terms.append(textus)
        msg = bot.send_message(message.chat.id, term02, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, term2)


def term2(message):
    global term03
    global term01
    global terms
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, salarytext, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, sala)
    elif textus == "Отменить":
        if len(terms) != 0:
            del terms[len(terms) - 1]
        msg1 = bot.send_message(message.chat.id, term01, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, term1)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        terms.append(textus)
        msg = bot.send_message(message.chat.id, term03, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, term3)


def term3(message):
    global salarytext
    global term02
    global terms
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, salarytext, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, sala)
    elif textus == "Отменить":
        if len(terms) != 0:
            del terms[len(terms) - 1]
        msg1 = bot.send_message(message.chat.id, term02, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, term2)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        terms.append(textus)
        msg = bot.send_message(message.chat.id, salarytext, parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, sala)


def sala(message):
    textus = message.text
    if textus == "Следующий шаг":
        msg = bot.send_message(message.chat.id, 'Выберите тариф', reply_markup=markup2)
        bot.register_next_step_handler(msg, tariff)
    elif textus == "Отменить":
        if len(terms) != 0:
            del terms[len(terms) - 1]
        msg1 = bot.send_message(message.chat.id, '📍Введите <b>пятое условие</b> (график, занятость, офис и т.д.)', parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg1, term3)
    elif textus == "/start" or textus == "Перезапустить":
        msg3 = bot.send_message(message.chat.id,
                                "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(
                                    message.from_user, bot.get_me()),
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg3, ans)
    else:
        global salary
        salary = textus
        msg = bot.send_message(message.chat.id, 'Выберите тариф:\nТариф 1:\n-день в день\n-300₽\n\nТариф 2:\n-в течение 3х дней\n-200₽\n\nТариф 3:\n-в течение недели\n-100₽', reply_markup=markup2)
        bot.register_next_step_handler(msg, tariff)


def tariff(message):
    global vacname
    global companyname
    global reqs
    global resps
    global terms
    global salary
    request = 'Требования:\n'
    respon = 'Обязанности:\n'
    termm = 'Условия:\n'
    name = '@' + message.from_user.username
    textus = message.text
    tarif = textus

    for req in reqs:
        request += str('- ') + req + '\n'

    for resp in resps:
        respon += str('- ') + resp + '\n'

    for ter in terms:
        termm += str('- ') + ter + '\n'

    finish = 'Вакансия: ' + vacname + '\n' + 'Название компании: ' + companyname + '\n' + request + respon + termm +\
             'Зарплата - ' + salary + '\n' + tarif + '\n' + 'Отправил ' + name
    terms = []
    resps = []
    reqs = []
    bot.send_message(message.chat.id, 'Спасибо, с вами свяжется менеджер', reply_markup=markup)
    bot.send_message('@vaccccan', finish)


if __name__ == '__main__':
     bot.infinity_polling()