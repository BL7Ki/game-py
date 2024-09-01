from models.calcular import Calcular  # Importa a classe Calcular do módulo models

# lembrando que pra executar o objeto tem que apertar o botao direito aqui em game porque nele tem a main

# Função principal que inicializa o jogo
def main() -> None:
    pontos: int = 0  # Inicializa a pontuação com 0
    jogar(pontos)  # Chama a função jogar passando a pontuação inicial

# Função que contém a lógica do jogo
def jogar(pontos: int) -> None:
    # Solicita ao usuário que informe o nível de dificuldade desejado
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))

    # Cria um objeto da classe Calcular com o nível de dificuldade escolhido
    calc: Calcular = Calcular(dificuldade)

    # Exibe a operação que o usuário deve resolver
    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    # Recebe a resposta do usuário
    resultado: int = int(input())

    # Verifica se a resposta está correta
    if calc.checar_resultado(resultado):
        pontos += 1  # Incrementa a pontuação se a resposta estiver correta
        print(f'Você tem {pontos} ponto(s).')

    # Pergunta ao usuário se deseja continuar jogando
    continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não] '))

    # Se o usuário quiser continuar, chama a função jogar novamente com a pontuação atualizada
    if continuar:
        jogar(pontos)
    else:
        # Se o usuário não quiser continuar, exibe a pontuação final e encerra o jogo
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até a próxima!')

# Verifica se o script está sendo executado diretamente (e não importado como módulo)
if __name__ == '__main__':
    main()  # Chama a função principal para iniciar o jogo
