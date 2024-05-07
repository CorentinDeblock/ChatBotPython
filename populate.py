from shared import bot_name, database_uri, storage_adapter
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import os
import json
import re

root = "data"

def remove_emoji(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', text)

def read_file(filepath):
    file_str = ""

    with open(filepath, 'r', encoding="utf-8") as file:
        file_str += file.read()

    return file_str

def read_json(filepath):
    file_str = read_file(filepath)
    json_data = json.loads(file_str)
    data = []

    if json_data["type"] == "messenger":
        for message in json_data["messages"]:
            if message["type"] == "Text":
                content = message["content"]
                
                if not content.startswith("https") and len(remove_emoji(content)) > 0:
                    data.append(message["content"])

    return data


def load():
    data = []

    for root_dir in os.listdir(root):
        sub_filepath = root + "/" + root_dir + "/"
        for file in os.listdir(sub_filepath):
            if file == "data.json":
                data.extend(read_json(sub_filepath + file))
            if file == "data.txt":
                data.extend(read_file(sub_filepath + file).split("\n"))
            
    return data

chatbot = ChatBot(
    bot_name,
    storage_adapter=storage_adapter,
    database_uri=database_uri
)

trainer = ListTrainer(chatbot)
trainer.train(load())