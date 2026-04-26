# 🤖 КУРС «TELEGRAM BOT API: БОТ-БОЦМАН»

> **Версия:** 1.0
>
> **Возраст:** 13–16 лет
>
> **Длительность:** 8 занятий по 75–90 минут
>
> **Проводник:** Termix — кибер-пиратский кот, Хранитель Ядра
>
> **Принцип:** Не учить API, а создавать живых ботов. Не зубрить методы, а оживлять Termix'а в Telegram.

---

## 🧠 ФИЛОСОФИЯ КУРСА

Обычный подход: Telegram API → токены → методы → скучно → «зачем это нужно?».

Подход Termix Academy: Telegram API → Бот-Боцман → Termix отвечает → команда /meme присылает кота → «я сделал своего бота!».

Telegram Bot API — это интерфейс для создания ботов в Telegram. Миллионы ботов уже работают: от погоды до онлайн-магазинов. Termix учит детей создавать своего бота-помощника: с командами, реакциями на сообщения, клавиатурами, мемами и базой данных. К концу курса у каждого будет работающий бот Termix Academy.

---

## 🎯 ЧЕМУ НАУЧИТСЯ РЕБЁНОК

- Регистрировать бота через BotFather.
- Понимать структуру Telegram Bot API.
- Использовать библиотеку python-telegram-bot.
- Создавать обработчики команд (/start, /help).
- Обрабатывать текстовые сообщения.
- Создавать кнопки и клавиатуры.
- Отправлять изображения, стикеры и файлы.
- Работать с состояниями пользователя.
- Хранить данные в JSON или SQLite.
- Деплоить бота на сервер.

---

## 🗺️ КАРТА КУРСА

- **Занятие 1 — «Первый контакт».** Регистрация бота. Токен. Первый ответ на /start.
- **Занятие 2 — «Команды: Штурвал».** CommandHandler. /help, /meme, /status.
- **Занятие 3 — «Сообщения: Радар».** MessageHandler. Реакция на ключевые слова.
- **Занятие 4 — «Кнопки: Панель».** ReplyKeyboardMarkup, InlineKeyboardMarkup.
- **Занятие 5 — «Медиа: Попугай».** Отправка фото, стикеров, файлов.
- **Занятие 6 — «Состояния: Память».** ConversationHandler. Диалог с ботом.
- **Занятие 7 — «Данные: Трюм».** JSON, SQLite. Сохранение данных.
- **Занятие 8 — «Деплой: Выход в море».** Запуск бота на сервере. Парад проектов.

---

## 📖 ЗАНЯТИЕ 1: ПЕРВЫЙ КОНТАКТ

### 🎯 Цель

Зарегистрировать бота, получить токен, написать первого бота.

### ⏱️ Тайминг (75–90 минут)

- 0–5 мин: Termix: «Бип! Сегодня я оживу в Telegram! Ты создашь моего цифрового двойника. Погнали!»
- 5–15 мин: Что такое Telegram Bot API. Как боты общаются с сервером.
- 15–25 мин: BotFather. Регистрация бота. Получение токена.
- 25–45 мин: Установка библиотеки: `pip install python-telegram-bot`.
- 45–70 мин: Первый бот. Команда /start.
- 70–80 мин: Запуск. Тестирование в Telegram.
- 80–90 мин: Итоги. Бадж «Первый Контакт».

### 🛠️ Практика

Ребёнок открывает BotFather (@BotFather). Пишет `/newbot`. Даёт имя: `Termix Academy Bot`. Получает токен.

Устанавливает библиотеку:
```bash
pip install python-telegram-bot
```

Создаёт файл bot.py:

```python
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = "ТВОЙ_ТОКЕН_ОТ_BOTFATHER"

async def start(update: Update, context):
    await update.message.reply_text("Бип! Привет, юнга! Я — Termix! Готов к приключениям!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Бип! Termix запущен!")
app.run_polling()
```

Запускает. Открывает бота в Telegram. Пишет /start. Видит ответ.

🎮 Игровая механика

Соревнование «Кто первый?». Наставник: «Зарегистрируй бота, напиши /start, покажи мне ответ». Кто первый — жетон.

🏠 Миссия

· 🥉 Юнга: Зарегистрировать бота и сделать команду /start.
· 🥈 Боцман: Добавить приветственное сообщение с именем пользователя.
· 🥇 Штурман: Добавить команду /ping, которая отвечает "Pong!".

---

📖 ЗАНЯТИЕ 2: КОМАНДЫ — ШТУРВАЛ

🎯 Цель

Освоить обработку команд бота.

⏱️ Тайминг (75–90 минут)

