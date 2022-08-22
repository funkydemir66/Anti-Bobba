# encoding:utf-8

INVISIBLE = "ђђ"

CMD = ":ab"


import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction


extension_info = {
    "title": "Anti-Bobba",
    "description":":ab on / off",
    "version": "0.3",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv)
ext.start()


on = False


def speech(msg):
    global on

    (text, bubble, idd) = msg.packet.read('sii')

    if on:
        if not text.startswith(CMD):
            msg.is_blocked = True
            message = "ђђ"

            for i in text:
                message += INVISIBLE + i

            ext.send_to_server('{out:Chat}{s:"%s"}{i:%s}{i:%s}' % (message, bubble, idd))

    if text == CMD + " on":
        msg.is_blocked = True
        on = True
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Anti-Bobba: v/"}{i:0}{i:30}{i:0}{i:0}')

    if text == CMD + " off":
        msg.is_blocked = True
        on = False
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Anti-Bobba: x"}{i:0}{i:30}{i:0}{i:0}')



ext.intercept(Direction.TO_SERVER, speech, 'Chat')
