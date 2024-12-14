import smtplib

import os
from dotenv import load_dotenv
load_dotenv()

referal_link = 'https://dvmn.org/profession-ref-program/lesha37lim/Alexey/'
inviter_name = 'Alexey'
inviter_email = os.getenv('MY_LOGIN')
friend_name = 'Andrey'
friend_email = os.getenv('FRIEND_MAIL')

letter = """From: {email_from}
To: {email_to}
Subject: Приглашение
Content-Type: text/plain; charset="UTF-8";

Привет, {friend}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(friend=friend_name, my_name=inviter_name , website=referal_link, email_from=inviter_email, email_to=friend_email)
letter = letter.encode ("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(inviter_email, os.getenv('PASSWORD'))
server.sendmail(inviter_email, friend_email, letter)
server.quit()
