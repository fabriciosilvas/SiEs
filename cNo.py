from typing import Optional

class No:
    
    """A classe No representa os nós da lista duplamente encadeada, que servirá de base para a implementação dos algoritmos de paginação."""
    
    
    
    def __init__(self, pID: int, numeroPagina: int) -> None:
        
        """Construtor da classe No. Recebe como argumentos o PID do processo e o número da página."""
        
        self.pID = pID
        self.numeroPagina = numeroPagina
        self.noAnterior = None
        self.noPosterior = None


    
    def getNoAnterior(self) -> Optional['No']:
        
        """Retorna o nó anterior ao nó que invocou a função."""
        
        return self.noAnterior
    
    
    
    def getNoPosterior(self) -> Optional['No']:
        
        """Retorna o nó posterior ao nó que invocou a função."""
        
        return self.noPosterior
    
    
        
    def getPID(self) -> int:
        
        """Retorna o PID do processo dono da página que representa o nó."""
        
        return self.pID
    
    
    
    def getNumeroPagina(self) -> int:
        
        """Retorna o número da página que representa o nó."""
        
        return self.numeroPagina
    
    
    
    def setPID(self, pID: int) -> None:
        
        """Altera o valor do PID."""
        
        self.pID = pID
    
    
    
    def setNumeroPagina(self, numeroPagina: int) -> None:
        
        """Altera o valor do número da página."""
        
        self.numeroPagina = numeroPagina
        
        
        
    def setNoAnterior(self, noAnterior: Optional['No']) -> None:
        
        """Modifica o nó anterior ao nó que invocou a função."""
        
        self.noAnterior = noAnterior
    
    
    
    def setNoPosterior(self, noPosterior: Optional['No']) -> None:
        
        """Modifica o nó posterior ao nó que invocou a função."""
        
        self.noPosterior = noPosterior
    
    def __eq__(self, no: Optional['No']) -> bool:
        
        """Compara dois nós. Retorna True caso eles representem a mesma página."""
        
        if no is None:
            return False
        
        return self.pID == no.getPID() and self.numeroPagina == no.getNumeroPagina()
    
    
    
    def __str__(self) -> str:
        
        """Gera uma saída formatada do objeto No, exibindo o PID e o número da página."""   
        
        return f"PID {self.pID}, nº página {self.numeroPagina}" 