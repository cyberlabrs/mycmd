import fire
import requests
import webbrowser


def push(command: str, folder: str = "root"):
    """
    Push command to repo
    :param command : command for push on repository
    :param folder: folder for push  (default : root )
    :return: OK - push success
            ERROR - push failed
    """

    url = 'http://my-commands.herokuapp.com/commands/create-command'
    new_command = {
        "content": command,
        "folder": folder,
        "author": "andrija"
    }
    x = requests.post(url, json=new_command)
    return x.status_code


def open():
    """
    Open My Commands repo
    :return:
    """
    webbrowser.open('http://my-commands.herokuapp.com/commands', new=2)


def main():
    fire.Fire({
        "push": push,
        "open": open
    })


if __name__ == "__main__":
    main()
