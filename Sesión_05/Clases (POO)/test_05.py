"""
    Programación Orientada a Objetos
    Participación

Requerimientos:
    - Crear una Clase Alumno
    - Debe tener un atributo de nacionalidad con el valor "Peruano"
    - Tendrá 3 notas, la nota inicial de c/u será de 0
    - Crear un método que indicará el promedio del alumno
    - Crear un método que indicará si el alumno está aprobado o no de acuerdo a su promedio
    - Las notas serán pasadas por parámetro al momento de instanciar la clase
    - Crear un método para obtener el nombre y distrito de residencia del alumno
    - Instanciar la clase para el caso de 2 alumnos necesariamente
"""


class Alumno:
    # Atributo de clase
    nacionalidad = "Peruano"

    def __init__(self, nota1=0, nota2=0, nota3=0, nombre="", distrito=""):
        # Atributos de instancia
        self.notas = [nota1, nota2, nota3]
        self.nombre = nombre
        self.distrito = distrito

    # Método para calcular el promedio del alumno
    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    # Método para verificar si el alumno está aprobado
    def esta_aprobado(self):
        promedio = self.calcular_promedio()
        return promedio >= 11  # Se considera aprobado si el promedio es igual o mayor a 11

    # Método para obtener el nombre y distrito de residencia del alumno
    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Distrito: {self.distrito}"


# Instanciar la clase para 2 alumnos
alumno1 = Alumno(nota1=15, nota2=18, nota3=13, nombre="Juan Pérez", distrito="Lima")
alumno2 = Alumno(nota1=5, nota2=7, nota3=2, nombre="Ana López", distrito="Cusco")

# Mostrar información y resultados para cada alumno
print(f"Alumno 1 ({alumno1.nacionalidad}):")
print(alumno1.obtener_informacion())
print(f"Promedio: {alumno1.calcular_promedio()}")
print(f"¿Está aprobado? {'Sí' if alumno1.esta_aprobado() else 'No'}")

print(f"\nAlumno 2 ({alumno2.nacionalidad}):")
print(alumno2.obtener_informacion())
print(f"Promedio: {alumno2.calcular_promedio()}")
print(f"¿Está aprobado? {'Sí' if alumno2.esta_aprobado() else 'No'}")

