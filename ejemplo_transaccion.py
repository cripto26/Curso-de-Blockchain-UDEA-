class Banco:
    def __init__(self):
        self.saldo_cuenta_origen = 1000
        self.saldo_cuenta_destino = 500

    def mostrar_saldos(self):
        print("Saldo en cuenta origen:", self.saldo_cuenta_origen)
        print("Saldo en cuenta destino:", self.saldo_cuenta_destino)

    def transferencia(self, monto_transferir):
        if monto_transferir <= self.saldo_cuenta_origen:
            self.saldo_cuenta_origen -= monto_transferir
            self.saldo_cuenta_destino += monto_transferir
            print("Transferencia exitosa.")
            self.mostrar_saldos()
        else:
            print("Saldo insuficiente para realizar la transferencia.")


banco = Banco()

print("Saldos iniciales:")
banco.mostrar_saldos()

monto = float(input("Ingrese el monto a transferir: "))
banco.transferencia(monto)


