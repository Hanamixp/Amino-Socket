from .wss import Wss, WssClient, Actions, SetAction
from json.decoder import JSONDecodeError
from requests import get

version = '1.0.1'
try:
    newest = get("https://pypi.python.org/pypi/Amino-Socket/json").json()["info"]["version"]
    if version != newest:
        print(f"\033[1;33mAmino-Socket New Version!: {newest} (Your Using {version})\033[1;0m")
except JSONDecodeError:
    pass
