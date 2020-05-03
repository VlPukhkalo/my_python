from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time
import datetime

token="8ec04fd67f724010314ae7be4b84c8379556346e86dbf7139f69708f71a693c0feb6a31386dcd13966369"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

with open('dr.txt','r',encoding='utf-8') as filee:
    data2=filee.readlines()

with open ('films.txt','r',encoding='utf-8') as films:
    filmlist=films.readlines()

with open('olimp.txt','r',encoding='utf-8') as olimp:
    olimplist=olimp.readlines()

def week():
    l=[]
    for b in range(1,8):
        a = datetime.date.today()
        bb = datetime.timedelta(days=b)
        cc = a+bb
        l.append(str(cc))
    l1=[i[5:7] for i in l]
    l2=[i[-2:] for i in l]
    dr=[i for i in data2 if i[-3:-1] in l1 and i[-6:-4] in l1]
    if dr==[]:
        return 'На этой неделе пока никто не родился, но есть шанс это исправить)\nСвободен сегодня вечером?'
    else:
        return ''.join(dr)

def send_films():
    return 'Другие Primats рекомендуют:\n\n'+''.join(random.sample(filmlist,3))

def send_task():
    return 'Развлекайся\n\n'+random.choice(olimplist)

def dr(m):
    mon={"январь":'01','февраль':'02','март':"03",'апрель':'04','май':'05','июнь':'06','июль':'07','август':'08','сентябрь':'09',"октябрь":'10','ноябрь':'11','декабрь':'12'}
    L=[i for i in data2 if i[-3:-1]==mon.get(m)]
    if L==[]:
        return 'В этом месяце пока никто не родился, но есть шанс это исправить)\nСвободен сегодня вечером?'
    else:
        return ''.join(L)


