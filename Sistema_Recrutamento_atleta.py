import PySimpleGUI as sg # Importa a bibloteca de interface gráfica
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED, WIN_CLOSED, InputText, Window # Importa os métodos da biblioteca
from Atleta import * # Importa todas as classes do módulo "Atleta"


class Sistema_recrutamento_atleta: # Define a classe que administra o sistema

    @staticmethod
    def __janela_imc(): # Janela do IMC
        layout = [
            [sg.Text('Digite seu peso:'), sg.InputText(key='peso')], [sg.Text('Digite sua altura:'), sg.InputText(key='altura')], [sg.Button('Enviar'), sg.Button('Cancelar')]
        ]

        return sg.Window(title='Cadastro do Atleta', layout=layout)
    

    @staticmethod
    def __janela_treino(): # Janela do treino
        layout = [
            [sg.Text('Quantas vezes você treina por semana?'), sg.InputText(key='dias')], [sg.Text('Quantos minutos dura cada treino?'), sg.InputText(key='tempo')], [sg.Button('Enviar'), sg.Button('Cancelar')]
        ]

        return sg.Window(title='Cadastro', layout=layout)


    def window_init(self): # Função que aadministra a dinâmica das janelas
        window = self.__janela_imc() # Atribui a janela à variável "window"


        while True: # Looping da primeira janela
            event, values = window.read() # Leitura da janela

            if event == 'Cancelar' or event == WINDOW_CLOSED: # Verifica se a janela foi fechada
                break

            elif event == 'Enviar': # Verifica se o evento é "ENVIAR"
                imc = Imc_atleta(values['peso'], values['altura'])

                if not imc.classificacao: # Verifica se o atleta passou da primeira etapa

                    window2 = self.__janela_treino() # Atribui a segunda janela à variável "window2"

                    while True: # Looping da segunda janela
                       e, v = window2.read() # Leitura da segunda janela

                       if e == 'Cancelar' or e == WIN_CLOSED: # Verifica se a janela foi fechada
                           break

                       elif e == 'Enviar': 
                           treino = Treino_atleta(v['dias'], v['tempo'])

                           sg.popup(treino.classifica_treino) # Exibe um popup com uma mensagem
                           continue

                    window2.close() # Fecha a segunda janela

                else:
                    sg.popup(imc.classificacao) # Exibe uma mensagem caso o IMC seja alto
        
        window.close() # Fecha a primeira janela


if __name__ == '__main__': # Verifica se o sistema esta no escopo de execução global
    sistema = Sistema_recrutamento_atleta() # Atribui a classe "Sistema_recrutamento_atleta" à variável sistema

    sistema.window_init() # Inicializa o programa
            