import datetime as date
import hashlib


class Block:
    def __init__(self, index, data, previous):
        self.index = index
        self.timestamp = date.datetime.now()
        self.data = data
        self.previous = previous
        self.hash = self.get_hash()

    def __str__(self):
        previous_hash = self.previous.hash if self.previous else 0
        return f'{self.index}{self.timestamp}{self.data}{previous_hash}'

    def get_hash(self):
        return hashlib.sha256(f'{self}'.encode()).hexdigest()
