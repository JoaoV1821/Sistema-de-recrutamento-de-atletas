class Imc_atleta: # Classe que trata o IMC do candidato
    def __init__(self, peso, altura):
        self.__classificacao = self.__classifica_imc(float(peso), float(altura)) # Classificação do IMC 
    

    @staticmethod
    def __classifica_imc(peso, altura): # Retorna uma mensagem se o imc for inadequado senão, retorna um valor booleano
        if peso / (altura**2) > 24.9:
            return 'Volte aqui depois de regulamentar o seu porte físico'
        else: 
            return False
    

    @property
    def classificacao(self): # Getter da classificação
        return self.__classificacao


class Treino_atleta: # Classe que trata do treino do candidato
    def __init__(self, dias_de_treino, minuto_treino):
        self.__classifica_treino = self.__calcula_total(float(dias_de_treino), float(minuto_treino)) # Calssificação do treino
    

    @staticmethod
    def __calcula_total(dias_de_treino, minuto_treino): # Retorna uma mensagem de acordo com o número de minutos / treino
        if dias_de_treino * minuto_treino < 300:
            return 'Muito obrigado, agradecemos a sua participação!'
        else:
            return 'Parabéns, você passou em todos os nossos testes, agora você fará um teste pessoal em nossa sede,favor comparecer ao endereço: Rua dos Atletas, 43, Bairro do Futebol. Nos vemos lá!'
    

    @property
    def classifica_treino(self): # Getter da classificação do treino
        return self.__classifica_treino
