"""
Ejercicio propuesto (POO)

Crear una clase Cajero Automatico que permita simular las operaciones básicas
de un cajero automático, como consultar saldo, depositar dinero, retirar dinero
y mostrar historial de transacciones.

Requisitos:
- Deberá tener los métodos de: consultar_saldo, depositar(monto), retirar(monto), mostrar_historial()
- Inicializa el cajero con los atributos de saldo inicial y un historial vacío (lista).
- En el método depositar() debe indicar que "El monto a depositar debe ser mayor a cero"
si ingresa un monto negativo
- Si se logra realizar el depósito mostrará un mensaje de "Depósito exitoso de S/ 'monto'"

Tomar en cuenta lo siguiente:
- historial será un tipo de datos list para que puedan ingresar todo el historial
- Recorrer el historial con un for para poder mostrar el historial completo en el método
mostrar_historial()
- Si self.historial está vacío indicar que "no hay transacciones registradas"
- Si en el método retirar(monto) el monto es mayor a self.saldo indicar que hay saldo insuficiente
para poder realizar el retiro
- Cada vez que e haga un depósito se irá actualizando el self.historial (append(Depósito: S/ {monto}))

"""
class CajeroAutomatico:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.historial = []  # Historial vacío inicialmente

    def consultar_saldo(self):
        return f"Saldo actual: S/ {self.saldo:.2f}"

    def depositar(self, monto):
        if monto <= 0:
            return "El monto a depositar debe ser mayor a cero."
        else:
            self.saldo += monto
            self.historial.append(f"Depósito: S/ {monto:.2f}")
            return f"Depósito exitoso de S/ {monto:.2f}"

    def retirar(self, monto):
        if monto > self.saldo:
            return "Saldo insuficiente para poder realizar el retiro."
        elif monto <= 0:
            return "El monto a retirar debe ser mayor a cero."
        else:
            self.saldo -= monto
            self.historial.append(f"Retiro: S/ {monto:.2f}")
            return f"Retiro exitoso de S/ {monto:.2f}"

    def mostrar_historial(self):
        if not self.historial:
            return "No hay transacciones registradas."
        historial_completo = "Historial de transacciones:"
        for transaccion in self.historial:
            historial_completo += f"\n{transaccion}"
        return historial_completo

# Ejemplo de uso
cajero = CajeroAutomatico(saldo_inicial=500)

# Operaciones simuladas
print(cajero.consultar_saldo())        # Consulta saldo
print(cajero.depositar(200))          # Depósito de S/ 200
print(cajero.retirar(100))            # Retiro de S/ 100
print(cajero.mostrar_historial())     # Muestra el historial de transacciones