# BDD com Python


## Resumo da live
- Como montar uma estória
    - Criando uma história:
        - Ator
        - Ação
        - Funcionalidade
    
    Exemplo: "Sendo um usuário (ator), eu quero me cadastrar (ação) para que seja possível ver informações do site (funcionalidade)."
- Como testar uma estória
- Como montar todo o ambiente
- Conhecendo o Behave

## Metodologias ágeis
- Extreme Programming
- Scrum

## Descrevendo em BDD (Behavior-Driven Development) o cadastro

**Dado que** o usuário se cadastre no sistema (GIVEN)

* O dado presume que algo já está lá

**e** insere um e-mail inválido (AND)

* Continuação de uma ação

**quando** apertar no botão "enviar" (WHEN)

* Quando eu vou executar uma ação

**então** a mensagem "e-mail inválido" deve ser exibida (THEN)

* Assertiva (Assert()). É o final da cadeia. É a assertiva de como aquilo funciona ou não, de como aquilo se relaciona.
* Ela precisa acertar que o sistema responde a uma condição. Não é pra ver se a ação deu certo ou errado, e sim para que a ação do usuário seja bem-sucedida. Se o usuário não conseguir se cadastrar, significa que ainda assim a assertiva cumpriu seu papel.

## Behave

O Behave é um framework para testes de BDD. Ele prega que os testes de comportamento sejam feitos da maneira mais simples possível.

### Estrutura  do Behave

* Raiz
  * Features
    * Steps
      * Python
  * Cucumber
    * teste.feature (exemplo)

