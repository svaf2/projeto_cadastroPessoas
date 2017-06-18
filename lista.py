#criacao basica da classe auxiliar no que guardara os objetos, no caso os objetos serao Pessoas
class No:
    def __init__(self, item = None, prox = None):
        self.item = item
        self.prox = prox

class Lista:
    #construtor que ja cria a raiz da lista como sendo um no vazio
    def __init__(self):
        self.primeiro = No()
        self.tamanho = 0
    
    #funcao idiota que so retorna quantos itens tem na lista
    def getTamanho(self):
        return self.tamanho

    #funcao para inserir ordenado
    def inserirOrdenado(self, item, cmp):
        novoNo = No(item) #cria um no com o valor 'item' recebido como parametro, esse no queremos inserir na lista
        if self.getTamanho() == 0: #apenas verifica se a lista esta vazia, se estiver inserimos no inicio
            self.primeiro.prox = novoNo #para inserir no inicio, basta a raiz apontar para o novoNo criado
            self.tamanho += 1 #como a lista estava vazia, novoNo nao aponta pra ninguem, finaliza aqui
            return
        
    ''' A logica abaixo e' para o caso de a lista ja ter elementos, como possivelmente precisamos inserir o novoNo entre
        outros dois nos, vamos precisar visualizar dois nos em sequencia. anterior e' a raiz, atual e' de fato o primeiro
        objeto que esta contido na lista
    '''
        anterior = self.primeiro
        atual = self.primeiro.prox
        
    ''' O laco serve apenas para encontrarmos em que ponto da lista vamos inserir novoNo, sempre vamos inserir novoNo
        apos anterior e antes de atual, para achar esse ponto as condicoes sao simples: atual deve existir (se ele nao
        existir significa que chegamos ao fim da lista) e o valor (nome, sobrenome) contidos em novoNo devem ser maiores
        que os contidos em atual. Enquanto essas duas condicoes forem verdadeiras vamos percorrer a lista, se uma delas
        se tornar falsa significa que encontramos o ponto exato onde devemos inserir novoNo entre anterior e atual
    '''
        
        while atual and cmp(novoNo.item, atual.item) != -1:
            anterior = atual
            atual = atual.prox
            
    ''' Aqui basta fazer a insercao, anterior ira apontar para novoNo e novoNo ira apontar para atual '''
        anterior.prox = novoNo
        novoNo.prox = atual
        self.tamanho += 1

    def remover(self, chave):
        anterior = self.primeiro
        atual = self.primeiro.prox
        while atual:
            if atual.item.getCPF() == chave:
                anterior.prox = atual.prox
                self.tamanho -= 1
                return True
            else:
                anterior = atual
                atual = atual.prox
        return False

    def buscar(self, chave):
        no = self.primeiro.prox
        while no:
            if no.item.getNome() == chave:
                return True
            no = no.prox
        return False

    def toCSV(self, sep):
        linha = ''
        aux = self.primeiro.prox
        while aux:
            nome = aux.item.getNome()
            sobrenome = aux.item.getSobrenome()
            rg = aux.item.getRG()
            cpf = aux.item.getCPF()
            tel = aux.item.getTel()
            cel = aux.item.getCel()
            linha += nome+sep+sobrenome+sep+rg+sep+cpf+sep+tel+cel+'\n'
            aux = aux.prox
        return linha

    def __str__(self):
        imprimir = ""
        no = self.primeiro.prox
        while no:
            imprimir += no.item.getNome() + "\n"
            no = no.prox
        return imprimir
    
    def __repr__(self):
        return str(self)
    
