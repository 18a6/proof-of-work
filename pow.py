import hashlib

class Block():
    __slots__ = 'contents_hash', 'previous_hash'
    
    def __init__(self, contents_hash=0, previous_hash=0):
        # assert len(contents_hash) == 256 and len(previous_hash) == 256

        self.contents_hash = contents_hash
        self.previous_hash = previous_hash 
        
        # when this block started being mined
        # self.timestamp

        # this is adjusted to make the hash of this header fall in the valid range
        # self.nonce
    
    def build_block(self, previous, contents):
        block_header = Block()
        assert isinstance(previous, Block)

        if(previous):
            # calculate previous block header hash
            previous_hash = str(previous.previous_hash)
            block_header.previous_hash = hashlib.sha256(previous_hash.encode('utf-8')).hexdigest()
        else:
            # genesis has no previous. just use zeroed hash
            block_header.previous_hash = 0
        # add data hash
        block_header.contents_hash = hashlib.sha256(str(contents).encode('utf-8')).hexdigest()
        print(block_header.contents_hash)


block_header = Block()
previous = Block(0, '0x')
block_header.build_block(previous, 0)





