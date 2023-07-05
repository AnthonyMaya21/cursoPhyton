class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre # encapsulamiento "sencillo"
        # self.__nombre = nombre  encapsulamiento doble y menos comun
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        print("Llamando metodo get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        print("Llamando metodo set")

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):  # declaramos metodos
        print(f'Persona: {self._nombre} {self._apellido} {self._edad} ')

if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28)
    persona1.nombre = 'Juan Carlos'
    persona1.apellido = 'Alvarez'
    persona1.edad = 24
    persona1.mostrar_detalle()