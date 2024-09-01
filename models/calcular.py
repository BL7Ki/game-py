from random import randint

class Calcular:

    # Construtor da classe, inicializa a dificuldade e gera valores e operação aleatórios
    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade  # Define o nível de dificuldade
        self.__valor1: int = self._gerar_valor  # Gera o primeiro valor baseado na dificuldade
        self.__valor2: int = self._gerar_valor  # Gera o segundo valor baseado na dificuldade
        self.__operacao: int = randint(1, 3)  # Gera a operação: 1 = somar, 2 = diminuir, 3 = multiplicar
        self.__resultado: int = self._gerar_resultado  # Calcula o resultado da operação

    # Propriedade para acessar a dificuldade
    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    # Propriedade para acessar o valor 1
    @property
    def valor1(self: object) -> int:
        return self.__valor1

    # Propriedade para acessar o valor 2
    @property
    def valor2(self: object) -> int:
        return self.__valor2

    # Propriedade para acessar a operação
    @property
    def operacao(self: object) -> int:
        return self.__operacao

    # Propriedade para acessar o resultado
    @property
    def resultado(self: object) -> int:
        return self.__resultado

    # Método que retorna uma string representando o objeto
    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'  # Operação de soma
        elif self.operacao == 2:
            op = 'Diminuir'  # Operação de subtração
        elif self.operacao == 3:
            op = 'Multiplicar'  # Operação de multiplicação
        else:
            op = 'Operação desconhecida'  # Caso de erro
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    # Propriedade para gerar valores baseados na dificuldade
    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)  # Dificuldade 1: valores entre 0 e 10
        elif self.dificuldade == 2:
            return randint(0, 100)  # Dificuldade 2: valores entre 0 e 100
        elif self.dificuldade == 3:
            return randint(0, 1000)  # Dificuldade 3: valores entre 0 e 1000
        elif self.dificuldade == 4:
            return randint(0, 10000)  # Dificuldade 4: valores entre 0 e 10000
        else:
            return randint(0, 100000)  # Dificuldade 5 ou superior: valores entre 0 e 100000

    # Propriedade para calcular o resultado da operação
    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:  # Se a operação for somar
            return self.valor1 + self.valor2
        elif self.operacao == 2:  # Se a operação for subtrair
            return self.valor1 - self.valor2
        else:  # Se a operação for multiplicar
            return self.valor1 * self.valor2

    # Propriedade para retornar o símbolo da operação
    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'

    # Método para checar se a resposta do usuário está correta
    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False

        if self.resultado == resposta:  # Verifica se a resposta é igual ao resultado
            print('Resposta correta!')
            certo = True
        else:
            print('Resposta errada!')
        # Mostra a operação realizada e o resultado correto
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    # Método para mostrar a operação ao usuário
    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
