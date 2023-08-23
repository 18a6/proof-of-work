class BlockHeader:
    def __init__(self, blockhash, timestamp, data, prevhash):
        self.blockhash = blockhash
        self.timestamp = timestamp
        self.data = data
        self.prevhash = prevhash

block_hash = "0xd7fdfbeaf23834313e3c976e75feca61e95af38f00588a75cb3911073516e4f7"
timestamp = "2023-08-23 1:00:00"
data = "pow exercise from solidity study group"
prev_hash = "0xd7fdfbeaf23834313e3c976e75feca61e95af38f00588a75cb3911073516e4f7"

block_header = BlockHeader(block_hash, timestamp, data, prev_hash)

print("Block Hash:", block_header.blockhash)
print("Block timestamp:", block_header.timestamp)
print("Block data:", block_header.data)
print("Block previous Hash:", block_header.prevhash)
