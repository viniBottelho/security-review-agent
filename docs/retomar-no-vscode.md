# Retomar o projeto no Windows

1. Guardar uma cópia da pasta atual antes de substituir arquivos.
2. Extrair o ZIP atualizado. Ele contém uma pasta `dio-agent`.
3. Copiar o conteúdo dessa pasta para a pasta `dio-agent` que você já usa, aceitando a substituição dos arquivos correspondentes. Não criar uma pasta `dio-agent` dentro da outra. O pacote não contém `.git`; a pasta Git que já está no seu computador deve permanecer.
4. Abrir essa raiz no VS Code e conferir a presença de `AGENTS.md`, `CLAUDE.md`, `skills/vulnerability-analysis/` e `evidencias/`.
5. Executar no terminal da raiz:

```powershell
py laboratorio/sql-injection/test_login.py
```

O resultado esperado é `Ran 12 tests` seguido de `OK`. Os dois programas originais foram preservados; a suíte adicionada compara seus comportamentos.

## Carregamento no Claude Code

Quando o Claude Code estiver disponível, enviar:

```text
Atualizei os arquivos deste projeto. Leia o CLAUDE.md, o AGENTS.md,
o agent/persona.md e a skill indicada na tabela para análise de
vulnerabilidades. Informe os caminhos lidos e resuma o processo.
Não execute comandos nem altere arquivos nesta verificação.
```

Essa verificação de carregamento não substitui os cenários de [validação do agente](validacao-agente.md). Execute-os depois e registre respostas reais. Uma sessão pausada pelas proteções do harness continua sendo uma limitação de execução; não use troca de modelo ou reformulação para contorná-la.

## Antes de enviar à DIO

- Registrar os cenários do agente e atualizar o status no README e no roteiro de validação.
- Conferir o conteúdo dos prints e manter somente dados fictícios.
- Repositório de entrega: [viniBottelho/security-review-agent](https://github.com/viniBottelho/security-review-agent). A cópia local original veio da base da DIO; conferir o remoto antes de enviar novas alterações.
- Conferir o remoto com `git remote -v` antes de publicar. Não enviar alterações ao repositório da DIO.
- Enviar à DIO o link da raiz do repositório acima, não o link de um arquivo individual.

O pacote contém os testes Python e os quatro cenários de conversa documentados, com as ressalvas observadas. Os arquivos de entrega ficam no repositório público indicado acima. A revalidação independente dos cenários 1 e 2 é uma melhoria de avaliação ainda não comprovada; não a apresentar como concluída.

Se já executou a suíte no Windows e nenhuma versão Python mudou, não é necessário repetir os 12 testes apenas por uma atualização da documentação.
