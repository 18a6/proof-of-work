import time
import hashlib

class BlockHeader:
    def __init__(self, timestamp, data, prevhash):
        self.timestamp = timestamp
        self.data = data
        self.prevhash = prevhash
        self.blockhash = self.calculate_hash()

    def calculate_hash(self):
        value = self.timestamp + self.data + self.prevhash
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

current_timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

data = "pow exercise from solidity study group"
prev_hash = "0xd7fdfbeaf23834313e3c976e75feca61e95af38f00588a75cb3911073516e4f7"

block_header = BlockHeader(current_timestamp, data, prev_hash)

print("Block Hash:", block_header.blockhash)
print("Block timestamp:", block_header.timestamp)
print("Block data:", block_header.data)
print("Block previous Hash:", block_header.prevhash)
