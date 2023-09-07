import hashlib
import time
import random

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
        

    def transferencia(self):
        if self.monto <= self.remitente.saldo:
            self.destinatario.saldo += self.monto
            self.remitente.saldo -= self.monto
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

class Block:
    def __init__(self, transactions, previous_hash, nonce, optional_data=None):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = time.time()
        self.merkle_tree = MerkleTree([str(trx.__dict__) for trx in self.transactions])

    def calculate_hash(self):
        data = str(self.merkle_tree.root_hash) + self.previous_hash + str(self.nonce) 
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.mining_reward = 0.1  # Recompensa para el minero por cada bloque minado
        self.pending_transactions = []

    def create_genesis_block(self):
        # Transacción Coinbase en el bloque génesis (sin recompensa para el minero)
        coinbase_transaction = Transaction(usuario_a=None, usuario_b=None, monto=1)
        return Block(transactions=[coinbase_transaction], previous_hash="0", nonce=0)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().calculate_hash()
        self.chain.append(new_block)

    def mine_block(self, miner_address):
        transactions = self.get_pending_transactions()[:4]  # Limitar a 4 transacciones por bloque
        previous_hash = self.get_last_block().calculate_hash()
        nonce = self.proof_of_work(previous_hash, transactions, miner_address)
        
        # Crear una transacción de recompensa para el minero
        miner_reward_transaction = Transaction(usuario_a=None, usuario_b=miner_address, monto=self.mining_reward)
        transactions.append(miner_reward_transaction)

        new_block = Block(transactions, previous_hash, nonce)
        self.add_block(new_block)
        print("Bloque minado con éxito.")
        print(f"Recompensa para el minero: {self.mining_reward}")
        return new_block

    def proof_of_work(self, previous_hash, transactions, miner_address):
        target_prefix = "0000"  # Dificultad del PoW (número de ceros iniciales requeridos)
        nonce = 0
        while True:
            data = "".join([str(trx.__dict__) for trx in transactions]) + previous_hash + str(nonce)
            hash_result = hashlib.sha256(data.encode('utf-8')).hexdigest()
            if hash_result[:len(target_prefix)] == target_prefix:
                return nonce
            nonce += 1

    def get_pending_transactions(self):
        # Retorna las transacciones pendientes en el mempool
        return self.pending_transactions

# Crear una lista de billeteras con saldos aleatorios
wallets = [Wallet(id=i, saldo=random.randint(10, 100)) for i in range(1, 11)]

# Algunas billeteras minarán bloques
mining_wallets = wallets[:5]

# Crear una instancia de Blockchain
blockchain = Blockchain()

# Simular transacciones entre billeteras
for _ in range(20):
    sender = random.choice(wallets)
    receiver = random.choice(wallets)
    while receiver == sender:
        receiver = random.choice(wallets)
    amount = random.randint(1, sender.saldo)
    transaction = Transaction(usuario_a=receiver, usuario_b=sender, monto=amount)
    transaction.transferencia()
    blockchain.pending_transactions.append(transaction)

    # Verificar si hay 4 transacciones pendientes para iniciar la minería
    if len(blockchain.pending_transactions) >= 4:
        # Simular la minería de bloques por una billetera minera
        miner_wallet = random.choice(mining_wallets)
        blockchain.mine_block(miner_wallet.id)
        # Limpiar las transacciones minadas de la lista de transacciones pendientes
        blockchain.pending_transactions = blockchain.pending_transactions[4:]

# Imprimir la información de la cadena de bloques
print("Blockchain:")
for i, block in enumerate(blockchain.chain):
    print(f"Block {i+1}")
    print("Block Hash:", block.calculate_hash())
    print("Previous Hash:", block.previous_hash)
    print("Transactions:", [tx.__dict__ for tx in block.transactions])
    print("Nonce:", block.nonce)
    print("Tiempo de creación:", time.ctime(block.timestamp))
   
