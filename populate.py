from shared import bot_name, database_uri, storage_adapter, ignores, read_json, read_file
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import os
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

def read_data(filepath):
    json_data = read_json(filepath)
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
        if root_dir in ignores:
            continue

        sub_filepath = root + "/" + root_dir + "/"
        for file in os.listdir(sub_filepath):
            if file == "data.json":
                data.extend(read_data(sub_filepath + file))
            if file == "data.txt":
                data.extend(read_file(sub_filepath + file).split("\n"))
            
    return data

if storage_adapter == "chatterbot.storage.SQLStorageAdapter":
    sqlite_path = database_uri.removeprefix("sqlite:///")
    
    if os.path.exists(sqlite_path):
        os.remove("./" + sqlite_path)

chatbot = ChatBot(
    bot_name,
    storage_adapter=storage_adapter,
    database_uri=database_uri
)

trainer = ListTrainer(chatbot)
trainer.train(load())