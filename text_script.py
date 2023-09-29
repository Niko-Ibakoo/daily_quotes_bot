import smtplib
import random
from email.mime.text import MIMEText
from email.utils import formataddr

import os
from dotenv import load_dotenv



load_dotenv()

#os.get
smtp_server = os.getenv('SMTP_SERVER')
smtpd_port = os.getenv('SMTPD_PORT')
sender_email = os.getenv('SENDER_EMAIL')
sender_pass = os.getenv('SENDER_PASS')

sender_name = "Niko's Happy Bot"
sender = f'{sender_name} <{sender_email}>'
niko = os.getenv('USER1')
gina = os.getenv('USER2')
used_quotes = []

quotes =  [
        "The only way to do great work is to love what you do.",
        "You are never too old to set another goal or to dream a new dream.",
        "The pessimist complains about the wind; the optimist expects it to change; the realist adjusts the sails.",
        "In the middle of every difficulty lies opportunity.",
        "Believe you can and you're halfway there.",
        "Stay positive and happy. Work hard and don't give up hope. Be open to criticism and keep learning. Surround yourself with happy, warm, and genuine people.",
        "Keep your face always toward the sunshine—and shadows will fall behind you.",
        "Happiness is not something ready made. It comes from your own actions.",
        "Positivity, confidence, and persistence are key in life, so never give up on yourself.",
        "The only limit to our realization of tomorrow will be our doubts of today.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. ",
        "The future belongs to those who believe in the beauty of their dreams. ",
        "You miss 100 percent of the shots you don't take. - Wayne Gretzky",
        "In the end, we will remember not the words of our enemies, but the silence of our friends. ",
        "Life is 10% what happens to us and 90 percent how we react to it. ",
        "The only person you are destined to become is the person you decide to be. ",
        "Don't count the days, make the days count. ",
        "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks. ",
        "The best way to predict the future is to create it. ",
        "The harder I work, the luckier I get. ",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
        "I can't change the direction of the wind, but I can adjust my sails to always reach my destination. - Jimmy Dean",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "Success is walking from failure to failure with no loss of enthusiasm. - Winston S. Churchill",
        "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. - Steve Jobs",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison",
        "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time. - Thomas A. Edison",
        "The road to success and the road to failure are almost exactly the same. - Colin R. Davis",
        "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible. - Joel Brown",
        "You don't have to be great to start, but you have to start to be great. - Zig Ziglar",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "The best revenge is massive success. - Frank Sinatra",
        "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
        "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
        "Your attitude, not your aptitude, will determine your altitude. - Zig Ziglar",
        "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
        "Don't let yesterday take up too much of today. - Will Rogers",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "If you are not willing to risk the usual, you will have to settle for the ordinary. - Jim Rohn",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
        "The secret to success is to know something nobody else knows. - Aristotle Onassis",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "In order to succeed, we must first believe that we can. - Nikos Kazantzakis",
        "Believe you can and you're halfway there. -Theodore Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
        "You miss 100 percent of the shots you don't take. - Wayne Gretzky",
        "The best way to predict the future is to create it. - Peter Drucker",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "If you want to achieve greatness stop asking for permission. - Anonymous",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "The harder I work, the luckier I get. - Samuel Goldwyn",
        "Don't count the days, make the days count. - Muhammad Ali",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
        "Life is 10% what happens to us and 90 percent how we react to it. - Charles R. Swindoll",
        "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks. - Mark Zuckerberg",
        "The best revenge is massive success. - Frank Sinatra",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible. - Joel Brown",
        "The road to success and the road to failure are almost exactly the same. - Colin R. Davis",
        "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
        "Success is walking from failure to failure with no loss of enthusiasm. - Winston S. Churchill",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time. - Thomas A. Edison",
        "I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison",
        "Don't let yesterday take up too much of today. - Will Rogers",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "If you are not willing to risk the usual, you will have to settle for the ordinary. - Jim Rohn",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
        "The secret to success is to know something nobody else knows. - Aristotle Onassis",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "In order to succeed, we must first believe that we can. - Nikos Kazantzakis",
        "Believe you can and you're halfway there. -Theodore Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
        "You miss 100 percent of the shots you don't take. - Wayne Gretzky",
        "The best way to predict the future is to create it. - Peter Drucker",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "If you want to achieve greatness stop asking for permission. - Anonymous",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "The harder I work, the luckier I get. - Samuel Goldwyn",
        "Don't count the days, make the days count. - Muhammad Ali",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
        "Life is 10% what happens to us and 90 percent how we react to it. - Charles R. Swindoll",
        "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks. - Mark Zuckerberg",
        "The best revenge is massive success. - Frank Sinatra",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible. - Joel Brown",
        "The road to success and the road to failure are almost exactly the same. - Colin R. Davis",
        "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
        "Success is walking from failure to failure with no loss of enthusiasm. - Winston S. Churchill",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time. - Thomas A. Edison",
        "I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison",
        "Don't let yesterday take up too much of today. - Will Rogers",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "If you are not willing to risk the usual, you will have to settle for the ordinary. - Jim Rohn",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
        "The secret to success is to know something nobody else knows. - Aristotle Onassis",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "In order to succeed, we must first believe that we can. - Nikos Kazantzakis",
        "Believe you can and you're halfway there. -Theodore Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
        "You miss 100 percent of the shots you don't take. - Wayne Gretzky",
        "The best way to predict the future is to create it. - Peter Drucker",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "If you want to achieve greatness stop asking for permission. - Anonymous",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "The harder I work, the luckier I get. - Samuel Goldwyn",
        "Don't count the days, make the days count. - Muhammad Ali",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
        "Life is 10% what happens to us and 90 percent how we react to it. - Charles R. Swindoll",
        "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks. - Mark Zuckerberg",
    ]


def send_txt(recipient):
    global used_quotes

    #check if is used, if is used find another random one and assign it to message
    while True:
        random_index1 = random.randint(0, len(quotes) - 1)
        quote_of_the_day = quotes[random_index1]

        if quote_of_the_day not in used_quotes:
            break


    msg = MIMEText(quote_of_the_day, 'plain')
    msg['TO'] = recipient
    msg['From'] = formataddr((sender_name, sender_email))

    with smtplib.SMTP(smtp_server,smtpd_port) as server:
        server.starttls()
        server.login(sender_email,sender_pass)
        server.sendmail(sender,recipient,msg.as_string())
        print(f'message sent to{recipient}')

    used_quotes.append(quote_of_the_day)


send_txt(niko)
# send_txt(gina)

# scheduled everyday at 6pm
# def job():
#     # Calculate the current time in EST
#     est = pytz.timezone('US/Eastern')
#     current_time_est = datetime.now(est)

#     # Check if it's 6 PM EST
#     if current_time_est.hour == 8 and current_time_est.minute == 0:
#         send_txt(gina)

# # Schedule the job to run every minute
# schedule.every(1).minutes.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)