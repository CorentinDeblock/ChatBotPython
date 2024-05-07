# ChatBotPython

ChatBotPython is a repo to test machine learning on python with a simple chat bot project. This is for learning purpose only

Made with Python version 3.12.3

## How to use the bot

You need to run it into the console via 

```bash
python main.py
```

ctrl+c to close the console

## Prerequesite

While you can train the bot by chatting with him. It's not very recommended because it's very long and will take forever before getting something interresting.

Instead you will train the bot but with train data. Train data are just normal conversation data like the one you have on messenger, etc...

You can also populate with a list of word if you want via txt file.

When you have all the data that you want. You can type the following into the console.

```bash
python populate.py
```

This will create a sqlite database with all the data.

### How to train the bot ?

To train the bot with train data. You will need to have some data. You have two ways to get some data.

You can either
- Create a folder with any name that you want. Create a txt file inside it and type a list of words in a txt file
- Download messenger conversation with friends and place the folder into the data folder

If you chose the second option. Do not forget to indicate the type of the data file (messenger, whatsapp, etc...).

```json
{
    // The type of the data file
    "type": "messenger",
    "messages": [
        // message data here...
    ],
    "participants": []
}
```

### What type are supported ?

Right now the only data file type that are supported are

- messenger

## If you have the "module 'time' has no attribute 'clock'" error

This error is coming from sqlalchemy module. This can be fix in two ways.

Either you use a version of python that is below 3.8.

Or you fix the sqlalchemy module error.

### If you plain to fix sqlalchemy

The error is on line 264 and look like this.

```python
if win32 or jython:
    time_func = time.clock
else:
    time_func = time.time
```

Just change it to

```python
if win32 or jython:
    #time_func = time.clock
    pass
else:
    time_func = time.time
```

#### Path of the module

If you use virtual environment.
The path will be <ENV_FOLDER>\Lib\site-packages\sqlalchemy\util\compat.py

If you are not using a virtual environment. 
The path will be <PYTHON_FOLDER>\Lib\site-packages\sqlalchemy\util\compat.py

This fix was found on [Stackoverflow](https://stackoverflow.com/questions/66799322/chatterbot-attributeerror-module-time-has-no-attribute-clock)