import fire
import requests
import webbrowser
from json import loads



def push(command: str, f: str = "root", a: str = "cyberlab"):
    """
    Push command to repo
    :param command : command for push on repository
    :param f: folder for push  (default : root )
    :param a: author of command  (default: cyberlab)
    :return:
        Message of success or error
    """

    url = 'http://my-commands-backend.herokuapp.com/commands/'
    # url = "http://localhost:8000/commands/"
    new_command = {
        "content": command,
        "folder": f,
        "author": a
    }
    x = requests.post(url, json=new_command)
    if x.status_code == 200:
        return "Command successfully pushed"
    else:
        return "Error!"


def get_all_folders():
    """
        Get names of all folders
    :return:
        List of all folders
    """
    url = 'http://my-commands-backend.herokuapp.com/commands/folders'
    x = requests.get(url)
    folders = loads(x.content)
    if x.status_code == 200:
        return folders
    else:
        return "Error!"


def get_all_commands_by_folder(folder: str):
    """
    Get commands by folder
    :param folder: Name of folder
    :return:
        List of all commands in specific folder
    """
    url = f'http://my-commands-backend.herokuapp.com/commands/folder/{folder}'
    x = requests.get(url)
    commands = loads(x.content)
    commands = [item['content'] for item in commands]
    if x.status_code == 200:
        return commands
    else:
        return "Error!"


def search_commands(query: str):
    """
    Search all commands by query
    :param query:
    :return:
        List of commands which contain given query
    """
    url = f'http://my-commands-backend.herokuapp.com/commands/search/{query}'
    x = requests.get(url)
    commands = loads(x.content)

    commands = [item['content'] for item in commands]
    if x.status_code == 200:
        return commands
    else:
        return "Error!"


def get_all_commands():
    """
    Get all commands
    :return:
        Return all commands in repository
    """
    url = f'http://my-commands-backend.herokuapp.com/commands/'
    x = requests.get(url)
    commands = loads(x.content)
    commands = [item['content'] for item in commands]
    if x.status_code == 200:
        return commands
    else:
        return "Error!"


def open():
    """
    Open My Commands repo
    :return:
    """
    webbrowser.open('https://my-command.herokuapp.com/', new=2)


def main():
    fire.Fire({
        "push": push,
        "open": open,
        "getf": get_all_folders,
        "getc": get_all_commands,
        "getcf": get_all_commands_by_folder,
        "getcs": search_commands
    })


if __name__ == "__main__":
    main()