· 0–5 мин: Termix: «Команды — это штурвал! /help — справка. /meme — смех. /status — как там Ядро?»
· 5–15 мин: CommandHandler. Разные команды.
· 15–30 мин: Создание /help и /about.
· 30–50 мин: /meme — отправка случайного мема из списка.
· 50–70 мин: /status — бот показывает статус Termix'а (хвост зелёный/жёлтый/красный).
· 70–80 мин: Команда с аргументом: /say Привет → бот повторяет.
· 80–90 мин: Итоги. Бадж «Штурвальный».

🛠️ Практика

```python
import random

async def help_command(update: Update, context):
    text = """
🦾 Доступные команды:
/start — начать
/help — справка
/meme — получить мем
/status — проверить хвост
/about — о боте
    """
    await update.message.reply_text(text)

async def meme(update: Update, context):
    memes = [
        "🐱 Кот на клавиатуре: 'Я не сплю, я компилируюсь!'",
        "🐱 Termix: 'Код либо работает, либо идёшь кормить кракена!'",
        "🐱 'Бип! Обнаружен баг. Это фича, а не баг.'",
        "🐱 Кот с крюком: 'Enter — моё оружие. Синтаксис — моя броня.'"
    ]
    await update.message.reply_text(random.choice(memes))

async def status(update: Update, context):
    colors = ["🟢 Хвост зелёный. Система в порядке!", 
              "🟡 Хвост жёлтый. Есть ошибки.", 
              "🔴 Хвост красный. СРОЧНО ЗОВИ АДМИНА!"]
    await update.message.reply_text(random.choice(colors))

async def about(update: Update, context):
    await update.message.reply_text("Я — Termix, кибер-пиратский кот. Хранитель Ядра. Версия 1.0.")

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("meme", meme))
app.add_handler(CommandHandler("status", status))
app.add_handler(CommandHandler("about", about))
```

🎮 Игровая механика

Конкурс «Самая смешная команда». Дети добавляют команду /joke. У кого смешнее — жетон.

🏠 Миссия

· 🥉 Юнга: Добавить /help и /about.
· 🥈 Боцман: Добавить /meme со случайными мемами.
· 🥇 Штурман: Добавить /dice — бот кидает кубик (random 1-6).

---

📖 ЗАНЯТИЕ 3: СООБЩЕНИЯ — РАДАР

🎯 Цель

Освоить обработку обычных сообщений.

⏱️ Тайминг (75–90 минут)

· 0–5 мин: Termix: «Радар включён! Бот слушает всё, что ты пишешь. Скажешь 'рыба' — я отвечу!»
· 5–15 мин: MessageHandler. filters.TEXT.
· 15–30 мин: Реакция на ключевые слова.
· 30–50 мин: Игровой бот. Угадай число.
· 50–70 мин: Эхо-бот. Повторяет за пользователем.
· 70–80 мин: Фильтрация команд (~filters.COMMAND).
· 80–90 мин: Итоги. Бадж «Радист».

🛠️ Практика

```python
from telegram.ext import MessageHandler, filters

async def echo(update: Update, context):
    text = update.message.text.lower()
    
    if "привет" in text or "здравствуй" in text:
        await update.message.reply_text("Бип! Привет, юнга!")
    elif "рыба" in text:
        await update.message.reply_text("Рыба? Где? Давай сюда! 🐟")
    elif "бип" in text:
        await update.message.reply_text("Бип-бип! На связи!")
    elif "спасибо" in text:
        await update.message.reply_text("Мур-мур! Всегда пожалуйста!")
    else:
        await update.message.reply_text(f"Ты сказал: {text}. Но я просто кот. Пиши /help!")

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
```

🎮 Игровая механика

Игра «Разговори бота». Дети придумывают ключевые слова и реакции. Чей бот отвечает на большее число слов — жетон.

🏠 Миссия

· 🥉 Юнга: Реакция на слово «привет».
· 🥈 Боцман: Реакция на 5 ключевых слов.
· 🥇 Штурман: Бот отвечает на вопросы (используя if/elif).

---

📖 ЗАНЯТИЕ 4: КНОПКИ — ПАНЕЛЬ

🎯 Цель

Освоить создание клавиатур.

⏱️ Тайминг (75–90 минут)

· 0–5 мин: Termix: «Кнопки! Не надо печатать команды — просто нажимай! Reply-кнопки и Inline-кнопки!»
· 5–15 мин: ReplyKeyboardMarkup. Кнопки под сообщением.
· 15–30 мин: InlineKeyboardMarkup. Кнопки внутри сообщения.
· 30–50 мин: Главное меню бота.
· 50–70 мин: CallbackQuery. Обработка нажатий на inline-кнопки.
· 70–80 мин: Практика. Меню с кнопками.
· 80–90 мин: Итоги. Бадж «Инженер Панели».

