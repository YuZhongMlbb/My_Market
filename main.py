import telebot
from config import TOKEN
import requests
from bs4 import BeautifulSoup
import random
import psycopg2

class Market():

    def __init__(self) -> None:

        self.enter_monitors = 'https://enter.kg/monitory_bishkek'
        self.enter_processors = 'https://enter.kg/processory_bishkek'
        self.enter_MP = 'https://enter.kg/materinskie-platy_bishkek'

        self.kivano_elektronika = 'https://www.kivano.kg/elektronika'
        self.kivano_computers = 'https://www.kivano.kg/kompyutery'
        self.kivano_tech = 'https://www.kivano.kg/bytovaya-tekhnika'
    
    def parse_enter_monitors(self):
        r = requests.get(url=self.enter_monitors)
        soup = BeautifulSoup(r.content, 'html.parser')
        items = soup.find_all('div', class_="product vm-col vm-col-1")
        new_list = list()

        for elem in items:
            new_list.append(
                {
                    'title': elem.find('span', class_="prouct_name").find('a').get_text(strip=True),
                    'price': elem.find('span', class_="price").get_text(strip=True),
                    'image': elem.find('a', class_="product-image-link").find('img').get('src'),
                    'articul': elem.find('span', class_="sku").get_text(strip=True)
                }
            )

        for new in new_list:
            yield new
    
    def parse_enter_processors(self):
        r = requests.get(url=self.enter_processors)
        soup = BeautifulSoup(r.content, 'html.parser')
        items = soup.find_all('div', class_="product vm-col vm-col-1")
        new_list = list()

        for elem in items:
            new_list.append(
                {
                    'title': elem.find('span', class_="prouct_name").find('a').get_text(strip=True),
                    'price': elem.find('span', class_="price").get_text(strip=True),
                    'image': elem.find('a', class_="product-image-link").find('img').get('src'),
                    'articul': elem.find('span', class_="sku").get_text(strip=True)
                }
            )
        
        for new in new_list:
            yield new
    
    def parse_enter_MP(self):
        r = requests.get(url=self.enter_MP)
        soup = BeautifulSoup(r.content, 'html.parser')
        items = soup.find_all('div', class_="product vm-col vm-col-1")
        new_list = list()

        for elem in items:
            new_list.append(
                {
                    'title': elem.find('span', class_="prouct_name").find('a').get_text(strip=True),
                    'price': elem.find('span', class_="price").get_text(strip=True),
                    'image': elem.find('a', class_="product-image-link").find('img').get('src'),
                    'articul': elem.find('span', class_="sku").get_text(strip=True)
                }
            )
        
        for new in new_list:
            yield new
    
    def parse_kivano_computers(self):
        r = requests.get(url=self.kivano_computers)
        soup = BeautifulSoup(r.content, 'html.parser')
        items = soup.find_all('div', class_="item product_listbox oh")
        new_list = list()

        for elem in items:
            new_list.append(
                {
                    'title': elem.find('div', class_="listbox_title oh").find('a').get_text(strip=True),
                    'price': elem.find('div', class_="listbox_price text-center").get_text(strip=True),
                    'image': elem.find('div', class_="listbox_img pull-left").find('a').find('img').get('src'),
                    'articul': f"{random.randint(200000, 299999)}"
                }
            )
        
        for new in new_list:
            yield new
    
    def parse_kivano_elektronika(self):
        r = requests.get(url=self.kivano_elektronika)
        soup = BeautifulSoup(r.content, 'html.parser')
        items = soup.find_all('div', class_="item product_listbox oh")
        new_list = list()

        for elem in items:
            new_list.append(
                {
                    'title': elem.find('div', class_="listbox_title oh").find('a').get_text(strip=True),
                    'price': elem.find('div', class_="listbox_price text-center").get_text(strip=True),
                    'image': elem.find('div', class_="listbox_img pull-left").find('a').find('img').get('src'),
                    'articul': f"{random.randint(200000, 299999)}"
                }
            )
        
        for new in new_list:
            yield new
    
    def parse_kivano_tech(self):
        r = requests.get(url=self.kivano_tech)
        soup = BeautifulSoup(r.content, 'html.parser')
        items = soup.find_all('div', class_="item product_listbox oh")
        new_list = list()

        for elem in items:
            new_list.append(
                {
                    'title': elem.find('div', class_="listbox_title oh").find('a').get_text(strip=True),
                    'price': elem.find('div', class_="listbox_price text-center").get_text(strip=True),
                    'image': elem.find('div', class_="listbox_img pull-left").find('a').find('img').get('src'),
                    'articul': f"{random.randint(200000, 299999)}"
                }
            )
    
        for new in new_list:
            yield new.text

