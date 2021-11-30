import hmac
import json
import base64
import requests
import websocket
import threading
import time as timer
from time import time
from hashlib import sha1
from time import timezone
from typing import BinaryIO
from .src import headers as header
from json_minify import json_minify
from .src.exception import exception


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
        SetAction(self.socket, {
            "o": {"actions": ["Browsing"], "target": f"ndc://x{self.comId}/", "ndcId": int(self.comId),
                  "params": {"duration": 27605}, "id": "363483"}, "t": 306}).start()

    def Browsing(self, blogId: str = None, blogType: int = 0):
        """
        Send Browsing Action

        **Paramaters**
            - **blogId**: 2 For Public 1 & 0 For Private (str)
            - **blogType**: Type Of the Blog *poll & blog & wiki* (int)

        **Return**
            - **SetAction**:  (Class)
        """
        if blogId and blogType:
            target = f"ndc://x{self.comId}/blog/"
        else:
            target = f"ndc://x{self.comId}/featured"

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
        timer.sleep(2)
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
        timer.sleep(2)
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
        timer.sleep(2)
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
        timer.sleep(2)
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
        timer.sleep(2)
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
        timer.sleep(2)
        self.wss.send(data)

    def threadJoin(self, comId: str, chatId: str):
        data = {
            "o": {
                "ndcId": int(comId),
                "threadId": chatId,
                "joinRole": 1,
                "id": "10335106"
            },
            "t": 112
        }
        self.wss.send(data)

    def channelJoin(self, comId: str, chatId: str):
        data = {
            "o": {
                "ndcId": int(comId),
                "threadId": chatId,
                "channelType": 5,
                "id": "10335436"
            },
            "t": 108
        }
        self.wss.send(data)

    def videoPlayer(self, comId: str, chatId: str, path: str, title: str, background: str, duration: int):
        self.actions(comId, chatId).Chatting().start()
        self.threadJoin(comId, chatId)
        self.channelJoin(comId, chatId)
        data = {
            "o": {
                "ndcId": int(comId),
                "threadId": chatId,
                "playlist": {
                    "currentItemIndex": 0,
                    "currentItemStatus": 1,
                    "items": [{
                        "author": None,
                        "duration": duration,
                        "isDone": False,
                        "mediaList": [[100, background, None]],
                        "title": title,
                        "type": 1,
                        "url": f"file://{path}"
                    }]
                },
                "id": "3423239"
            },
            "t": 120
        }
        self.wss.send(data)
        timer.sleep(2)
        data["o"]["playlist"]["currentItemStatus"] = 2
        data["o"]["playlist"]["items"][0]["isDone"] = True
        self.wss.send(data)

    def playVideo(self, comId: str, chatId: str, path: str, title: str, background: BinaryIO, duration: int):
        """
        Play Custom Vide

        **Parameters**
            - **comId** : ID of the Community (str)
            - **chatId** : ID of the Chat (str)
            - **path** : Video Path | /C:/Users/User/Downloads/video.mp4 | /storage/emulated/0/Download/video.mp4 (str)
            - **title** : Video Title (str)
            - **background** : Background of the video (BinaryIO)
            - **duration** : length of the mp4/mp3 (int)
        """
        threading.Thread(target=self.videoPlayer, args=(comId, chatId, path, title, self.wss.uploadMedia(background, "image"), duration)).start()

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
        timer.sleep(2)
        self.wss.send(data)
        data["t"] += 2
        self.wss.send(data)
        timer.sleep(0.50)
        return self.wss.receive()

    def actions(self, comId: str, chatId: str):
        threading.Thread(target=self.wss.sendActive, args=(comId, 25, )).start()
        return Actions(self.wss, comId, chatId)


class Wss:
    def __init__(self, headers: dict, trace: bool = False):
        """
        Scheduling WssClient with Wss

        **Parameters**
            - **headers**: Your Amino Headers (dict)
        """
        heders = {
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8 Build/PKQ1.190616.001; com.narvii.amino.master/3.4.33578)",
            "AUID": "dfec1b8a-92f7-4cf0-928c-3b60aa33429a",
            "SMDEVICEID": "6e28d4c5-2d25-4977-93ec-9a4ce077fb7b",
            "Host": "service.narvii.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
        }
        self.narvi = "https://service.narvii.com/api/v1/"
        self.api = 'https://aminoapps.com/api-p'
        self.socket_url = "wss://ws1.narvii.com"
        websocket.enableTrace(trace)
        self.socket = websocket.WebSocket()

        if headers.get("NDCAUTH") and headers.get("NDCDEVICEID"):
            self.sid = headers["NDCAUTH"]
            self.deviceid = headers["NDCDEVICEID"]
            heders["NDCDEVICEID"] = self.deviceid
            heders["NDCAUTH"] = self.sid
            header.headers = heders
            self.headers = header.Headers().headers

        else:
            exception({"api:message": "Headers Should Contains \"NDCAUTH\" and \"NDCDEVICEID\" header or key"})

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
        response = requests.get("https://aminoapps.com/api/chat/web-socket-url", headers={'cookie': self.sid})
        if response.status_code != 200:
            return exception(response.json())
        else:
            self.socket_url = response.json()["result"]["url"]
            return self.socket_url

    def launch(self):
        """
        Launching the Socket
        """
        head = {'cookie': self.sid}
        self.socket.connect(self.webSocketUrl(), header=head)

    def getClient(self):
        """
        Get Amino Websocket Types

        **Returns**
            - **WssClient**: A Client With Amino Socket Functions (Class)
        """
        return WssClient(self.socket, self)

    def uploadMedia(self, file: BinaryIO, fileType: str):
        if fileType == "audio":
            typee = "audio/aac"
        elif fileType == "image":
            typee = "image/jpg"
        else:
            raise TypeError("[i] Report this error in Discord Server as [15:0]")

        data = file.read()
        headers = self.headers
        headers["content-type"] = typee
        headers["content-length"] = str(len(data))

        response = requests.post(f"{self.narvi}/g/s/media/upload", data=data, headers=headers)
        if response.json()["api:statuscode"] != 0:
            return exception(response.json())
        else:
            return response.json()["mediaValue"]

    def sendActive(self, comId: str, rang: int = 1, tz: int = -timezone // 1000, timers: list = None, timestamp: int = int(time() * 1000)):
        """
        Send A Active Time To Community

        **Returns**
            - **Success**: Post Request objects (
            - **WssClient**: A Client With Amino Socket Functions (Class)
        """
        chunkes = []

        for i in range(rang):
            start = int(time())
            end = start + 300
            chunkes.append({"start": start, "end": end})

        data = {
            "userActiveTimeChunkList": chunkes,
            "timestamp": timestamp,
            "optInAdsFlags": 2147483647,
            "timezone": tz
        }

        if timers:
            data["userActiveTimeChunkList"] = timers

        data = json_minify(json.dumps(data))
        headers: dict = self.headers
        headers["NDC-MSG-SIG"] = base64.b64encode(b"\x22" + hmac.new(bytes.fromhex("307c3c8cd389e69dc298d951341f88419a8377f4"), data.encode(), sha1).digest()).decode()
        headers["Content-Length"] = str(len(data))
        response = requests.post(f"{self.narvi}/x{comId}/s/community/stats/user-active-time", headers=headers, data=data)
        if response.json()["api:statuscode"] != 0:
            return exception(response.json())
        else:
            return response
