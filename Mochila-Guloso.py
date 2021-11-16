import os, time

#PROCURANDO OS ARQUIVOS DE ENTRADA NA PASTA ATUAL
caminhos = [os.path.join(nome) for nome in os.listdir(os.curdir)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
ins = [arq for arq in arquivos if arq.lower().endswith(".in")]

#EM CADA ARQUIVO DE ENTRADA EXECUTAR O ALGORITMO
for arquivo in ins:

    #ABRINDO O ARQUIVO PARA SALVAR OS RESULTADOS
    with open("Resultados.txt","a") as result:

        #ABRE UM ARQUIVO DE ENTRADA
        h = open(arquivo,"r")

        #INICIA A CONTAGEM DO TEMPO
        ini = time.time()

        #PEGA A QUANTIDADE DE ITENS E INICIALIZA O VETOR DE PESOS E DE VALORES
        n = int(h.readline())
        S = []
        V = []

        #AJEITANDO A ENTRADA PARA QUE OS ITENS FIQUEM DISPONIVEIS PARA USO
        for i in range(n):
            x = h.readline()
            x = x.split("\n")
            x = x[0].split(" ")
            aux = []
            for a in x:
                if a != "" :
                    aux.append(a)
            S.append(int(aux[2]))
            V.append(int(aux[1]))

        #PEGA A CAPACIDADE DA MOCHILA
        W = int(h.readline())

        Sl = []
        Sl2 = []
        aux = []

        #ADICIONA AS VALIOSIDADES DOS ITENS EM UM OUTRO VETOR
        for i in range(n):
            Sl.append(V[i]/S[i])

        #FAZ UMA COPIA DO VETOR DE VALIOSIDADE 
        Sl2 = Sl.copy()

        #ORDENA O VETOR COPIA PARA QUE FIQUE O MAIS VALIOSO PARA O MENNOS VALIOSO
        Sl2.sort(reverse=True)

        #ADICIONA O INDICE DO ITEM BASEADO NO VETOR DE VALIOSIDADE 
        for i in range(n):
            for x in range(n):
                if Sl[x] == Sl2[i]:
                    aux.append(x)

        soma = 0
        Itens = []
        #EXECUTA O ALGORITMO GULOSO PARA ENCONTRAR OS ITENS MAIS VALIOSOS QUE CABERAO NA MOCHILA
        for i in range(n):
            if soma + S[aux[i]] <= W :
                soma += S[aux[i]]
                Itens.append(aux[i])

        #ORDENA OS ITENS ENCONTRADOS
        Itens.sort()

        #PARA A CONTAGEM DO TEMPO
        fim = time.time()

        resultado = "Arquivo [{}] - Itens: {} - Tempo de execucao: {} segundos\n".format(arquivo,Itens,str(fim-ini)) 
        print(resultado)

        #ESCREVE O RESULTADO NO ARQUIVO DE RESULTADOS
        result.write(resultado)
        result.close()