🛠️ Практика

Reply Keyboard:

```python
from telegram import ReplyKeyboardMarkup

async def start(update: Update, context):
    keyboard = [
        ["/meme", "/status"],
        ["/help", "/about"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Выбери команду:", reply_markup=reply_markup)
```

Inline Keyboard:

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def menu(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Мем", callback_data="meme"),
         InlineKeyboardButton("Статус", callback_data="status")],
        [InlineKeyboardButton("Помощь", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Что хочешь?", reply_markup=reply_markup)

async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data == "meme":
        await query.edit_message_text("🐱 Кот на клавиатуре: 'Я не сплю, я компилируюсь!'")
    elif query.data == "status":
        await query.edit_message_text("🟢 Хвост зелёный!")
    elif query.data == "help":
        await query.edit_message_text("Используй /help для списка команд!")
```

🎮 Игровая механика

Конкурс «Лучшее меню». Дети создают inline-меню для своего бота. Голосование стикерами.

🏠 Миссия

· 🥉 Юнга: Добавить ReplyKeyboard с 3 кнопками.
· 🥈 Боцман: Добавить InlineKeyboard с обработкой.
· 🥇 Штурман: Сделать меню с вложенными кнопками (категории).

---

📖 ЗАНЯТИЕ 5: МЕДИА — ПОПУГАЙ

🎯 Цель

Освоить отправку изображений, стикеров и файлов.

⏱️ Тайминг (75–90 минут)

· 0–5 мин: Termix: «Попугай доставляет картинки! Бот умеет отправлять не только текст!»
· 5–15 мин: send_photo, send_sticker, send_document.
· 15–30 мин: Отправка картинки Termix'а по команде.
· 30–50 мин: Отправка случайного стикера.
· 50–70 мин: Отправка файла (шпаргалка PDF).
· 70–80 мин: Получение фото от пользователя и сохранение.
· 80–90 мин: Итоги. Бадж «Попугай».

🛠️ Практика

```python
async def photo(update: Update, context):
    await update.message.reply_photo(
        photo=open("termix.png", "rb"),
        caption="Это я! Termix! 🐱"
    )

async def sticker(update: Update, context):
    stickers = [
        "CAACAgIAAxkBAA...",  # ID стикеров
    ]
    await update.message.reply_sticker(sticker=random.choice(stickers))

async def document(update: Update, context):
    await update.message.reply_document(
        document=open("cheatsheet.pdf", "rb"),
        filename="git-cheatsheet.pdf",
        caption="Шпаргалка по Git 📚"
    )
```

🎮 Игровая механика

Конкурс «Самый смешной стикер». Дети добавляют команду /sticker. Чей стикер смешнее — жетон.

🏠 Миссия

· 🥉 Юнга: Отправить картинку по команде /photo.
· 🥈 Боцман: Отправить случайный стикер из списка.
· 🥇 Штурман: Бот принимает фото и отвечает на него.

---

📖 ЗАНЯТИЕ 6: СОСТОЯНИЯ — ПАМЯТЬ

🎯 Цель

Освоить ConversationHandler для диалогов.

⏱️ Тайминг (75–90 минут)

· 0–5 мин: Termix: «Память! Бот запоминает, что ты сказал. Диалог — это цепочка вопросов и ответов!»
· 5–15 мин: Что такое состояния. ConversationHandler.
· 15–30 мин: Диалог: «Как тебя зовут?» → «Сколько тебе лет?» → «Приятно познакомиться!».
· 30–50 мин: Регистрация пирата через диалог.
· 50–70 мин: Отмена диалога (/cancel).
· 70–80 мин: Сохранение данных из диалога.
· 80–90 мин: Итоги. Бадж «Память».

🛠️ Практика

```python
from telegram.ext import ConversationHandler

NAME, AGE, RANK = range(3)

async def start_register(update: Update, context):
    await update.message.reply_text("Давай зарегистрируем тебя в экипаже! Как тебя зовут?")
    return NAME

async def get_name(update: Update, context):
    context.user_data["name"] = update.message.text
    await update.message.reply_text("Сколько тебе лет?")
    return AGE

async def get_age(update: Update, context):
    context.user_data["age"] = int(update.message.text)
    await update.message.reply_text("Какое твоё звание? (Юнга/Боцман/Штурман)")
    return RANK

async def get_rank(update: Update, context):
    context.user_data["rank"] = update.message.text
    name = context.user_data["name"]
    age = context.user_data["age"]
    rank = context.user_data["rank"]
    await update.message.reply_text(f"Бип! {rank} {name}, {age} лет, добро пожаловать в экипаж!")
    return ConversationHandler.END

async def cancel(update: Update, context):
    await update.message.reply_text("Регистрация отменена.")
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("register", start_register)],
    states={
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
        AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_age)],
        RANK: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_rank)],
    },
    fallbacks=[CommandHandler("cancel", cancel)]
)
app.add_handler(conv_handler)
```

🎮 Игровая механика

Игра «Квест». Наставник: «Сделай диалог, где бот загадывает загадку и ждёт ответ». Кто первый — жетон.

🏠 Миссия

· 🥉 Юнга: Диалог из 2 вопросов.
· 🥈 Боцман: Диалог из 3 вопросов с сохранением данных.
· 🥇 Штурман: Квест с 5 шагами и ветвлением (if в диалоге).

---

📖 ЗАНЯТИЕ 7: ДАННЫЕ — ТРЮМ

🎯 Цель

Освоить сохранение данных в JSON и SQLite.

⏱️ Тайминг (75–90 минут)

· 0–5 мин: Termix: «Трюм! Данные должны храниться вечно. Контейнер умер — данные остались!»
· 5–15 мин: JSON. Запись и чтение файла.
· 15–30 мин: Сохранение данных пользователей в JSON.
· 30–50 мин: SQLite. База данных в файле.
· 50–70 мин: Таблица пользователей. Запись и чтение.
· 70–80 мин: Счётчик сообщений для каждого пользователя.
· 80–90 мин: Итоги. Бадж «Хранитель Трюма».

🛠️ Практика

JSON:

```python
import json

