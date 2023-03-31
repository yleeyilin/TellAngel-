# TellAngel
Once a user adds TellAngel to their telegram, TellAngel can be added to any chats of their wish. Through sentiment analysis, TellAngel can detect the sentimental polarity of any message (in the spectrum from positive to negative). When a positive message is delivered, TellAngel will privately messages such as “keep it up! Treat others the way you want to be treated”. As for the negative messages, TellAngel will say something like: “Any fool can criticise, condemn and complain and most fools do. - Benjamin Franklin”. TellAngel will encourage you to spread words of kindness and discourage you from succumbing to your anger, impulsiveness and whims. Moreover, TellAngel tracks your progress in your emotional journey through a “kindness score”. Upon being added to the group chat, TellAngel assigns a kindness score of 0 to each member of the group. This score either increases or decreases according to the sentimental polarity of the message one sends. This system will encourage users to more actively spread words of kindness, considering our psychological tendency to detest losing something (e.g., seeing the kindness score initially assigned to 0 going downwards towards a negative value). It will allow us to monitor whether we are on the right track of spreading kind words through checking the kindness score and TellAngel’s private message to us after sending a message will also motivate us to be more kind and pause before sending hate-texts.

However, a big limitation is that the users can manipulate the “kindness score” system. They can just spam kind messages to increase their score causing the score to falsely reflect one’s “kindness status”. We have to find a way for TellAngel to differentiate genuine texts from the fake ones, allowing the programme to be more sophisticated and accurate. If this problem is solved, TellAngel has the potential to be monetised as well. We can create a reward system like “acclaim 5% voucher for the “kindness score” of 100”.

# **How to customise this telegram bot?**
1. Go to BotFather to generate your own token.
2. Substitute ${{secrets.token}} with your own. 
3. Instead of simply sentiment analysis, you can add other functions like sarcasm detection, webscrapping etc. 

## Types of commands in a telegram bot
For functions that includes interactions between users and bot, the functions should be falling between these two categories. 
### 1. Detects messages sent by user 
`dispatcher.add_handler(MessageHandler(Filters.text, {{name of function}}))` 
### 2. Called by a command 
`dispatcher.add_handler(CommandHandler('start', start))`
