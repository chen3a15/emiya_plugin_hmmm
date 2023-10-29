
from libs.event.qqevent import onmessage

# 人的本质是复读机
msg = {}

@onmessage()
async def handle(e):
    event = e.netpackage
    
    if event.post_type != "message":
      # event类型
      return
    if event.message_type != "group":
      # 消息类型
      return
    if event.sub_type == "notice":
      # 忽略群通知
      return
    if event.self_id == event.user_id:
      # 忽略自身消息
      return
    
    group_id = str(event.group_id)
    
    if msg.get(group_id, ["", False])[0] == event.raw_message:
      if msg.get(group_id, ["", False])[1] == False:
        await e.callAPI(url="send_group_msg", group_id=event.group_id, message=msg[group_id][0])
        msg[group_id] = [event.raw_message, True]
    else:
        msg[group_id] = [event.raw_message, False]
    