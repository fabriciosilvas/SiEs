from typing import Optional

class Processo:
    
    """A classe Processo representa a abstração de um processo."""
    
    
    
    def __init__(self, id: int, tChegada: int, tExecucao: int, deadline: int, prioridade: int, qtdPaginas: int) -> None:
        
        """Constutor da classe Processo. Inicializa o objeto e sua tabela de páginas."""
        
        self.id = id
        self.tChegada = tChegada
        self.tExecucao = tExecucao
        self.deadline = deadline
        self.prioridade = prioridade
        self.qtdPaginas = qtdPaginas
        self.tabelaPaginas = self.criarPaginas(qtdPaginas)
        self.posicao = 0
        self.tExecutado = 0
        self.tConclusao = 0
        
        
    
    def criarPaginas(self, qtdPaginas: int) -> list:
        
        """Inicializa a tabela de páginas do processo. Cada elemento é represnetado por uma tupla (int, bool), que representa o número da página e se ela está ou não mapeada na memória física."""
        
        tabela = []
        
        for i in range(0, qtdPaginas*4, 4):
            tabela.append([i, False])   
            
        return tabela
    
    
    
    def getTabelaPaginas(self) -> list:
        
        """Retorna a tabela de páginas do processo.""" 
        
        return self.tabelaPaginas
    
    
    
    def getTConclusao(self) -> int:
        
        """Retorna o tempo em que o processo concluiu sua execução."""
        
        return self.tConclusao
        
        
        
    def getTExecutado(self) -> int:
        
        "Retorna a quantidade de tempo que o processo já executou."
        
        return self.tExecutado
    
    
        
    def getID(self) -> int:
        
        """Retorna o PID do processo."""
        
        return self.id
    
    
    
    def getTChegada(self) -> int:
        
        """Retorna o tempo em que o processo chegou à CPU."""
        
        return self.tChegada
    
    
    
    def getTExecucao(self) -> int:
        
        """Retorna o tempo de execução do processo."""
        
        return self.tExecucao
    
    
    
    def getDeadline(self) -> int:
        
        """Retorna o deadline do processo."""
         
        return self.deadline
    
    
    
    def getPrioridade(self) -> int:
        
        """Retorna a prioridade do processo."""
         
        return self.prioridade
    
    
    
    def getQtdPaginas(self) -> int:
        
        """Retorna a quantidade de páginas do processo."""
        
        return self.qtdPaginas
    
    
    
    def getPosicao(self) -> int:
        
        """Retorna a atual posição do processo no gráfico de Gaant."""
        
        return self.posicao
        
        
        
    def setTConclusao(self, tempoConclusao: int) -> None:
        
        """Modifica o tempo em que o processo concluiu sua execução."""
        
        self.tConclusao = tempoConclusao
    
    
    
    def setID(self, id: int) -> None:
        
        """Modifica o PID do processo."""
        
        self.id = id
        
        
        
    def setPosicao(self, posicao: int) -> None:
        
        """Modifica a posição do processo no gráfico de Gaant."""
        
        self.posicao = posicao
        
        
        
    def setTExecucao(self, tExecucao: int) -> None:
        
        """Modifica o tempo necessário de execução do processo."""
        
        self.tExecucao = tExecucao
        
        
        
    def setTChegada(self, tChegada: int) -> None:
        
        """Modifica o momento de chegada do processo à CPU."""
        
        self.tChegada = tChegada
    
    
    
    def setTExecutado(self, tExecutado: int) -> None:
        
        """Modifica a quantidade de tempo que o processo já executou para o tempo passado como argumento."""
        
        self.tExecutado = tExecutado
    
    
    
    def iTExecutado(self) -> None:
        
        """Incrementa a quantidade de tempo que o processo já executou em 1 unidade de tempo."""
        
        self.tExecutado += 1
        
        
        
    def setDeadline(self, deadline: int) -> None:
        
        """Modifica o deadline do processo."""
        
        self.deadline = deadline
        
        
    
    def setPrioridade(self, prioridade: int) -> None:
        
        """Modifica a prioridade do processo."""
        
        self.prioridade = prioridade
        
        
        
    def setqtdPaginas(self, qtdPaginas: int) -> None:
        
        """Modifica a quantidade de páginas do processo."""
        
        self.qtdPaginas = qtdPaginas
        
        
        
    def __str__(self) -> str:
        
        """Gera uma saída formatada do objeto Processo, exibindo seu ID e o tempo de chegada à CPU."""
        
        return f"ID: {self.id}, tC: {self.tChegada}"
    
    
    
    def __eq__(self, processo: Optional['Processo']) -> bool:
        
        """Compara dois processos. Retorna True caso eles sejam iguais, ou seja, possuam o mesmo PID."""
        
        if processo is None:
            return False
        
        return self.id == processo.getID()
        