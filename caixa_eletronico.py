valor = int(input('Valor que deseja sacar: '))

quantidadeDeNotas = 0

notasDisponiveis = [100,50,20,10]

for notaAtual in notasDisponiveis:
    if(valor>=notaAtual):
        quantidadeDeNotas = int(valor/notaAtual)
        valor = int(valor%notaAtual)
        if(quantidadeDeNotas>1):
            print(quantidadeDeNotas, "notas de R$" + str(notaAtual) +",00")
        else:
            print(quantidadeDeNotas, "nota de R$" + str(notaAtual) +",00")