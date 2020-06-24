import random
import telebot
import telegram

bot = telebot.TeleBot('1093985418:AAGalemUk_ayyGBXkH9-ihoWGX3dLtAWgzQ')


class Person:

    def __str__(self):
        return "1. Ваша профессия - {};\n" \
               "2. Ваш пол и возраст - {}, {};\n" \
               "3. Ваше хобби - {};\n" \
               "4. Ваше состояние здоровья - {};\n" \
               "5. Ваша фобия - {};\n" \
               "6. Ваш багаж - {};\n" \
               "7. Ваша дополнительная информация - {};\n" \
               "8. Карта действия - {};\n".format(self.job, self.sex, self.age,
                                                  self.hobbi, self.healthStatus,
                                                  self.phobia, self.baggage,
                                                  self.extraInfo, self.card)

    def set_job(self, job):
        self.job = job

    def set_sex(self, sex):
        self.sex = sex

    def set_age(self, age):
        self.age = age

    def set_hobbi(self, hobbi):
        self.hobbi = hobbi

    def set_status(self, healthStatus):
        self.healthStatus = healthStatus

    def set_phobia(self, phobia):
        self.phobia = phobia

    def set_baggage(self, baggage):
        self.baggage = baggage

    def set_extra(self, extra):
        self.extraInfo = extra

    def set_card(self, card):
        self.card = card

    def get_job(self):
        return self.job


person = Person()

job = ["Резчик по камню", "Режиссер", "Космонавт", "Врач-кибернетик", "Кондитер", "Хирург",
       "Web-дизайнер", "Архитектор-проектировщик", "Реаниматолог", "Графический дизайнер", "Ландшафтный архитектор",
       "Дизайнер", "Пожарный", "Медицинский лабораторный техник", "Астроном", "Бионик", "Кинолог", "Биотехнолог",
       "Судья", "Инженер-проектировщик", "Адвокат", "Врач", "Инженер", "Программист-разработчик",
       "Молекулярный биолог", "Лаборант химического анализа", "Патологоанатом", "Астрофизик",
       "Инженер-испытатель",
       "Корреспондент", "Лаборант", "Ветеринар", "Журналист-международник", "Химик", "Психотерапевт",
       "Частный детектив", "Композитор", "Шоколатье", "Звукорежиссер", "Сценарист",
       "Авиаконструктор", "IT-специалист", "Вирусолог", "Художник", "Метеоролог",
       "Пластический хирург", "Психолог", "Модельер", "Следователь", "Онколог",
       "Переводчик", "Дипломат", "Технолог по нефтепереработке", "Музыкант", "Бармен",
       "Ювелир", "Повар", "Военный лётчик", "Экспедитор", "Скульптор", "Каскадер",
       "Учитель", "Менеджер по развитию территории", "Стилист", "Гинеколог", "Бариста",
       "Физик", "Хед-хантер", "Водолаз", "Президент"]

sex = ['Мужской', 'Женский']
hobbi = ['рисование', 'плавание', 'преподаватель вокала', 'собирание грибов', 'агроном',
         'умеет делать алко коктейли', 'игра на гитаре', 'выращивание растений', 'кулинария',
         'стрельба из лука', 'стрельба из пневмата', 'астрономия', 'любит смотреть фильмы про выживание',
         'любит смотреть фильмы про зомби апокалипсисы', 'смешанные единоборства', 'бодибилдер',
         'занимается программированием', 'изучает иностранные языки', 'акробатика', 'занимается фотографированием',
         'снимает видеоблоги']

healthStatus = ['Идеально здоров', 'Алкоголизм', 'Болезнь Альцгеймера', 'Болезни сердца и сосудов',
                'Бронхиальная астма', 'ВИЧ/СПИД', 'Геморрой', 'Гепатит', 'Головная боль',
                'Слабоумие', 'Наркомания', 'Ожирение', 'ОРВИ', 'Панкреатит', 'Плоскостопие', 'Сколиоз', 'Идеально здоров',
                'Сахарный диабет', 'Туберкулёз','Идеально здоров', 'Шизофрения', 'Депрессия', 'Синдром хронической усталости',
                'Выдуманные болезни', 'Аллергия на пыль','Идеально здоров', 'Аллергия на животных', 'Родинки', 'Одышка','Идеально здоров',
                'Шепелявость']
phobia = ['Аблютофобия', 'Агирофобия', 'Аграфобия', 'Арахнофобия', 'Верминофобия','Нет фобий',
          'Гелотофобия', 'Гемофобия', 'Генофобия','Нет фобий', 'Гетерофобия', 'Гомофобия', 'Зоофобии','Нет фобий', 'Клаустрофобия',
          'Клептофобия', 'Нет фобий']
baggage = ['3 ящика алкоголя', 'собака', 'кот', 'террариум с пауками',
           'набор респираторных масок', 'костюмы химической защиты',
           'набор столярных инструментов', 'сборник стихов пушкина',
           'набор для шитья', 'инкубатор с яйцами', 'семена пшеницы',
           'мешок картошки', 'слесарный набор инструментов', 'ноутбук',
           'переносная зарядная станция', 'годовалый ребенок',
           'набор детского питания', 'гитара', 'набор комиксов',
           'переносной кондиционер', '5 павербанков', 'музыкальня колонка']
