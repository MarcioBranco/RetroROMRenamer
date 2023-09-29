import pandas as pd
import os
import ftplib
import json
from env import DATAFRAME_FILE
import sqlite3


def criar_tabela_systems(conexao):
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS systems (
                        id INTEGER PRIMARY KEY,
                        directory TEXT,
                        title TEXT,
                        description TEXT
                    )''')
    conexao.commit()

def criar_tabela_roms(conexao):
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS roms (
                        id INTEGER PRIMARY KEY,
                        romname TEXT,
                        title TEXT,
                        description TEXT,
                        releasedate TEXT,
                        developer TEXT,
                        publisher TEXT,
                        genre TEXT,
                        players TEXT,
                        Capa TEXT,
                        Wheel TEXT,
                        Screenshot TEXT,
                        Marquee TEXT,
                        System INTEGER,
                        FOREIGN KEY (System) REFERENCES systems(id)
                    )''')
    conexao.commit()


def pesquisar_com_like(conexao, tabela, campo_pesquisa, palavra_chave):
    """
    Realiza uma pesquisa em um campo de texto com LIKE e retorna os resultados em uma lista.

    Parâmetros:
    - conexao: A conexão SQLite já aberta.
    - tabela: O nome da tabela onde a pesquisa será realizada.
    - campo_pesquisa: O nome do campo onde a pesquisa será feita.
    - palavra_chave: A palavra-chave para a pesquisa.

    Retorna:
    - Uma lista de registros que correspondem à pesquisa.
    """
    cursor = conexao.cursor()

    # Execute a consulta usando LIKE
    try:
        cursor.execute(f"SELECT * FROM {tabela} WHERE {campo_pesquisa} LIKE ?", (f'%{palavra_chave}%',))

        # Recupere os resultados da consulta
        resultados = cursor.fetchall()

        return resultados
    except:
        return []


def criar_tabela_platform(conexao):
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS platform (
                        id INTEGER PRIMARY KEY,
                        path TEXT,
                        romname TEXT,
                        system INTEGER,
                        FOREIGN KEY (system) REFERENCES systems(id)
                    )''')
    conexao.commit()

def inserir_system(conexao, directory, title, description):
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO systems (directory, title, description) VALUES (?, ?, ?)''', (directory, title, description))
    conexao.commit()

def inserir_rom(conexao, romname, title, description, releasedate, developer, publisher, genre, players, Capa, Wheel, Screenshot, Marquee, System):
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO roms (romname, title, description, releasedate, developer, publisher, genre, players, Capa, Wheel, Screenshot, Marquee, System)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (romname, title, description, releasedate, developer, publisher, genre, players, Capa, Wheel, Screenshot, Marquee, System))
    conexao.commit()

def inserir_platform(conexao, path, romname, system):
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO platform (path, romname, system) VALUES (?, ?, ?)''', (path, romname, system))
    conexao.commit()

def buscar_system_por_id(conexao, system_id):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM systems WHERE id = ?', (system_id,))
    return cursor.fetchone()

def buscar_todos_systems(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM systems')
    return cursor.fetchall()

# Funções semelhantes para roms e platform

def atualizar_system(conexao, system_id, directory, title, description):
    cursor = conexao.cursor()
    cursor.execute('''UPDATE systems SET directory = ?, title = ?, description = ? WHERE id = ?''', (directory, title, description, system_id))
    conexao.commit()

def excluir_system(conexao, system_id):
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM systems WHERE id = ?', (system_id,))
    conexao.commit()



def verifica_df():
    try:
        df = pd.read_pickle(DATAFRAME_FILE)
        lista = df.columns.to_list()
        if not "Romname" in lista:
            print("Erro no Dataframe")
            quit()
        else:
            return True
    except:
        print("Erro no Dataframe")
        quit()

def lista():
    df = pd.read_pickle(DATAFRAME_FILE)
    lista = df.columns.to_list()
    return lista

def rename_column(df,col_ori, col_new):
    df_ret = pd.DataFrame()
    if type(df) != type(df_ret):
        df = pd.read_pickle(DATAFRAME_FILE)
    try:
        df_ret = df.rename(columns={col_ori: col_new})
        return df_ret
    except:
        print(f"Column {col_ori} does not exist.")
        return df

def salva_json(path, content):
    # Salve o mapeamento em um arquivo JSON
    if not "jsons" in path:
        path = os.path.join("jsons",path)

    if os.path.exists(path):
        os.remove(path)
    
    with open(path, 'w') as json_file:
        json.dump(content, json_file, indent=4)

def carrega_json(path):
    content = {}
    if not os.path.exists(path):
        path = os.path.join("jsons",path)

    with open(path, 'r') as arquivo:
        content = json.load(arquivo)
    return content

if __name__ == "__main__":
    pass