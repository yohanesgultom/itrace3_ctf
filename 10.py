# NOTE Required Python 3

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pytg.sender import Sender
from pytg.receiver import Receiver
from pytg.utils import coroutine
import re

telegramcli = "/home/yohanesgultom/tg"
telegrampubkey = "/home/yohanesgultom/tg/tg-server.pub"


# this is the function which will process our incoming messages
@coroutine
def example_function(sender):  # name "example_function" and given parameters are defined in main()
    quit = False
    try:
        while not quit:  # loop for messages
            msg = (yield)  # it waits until the generator has a has message here.
            sender.status_online()  # so we will stay online.
            # (if we are offline it might not receive the messages instantly,
            #  but eventually we will get them)
            # print(msg)
            if msg.event != "message":
                continue  # is not a message.
            if msg.own:  # the bot has send this message.
                print("me: {}".format(msg.text))
                continue  # we don"t want to process this message.
            if msg.text is None:  # we have media instead.
                continue  # and again, because we want to process only text message.

            # text message
            print(msg.text)
            if msg.text == "Too long time. Solve it faster.":
                res = sender.send_msg("@ScazzyBot", "/start")

            # maybe a question
            match = re.search(r"Solve this: (.+) in less than 20 seconds", msg.text, re.M | re.I)
            if match and len(match.groups()) > 0:
                expression = match.groups(1)[0]
                print(expression)
                ans = answer(expression)
                res = sender.send_msg("@ScazzyBot", "/answer {}".format(ans))

    except GeneratorExit:
        # the generator (pytg) exited (got a KeyboardIterrupt).
        pass
    except KeyboardInterrupt:
        # we got a KeyboardIterrupt(Ctrl+C)
        pass
    else:
        # the loop exited without exception, becaues _quit was set True
        pass


def answer(exp):
    tokens = exp.split(" ")
    for i in range(len(tokens)):
        if i % 2 == 0:
            tokens[i] = str(int(tokens[i], 16)) if "x" in tokens[i] else str(int(tokens[i], 2))
        else:
            if tokens[i] == "add":
                tokens[i] = "+"
            elif tokens[i] == "x":
                tokens[i] = "*"
            elif tokens[i] == "÷":
                tokens[i] = "//"
    exp = " ".join(tokens)
    print(exp)
    return eval(exp)

# main
receiver = Receiver("127.0.0.1", 4458)
sender = Sender("127.0.0.1", 4458)
res = sender.send_msg("@ScazzyBot", "/start")
print("me: /start")
receiver.start()
receiver.message(example_function(sender))
receiver.stop()
