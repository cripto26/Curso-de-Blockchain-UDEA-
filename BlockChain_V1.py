import hashlib
import time

class Block:
    def __init__(self, transactions, previous_hash, nonce, optional_data=None):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.optional_data = optional_data if optional_data else {}
        self.timestamp = time.time()

    def calculate_hash(self):
        transaction_data = [str(trx.__dict__) for trx in self.transactions]
        data = "".join(transaction_data) + self.previous_hash + str(self.nonce) + str(self.optional_data)
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(transactions=[], previous_hash="0", nonce=0)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().calculate_hash()
        self.chain.append(new_block)

class Wallet:
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo

    def sumar_saldo(self, monto):
        self.saldo += monto

    def resta_saldo(self, monto):
        self.saldo -= monto

class Transaction:
    def __init__(self, usuario_a, usuario_b, monto):
        self.destinatario = usuario_a
        self.remitente = usuario_b
        self.monto = monto

    def mostrar_saldos(self):
        print("Saldo en cuenta origen:", self.remitente.saldo)
        print("Saldo en cuenta destino:", self.destinatario.saldo)

    def transferencia(self):
        if self.monto <= self.remitente.saldo:
            self.destinatario.saldo -= self.monto
            self.remitente.saldo += self.monto
            
        else:
            print("Saldo insuficiente para realizar la transferencia.")

class MerkleTree:
    def __init__(self, data_list):
        if len(data_list) == 1:
            self.root_hash = self.calculate_hash(data_list[0])
        else:
            new_data_list = []

            for i in range(0, len(data_list) - 1, 2):
                combined_data = data_list[i] + data_list[i + 1]
                hash_combined = self.calculate_hash(combined_data)
                new_data_list.append(hash_combined)

            if len(data_list) % 2 != 0:
                new_data_list.append(data_list[-1])  
            self.root_hash = self.calculate_hash(''.join(new_data_list))

    def calculate_hash(self, data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()



# Ejemplo de uso
if __name__ == "__main__":
    blockchain = Blockchain()

    wallet_a = Wallet(id=1, saldo=100)
    wallet_b = Wallet(id=2, saldo=50)

    transaction = Transaction(usuario_a=wallet_a, usuario_b=wallet_b, monto=30)
    transaction.transferencia()
    transaction.mostrar_saldos()

    transactions = [transaction]
    merkle_tree = MerkleTree([f"{tx.remitente.id}{tx.destinatario.id}{tx.monto}" for tx in transactions])
    
    new_block = Block(transactions=transactions, previous_hash=blockchain.get_last_block().calculate_hash(), nonce=0, optional_data={"id_bloque": 1})
    blockchain.add_block(new_block)

    print("Blockchain:")
    for i, block in enumerate(blockchain.chain):
        print(f"Block {i+1}")
        print("Block Hash:", block.calculate_hash())
        print("Previous Hash:", block.previous_hash)
        print("Transactions:", [tx.__dict__ for tx in block.transactions])
        print("Nonce:", block.nonce)
        print("Optional Data:", block.optional_data)
        print("=" * 50)