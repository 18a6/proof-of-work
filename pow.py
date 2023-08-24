import hashlib

def hash(input):
    return hashlib.sha256(str(input).encode('utf-8')).hexdigest()

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
        self.nonce = -1
    
    def build_block(self, previous, contents):
        assert isinstance(previous, Block) or previous == None

        if(previous):
            # calculate previous block header hash
            self.previous_hash = hash(previous.previous_hash)
        else:
            # genesis has no previous. just use zeroed hash
            self.previous_hash = 0

    
        # add data hash
        self.contents_hash = hash(contents)

    def mine_block(self):
        MAX_HASH = 2 ** 256
        target = 0x0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

        # MINING: start of the mining round
        for nonce in range(MAX_HASH):
            h = hash(self.contents_hash + str(nonce))
            if (int(h, 16) < target):
                self.nonce = nonce
                print(hash(self.contents_hash + str(nonce)))
                return
    
class Blockchain():
    __slots__ = 'blocks'

    def __init__(self):
        self.blocks = []

    def add_block(self, contents):
        block = Block()
        if(len(self.blocks) != 0):
            block.build_block(self.blocks[-1], contents)
        else:
            block.build_block(None, contents)
        block.mine_block()
        self.blocks.append(block)

blockchain = Blockchain()
blockchain.add_block('tx0: A -1BTC-> B')