extraInformation = ['работал барменом', 'работал психологом', 'копрофил',
                    'по первому образованию социолог', 'по первому образованию биолог',
                    'образование философа', 'тренер айкидо', 'знает все стихи шевченко наизусть',
                    'коллекционирует монеты', 'знает 10 языков', 'лечил больных от коронавируса',
                    'умеет шить одежду', 'по первому образованию архитектор',
                    'выступал со стендап программой по стране', 'солист музыкальной группы',
                    'воевал в АТО', 'умеет варить мыло', 'чемпион мира по покеру', 'ограбил банк',
                    'посетил все страны мира', 'коллекционирует ножи', 'умеет чинить сантехнику',
                    'работал плотником', 'работал няней', 'другая ориентация']

cards = ['Воскресить игрока', 'Восстановить свое или чьё-то здоровье до идеального',
         'Поменяться багажом с любым игроком', 'Поменяться со следующим игроком багажом',
         'Поменяться с любым игроком состоянием здоровья', 'Поменяться со следующим игроком состоянием здоровья',
         'Поменять всем игрокам профессии', 'Поменять половине игроков профессии',
         'Поменяться с любым игроком профессиями',
         'Поменяться со следующим игроком профессиями', 'Поменять себе или другому игроку профессию',
         'Поменяться хобби с любым игроком', 'Поменяться хобби со следующим игроком',
         'Поменяться доп инфой с любым игроком',
         'Поменяться доп инфой со следующим игроком',
         'Карточка друга с предыдущим игроком', 'Карточка друга со следующим игроком',
         'Карточка врага с предыдущим игроком',
         'Карточка врага со следующим игроком', 'Вскрыть соседний бункер с 2-умя 40 летними мужчинами химиками',
         'Вскрыть соседний бункер с 2-умя 40 летними женщинами химиками', 'Вскрыть склад с оружием находящийся рядом',
         'Исключить любого игрока из бункера']

isJob = []
isHobbi = []
isHealth = []
isPhobia = []
isBaggage = []
isExtra = []
isCard = []


def give_person():
    if len(job) > 0:
        j = job[random.randint(0, len(job) - 1)]  #
        isJob.append(j)
        job.remove(j)
        person.set_job(j)
    else:
        for i in range(len(isJob) - 1):
            job.append(isJob[i])
        j = job[random.randint(0, len(job) - 1)]  #
        isJob.append(j)
        job.remove(j)
        person.set_job(j)

    person.set_sex(sex[random.randint(0, len(sex) - 1)])  #
    person.set_age(random.randint(15, 80))  #

    if len(hobbi) > 0:
        j = hobbi[random.randint(0, len(hobbi) - 1)]  #
        isHobbi.append(j)
        hobbi.remove(j)
        person.set_hobbi(j)
    else:
        for i in range(len(isHobbi) - 1):
            hobbi.append(isHobbi[i])
        j = hobbi[random.randint(0, len(hobbi) - 1)]  #
        isHobbi.append(j)
        hobbi.remove(j)
        person.set_hobbi(j)

    if len(healthStatus) > 0:
        j = healthStatus[random.randint(0, len(healthStatus) - 1)]  #
        isHealth.append(j)
        healthStatus.remove(j)
        person.set_status(j)
    else:
        for i in range(len(isHealth) - 1):
            healthStatus.append(isHealth[i])
        j = healthStatus[random.randint(0, len(healthStatus) - 1)]  #
        isHealth.append(j)
        healthStatus.remove(j)
        person.set_status(j)

    if len(phobia) > 0:
        j = phobia[random.randint(0, len(phobia) - 1)]  #
        isPhobia.append(j)
        phobia.remove(j)
        person.set_phobia(j)
    else:
        for i in range(len(isPhobia) - 1):
            phobia.append(isPhobia[i])
        j = phobia[random.randint(0, len(phobia) - 1)]  #
        isPhobia.append(j)
        phobia.remove(j)
        person.set_phobia(j)

    if len(baggage) > 0:
        j = baggage[random.randint(0, len(baggage) - 1)]  #
        isBaggage.append(j)
        baggage.remove(j)
        person.set_baggage(j)
    else:
        for i in range(len(isBaggage) - 1):
            baggage.append(isBaggage[i])
        j = baggage[random.randint(0, len(baggage) - 1)]  #
        isBaggage.append(j)
        baggage.remove(j)
        person.set_baggage(j)

    if len(extraInformation) > 0:
        j = extraInformation[random.randint(0, len(extraInformation) - 1)]  #
        isExtra.append(j)
        extraInformation.remove(j)
        person.set_extra(j)
    else:
        for i in range(len(isExtra) - 1):
            extraInformation.append(isExtra[i])
        j = extraInformation[random.randint(0, len(extraInformation) - 1)]  #
        isExtra.append(j)
        extraInformation.remove(j)
        person.set_extra(j)

    if len(cards) > 0:
        j = cards[random.randint(0, len(cards) - 1)]  #
        isCard.append(j)
        cards.remove(j)
        person.set_card(j)
    else:
        for i in range(len(isCard) - 1):
            cards.append(isCard[i])
        j = cards[random.randint(0, len(cards) - 1)]  #
        isCard.append(j)
        cards.remove(j)
        person.set_card(j)

    return person


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/Giverole":
        bot.send_message(message.from_user.id, give_person())
        #print(message.from_user.first_name)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /Giverole")

    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Напиши /Giverole")

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
