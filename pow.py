import random
import hashlib

class Block():
    __slots__ = 'contents_hash', 'previous_hash', 'nonce'
    
    def __init__(self, contents_hash='0'*256, previous_hash='0'*256):
        assert type(contents_hash) == str and type(previous_hash) == str
        assert len(contents_hash) == 256 and len(previous_hash) == 256

        self.contents_hash = contents_hash
        self.previous_hash = previous_hash 
        
        # when this block started being mined
        # self.timestamp

        # this is adjusted to make the hash of this header fall in the valid range
        self.nonce = 0
    
    def build_block(self, previous, contents):
        assert isinstance(previous, Block) or previous == None

        if(previous):
            # calculate previous block header hash
            previous_hash = previous.previous_hash
            self.previous_hash = hashlib.sha256(previous_hash.encode('utf-8')).hexdigest()
        else:
            # genesis has no previous. just use zeroed hash
            self.previous_hash = 0

    
        # add data hash
        self.contents_hash = hashlib.sha256(str(contents).encode('utf-8')).hexdigest()

    def mine_block(self):
        MAX_HASH = 2 ** 6
        target = hashlib.sha256(str(random.randint(0, MAX_HASH - 1)).encode('utf-8')).hexdigest()
        # MINING: start of the mining round
        for nonce in range(MAX_HASH):
            current_hash = hashlib.sha256((self.contents_hash + str(nonce)).encode('utf-8')).hexdigest()
            if(current_hash < target):
                self.nonce = nonce
                print(nonce)
                return
    
class Blockchain():
    def __init__(self):
        self.blocks = []

    def add_block(self, contents):
        block = Block()
        if(len(self.blocks) == 0):
            block.build_block(None, contents)

        else:
            block.build_block(self.blocks[-1], contents)
        block.mine_block()
        self.blocks.append(block)

blockchain = Blockchain()
blockchain.add_block('0x0')