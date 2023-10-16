from libs.event.qqevent import onkeyword,oncommand

import os
import requests

os.system("")

with open("./data/voice/voice.json", 'r', encoding="utf-8") as f:
  voice = json.load(f)

@onkeyword(keywordList=["语音"])
def _(event: dict) -> bool:
  msg = event.message.split("语音")
  if msg[0].split("-", 1)[0] not in ["gs", "sr"]:
    msg[0] = "gs-" + msg[0]
  username = msg[0]
  if msg[1] and voice["角色"].get(msg[0]) and voice["角色"][username]["语音"].get(msg[1]):
    message = {
      "group_id": event.group_id,
      "message": {
        "type": "music",
        "data": {
          "type": "custom",
          "subtype": random.choice(["qq", "163", "kuwo", "kugou"]),
          "url": "https://qm.qq.com/cgi-bin/qm/qr?k=J8wG4ovLfaazjhrWbyX2902XhkbxfNq6&noverify=0&personal_qrcode_source=4",
          "voice": voice["角色"][username]["语音"][msg[1]][0],
          "title": msg[1],
          "content": voice["角色"][username]["语音"][msg[1]][1],
          "image": voice["角色"][username]["icon"]
        }
      }
    }
  if not username in voice["角色"]:
    message = {
      "group_id": event.group_id,
      "message": {
        "type": "text",
        "data": {
          "text": f"没有找到原神中%s的语音" % (username)
        }, {
        "type": "reply",
        "data": {
          "id": event.message_id
        }
      }
    }
  
  BASEURL = "http://127.0.0.1:5700"
  requests.post(f"{BASEURL}/send_group_msg", data=message)
  return True