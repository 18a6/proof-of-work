import hashlib
import sys

class BlockChain:
    def __init__(self):
        self.blocks = []


class Block:
    def __init__(self, data, previous_hash):
        self.nonce = 0
        self.data = data
        self.previous_hash = previous_hash

    
    def mine(block, target_hash):
        blockChain = BlockChain()

        for i in range(sys.maxsize):
            block.nonce = i

            #creating an object for SHA-256
            sha256 = hashlib.sha256()

            #update the object with the bytes of the variables
            sha256.update(block.nonce.to_bytes(32, byteorder='big'))
            sha256.update(block.previous_hash)
            sha256.update(block.contents_hash)

            #calculate the block's hash
            blockHash = sha256.hexdigest()


            #compare the block's hash to the target hash
            if(blockHash < target_hash):
                #print the nonce
                print(f"The block\'s hash is:{block.nonce}")
                
                #add the block to the blockchain
                blockChain.append(block)
                break



