import sqlite3 as sq
import os


class BancodeDados:

    caminho_base = f'{os.getcwd()}/BancoDados'

    def __init__(self, caminho_base=caminho_base):
        self.banco = sq.connect(f'{caminho_base}/bancofilmes.db')
        self.cursor = self.banco.cursor()

    def inserirdados(self, filme, Ano, rating, genero):
        self.cursor.execute(
            f'INSERT INTO filmes VALUES("{filme}", "{Ano}", "{rating}", "{genero}")')
        self.banco.commit()

    def excluirdados(self):
        self.cursor.execute("DELETE FROM filmes")
        self.banco.commit()

    def consulta(self, generop):
        pesquisa = self.cursor.execute(
            f'SELECT * FROM filmes f WHERE f.generos LIKE "%{generop}%"')
        return pesquisa.fetchall()
