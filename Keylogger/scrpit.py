import keyboard


def on_key_press(event: keyboard.KeyboardEvent):
    with open('./keyLoggerTests.json', 'w') as f:
        f.write(event.to_json())
