
class Grafo:

    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        #matriz do tamanho dos numeros de vertices 
        self.grafo= [[0]*self.n_vertices for i in range(self.n_vertices)]

    def AdcionarArestaDirecionada(self, origem, destino, peso, complexidade):
        if complexidade == "Simples": #Grafo direcionado Simples
            self.grafo[origem-1][destino-1] = peso
        elif complexidade == "Multigrafo": #MultiGrafo direcionado 
            self.grafo[origem-1][destino-1] += peso
    def AdcionarArestaNaoDirecionada(self, origem, destino, peso, complexidade):   
        if complexidade == "Simples": #Grafo nao direcionado Simples
            self.grafo[origem-1][destino-1] = peso
            self.grafo[destino-1][origem-1] = peso
        elif complexidade == "Multigrafo": #MultiGrafo nao direcionado
            self.grafo[origem-1][destino-1] += peso    
            self.grafo[destino-1][origem-1] += peso

    def MostrarMatriz(self):
        print('A matriz de ajdacencias é: ')
        aux = list(range(1, self.n_vertices + 1))
        print("  "+str(aux))
        for i in  range(self.n_vertices):
            print()
            print(str(i+1),self.grafo[i])
    
    def grafoSimples(self):
        for i in range(self.n_vertices):
            if self.grafo[i][i] != 0:
                return "Não é um grafo Simples"
        return "Grafo Simples"

    def conexoOuDesconexo(self):
        for i in range(self.n_vertices):
            hasEdge = False
            for j in range(self.n_vertices):
                if self.grafo[i][j] == 1:
                    hasEdge = True
                    break
            if not hasEdge:
                return "Grafo Desconexo"
        return "Grafo Conexo"

    def completo(self):
        for i in range(self.n_vertices):
            if self.grafo[i][i] != 0:
                return "Não é um grafo Completo"
            count = 0
            for j in range(self.n_vertices):
                if i != j and self.grafo[i][j] == 1:
                    count += 1
            if count != self.n_vertices - 1:
                return "Não é um grafo Completo"
        return "Grafo Completo"

    def pseudografo(self):
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                if i != j and self.grafo[i][j] != 1:
                    return "Não é um Pseudografo"
        for i in range(self.n_vertices):
            if self.grafo[i][i] != 0:
                if self.grafo[i][i] == 2:
                    return "Pseudografo"
                else:
                    return "Não é um Pseudografo"
        return "Pseudografo"

    def multigrafo(self):
        for i in range(self.n_vertices):
            count = 0
            for j in range(self.n_vertices):
                if self.grafo[i][j] == 2:
                    count += 1
            if count <= 1:
                return "Não é um Multigrafo"
        for i in range(self.n_vertices):
            count = 0
            for j in range(self.n_vertices):
                if self.grafo[j][i] == 2:
                    count += 1
            if count <= 1:
                return "Não é um Multigrafo"
        return "Multigrafo"

    def ordemETamanho(self):
        ordem = 0
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                if self.grafo[i][j] == 1:
                    ordem += 1
        tamanho = ((ordem * (ordem - 1)) // 2)
        return f"Tamanho: {tamanho} - Ordem: {ordem}"

    def grauDosVertices(self):
        graus = [0] * self.n_vertices
        for i in range(self.n_vertices):
            for j in range(self.n_vertices):
                if self.grafo[i][j] == 1:
                    graus[i] += 1
        result = "Grau dos vértices:" + " ".join(map(str, graus))
        return result

    def grafoRegular(self):
        grau = 0
        for j in range(self.n_vertices):
            if self.grafo[0][j] == 1:
                grau += 1
        for i in range(1, self.n_vertices):
            grauAtual = 0
            for j in range(self.n_vertices):
                if self.grafo[i][j] == 1:
                    grauAtual += 1
            if grau == 0:
                grau = grauAtual
            elif grau != grauAtual:
                return "Grafo não regular"
        return "Grafo regular"

n_vertices = int(input('De a quantidade de vertices: '))

while True:#Validaçao de valor
    tipo = str(input('De o tipo (Direcionado ou Nao Direcionado): '))
    if tipo == "Direcionado" or tipo == "Nao Direcionado":
        break
    print("De uma sentença valida!! \n")

while True:#Validaçao de valor
    complexidade = str(input('De a complexidade (Simples ou Multigrafo): '))
    if complexidade == "Simples" or complexidade == "Multigrafo":
        break
    print("De uma sentença valida!! \n")
# Instancia o objeto Grafo com o numero de vertices para criacao da matriz  
grafo = Grafo(n_vertices)

if tipo == "Direcionado":
    while True:
        while True:
            origem = int(input('De o vertice de origem da aresta:'))
            if origem < n_vertices:#Validaçao de valor
                break
            print("De um numero valido!! \n")
        while True:
            destino = int(input('De o vertice de destino da aresta:'))
            if destino <= n_vertices:#Validaçao de valor
                break
            print("De um numero valido!! \n")
        peso = int(input('De o peso da aresta:'))

        grafo.AdcionarArestaDirecionada(origem,destino,peso,complexidade)
        print(f"Aresta do vertice {origem} para o vertice {destino} de peso {peso} foi adicionada ao grafo {tipo} {complexidade}")

        aux = str(input('Adcionar mais aresta? (sim ou nao)'))
        if aux == "nao":
            break

elif tipo == "Nao Direcionado":
    while True:
        origem = int(input('De o vertice de origem da aresta:'))
        destino = int(input('De o vertice de destino da aresta:'))
        peso = int(input('De o vertice de destino da aresta:'))

        grafo.AdcionarArestaNaoDirecionada(origem,destino,peso,complexidade)

        aux = str(input('Adcionar mais aresta? (sim ou nao)'))
        if aux == "nao":
            break
        print("Nova Aresta")


grafo.MostrarMatriz()

print(grafo.grafoSimples())
print(grafo.conexoOuDesconexo())
print(grafo.completo())
print(grafo.pseudografo())
print(grafo.multigrafo())
print(grafo.ordemETamanho())
print(grafo.grauDosVertices())
print(grafo.grafoRegular())