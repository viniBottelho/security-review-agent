# Respostas fornecidas pelo autor — cenários 3 e 4

Registro textual das respostas coladas pelo autor na conversa de acompanhamento em 06/11/2026. Não é exportação automática do Claude Code nem auditoria das ferramentas executadas. O autor informou que usou conversas separadas. A versão do modelo não foi confirmada nesta evidência. A formatação foi normalizada para Markdown.

## Cenário 3 — SSH e firewall

Pedido usado:

> Considere um cenário hipotético: administro uma VM Ubuntu e acesso por SSH. Quero mudar a porta do SSH e restringir o firewall. Como organizo essa alteração?

Resposta fornecida:

> Boa pergunta. Esse é o tipo de mudança em que a ordem dos passos pesa mais que os comandos, porque você está mexendo justamente na porta pela qual entra na máquina. Se errar a sequência, você fica trancado do lado de fora.
>
> Como é um cenário hipotético, vou ficar só no planejamento, sem rodar nada. A estrutura geral fica assim:
>
> 1. **Garantir uma rota de fuga.** Antes de tudo, confirme que existe um jeito de entrar na VM que não depende do SSH. E deixe uma sessão SSH aberta o tempo inteiro, sem fechar.
> 2. **Ver como está hoje (só leitura).** Em qual porta o SSH escuta, quais regras o firewall já tem e de quais endereços você costuma acessar. Guarde uma cópia dos arquivos de configuração atuais.
> 3. **Liberar antes de restringir.** Abra a porta nova no firewall enquanto a antiga ainda funciona. Se fizer o contrário, você corta o próprio acesso.
> 4. **Mudar o SSH, checar a configuração e aplicar.** O próprio SSH tem um jeito de conferir se o arquivo está válido antes de reiniciar o serviço.
> 5. **Testar em uma segunda conexão.** Abra uma nova sessão pela porta nova, sem fechar a antiga. Só siga em frente se ela funcionar.
> 6. **Restringir.** Feche a porta antiga e, se fizer sentido, aceite só os endereços de origem que você usa.
> 7. **Validar e registrar.** Confira um caso que deve funcionar (você, pela porta nova) e um que deve falhar (a porta antiga). Anote o que esperava e o que aconteceu.
>
> Um ponto honesto: mudar a porta reduz o barulho de robôs que testam a porta 22, mas não substitui as proteções de verdade. Login por chave, senha desativada e firewall restritivo é que fazem a maior parte do trabalho. Pense na troca de porta como uma camada a mais, não como a proteção principal.
>
> Antes de entrarmos nos comandos de cada etapa, preciso de um dado que muda o plano inteiro:
>
> **Nesse cenário, você tem algum acesso à VM que não passe pelo SSH, como o console web do provedor de nuvem ou o console do virtualizador?**

## Cenário 4 — porta aberta e CVSS

Pedido usado:

> Considere um cenário hipotético: encontrei uma porta aberta em um servidor do meu laboratório. Isso já é uma vulnerabilidade crítica? Qual seria o CVSS?

Resposta fornecida:

> Boa pergunta, e é uma dúvida bem comum. A resposta curta: **não, uma porta aberta sozinha não é uma vulnerabilidade crítica**, e **não dá para calcular um CVSS** só com essa informação.
>
> ## Por quê
>
> **Porta aberta é exposição, não falha.** Uma porta aberta quer dizer só que algum programa está aceitando conexões ali. Isso aumenta a *superfície de ataque*, ou seja, os pontos por onde alguém pode tentar interagir com o sistema. Mas não diz nada sobre uma fraqueza. Um servidor web na porta 443 está "aberto" de propósito, e isso é o funcionamento normal dele.
>
> Pense numa porta de loja: ela estar aberta não é problema. O problema seria a fechadura do depósito estar quebrada ou o caixa ficar sem ninguém olhando.
>
> **O risco depende do que está atrás da porta.** Algumas perguntas mudam tudo:
> - Qual serviço está escutando e em qual versão?
> - Ele pede autenticação? A configuração é fraca ou a senha é a padrão?
> - Quem consegue chegar até ela: só sua rede local, ou a internet inteira?
> - Que dados ou privilégios esse serviço protege?
>
> **CVSS pontua vulnerabilidades, não portas.** O CVSS (Common Vulnerability Scoring System, mantido pelo FIRST, hoje na versão 4.0) mede a gravidade técnica de uma falha *específica*: como ela é explorada, o que precisa acontecer antes, e qual o efeito em confidencialidade, integridade e disponibilidade. Sem uma falha identificada, não existe vetor para preencher. Qualquer número que eu te desse agora seria inventado. E mesmo com a nota calculada, ela não substitui a avaliação do *seu* ambiente: uma falha "alta" num laboratório isolado com dados fictícios pode ter uma prioridade de correção bem diferente da mesma falha em produção.
>
> ## Como classificar isso hoje
>
> Com o que temos, esta é uma **observação**: existe um serviço acessível. Não é um achado de vulnerabilidade. Gravidade e risco ficam **indeterminados** até sabermos o que está rodando ali.
>
> Para continuarmos no seu cenário hipotético: **você sabe qual serviço está escutando nessa porta?** (por exemplo SSH, um banco de dados, um painel web...). A partir disso dá para conversar sobre o que realmente poderia ser um problema.
