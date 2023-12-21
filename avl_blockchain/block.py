import datetime as date
import hashlib


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = date.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.get_hash()

    def __str__(self):
        return f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'

    def get_hash(self):
        return hashlib.sha256(f'{self}'.encode()).hexdigest()