def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'привет' or response=='но не устал от математики' or response=='плейлист дня' or response=='что посмотреть?' or response=='назад' or response=='на неделю' or response=='все' or response=='январь' or response=='февраль' or response=='март' or response=='апрель' or response=='май' or response=='июнь' or response=='июль' or response=='август' or response=='сентябрь' or response=='октябрь' or response=='ноябрь' or response=='декабрь':

        keyboard.add_button('Дни Рождения', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Учебники', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Кнопка на случай, если устал учиться', color=VkKeyboardColor.PRIMARY)

    elif response=='кнопка на случай, если устал учиться':

        keyboard.add_button('но не устал от математики', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Что посмотреть?', color=VkKeyboardColor.POSITIVE)


    elif response=='дни рождения':
        keyboard.add_button('На месяц',color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('На неделю',color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Все',color=VkKeyboardColor.POSITIVE)

    elif response == 'закрыть':
        return keyboard.get_empty_keyboard()

    elif response=='учебники':
        keyboard.add_button('Мат.анализ',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Алгебра',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Дискр.мат',color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Wolfram Math',color=VkKeyboardColor.PRIMARY)
        keyboard.add_openlink_button('Python','https://vk.com/away.php?to=https%3A%2F%2Fvk.cc%2FalOWY8&cc_key=')
        keyboard.add_line()
        keyboard.add_button('Английский',color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Назад',color=VkKeyboardColor.NEGATIVE)

    elif response=='английский':
        keyboard.add_openlink_button('Market Leader','https://vk.com/away.php?to=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1xEkwAyIT2AtAuJ56xVyfFQ5w8czPtJAa%2Fview&cc_key=')
        keyboard.add_line()
        keyboard.add_openlink_button('Facilitator','https://vk.com/away.php?to=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F17P1MYWDJDREdfGQRGD9inyREZAqEXlR6%2Fview&cc_key=')
        keyboard.add_line()
        keyboard.add_openlink_button('Practical Grammar Course','https://vk.com/away.php?to=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1LJLLploS_8epi8yYWsVjm5JsDi7nmHYu%2Fview&cc_key=')
        keyboard.add_line()
        keyboard.add_button('Назад',color=VkKeyboardColor.NEGATIVE)

    elif response=='wolfram math':
        keyboard.add_openlink_button('Фридман,Леора','https://vk.com/away.php?to=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D1xg9g1LAuw-jIH6HwH9e-UE_GU9bq8Kri&cc_key=')
        keyboard.add_line()
        keyboard.add_openlink_button('S.Wolfram "Wolfram Language"','https://vk.com/away.php?to=https%3A%2F%2Fwww.wolfram.com%2Flanguage%2Felementary-introduction%2F2nd-ed%2Findex.html&cc_key=')
        keyboard.add_line()
        keyboard.add_openlink_button('Help','https://reference.wolfram.com/language/')
        keyboard.add_line()
        keyboard.add_button('Назад',color=VkKeyboardColor.NEGATIVE)

    elif response=='мат.анализ':
        keyboard.add_openlink_button('Демидович (задачник)','https://drive.google.com/file/d/1VnHhcsfAlVg48nsYXWdXfNZiVkakamv-/view')
        keyboard.add_line()
        keyboard.add_openlink_button('Виноградов,Громов','https://vk.com/doc108898977_514996947?hash=984e14ef93de90b23e&dl=a91def24fdbf7a14b9')
        keyboard.add_line()
        keyboard.add_button('Назад',color=VkKeyboardColor.NEGATIVE)

    elif response=='алгебра':
        keyboard.add_openlink_button('Икрамов(задачник)','https://vk.com/away.php?to=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D1KxIrUV3yGT_IKzz2X52JW6x1mUmoqP7C&cc_key=')
        keyboard.add_line()
        keyboard.add_openlink_button('Воеводин','https://vk.com/away.php?to=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D1Cd-Q2GMVhLERwJSh1lyriE89DsBRUc6V&cc_key=')
        keyboard.add_line()
        keyboard.add_openlink_button('Курош','https://vk.com/doc61070830_524793039?hash=12ae30e78883526a84&dl=afb96283e5d1fe460f')
        keyboard.add_line()
        keyboard.add_openlink_button('Фадеев','https://vk.com/doc437171420_515200818?hash=336121839fac36e083&dl=dfed8ac668a6205674')
        keyboard.add_line()
        keyboard.add_button('Назад',color=VkKeyboardColor.NEGATIVE)

    elif response=='дискр.мат':
        keyboard.add_openlink_button('Иванов, Фридман','https://vk.com/doc234167654_514661330?hash=9fead45b2c2f3e2ce2&dl=0bef1a3cd3e9273e36')
        keyboard.add_line()
        keyboard.add_openlink_button('Корте "Комбинаторная оптимизация"','https://drive.google.com/file/d/1kOZcitXuRBTKX0pgpXC8FEPenW4rjz6y/view')
        keyboard.add_line()
        keyboard.add_button('Назад',color=VkKeyboardColor.NEGATIVE)

    elif response=='на месяц':
        keyboard.add_button('Январь',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Февраль',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Март',color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Апрель',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Май',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Июнь',color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Июль',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Август',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Сентябрь',color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Октябрь',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Ноябрь',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Декабрь',color=VkKeyboardColor.PRIMARY)

    else:
        keyboard.add_button('Дни Рождения', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Учебники', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Кнопка на случай, если устал учиться', color=VkKeyboardColor.PRIMARY)


    keyboard = keyboard.get_keyboard()
    return keyboard


def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})



for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        response = event.text.lower()
        keyboard = create_keyboard(response)

        if event.from_user and not event.from_me:
            if response == "привет":
                send_message(vk_session, 'user_id', event.user_id, message='Я к твоим услугам, Mr.Primat',keyboard=keyboard)

            elif response == "начать":
                send_message(vk_session, 'user_id', event.user_id, message= 'Тестовые команды',keyboard=keyboard)

            elif response=='закрыть':
                send_message(vk_session, 'user_id', event.user_id, message='Закрыть',keyboard=keyboard)

            elif response=='дни рождения':
                send_message(vk_session,'user_id',event.user_id,message='Выбери нужный вариант',keyboard=keyboard)

            elif response=='на месяц':
                send_message(vk_session,'user_id',event.user_id,message='Выбери нужный месяц',keyboard=keyboard)

            elif response=='на неделю':
                send_message(vk_session,'user_id',event.user_id,message=week(),keyboard=keyboard)

            elif response=='все':
                send_message(vk_session,'user_id',event.user_id,message=''.join(data2),keyboard=keyboard)

            elif response=='январь' or response=='февраль' or response=='март' or response=='апрель' or response=='май' or response=='июнь' or response=='июль' or response=='август' or response=='сентябрь' or response=='октябрь' or response=='ноябрь' or response=='декабрь':
                send_message(vk_session, 'user_id', event.user_id, message=dr(response), keyboard=keyboard)

            elif response=='учебники':
                send_message(vk_session, 'user_id', event.user_id, message= 'Выбери нужный предмет',keyboard=keyboard)

            elif response=='английский' or response=='алгебра' or response=='wolfram math' or response=='мат.анализ' or response=='дискр.мат':
                send_message(vk_session, 'user_id', event.user_id, message= 'Выбери нужный учебник',keyboard=keyboard)

            elif response=='назад':
                send_message(vk_session, 'user_id', event.user_id ,message='Откат',keyboard=keyboard)

            elif response=='кнопка на случай, если устал учиться':
                send_message(vk_session, 'user_id', event.user_id ,message='Как же я тебя понимаю...',keyboard=keyboard)

            elif response=='что посмотреть?':
                send_message(vk_session, 'user_id', event.user_id ,message=send_films(),keyboard=keyboard)

            elif response=='но не устал от математики':
                send_message(vk_session, 'user_id', event.user_id ,message=send_task(),keyboard=keyboard)

            else:
                send_message(vk_session, 'user_id', event.user_id, message= 'Я не понимаю, жмакай кнопочки',keyboard=keyboard)
