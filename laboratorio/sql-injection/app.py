import sqlite3


def criar_banco():
    conexao = sqlite3.connect(":memory:")
    cursor = conexao.cursor()
    cursor.execute(
        "CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT NOT NULL UNIQUE, senha TEXT NOT NULL)"
    )
    cursor.execute(
        "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
        ("aluno", "AulaDIO_2026!"),
    )
    conexao.commit()
    return conexao


def autenticar(conexao, usuario, senha):
    consulta = "SELECT id, usuario FROM usuarios WHERE usuario = ? AND senha = ?"
    print(f"Consulta executada: {consulta}")
    cursor = conexao.cursor()
    cursor.execute(consulta, (usuario, senha))
    return cursor.fetchone()


def main():
    print("Laboratório local de SQL Injection — use apenas dados fictícios")
    conexao = None
    try:
        conexao = criar_banco()
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        resultado = autenticar(conexao, usuario, senha)
        if resultado:
            print("Acesso permitido")
        else:
            print("Acesso negado")
    except sqlite3.Error as erro:
        print(f"Erro no SQLite: {erro}")
        print("Acesso negado")
    finally:
        if conexao is not None:
            conexao.close()


if __name__ == "__main__":
    main()
