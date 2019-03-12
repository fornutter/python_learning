import itchat
from bus_search_v4_coding import bus_search

def bus(destion):
    to_str = []
    bus_home = bus_search()
    bus_home.ask(destion)
    bus_home.get()
    a = bus_home.direct_bus()
    for i in a:
        no = "_".join(i)
        to_str.append(no)
    result = "\n".join(to_str)
    return result

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    if msg["Text"] in ["home", "work"]:
        a = bus(msg["Text"])
        itchat.send(a, toUserName=msg['FromUserName'])
    else:
        return

itchat.auto_login()
itchat.run()