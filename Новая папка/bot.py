
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from options import TOKEN

qa_dict = {
    "Лучшие настройки для новичка?": "Средний мир, сложность Эксперт, биом Багрянец",
    "Какой класс выбрать новичку?": "Стрелок - самый удобный класс для первого прохождения",
    "Порядок битв с боссами?": "Король слизней → Глаз → Мозг/Пожиратель → Скелетрон → Стена плоти → Механики → Плантера → Голем → Культист → Лунный лорд",
    "Как победить Короля слизней?": "100 веревок для арены и гранаты",
    "Как найти Мозг Ктулху?": "В багряных землях найдите и разбейте 3 сердца",
    "Где найти Скелетрона?": "Ночью у входа в данж, поговорите со стариком",
    "Что такое хардмод?": "Режим после победы над Стеной плоти. Появляются новые руды и враги",
    "Как получить крылья?": "В хардмоде можно купить у Ведьмы или добыть с гарпий в небе",
    "Лучшая броня до хардмода?": "Метеоритная для мага, Теневая/Багряная для остальных",
    "Как увеличить здоровье?": "Собирайте кристаллы жизни под землей, в хардмоде - фрукты жизни в джунглях",
    "Что делать после Культиста?": "Уничтожьте 4 колонны, затем сразитесь с Лунным лордом",
    "Как призвать Стену плоти?": "Бросьте Гайда в лаву в аду",
    "Где найти редкие руды?": "Глубоко под землей. В хардмоде появляются после уничтожения алтарей",
    "Как защитить базу от монстров?": "Постройте стены и расставьте факелы. НПС помогут в защите",
    "Что делать в кровавую луне?": "Событие ночью с усиленными монстрами. Фармите редкие предметы",
    "Как получить питомца?": "Найдите зелья призыва питомцев в сундуках или создайте их из особых материалов",
    "Как создать верстак?": "Соберите дерево и создайте из него. Это базовый предмет для крафта",
    "Где найти алтари крафта?": "Алтари находятся в данже, джунглях и адском мире",
    "Как получить крюк?": "Убивайте пираний или создайте из драгоценных камней и цепей",
    "Как быстро копать?": "Используйте кирки лучше железной, зелья копания и шахтерскую броню",
    "Где найти НПС?": "Стройте подходящие комнаты и выполняйте условия появления каждого НПС",
    "Как получить молот души?": "Выпадает с механических боссов в хардмоде с шансом 25%",
    "Где найти жизненные фрукты?": "В джунглях в хардмоде, светятся розовым в пещерах",
    "Как сделать зелья?": "Нужна бутылка, вода и ингредиенты. Варить на алхимическом столе",
    "Как призвать Плантеру?": "Разбейте розовый бутон в джунглях после всех механиков",
    "Что такое эклипс?": "Опасное дневное событие в хардмоде с сильными монстрами",
    "Как получить клетки хлорофита?": "Добывайте хлорофитовую руду в джунглях в хардмоде",
    "Где найти летающий ковер?": "В пирамидах в пустыне, редкий предмет из сундуков",
    "Как получить посох воды?": "Создается из жемчужин, кристаллов и звездной пыли",
    "Что делать с геммами?": "Используются для создания крюков и магических посохов",
    "Как получить черепаший панцирь?": "Выпадает с гигантских черепах в джунглях"
}

