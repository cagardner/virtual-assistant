import pyjokes
from ai import AI

assistant = AI()


def jokes():
    funny = pyjokes.get_joke()
    print(funny)
    assistant.say(funny)


command = ""
while True and command != "goodbye":
    command = assistant.listen()
    print("command was:", command)

    if command == "tell me a joke":
        jokes()
assistant.say("Going to standby. Ready when you are.")
