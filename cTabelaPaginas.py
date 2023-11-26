class TabelaPaginas:
    
    """A classe TabelaPaginas é uma abstração da estrutura de uma tabela de páginas invertida. Essa classe mapeia os quadros de páginas que estão presentes na memória física (RAM)."""
    
    def __init__(self) -> None:
        
        """Construtor da classe TabelaPaginas. Inicializa a estrutura que irá armazenar as tuplas (pID, pagina)."""
        
        self.tabela = [None]*50
        self.tamMax = 50
        self.tam = 0
        
        
        
    def adicionaPagina(self, pID: int, numeroPagina: int) -> int:
        
        """Adiciona uma nova entrada à tabela de páginas. Essa função recebe como argumentos o ID do processo e o número da página, e retorna a posição da tabela em que a página foi alocada."""
        
        if self.tam < self.tamMax:
            for i in range(self.tamMax):
                if self.tabela[i] is None:
                    novaEntrada = (pID, numeroPagina)
                    self.tabela[i] = novaEntrada
                    self.tam += 1
            
                    return i
        
        return -1
        
    
    
    def removePagina(self, pID: int, numeroPagina: int) -> int:
        
        """Remove uma página da tabela de páginas. Essa função recebe como argumento o PID do processo e o número da página a ser removida e retorna a posição da tabela em que a página ocupava."""
        
        endereco = self.buscaPagina(pID, numeroPagina)
        
        if endereco != -1:
            self.tabela[endereco] = None
            self.tam -= 1
            
            return endereco
        
        return -1


    
    def buscaPagina(self, pID: int, numeroPagina: int) -> int:
        
        """Verifica se uma determinada página de um processo está mapeada na tabela de páginas e retorna o endereço na memória física. Retorna -1 caso não encontre uma referência à página na tabela."""
        
        endereco = 0
        
        for elem in self.tabela:
            if elem is not None:
                tPID, tPagina = elem
                if pID == tPID:
                    if tPagina == numeroPagina:
                        return endereco
            
            endereco += 1
        
        return -1
    
    
    
    def estaCheia(self) -> bool:
        
        """Verifica se há espaço na tabela de páginas. Retorna True, caso haja."""
        
        return self.tam == self.tamMax
    
    
    
    def __len__(self) -> int:
        
        """Retorna a quantidade atual de entradas na tabela de página."""
        
        return self.tam
