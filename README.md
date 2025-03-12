### Aula de programacao de computadores 

### Descrição aula 02 - Conceitos - 25/02/2025


Algorimos e Lógica de Programação: 
- Conceitos básicos;
- Definição de algoritmos, raciocínio lógico e lógica de programação;
- Estrutura de um programa;
- Diagramas de bloco/fluxogramas;
- Testes de mesa.

#### Links 

- <a href="https://portugol.dev/">Portugol.div</a>&nbsp;&nbsp;&nbsp;
- <a href="https://www.lucidchart.com/pages/what-is-a-flowchart-tutorial">Fluxograma</a>&nbsp;&nbsp;&nbsp;

#### 1-Portugol 

<pre>
    programa {
  /*
    Exercício 2.1:
    Faça um algoritmo que leia o nome de uma pessoa, sua idade e o seu salário e ao final
    mostre essas informações.

    Exercício 2.2:
    Faça um algoritmo que leia 2 números e faça as 4 operações matemáticas e mostre
    esses resultados.
   */

  funcao inicio() {

    inteiro n1, n2, idade 
    cadeia nome 
    real salario

    //escreva("Qual é seu nome ? ")
    //leia(nome)

    //escreva("Qual é sua idade ? ")
    //leia(idade)

    //escreva("Qual é o seu salario ?")
    //leia(salario)

    //escreva("\nSeu nome é: ", nome)
    //escreva("\nsua idade é: ", idade)
    //escreva("\nseu salario é: ", salario)


    escreva("Digite o primeiro numero: ")
    leia(n1)

    escreva("Digites o segundo numero: ")
    leia(n2)

    escreva("\nA somda do n1+n2 é: ", n1+n2)
    escreva("\nA Subtração de n1-n2 é: ", n1-n2)
    escreva("\nA Multiplicação de n1*n2 é: ", n1*n2)
    escreva("\nA Divição de n1/n2 é: ", n1/n2)

       /* 1- Duas variáveis (A e B) possuem valores distintos (A = 5 e B = 10, por exemplo). Crie um
          algoritmo que armazene esses valores nas 2 variáveis e efetue a troca de valores de
          forma que a variável A passe a possuir o valor de B e que a variável B passe a possuir o
          valor de A. Ao final mostrar esses valores trocados. */
          
  inteiro A , B, Aux

  escreva("\nDigite um numero inteiro para A: ")
  leia(A)
  escreva("\nvalor A: ", A)

  escreva("\nDigite um numero inteiro para B: ")
  leia(B)
  escreva("\nvalor B: ", B)

  Aux = A
  A = B
  B = Aux


  escreva("\n valor A: ", A)
  escreva("\n valor B: ", B)

   



  }
}

</pre>
