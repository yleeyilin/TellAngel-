import telegram
import sqlite3
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from textblob import TextBlob
positiveArr = ["No act of kindness, no matter how small, is ever wasted. Keep it up!","It takes courage to be kind. Well done!","Let others see the good that you see in them. You're doing great!","Kindness is free - sprinkle that stuff everywhere","Love you kind message. If you were a booger, I will pick you :)","You cannot do kindness too soon, for you never know how soon it will be too late.-Ralph Waldo Emerson","Kindness is not what you do, but who you are.","Kindness is something anyone can give without losing anything themselves.","Kindness is seeing the best in others when they cannot see it in themselves." ,"When you are kind to others, it not only changes you, it not only changes you, it changes the world. - Harold Kushner","How do we change the world? One random act of kindess at a time - Morgan Freeman","How far that little candle throws his beams! So shines a good deed in a weary world. - William Shakespeare","Know that your kindness has a ripple effect in the universe! :)", "Spread love everywhere you go!", "to kindness and love, the things we need most!", "keep it up! treat others the way you want to be treated"]
negativeArr = ["LOL someone really thinks they are the main character…Reconsider what you just said.","God help… You might want to think about what you said there","Even the president does not have the right to be this rude! Think again…","Please check yourself before you wreck yourself.","For someone with your IQ level, you sure are brave…Think about what you just said.","Goodness, someone woke up on the wrong side of the bed! Consider rephrasing.","Ok boomer. Are you sure you want to be so rude","Say what you mean, but dont say it mean","I am so sorry you are having a bad day, but try to be nicer","Meanness is a sign of weakness! reevaluate your last message.","Any fool can criticize, condemn and complain and most fools do. - Benjamin Franklin","Thats not very nice. Consider rephrasing your message.", "Are you sure you should have said that? Think again!", "Won't that hurt their feelings? reconsider.", "Would you like to be spoken to that way? think again!"]
updater = Updater(${{ secrets.TOKEN }}, use_context = True)
dispatcher= updater.dispatcher
def start(update, context):
    update.message.reply_text("Hey, I am TellAngel, here to remind you to send kind messages to your precious friends. You are given a kindness score of 0. ")
    update.message.reply_text("You can use me by adding me to your telegram group chats. With each kind message, I will increase your score by 1. However, if you send a mean message, your score will drop.")
def sentiment(update, context):
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            user_id INTEGER PRIMARY KEY,
            score INTEGER
        )
    ''')
    conn.commit()
    message = update.message.text
    text = str(update.message.text).lower()
    user_id = update.message.from_user.id
    cursor.execute('''
        SELECT score FROM scores WHERE user_id = ?
    ''', (user_id,))
    result = cursor.fetchone()
    if result:
        score = result[0]
    else:
        score = 0
    blob = TextBlob(message).correct()
    bot = telegram.Bot(token = ${{ secrets.TOKEN }})
    if blob.sentiment.polarity > 0:
        position = random.randint(0,len(positiveArr)-1)
        score += 1
        #update.message.reply_text("yasss lets spread rainbows and sunshine!")
        bot.send_message(chat_id = user_id, text = positiveArr[position])
        cursor.execute('''
            INSERT OR REPLACE INTO scores (user_id, score)
            VALUES (?, ?)
        ''', (user_id, score))
        conn.commit()
        # Send the score to the user
        context.bot.send_message(chat_id= user_id, text='Your current Kindness score is: {}'.format(score))
    elif blob.sentiment.polarity < 0:
        #update.message.reply_text("thats not very nice. consider rephrasing your message")
        position = random.randint(0,len(negativeArr)-1)
        score -= 1
        bot.send_message(chat_id = user_id, text = negativeArr[position])
        cursor.execute('''
            INSERT OR REPLACE INTO scores (user_id, score)
            VALUES (?, ?)
        ''', (user_id, score))
        conn.commit()
        # Send the score to the user
        context.bot.send_message(chat_id= user_id, text='Your current Kindness score is: {}'.format(score))

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, sentiment))
updater.start_polling()
updater.idle()
