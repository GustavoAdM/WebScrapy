from PyQt6 import uic, QtWidgets
from os import getcwd
import sys
from bancodados import BancodeDados


class RenderApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(RenderApp, self).__init__()
        caminho = getcwd()
        uic.loadUi(f'{caminho}/Interface/interface.ui', self)
        self.findButtons()
        self.controle()
        self.EventoButtons()
        self.addListaFilme()
        self.show()

    def findButtons(self):  # Localizar os Botoes disponivel na tela
        self.rad_acao = self.findChild(QtWidgets.QRadioButton, 'rad_acao')
        self.rad_aventura = self.findChild(
            QtWidgets.QRadioButton, 'rad_aventura')
        self.rad_biografia = self.findChild(
            QtWidgets.QRadioButton, 'rad_biografia')
        self.rad_comedia = self.findChild(
            QtWidgets.QRadioButton, 'rad_comedia')
        self.rad_drama = self.findChild(QtWidgets.QRadioButton, 'rad_drama')
        self.rad_scifi = self.findChild(QtWidgets.QRadioButton, 'rad_scifi')
        self.consultar = self.findChild(QtWidgets.QPushButton, 'consultar')
        self.line_genero = self.findChild(QtWidgets.QLineEdit, 'line_genero')
        self.lista_filme = self.findChild(QtWidgets.QListWidget, 'lista_filme')

    def EventoButtons(self):  # Realizar os eventos quanto selecionado os botoes
        self.rad_acao.clicked.connect(self.eventos)
        self.rad_aventura.clicked.connect(self.eventos)
        self.rad_biografia.clicked.connect(self.eventos)
        self.rad_comedia.clicked.connect(self.eventos)
        self.rad_scifi.clicked.connect(self.eventos)
        self.rad_drama.clicked.connect(self.eventos)
        self.consultar.clicked.connect(self.addListaFilme)

    def controle(self):
        self.genero = None

    # Evento que cada botão ao selecionar

    def eventos(self):
        self.lista_filme.clear()
        if self.rad_acao.isChecked():
            self.line_genero.setText('Ação')
            self.genero = 'Action'

        elif self.rad_aventura.isChecked():
            self.line_genero.setText('Aventura')
            self.genero = 'Adventure'

        elif self.rad_biografia.isChecked():
            self.line_genero.setText('Biografia')
            self.genero = 'Biography'

        elif self.rad_drama.isChecked():
            self.line_genero.setText('Dramas')
            self.genero = 'Drama'

        elif self.rad_scifi.isChecked():
            self.line_genero.setText('Sci-Fi')
            self.genero = 'Sci-Fi'

        elif self.rad_comedia.isChecked():
            self.line_genero.setText('Comédia')
            self.genero = 'Comedy'

    def addListaFilme(self):
        # Retorna uma lista com tuplas [(nomegenero, nomefilme)]
        
        if self.genero != None:
            con_banco = BancodeDados().consulta(self.genero)

            for qnt_filme in range(0, len(con_banco)):
                # Alinhas as informações pegando o total 45 - tamnho string
                # -------------------------------------------
                carkfilme = 45 - len(con_banco[qnt_filme][0])
                carkano = 10 - len(con_banco[qnt_filme][1])
                # --------------------------------------------
                # motras as informações, tamnho nomefilme + qunatidade espaço = 45
                self.lista_filme.addItem(
                    f'{con_banco[qnt_filme][0]}{" " * carkfilme}  ||  {con_banco[qnt_filme][1]}{" " * carkano}  ||  {con_banco[qnt_filme][2]}')


app = QtWidgets.QApplication(sys.argv)
janela = RenderApp()
app.exec()
