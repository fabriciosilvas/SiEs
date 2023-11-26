class AreaTroca:
    
    """A classe AreaTroca representa uma abstração de uma área de troca (swap area)."""
    
    
    
    def __init__(self, tamMax: int) -> None:
        
        """Construtor da classe AreaTroca. Inicializa o bitmap, baseando-se na quantidade de páginas."""
        
        self.bitMap = [None]*tamMax
        self.tamMax = tamMax
        self.tam = 0



    def alocaPagina(self, pID: int, numeroPagina: int) -> int:
        
        """Aloca uma página na área de troca e marca no bitmap a tupla (pID, numeroPagina). Retorna a posião em que a página foi alocada."""
        
        if self.isFull():
            return -1
        
        i = 0
        
        while i < self.tamMax:
            if self.bitMap[i] is None:
                self.bitMap[i] = (pID, numeroPagina)
                self.tam += 1
                
                return i
            
            i += 1
            
            
            
    def desalocaPagina(self, pID: int, numeroPagina: int) -> int:

        """Desaloca uma determinada página da área de troca. Retorna a posição em que a página estava presente."""
        
        for i in range(self.tamMax):
            if self.bitMap[i] == (pID, numeroPagina):
                self.bitMap[i] = None
                self.tam -= 1
                
                return i
            
        return -1
            
                
    
    def getBitMap(self) -> list:
        
        """Retorna o bitmap da área de troca."""
        
        return self.bitMap
    
    
    
    def isFull(self) -> bool:
        
        """Verifica se há espaço disponível na área de troca. Retorna True, caso haja."""
        
        return self.tam == self.tamMax
