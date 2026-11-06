# Análise do login em SQLite

## Contexto

Laboratório de Vinícius Botelho, executado pelo terminal no Windows com dados fictícios e banco SQLite em memória. Não há servidor web, serviço publicado ou acesso a um banco externo. Os arquivos enviados foram preservados nesta revisão.

## Achado e evidência

Em `laboratorio/sql-injection/app_vulneravel.py`, a função `autenticar()` insere as entradas diretamente em uma f-string SQL. O print [01-login-vulneravel.png](../evidencias/01-login-vulneravel.png) registra acesso permitido com o usuário `aluno' -- ` e uma senha incorreta.

O apóstrofo fecha o valor do usuário; os dois hífens comentam o restante da instrução. A comparação da senha deixa de participar da decisão. Já o apóstrofo isolado provoca erro de sintaxe na versão vulnerável, sem demonstrar por si só um login indevido.

O programa apenas imprime uma decisão de acesso: não abre sessão, área restrita ou funcionalidade administrativa. A conclusão observada é o desvio dessa decisão, não comprometimento do Windows ou de outros dados.

## Classificação e risco

O padrão de construção insegura corresponde à [CWE-89](https://cwe.mitre.org/data/definitions/89.html). Não foi atribuído CVE ao exemplo.

| Dimensão | Avaliação deste cenário |
|---|---|
| Impacto observado | Decisão de autenticação incorreta para uma conta fictícia |
| Impacto no ambiente | Baixo: banco descartável, sem dados reais ou funções protegidas posteriores |
| Probabilidade de repetição local | Alta nas condições do teste: entrada simples e resultado reproduzível |
| Exposição remota | Ausente no programa fornecido; não há um serviço escutando na rede |
| Severidade técnica | Alta para o controle de autenticação, pois sua condição de senha é contornada; classificação qualitativa restrita a esse controle |
| Prioridade | Corrigir antes de reutilizar o padrão em qualquer aplicação; guardar a versão insegura apenas para comparação no laboratório |

Esses rótulos seguem a convenção didática de [security-basics.md](../agent/knowledge/security-basics.md). Não foi calculado CVSS nem estimado risco de um sistema em produção. O alcance em confidencialidade, integridade e disponibilidade de uma aplicação real dependeria do que ela protege e das permissões do banco.

## Relação com MITRE ATT&CK

A [T1190 — Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) seria pertinente a um cenário em que uma aplicação pública vulnerável fosse explorada para acesso inicial. Este laboratório não reproduz essas condições. A referência é contextual, não uma afirmação de que T1190 foi executada aqui.

## Correção e validação

No `app.py`, a consulta é fixa, com dois placeholders `?`. Os valores são entregues separadamente a `cursor.execute(consulta, (usuario, senha))`. Isso segue o mecanismo de [parâmetros do sqlite3](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries).

O print [02-login-corrigido.png](../evidencias/02-login-corrigido.png) mostra três execuções feitas pelo autor: credenciais corretas aceitas, senha incorreta negada e a mesma entrada manipulada negada.

A suíte `test_login.py` compara seis casos em cada versão. Ela espera que a versão vulnerável ainda demonstre o desvio; passar nesses testes não torna essa versão segura. O registro da execução de revisão está em [resultados-testes.txt](../evidencias/resultados-testes.txt), com o ambiente utilizado. É uma execução separada dos prints do Windows.

## Limitações restantes

As duas versões guardam a senha fictícia em texto simples e usam `input()`, que deixa a digitação visível. A versão vulnerável também imprime a senha dentro da consulta; a corrigida imprime apenas placeholders. Os detalhes de erro são exibidos para estudo. Não há armazenamento seguro de senhas, sessões, autorização ou controles contra tentativas repetidas.

A consulta de autenticação foi corrigida; este programa não representa um login pronto para produção. A [orientação da OWASP sobre senhas](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) é uma referência para uma evolução posterior, fora desta comparação.
