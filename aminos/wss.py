import time
import json
from typing import BinaryIO

import requests
import websocket
from .src.exception import Exception
from .src import headers as header


class SetAction:
    def __init__(self, wss, data):
        self.action = data
        self.wss = wss

    def start(self):
        """
        Start the Action
        """
        self.wss.send(self.action)

    def stop(self):
        """
        Get back to the last board
        """
        act = self.action
        act["t"] = 303
        self.wss.send(self.action)


class Actions:
    def __init__(self, socket, comId, chatId):
        self.socket = socket
        self.chatId = chatId
        self.comId = comId

    def default(self):
        """
        Default Browsing
        """
        SetAction(self.socket, {"o": {"actions": ["Browsing"], "target": f"ndc://x{self.comId}/", "ndcId": int(self.comId), "params": {"duration": 27605}, "id": "363483"}, "t": 306}).start()

    def Browsing(self, blogId: str = None, blogType: int = 0):
        """
        Send Browsing Action

        **Paramaters**
            - **blogId**: 2 For Public 1 & 0 For Private (str)
            - **blogType**: Type Of the Blog *poll & blog & wiki* (int)

        **Return**
            - **SetAction**:  (Class)
        """
        if blogId and blogType: target = f"ndc://x{self.comId}/blog/"
        else: target = f"ndc://x{self.comId}/featured"

        data = {
            "o": {
                "actions": ["Browsing"],
                "target": target,
                "ndcId": int(self.comId),
                "params": {"blogType": blogType},
                "id": "363483"
            },
            "t": 306
        }
        self.default()
        return SetAction(self.socket, data)

    def Chatting(self, threadType: int = 2):
        """
        Send Chatting Action

        **Paramaters**
            - **threadType**: 2 For Public 1 & 0 For Private (int)

        **Return**
            - **SetAction**:  (Class)
        """
        data = {
            "o": {
                "actions": ["Chatting"],
                "target": f"ndc://x{self.comId}/chat-thread/{self.chatId}",
                "ndcId": int(self.comId),
                "params": {
                    "duration": 12800,
                    "membershipStatus": 1,
                    "threadType": threadType
                },
                "id": "1715976"
            },
            "t": 306
        }
        self.default()
        return SetAction(self.socket, data)

    def PublicChats(self):
        """
        Send PublicChats Action

        **Return**
            - **SetAction**:  (Class)
        """
        data = {
            "o": {
                "actions": ["Browsing"],
                "target": f"ndc://x{self.comId}/public-chats",
                "ndcId": int(self.comId),
                "params": {"duration": 859},
                "id": "363483"
            },
            "t": 306
        }
        self.default()
        return SetAction(self.socket, data)

    def LeaderBoards(self):
        """
        Send LeaderBoard Action

        **Return**
            - **SetAction**:  (Class)
        """
        data = {
            "o": {
                "actions": ["Browsing"],
                "target": f"ndc://x{self.comId}/leaderboards",
                "ndcId": int(self.comId),
                "params": {"duration": 859},
                "id": "363483"
            },
            "t": 306
        }
        self.default()
        return SetAction(self.socket, data)

    def Custom(self, actions: [str, list], target: str, params: dict):
        """
        Send Custom Action

        **Parameters**
            - **actions**: List of action Types (list[str])
            - **target**: Example | ndc://x000000/leaderboards (str)
            - **params**: Set the blogType and more with params (dict)

        **Return**
            - **SetAction**:  (Class)
        """
        data = {
            "o": {
                "actions": actions,
                "target": target,
                "ndcId": int(self.comId),
                "params": params,
                "id": "363483"
            },
            "t": 306
        }
        self.default()
        return SetAction(self.socket, data)


