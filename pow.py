class Block:
    def __init__(self, contents_length, contents_hash,previous_hash):
        self.contents_length = contents_length
        self.contents_hash = contents_hash
        self.previous_hash = previous_hash


