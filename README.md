# TellAngel-
Telegram bot that uses sentiment analysis to identify if a user is sending a mean or kind message. 
The telegram bot stores the user's kindness scores across all group chats. 
The score is initialised at 0.
If the user is being mean, the kindness score will drop by 1. However, for every kind words, the kindness score will increase by 1. 
We incorporated the use of autocorrect to ensure that sentiment analysis can be done even on sentences that are spelt incorrectly. 
For each kind word or mean message, a quote is given with their respective call-to-action. 
