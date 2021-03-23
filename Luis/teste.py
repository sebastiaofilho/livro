from Estudo1 import Conta
from cliente import Cliente

conta1 = Conta(123, 'tião', 1000, 2000)
conta2 = Conta(111, 'Luis', 300, 3000)
conta1.sacar(250)
conta1.transferir(200, conta2)
conta1.extrato(123)
conta2.extrato(111)
conta1.set__limite(10000)
print(Cliente)
conta1.get__limite

