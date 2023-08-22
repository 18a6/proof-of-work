import hashlib
#create a block class
class Block:
    #constructor the block class
    def __init__(self,data,prevHash):
        self.data=data
        self.prevHash=prevHash
        self.hash=self.calcHash()
    #calculatng the hash
    def calcHash(self):
        hash1 = hashlib.sha256()
        hash1.update(self.data.encodde('utf-8'))
        return hash1.hexdigest()
    #creating the blockchin   
    class BlockChain:
        #constructor for the blockchain
        def __init__(self):
            self.chain =[self.CreateGensisBlock()]
            def CreateGesisBlock(self):
                return Block("Gensis Block", "0")
    #adding a block to the chain
        def addBlock(self,data):
            prevBlock= self.chain[-1]
            NewBlock= Block(data, prevBlock.hash1) 
            self.chain.append(NewBlock)
    #testing
    blockchain = BlockChain()
    BlockChain.addBlock('block 1')
    BlockChain.addBlock('block 2')
    BlockChain.addBlock('block 3')

    print('BLOCKCHAIN XD:')
    for block in BlockChain.chain:
        print('Data: ', block.data)
        print('Previous Hash: ', block.prevHash)
        print('Hash: ', block.hash1)

        