registration = list()

f_market = Market()
se_market = Market()
t_market = Market()
fo_market = Market()
fi_market = Market()
si_market = Market()

a1 = f_market.parse_enter_monitors()
a2 = se_market.parse_enter_processors()
a3 = t_market.parse_enter_MP()
a4 = fo_market.parse_kivano_elektronika()
a5 = fi_market.parse_kivano_computers()
a6 = si_market.parse_kivano_tech()

conn = psycopg2.connect(dbname="new", user="new", password="new", host="localhost", port=5432)
cursor = conn.cursor()
conn.autocommit = True

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Enter", "Kivano", "О себе")
    bot.send_message(message.chat.id, f"<b>Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}.\nПредлагаем вам выбрать магазин: </b>", reply_markup=markup, parse_mode='html')

@bot.message_handler(content_types=['text'])

def msg(message):
    if message.text == "Enter":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("Мониторы", "Процессоры", "Материнские платы")
        bot.send_message(message.chat.id, "Выберите категорию: ", reply_markup=markup)
    elif message.text == "Kivano":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("Электроника", "Компьютеры", "Бытовая техника")
        bot.send_message(message.chat.id, "Выберите категорию: ", reply_markup=markup)
    elif message.text == "О себе":
        bot.send_message(message.chat.id, "Мне 15 лет, работаю с маркетами Enter и Kivano\nМоя фотка: ")
        bot.send_photo(message.chat.id, photo="/home/annur/Загрузки/рБез имени.jpeg")
    elif message.text == "Мониторы":
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        m1 = telebot.types.InlineKeyboardButton("Купить", callback_data="buy")
        m2 = telebot.types.InlineKeyboardButton("Далее", callback_data="next")
        markup.add(m1, m2)
        bot.send_message(message.chat.id, f"{next(a1)}", reply_markup=markup)
    elif message.text == "Процессоры":
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        m1 = telebot.types.InlineKeyboardButton("Купить", callback_data="buy")
        m2 = telebot.types.InlineKeyboardButton("Далее", callback_data="next")
        markup.add(m1, m2)
        bot.send_message(message.chat.id, f"{next(a2)}", reply_markup=markup)
    elif message.text == "Материнские платы":
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        m1 = telebot.types.InlineKeyboardButton("Купить", callback_data="buy")
        m2 = telebot.types.InlineKeyboardButton("Далее", callback_data="next")
        markup.add(m1, m2)
        bot.send_message(message.chat.id, f"{next(a3)}", reply_markup=markup)
    elif message.text == "Электроника":
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        m1 = telebot.types.InlineKeyboardButton("Купить", callback_data="buy")
        m2 = telebot.types.InlineKeyboardButton("Далее", callback_data="next")
        markup.add(m1, m2)
        bot.send_message(message.chat.id, f"{next(a4)}", reply_markup=markup)
    elif message.text == "Компьютеры":
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        m1 = telebot.types.InlineKeyboardButton("Купить", callback_data="buy")
        m2 = telebot.types.InlineKeyboardButton("Далее", callback_data="next")
        markup.add(m1, m2)
        bot.send_message(message.chat.id, f"{next(a5)}", reply_markup=markup)
    elif message.text == "Бытовая техника":
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        m1 = telebot.types.InlineKeyboardButton("Купить", callback_data="buy")
        m2 = telebot.types.InlineKeyboardButton("Далее", callback_data="next")
        markup.add(m1, m2)
        bot.send_message(message.chat.id, f"{next(a6)}", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)

def callback(call):
    if call.data == "buy":
        bot.send_message(call.message.chat.id, "Введите ФИО, артикул товара, контактный телефон и время заказа(через запятую): ")
        bot.register_next_step_handler(call.message, texts)
    elif call.data == "next":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("Enter", "Kivano", "О себе")
        bot.send_message(call.message.chat.id, "Продолжим?", reply_markup=markup)

@bot.message_handler(func=lambda message:True)

def texts(message):
    if message.text is not None:
        for i in message.text.split(','):
            registration.append(i)
        bot.send_message(message.chat.id, "Данные сохранены")
        save()

def save():
    if len(registration) >= 4:
        cursor.execute(f"insert into new(name, articul, phone, time) values('{registration[0]}', '{registration[1]}', '{registration[2]}', '{registration[3]}')")
    else:
        print('мало информации')

bot.polling(non_stop=True)