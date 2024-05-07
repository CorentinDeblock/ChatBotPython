import argparse
import json

def read_file(filepath):
    file_str = ""

    with open(filepath, 'r', encoding="utf-8") as file:
        file_str += file.read()

    return file_str

def read_json(filepath):
    file_str = read_file(filepath)
    json_data = json.loads(file_str)
    
    return json_data

def get_or_default_conf(default_value, field):
    return default_value if config[field] is None else config[field]

def get_or_default_arg(default_value, field):
    arg = getattr(args, field)
    return default_value if arg is None else arg

def get_or_default(default_value, field):
    value = get_or_default_conf(default_value, field)
    value = get_or_default_arg(value, field)
    return value

parser = argparse.ArgumentParser(
    prog="loader",
    description="Populate db with example data for the bot to train"
)

parser.add_argument("-n", "--name",
    help="The name of the bot"
)

parser.add_argument("-a", "--adapter",
    help="The adapter of the database (see sqlalchemy for more info)"
)

parser.add_argument("-di", "--database_uri",
    help="The database url"
)

parser.add_argument("-i", "--ignores", 
    help="Ignore one or multiple directory when populating database",
    nargs="+"
)

parser.add_argument("-c", "--config",
    help="The config file to read"
)

args = parser.parse_args()

config = read_json(get_or_default_arg("./chatbot.conf.json", "config"))

bot_name = get_or_default("Gerard", "name")
storage_adapter = get_or_default("chatterbot.storage.SQLStorageAdapter", "adapter")
database_uri = get_or_default("sqlite:///database.sqlite3", "database_uri")
ignores = get_or_default_conf([], "ignores")

if args.ignores is not None:
    ignores.extend(args.ignores)