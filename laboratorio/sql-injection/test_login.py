import os
from pathlib import Path
import subprocess
import sys
import unittest


PASTA = Path(__file__).resolve().parent
CASOS = (
    ("credenciais_corretas", "aluno", "AulaDIO_2026!", True, True, False),
    ("senha_incorreta", "aluno", "senha-incorreta", False, False, False),
    ("usuario_inexistente", "inexistente", "AulaDIO_2026!", False, False, False),
    ("apostrofo_isolado", "'", "qualquer", False, False, True),
    ("entrada_no_usuario", "aluno' -- ", "senha-incorreta", True, False, False),
    ("entrada_na_senha", "aluno", "' OR '1'='1", True, False, False),
)


class LoginTerminalTests(unittest.TestCase):
    pass


def criar_teste(arquivo, usuario, senha, permitido, erro_sql):
    def teste(self):
        ambiente = dict(os.environ, PYTHONIOENCODING="utf-8")
        processo = subprocess.run(
            [sys.executable, str(PASTA / arquivo)],
            input=f"{usuario}\n{senha}\n",
            text=True,
            encoding="utf-8",
            capture_output=True,
            timeout=10,
            env=ambiente,
        )
        self.assertEqual(processo.returncode, 0, processo.stderr)
        self.assertEqual(processo.stderr, "")
        esperado = "Acesso permitido" if permitido else "Acesso negado"
        self.assertEqual(processo.stdout.strip().splitlines()[-1], esperado)
        self.assertEqual("Erro no SQLite:" in processo.stdout, erro_sql)
        if arquivo == "app.py":
            self.assertNotIn(senha, processo.stdout)
    return teste


for indice, caso in enumerate(CASOS, start=1):
    nome, usuario, senha, vulneravel, corrigido, erro = caso
    for arquivo, esperado, erro_sql in (
        ("app_vulneravel.py", vulneravel, erro),
        ("app.py", corrigido, False),
    ):
        versao = "vulneravel" if arquivo == "app_vulneravel.py" else "corrigida"
        setattr(
            LoginTerminalTests,
            f"test_{indice:02d}_{versao}_{nome}",
            criar_teste(arquivo, usuario, senha, esperado, erro_sql),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