bosses_info = {
    "Король слизней": {
        "info": "Первый босс игры. Для победы нужны веревки и гранаты.",
        "image": "https://static.wikia.nocookie.net/character-power/images/0/04/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BB%D0%B8%D0%B7%D0%B5%D0%BD%D1%8C1.png/revision/latest?cb=20190330192521&path-prefix=ru"
    },
    "Глаз ктулху": {
        "info": "Второй босс. Нужна золотая/платиновая броня и оружие средней дистанции.",
        "image": "https://static.wikia.nocookie.net/character-power/images/6/6f/%D0%93%D0%BB%D0%B0%D0%B7_%D0%9A%D1%82%D1%83%D0%BB%D1%85%D1%831.jpg/revision/latest?cb=20190328202012&path-prefix=ru"
    },
    "Мозг ктулху": {
        "info": "Третий босс. Находится в багряных землях, нужна мини акула и 400 HP.",
        "image": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_67905fa78e9b1b4ee314d2dd_67905fae8e9b1b4ee314d4a3/scale_1200"
    },
    "Скелетрон": {
        "info": "Четвертый босс. Появляется ночью у входа в данж.",
        "image": "https://static.wikia.nocookie.net/terraria_gamepedia/images/a/a3/Skeletron_Head.png/revision/latest?cb=20191003231538"
    },
    "Стена Плоти": {
        "info": "Пятый босс. Появляеться если бросить куклу вуду в лаву",
        "image": "https://avatars.dzeninfra.ru/get-zen_doc/3614639/pub_63dfed989537fa377df9b898_63dfeefae174fb1647fc19c9/scale_1200"
    },
    "Механики": {
        "info": "Шестые боссы. Появляються ночью если призвать",
        "image": "https://static.wikia.nocookie.net/terraria/images/4/4d/Mechdusa.png/revision/latest?cb=20221121123252&path-prefix=ru"
    },
    "Плантера": {
        "info": "Седьмой босс. Появиться если сломать розовый бутон в джунглях",
        "image": "https://pm1.aminoapps.com/8384/3abbaf011dde1feacca7c7fe9c1678a7c9ee3ad6r1-466-516v2_hq.jpg"
    },
    "Голем": {
        "info": "Восьмой босс. Появиться в данже ящеров",
        "image": "https://terraria.wiki.gg/images/c/ce/Golem.png"
    },
    "Культист Лунатик": {
        "info": "Девятый босс. Появиться в данже после убийства обычных культистов",
        "image": "https://static.wikia.nocookie.net/terraria/images/c/c6/NPC_439.png/revision/latest?cb=20150701110204&path-prefix=ru"
    },
    "Мунлорд": {
        "info": "Финальный босс. Появиться после убийства башен",
        "image": "https://static.wikia.nocookie.net/terraria_gamepedia/images/7/7f/Moon_Lord.png/revision/latest/scale-to-width-down/250?cb=20200805023430"
    }
    
}

bot = telebot.TeleBot(token=TOKEN)



def create_main_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("Показать все вопросы", callback_data="show_questions"),
        InlineKeyboardButton("Информация о боссах", callback_data="show_bosses")
    )
    return keyboard

# Создаем словарь с короткими идентификаторами для вопросов
question_ids = {f"q{i}": q for i, q in enumerate(qa_dict.keys())}
question_ids_reverse = {v: k for k, v in question_ids.items()}

def create_questions_keyboard():
    keyboard = InlineKeyboardMarkup()
    for q_id, question in question_ids.items():
        keyboard.add(InlineKeyboardButton(question, callback_data=q_id))
    return keyboard

def create_bosses_keyboard():
    keyboard = InlineKeyboardMarkup()
    for boss in bosses_info.keys():
        keyboard.add(InlineKeyboardButton(boss, callback_data=f"b_{boss}"))
    return keyboard

@bot.message_handler(commands=['start', 'help'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}!\nЯ бот гид по игре Террария.",
        reply_markup=create_main_keyboard()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "show_questions":
        bot.edit_message_text(
            "Выберите интересующий вас вопрос:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=create_questions_keyboard()
        )
    elif call.data == "show_bosses":
        bot.edit_message_text(
            "Выберите босса, чтобы узнать о нём подробнее:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=create_bosses_keyboard()
        )
    elif call.data.startswith("q"):
        question = question_ids[call.data]
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            f"Вопрос: {question}\nОтвет: {qa_dict[question]}",
            reply_markup=create_main_keyboard()
        )
    elif call.data.startswith("b_"):
        boss_name = call.data[2:]
        boss_data = bosses_info[boss_name]
        bot.answer_callback_query(call.id)
        bot.send_photo(
            call.message.chat.id,
            boss_data["image"],
            caption=f"Босс: {boss_name}\n\nИнформация: {boss_data['info']}",
            reply_markup=create_main_keyboard()
        )

bot.polling(none_stop=True)