### Aula 4

Exercícios Aula 04


<pre>

programa {
  funcao inicio() {
    inteiro A, B, C, N1, N2, N3

    escreva("Digite o valor A ")
    leia(A)

    escreva("Digite o valor B ")
    leia(B)

    escreva("Digite o valor C ")
    leia(C)

    N1 = B+C
    N2 = A+C
    N3 = A+B

    se ((A< N1) e (B < N2) e (C < N3)) {
      escreva("É triângulo")
    } senao se (A == B e B == C e A == C ) {
      escreva("É equilátero")
    } senao se ((A == B) ou (A == C) ou (B == C)) {
      escreva("É isósceles")
    } senao {
      escreva("É escaleno")
    }
  }

        real N1, N2, N3, N4, Soma

    escreva("Digite sua primeira nota: ")
    leia(N1)

    escreva("Digite sua segunda nota: ")
    leia(N2)

    escreva("Digite sua terceira nota: ")
    leia(N3)

    escreva("Digite sua quarta nota: ")
    leia(N4)

    Soma = (N1 + N2 + N3 + N4)/4

    se( Soma >= 6) {
        escreva("O aluno foi aprovado. Parabéns!!!","\n", Soma)
    } senao {
      escreva("O aluno foi reprovado!!!!: ", "\n", Soma)
    }


}




</pre>