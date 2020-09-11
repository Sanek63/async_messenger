import time


class Messenger:
    db = []
    request_count = 0

    def send_message(self, name, text):
        timestamp = time.time()
        self.db.append({
            'name': name,
            'text': text,
            'time': timestamp
        })

    def get_messages(self):
        return self.db

    def get_new_messages(self):
        new_messages = self.db[self.request_count:]
        self.request_count += len(new_messages)
        return new_messages


messenger = Messenger()

messenger.send_message('Jack', 'privet')
messenger.send_message('Sasha', 'poka')
print(messenger.get_messages())
print(messenger.get_new_messages())
print()

messenger.send_message('Sasha', 'chto novogo')
messenger.send_message('Misha', 'two new messages')
print(messenger.get_messages())
print(messenger.get_new_messages())
print()