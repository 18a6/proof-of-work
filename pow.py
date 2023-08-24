class block_header_t():
    __slots__ = 'contents_length', 'contents_hash', 'previous_hash', 'timestamp', 'nonce'
    
    def __init__(self, contents_length, contents_hash, previous_hash):
        assert len(contents_hash) == 256 and len(previous_hash) == 256
        self.contents_length = contents_length
        self.contents_hash = contents_hash or []
        self.previous_hash = previous_hash or []
        
        # when this block started being mined
        self.timestamp

        # this is adjusted to make the hash of this header fall in the valid range
        self.nonce
    