class WssClient:
    def __init__(self, socket, wss):
        self.wss = wss
        self.socket = socket

    def joinVoiceChat(self, comId: str, chatId: str, joinType: int = 1):
        """
        Join The Voice Chat

        **Parameters**
            - **comId**: ID of the Community (str)
            - **chatId**: ID of the Chat (str)
            - **joinType**: Join type to Join Voice as.. (int)
        """
        data = {
            "o": {
                "ndcId": int(comId),
                "threadId": chatId,
                "joinRole": joinType,
                "id": "37549515"
            },
            "t": 112
        }
        time.sleep(2)
        self.wss.send(data)

    def joinVideoChat(self, comId: str, chatId: str, joinType: int = 1):
        """
        Join The Video Chat

        **Parameters**
            - **comId**: ID of the Community (str)
            - **chatId**: ID of the Chat (str)
            - **joinType**: Join type to Join Video as.. (int)
        """
        data = {
            "o": {
                "ndcId": int(comId),
                "threadId": chatId,
                "joinRole": joinType,
                "channelType": 5,
                "id": "2154531"
            },
            "t": 108
        }
        time.sleep(2)
        self.wss.send(data)

    def startVoiceChat(self, comId, chatId: str, joinType: int = 1):
        """
        Start The Voice Chat

        **Parameters**
            - **comId**: ID of the Community (str)
            - **chatId**: ID of the Chat (str)
            - **joinType**: Join type to Start voice as.. (int)
        """
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "joinRole": joinType,
                "id": "2154531"
            },
            "t": 112
        }
        time.sleep(2)
        self.wss.send(data)
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "channelType": 1,
                "id": "2154531"
            },
            "t": 108
        }
        time.sleep(2)
        self.wss.send(data)

    def endVoiceChat(self, comId: str, chatId: str, leaveType: int = 2):
        """
        End The Voice Chat

        **Parameters**
            - **comId**: ID of the Community (str)
            - **chatId**: ID of the Chat (str)
            - **leaveType**: Leave type to end voice as.. (int)
        """
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "joinRole": leaveType,
                "id": "2154531"
            },
            "t": 112
        }
        time.sleep(2)
        self.wss.send(data)

    def joinVideoChatAsSpectator(self, comId: str, chatId: str):
        """
        Join Video Chat As Spectator

        **Parameters**
            - **comId**: ID of the Community (str)
            - **chatId**: ID of the Chat (str)
        """
        data = {
            "o": {
                "ndcId": int(comId),
                "threadId": chatId,
                "joinRole": 2,
                "id": "72446"
            },
            "t": 112
        }
        time.sleep(2)
        self.wss.send(data)

    def playVideo(self, comId: str, chatId: str, path: str, title: str, background: BinaryIO):
        """
        Play Custom Video

        **Parameters**
            - **comId** : ID of the Community (str)
            - **chatId** : ID of the Chat (str)
            - **path** : Video Path (str)
            - **title** : Video Title (str)
            - **background** : Background of the video (BinaryIO)
        """
        icon = self.wss.upload_media(background, "image")
        self.wss.send({"o": {"ndcId": int(comId), "threadId": chatId, "joinRole": 1, "id": "10335106"}, "t": 112})
        self.wss.send({"o": {"ndcId": comId, "threadId": chatId, "channelType": 5, "id": "10335436"}, "t": 108})
        self.wss.send({"o": {"ndcId": comId, "threadId": chatId, "playlist": {"currentItemIndex": 0, "currentItemStatus": 1, "items": [{"author": None, "duration": 28.815, "isDone": False, "mediaList": [[100, icon, None]], "title": title, "type": 1, "url": f"file:///storage/emulated/0/{path}"}]}, "id": "10336041"}, "t": 120})
        self.wss.send({"o": {"ndcId": comId, "threadId": chatId, "playlist": {"currentItemIndex": 0, "currentItemStatus": 2, "items": [{"author": None, "duration": 28.815, "isDone": False, "mediaList": [[100, icon, None]], "title": title, "type": 1, "url": f"file:///storage/emulated/0/{path}"}]}, "id": "10337809"}, "t": 120})
        self.wss.send({"o": {"ndcId": comId, "threadId": chatId, "playlist": {"currentItemIndex": 0, "currentItemStatus": 2, "items": [{"author": None, "duration": 28.815, "isDone": True, "mediaList": [[100, icon, None]], "title": title, "type": 1, "url": f"file:///storage/emulated/0/{path}"}]}, "id": "10366159"}, "t": 120})

    def getActionUsers(self, comId: str, path: str):
        """
        Get Action Users

        **Parameters**
            - **comId**: ID of the Community (str)
            - **path**: Example: "users-chatting" (str)
        """
        data = {
            "o": {
                "ndcId": int(comId),
                "topic": f"ndtopic:x{comId}:{path}",
                "id": "4538416"
            },
            "t": 300
        }
        self.wss.send(data)
        time.sleep(2)
        return self.wss.receive()

    def actions(self, comId: str, chatId: str):
        return Actions(self.wss, comId, chatId)


class Wss:
    def __init__(self, headers: dict, trace: bool = False):
        """
        Scheduling WssClient with Wss

        **Parameters**
            - **headers**: Your Amino Headers (dict)
        """
        self.api = 'https://aminoapps.com/api-p'
        self.socket_url = "wss://ws1.narvii.com"
        websocket.enableTrace(trace)
        self.socket = websocket.WebSocket()

        if headers.get("NDCAUTH") and headers.get("NDCDEVICEID"):
            self.sid = headers["NDCAUTH"]
            self.deviceid = headers["NDCDEVICEID"]
            header.headers = headers
            self.headers = header.Headers().headers
        else:
            Exception({"api:message": "Headers Should Contains \"NDCAUTH\" and \"NDCDEVICEID\" header or key"})

    def send(self, data):
        """
        Send data to wss

        **Parameters**
             - **data**: The data you want to send (dict)
        """
        self.socket.send(json.dumps(data))

    def receive(self):
        """
        Receive data from wss

        **Returns**
            - **data**: Received data (json)
        """
        return json.loads(self.socket.recv())

    def webSocketUrl(self):
        req = requests.get("https://aminoapps.com/api/chat/web-socket-url", headers={'cookie': self.sid})
        if req.status_code != 200: return Exception(req.json())
        else:
            self.socket_url = req.json()["result"]["url"]
            return self.socket_url

    def launch(self):
        """
        Launching the Socket
        """
        self.headers = {'cookie': self.sid}
        self.socket.connect(self.webSocketUrl(), header=self.headers)

    def getClient(self):
        """
        Get Amino Websocket Types

        **Returns**
            - **WssClient**: A Client With Amino Socket Functions (Class)
        """
        return WssClient(self.socket, self)

    def uploadMedia(self, file: BinaryIO, fileType: str):
        if fileType == "audio": typee = "audio/aac"
        elif fileType == "image": typee = "image/jpg"
        else: raise TypeError("[i] Report this error in Discord Server as [15:0]")

        data = file.read()
        headers = self.headers
        headers["content-type"] = typee
        headers["content-length"] = str(len(data))

        req = requests.post(f"{self.api}/g/s/media/upload", data=data, headers=headers)
        if req.json()["api:statuscode"] != 0: return Exception(req.json())
        else: return req.json()["mediaValue"]