def save_user(user_id, data):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except:
        users = {}
    
    users[str(user_id)] = data
    
    with open("users.json", "w") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)

def load_user(user_id):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
        return users.get(str(user_id))
    except:
        return None
```

SQLite:

```python
import sqlite3

conn = sqlite3.connect("termix.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    rank TEXT,
    gold INTEGER DEFAULT 0,
    messages INTEGER DEFAULT 0
)
""")
conn.commit()

def update_messages(user_id):
    cursor.execute("UPDATE users SET messages = messages + 1 WHERE user_id = ?", (user_id,))
    conn.commit()
```

🎮 Игровая механика

Соревнование «Кто активнее?». Бот считает сообщения каждого пользователя. Вывод команды /top.

🏠 Миссия

· 🥉 Юнга: Сохранять имена пользователей в JSON.
· 🥈 Боцман: Перенести хранение в SQLite.
· 🥇 Штурман: Сделать рейтинг пользователей по сообщениям.

---

📖 ЗАНЯТИЕ 8: ДЕПЛОЙ — ВЫХОД В МОРЕ

🎯 Цель

Запустить бота на сервере и показать проекты.

⏱️ Тайминг (75–90 минут)

· 0–5 мин: Termix: «Выход в море! Бот больше не на твоём компьютере. Он живёт на сервере. 24/7!»
· 5–15 мин: Варианты хостинга: PythonAnywhere, Railway, VPS.
· 15–40 мин: Деплой на PythonAnywhere.
· 40–60 мин: Презентации ботов.
· 60–75 мин: Награждение.

🚀 Деплой на PythonAnywhere

· Зарегистрироваться на pythonanywhere.com.
· Upload файлы бота.
· Установить библиотеки: pip install python-telegram-bot.
· Запустить: python bot.py.
· Бот работает 24/7.

🏆 Итоговые баджи курса

· 🥉 Bot-Юнга — все миссии «Юнга».
· 🥈 Bot-Боцман — 4 миссии «Боцман».
· 🥇 Bot-Штурман — 3 миссии «Штурман».
· ⌨️ Штурвальный — освоил команды.
· 🎛️ Инженер Панели — освоил клавиатуры.
· 🗄️ Хранитель Трюма — освоил базы данных.
· 🚀 Мореход — задеплоил бота.
· 💎 Bot-Кэп — прошёл весь курс.

---

🐱 ФРАЗЫ TERMIX'А

Приветствия:

· «Бип! Telegram Bot API — это способ оживить меня в чате! Погнали!»
· «Готов создать бота? Хвост зелёный — токен получен!»

Похвала:

· «Бип-бип-БОТ! Твой Termix отвечает! Он живой!»
· «Мур-мур-деплой! Бот в море, работает 24/7!»

Поддержка:

· «Бот не отвечает? Проверь токен. И не закоммить его в GitHub!»
· «Ошибка 409? Два экземпляра бота запущены. Останови лишний.»