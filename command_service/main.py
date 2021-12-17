import fire
import requests


def push(command: str, folder: str = "root"):
    """
    Push command to repo
    :param command : command for push on repository
    :param folder: folder for push  (default : root )
    :return: OK - push success
            ERROR - push failed
    """

    url = 'http://localhost:8000/commands/create-command'
    new_command = {
        "content": command,
        "folder": folder,
        "author": "andrija"
    }
    x = requests.post(url, json=new_command)
    return x.status_code


def main():
    fire.Fire({
        "push": push
    })


if __name__ == "__main__":
    main()
