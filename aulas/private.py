class MyClass:

    def registry(self, ) -> None:
        print('Start process')
        self.__verify()  # Aqui dentro de um método da classe funciona
        self.__verify_registry()
        self.__insert_data()

    def __verify(self) -> None:  # __ = método PRIVADO
        print('verify data')

    def __verify_registry(self) -> None:  # __ = método PRIVADO
        print('verify registry')

    def __insert_data(self) -> None:  # __ = método PRIVADO
        print('insert in DB')


obj = MyClass()
obj.registry()  # Um método público que executa métodos privados DENTRO da classe. Métodos que executam uma tarefa cada

# obj.__verify()  # Só funciona DENTRO da classe e não fora assim
