import datetime
import hashlib

class Transaction():
    def __init__(self, val:float, send:str, rec:str):
        self.val = val
        self.send = send
        self.rec = rec
    def __repr__(self):
        return(f"Value: {self.val}, From: {self.send}, To:{self.rec}")

class Block():
    def __init__(self, transaction:Transaction, prev_hash:float):
        self.transaction = transaction
        self.time_stamp = datetime.datetime.now()

        self.nonce = 0
        self.hash =  None
        self.prev_hash = prev_hash

    def gen_hash(self):
        serialised = f"{self.transaction}, {self.prev_hash}, {self.time_stamp}"
        hash_object = hashlib.sha256(serialised.encode())
        hex_digest = hash_object.hexdigest()

        self.hash = hex_digest
        return (hex_digest)

    def __repr__(self):
        output=""

        output += "##################################\n"
        output += f"Block(T: {self.transaction})\n"
        output += f"Prev_hash: {self.prev_hash[0:5]}...{self.prev_hash[-5:]}\n"
        output += f"Hash: {self.hash[0:5]}...{self.hash[-5:]}\n"
        output += "##################################"

        return(output)

class Network():
    def __init__(self):
        self.chain = []

        self.genesis_block = Block(Transaction(0, "", ""), "GodBlock")
        self.genesis_block.gen_hash()
        self.chain.append(self.genesis_block)
    
    def add_block(self, transaction:Transaction):
        # Get prev hash
        prev_hash = self.chain[len(self.chain)-1].hash
        b = Block(transaction, prev_hash)

        # proof = proof_of_work(block)

        b.gen_hash()
        self.chain.append(b)
        return

    def print_ledger(self):
        ledger = {}
        for block in self.chain:
            s = block.transaction.send
            r = block.transaction.rec
            v = block.transaction.val

            ledger[s] = ledger.get(s, 0) - v
            ledger[r] = ledger.get(r, 0) + v

        print(f"Ledger:\n{ledger}")
        return(ledger)

    def val_chain(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i-1] 

            if curr.gen_hash() != curr.hash:
                print(f"hash of current block has changed. {curr}")
                return False
            if prev.gen_hash() != curr.prev_hash:
                print(f"prev hash has changed. {i}")
                return False
        return True

    def print_blocks(self):
        for block in self.chain:
            print(f"{block}")
        return


