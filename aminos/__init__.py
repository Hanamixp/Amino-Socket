from requests import get
from .api import Wss
from .src.objects import Event, Payload

version = '1.0.4'
newest = get("https://pypi.python.org/pypi/Amino-Socket/json").json()["info"]["version"]
if version != newest:
    print(f"\033[1;32mAmino-Socket New Version!: {newest} (Your Using {version})\033[1;0m")
