### Aula 3

Exercícios Aula 03


<pre>
  programa {
  funcao inicio() {
    /*Exercício 2.2:
      O custo ao consumidor de um carro novo, é a soma do custo de fábrica com a
      porcentagem do revendedor e com o custo dos impostos (aplicados ao custo da
      fabrica). Supondo que a porcentagem do revendedor seja de 25% do custo de fábrica e
      que os impostos custam 45% do custo de fábrica, faça um algoritmo que leia o valor de
      custo de fábrica e determine o preço do automóvel para o consumidor. */

    real porcentagemRevendedor, imposto, automovel
    real valorTotal
    porcentagemRevendedor = 25
    imposto = 45

    escreva("\nDigite o preço do automóvel ")
    leia(automovel)

    porcentagemRevendedor = automovel * porcentagemRevendedor / 100
    imposto = automovel * imposto / 100

    valorTotal = porcentagemRevendedor + imposto + automovel

    escreva("\nValor do automóvel final é: ", valorTotal) 
  ---------------------------------------------------------------------------------------------------
    
    /*Exercício 2.3:
      O sistema de avaliação de determinada disciplina é composto por três provas. A 1ª
      prova tem peso 2, a 2ª prova tem peso 3 e a 3ª prova tem peso 5. Faça um algoritmo
      para calcular a média final de um aluno desta disciplina.*/

      real A1, A2, A3, NotaFinal

      escreva("\nDigite a nota A1 :")
      leia(A1)

      escreva("\nDigite a nota A2 :")
      leia(A2)

      escreva("\nDigite a nota A3 :")
      leia(A3)

      NotaFinal = (A1 * 2 + A2 * 3 + A3 * 5) / (2 + 3 + 5)

      escreva("\nSua nota final é :", NotaFinal)
---------------------------------------------------------------------------------------------------------------
          /*Exercício 2.5:
      Uma empresa de vendas de softwares paga a seu vendedor um fixo de R$ 800,00 por
      mês, mais uma comissão de 15% pelo seu valor de vendas no mês. Faça um algoritmo
      que leia o valor da venda e determine o salário total do funcionário. Mostre as
      informações necessárias na tela. */

    real SalarioVendedor, Comissao, Vendas, SalarioTotal

    SalarioVendedor = 800

    escreva("\nDigite o valor da venda no mês: ")
    leia(Vendas)

    Comissao = ( Vendas * 15 ) / 100
    SalarioTotal =  Comissao + SalarioVendedor 

    escreva("\nValor da comissão ao mês: ", Comissao )
    escreva("\nValor do salario mais valor da comissão: ", SalarioTotal )
----------------------------------------------------------------------------------------

    /*Exercício 2.6:
        Uma empresa de desenvolvimento de softwares paga ao seu vendedor um salário fixo
        de R$ 500,00 por mês, mais um bônus de R$ 50,00 por sistema vendido. Faça um
        algoritmo que leia quantos softwares o funcionário vendeu e determine o salario total
        do funcionário. Mostre as informações que achar necessárias
     */

    inteiro SalarioFixo, Vendidos, Total

    escreva("\nDigite quantas vendas fez: ")
    leia(Vendidos)
    
    SalarioFixo = 500
    Total = Vendidos * 50 + SalarioFixo

    escreva("\nTotal de vendas no mês: ", Vendidos)
    escreva("\nSalário do vendedor: ", Total)
--------------------------------------------------------------------------------------------------------

    /*
    Exercício 2.7:
      Crie um algoritmo para calcular o salário líquido de um funcionário, considerando que
      seu salário bruto, incide um desconto de 9% em INSS para a previdência. O algoritmo
      deve mostrar o nome do funcionário, o seu salário bruto, o valor de desconto de INSS e
      o seu salário líquido.(dica.: Você deverá pedir (ler) o nome do funcionário e o valor do
      salário bruto).

     */

    real SalarioBruto, Desconto , Total
    inteiro INSS
    cadeia Nome

    INSS = 9

    escreva("\nDigite seu nome: ")
    leia(Nome)

    escreva("\nDigite o seu salário: ")
    leia(SalarioBruto)

    Desconto = SalarioBruto * INSS / 100
    Total = SalarioBruto - Desconto

    escreva("\nNome do funcionário: ", Nome)
    escreva("\nSalario bruto: ", SalarioBruto)
    escreva("\nDesconto INSS: ", Desconto)
    escreva("\nSalario já com o desconto INSS: ", Total)
------------------------------------------------------------------------------------------------

        /*
        Exercício 2.8:
      Considerando que para um consórcio, sabe-se o número total de prestações, a
      quantidade de prestações pagas e o valor atual da prestação, escreva um algoritmo que
      determine o total pago pelo consorciado e o saldo devedor. */

      inteiro NumeroTotalPrestacao, PrestacaoPagas 
      real ValorPrestacao, TotalPago, SaldoDevedor

      escreva("Digite o numero de prestações: ")
      leia(NumeroTotalPrestacao)

      escreva("Digite o numero de prestações pagas: ")
      leia(PrestacaoPagas)

      escreva("Digite o valor da prestação: ")
      leia(ValorPrestacao)

      TotalPago = PrestacaoPagas * ValorPrestacao
      SaldoDevedor = NumeroTotalPrestacao * ValorPrestacao - TotalPago 

      escreva("\nTotal Pago: ", TotalPago)
      escreva("\nSaldo devedor: ", SaldoDevedor)

      ----------------------------------------------------------------------------------------------

      programa {
  funcao inicio() {
    /*
      Exercício 2.9:
        Analisando a fórmula:
        Prestação = valor + (valor * (taxa/100) * tempo)
        Crie um algoritmo para efetuar o cálculo do valor de uma prestação em atraso. (Você
        deverá ler o VALOR da prestação, a TAXA de juros imposta pelo banco, e o número de
        dias em ATRASO).
     */

    real Prestacao, Valor, Taxa, Tempo, ValorComJuros

    escreva("Digite o valor da prestação: ")
    leia(Prestacao)

    escreva("Digite a taxa: ")
    leia(Taxa)

    escreva("Digite o número de dias em ATRASO: ")
    leia(Tempo)

    ValorComJuros = Prestacao + (Prestacao * (Taxa/100) * Tempo)

    escreva("Valor da divida com juros: ", ValorComJuros)



  }
}

  }
}

</pre>
