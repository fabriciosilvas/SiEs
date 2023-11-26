from typing import Optional
from cNo import No

class LDE:
    
    """A classe LDE é uma lista duplamente encadeada que contém as páginas que estão presentes na memória física. Essa classe é fundamental para a implementação dos algoritmos de paginação. Suas células são representadas por nós da classe No."""
    
    
    
    def __init__(self) -> None:
        
        """Construtor da classe LDE. Inicializa a estrutura de dados. """
        
        self.noPai = None
        self.tamanho = 0
        
        
        
    def isEmpty(self) -> bool:
        
        """Verifica se a lista está vazia. Retorna True caso não haja nós."""
        
        return self.tamanho == 0
    
    
    
    def __len__(self) -> int:
        
        """Retorna o tamanho atual da lista."""
        
        return self.tamanho
        
        
        
    def insereNoFIFO(self, no: No) -> bool:
        
        """Insere um nó na última posição da lista."""
        
        if self.noPai is None:
            self.noPai = no
            self.tamanho += 1
            
            return True
        
        noAtual = self.noPai
        while noAtual.getNoPosterior() is not None:
            noAtual = noAtual.getNoPosterior()
        
        noAtual.setNoPosterior(no)
        no.setNoAnterior(noAtual)
        self.tamanho += 1
        
        return True


    
    def insereNoLRU(self, no: No) -> bool:
        
        """Insere um nó na primeira posição da lista."""
        
        if self.noPai is None:
            self.noPai = no
            self.tamanho += 1
            
            return True
        
        noAtual = self.noPai
        noAtual.setNoAnterior(no)
        no.setNoPosterior(noAtual)
        self.noPai = no
        self.tamanho += 1
        
        return True
     
     
            
    def removeLRU(self) -> Optional['No']:
        
        """Remove o último nó da lista."""
        
        if self.tamanho == 0:
            return None
        
        noAtual = self.noPai
        
        if noAtual.getNoPosterior() is None:
            self.noPai = None
        else:
            while noAtual.getNoPosterior() is not None:
                noAtual = noAtual.getNoPosterior()
                
        noAtual.getNoAnterior().setNoPosterior(None)
        noAtual.setNoAnterior(None)
        self.tamanho -= 1
        
        return noAtual
    
    
    
    def removeFIFO(self, pID: int) -> Optional['No']:
        
        """Remove o primeiro nó da lista."""
        
        if self.tamanho == 0:
            return None
        
        noAtual = self.noPai
        
        while noAtual is not None and noAtual.getPID() == pID:
            noAtual = noAtual.getNoPosterior()
            
        if noAtual.getNoPosterior() is None:
            self.noPai = None
        else:
            self.noPai = noAtual.getNoPosterior()
            self.noPai.setNoAnterior(None)
            noAtual.setNoPosterior(None)
            
        self.tamanho -= 1
        
        return noAtual
    
    
    
    def reorganizaLRU(self, pID: int, numeroPagina: int) -> None:
        
        """Reorganiza a lista, movendo a página que foi referenciada para o início da lista."""
        
        if self.tamanho > 1:
            
            removido = self.retiraNo(No(pID, numeroPagina))
            
            if removido is not None: 
                noAtual = self.noPai
                noAtual.setNoAnterior(removido)
                removido.setNoPosterior(noAtual)
                self.noPai = removido
                    
                    
                    
    def retiraNo(self, no: No) -> Optional['No']:
        
        """Remove um determinado nó, passado como argumento, da lista."""
        
        if self.tamanho == 0:
            return None
        
        noAtual = self.noPai
        
        if no == noAtual:
            noProximo = noAtual.getNoPosterior()
            self.noPai = noProximo
            if noProximo is not None:
                noProximo.setNoAnterior(None)
        else:
            while noAtual is not None and noAtual != no:
                noAtual = noAtual.getNoPosterior()
            
            if noAtual is None:
                return None 
            
            noProximo = noAtual.getNoPosterior()
            noAnterior = noAtual.getNoAnterior()
            
            noAnterior.setNoPosterior(noProximo)
            if noProximo is not None:
                noProximo.setNoAnterior(noAnterior)    
        
        noAtual.setNoAnterior(None)
        noAtual.setNoPosterior(None)
        
        return noAtual
   
    
    
    def getNoPai(self) -> Optional['No']:
        
        """Retorna o primeiro nó da lista."""
        
        return self.noPai
    