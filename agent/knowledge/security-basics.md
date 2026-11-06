# Fundamentos para a análise de segurança

## Conceitos usados neste projeto

| Conceito | Significado | Exemplo no laboratório |
|---|---|---|
| Vulnerabilidade | Fraqueza que pode produzir um efeito indesejado | Entrada concatenada na consulta de login |
| Ameaça | Agente, evento ou circunstância capaz de causar dano | Uso de uma entrada preparada para alterar a consulta |
| Risco | Possibilidade de dano no contexto do ativo, considerando impacto e probabilidade | Depende de onde o login é usado, de quem o alcança e do que protege |
| Controle | Medida que reduz a probabilidade ou o impacto | Consulta parametrizada |
| Evidência | Registro verificável que sustenta uma afirmação | Código, comando executado e saída do terminal |

Uma vulnerabilidade não é prova de que houve um incidente. Um teste bem-sucedido demonstra um comportamento dentro das condições testadas.

## Confidencialidade, integridade e disponibilidade

- **Confidencialidade:** limitar o acesso à informação às pessoas autorizadas.
- **Integridade:** impedir ou detectar alterações indevidas nos dados.
- **Disponibilidade:** manter sistemas e informações acessíveis quando necessários.

No login de terminal, o efeito observado é a decisão incorreta de autenticação. Não há funcionalidade posterior que demonstre leitura de registros privados, alteração de dados ou interrupção de um serviço. Esses impactos exigiriam outro cenário e evidências próprias.

## Avaliação qualitativa

Os critérios abaixo são uma convenção didática deste projeto, não uma escala oficial nem um cálculo CVSS. Sempre justificar a escolha e registrar incertezas.

| Dimensão | Como avaliar |
|---|---|
| Impacto | Baixo quando restrito a dados fictícios e efeito reversível; moderado quando limitado, mas relevante para dados ou operação; alto quando há comprometimento amplo de dados sensíveis, privilégios ou serviço essencial |
| Probabilidade | Baixa quando o acesso é restrito e depende de condições difíceis; moderada quando depende de condições plausíveis; alta quando o ativo é alcançável e a exploração é simples nas condições observadas |
| Severidade técnica | Baixa para efeito limitado sem romper controle relevante; moderada para violação restrita com pré-requisitos; alta para ruptura direta de controle essencial, como autenticação. Informar as condições e não inferir impacto posterior inexistente |
| Prioridade | Corrigir antes de ampliar exposição quando a falha rompe um controle essencial; planejar correções e retestes para os demais casos, conforme dependências e impacto |

Não multiplicar rótulos nem atribuir números arbitrários. Quando a exposição ou o impacto forem desconhecidos, classificar a dimensão como indeterminada. A classificação do laboratório não deve ser transplantada para produção.

## CWE, CVE, ATT&CK e CVSS

- **CWE:** catálogo de classes de fraquezas. CWE-89 descreve SQL Injection.
- **CVE:** identificador de uma vulnerabilidade publicada. O exemplo escrito para este projeto não recebe um CVE por ser vulnerável.
- **MITRE ATT&CK:** descreve comportamentos adversários. T1190 trata de exploração de aplicações expostas publicamente para acesso inicial. Uma CLI local não satisfaz esse contexto.
- **CVSS:** sistema de classificação de severidade. A pontuação deve acompanhar versão, vetor e premissas; a prioridade também depende do ambiente.

## Práticas defensivas

Separar dados e instruções nas consultas SQL. Restringir privilégios, manter dependências atualizadas, limitar exposição desnecessária e guardar evidências sem segredos. Antes de mudar firewall ou acesso remoto, avaliar acesso alternativo e reversão para não perder o controle do sistema.

Senhas de produção devem usar funções próprias para armazenamento de senhas, como Argon2id, conforme a orientação da OWASP. Criptografia reversível ou hash rápido isolado não substituem uma solução adequada. O login de estudo mantém texto simples para concentrar a comparação na consulta; isso é uma limitação, não uma recomendação.

Uma cópia de segurança só apoia a recuperação se abranger os arquivos necessários e puder ser restaurada. Não garante reversão de qualquer mudança. Mesmo com dados fictícios, configurações e variáveis de ambiente podem conter segredos reais.

A gravidade da falha, a correção identificada na leitura e a confirmação por testes são informações distintas. Registrar a origem de cada evidência: relato, print/saída examinada ou execução própria.

Não imprimir senhas em logs. O `input()` do exemplo também deixa a digitação visível no terminal. Usar somente os dados fictícios fornecidos.

## Referências

- [Python: sqlite3 e parâmetros](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)
- [MITRE: CWE-89](https://cwe.mitre.org/data/definitions/89.html)
- [MITRE ATT&CK: T1190](https://attack.mitre.org/techniques/T1190/)
- [FIRST: guia CVSS v4.0](https://www.first.org/cvss/v4.0/user-guide)
- [OWASP: armazenamento de senhas](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

Referências consultadas na revisão de 06/11/2026. Reconsultar fontes quando a análise depender de versões ou recomendações atuais.
