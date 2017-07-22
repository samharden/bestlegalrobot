from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatterbot = ChatBot("Django ChatterBot Example")
chatterbot.set_trainer(ListTrainer)

chatterbot.train([
    "Hi there!",
    "Hello",
])

chatterbot.train([
    "Greetings!",
    "Hello",
])
