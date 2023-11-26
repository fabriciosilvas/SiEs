from PySide6 import QtCore
from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QIcon, QBrush, QFont, QColor
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, QGraphicsRectItem, QGraphicsSimpleTextItem)
from interface_main import Ui_MainWindow
import sys
import time
from cProcesso import Processo
from cAreaTroca import AreaTroca
from cTabelaPaginas import TabelaPaginas
import cTurnoround
from cLDE import LDE
from cNo import No



#####################################
#            CONSTANTES             #
#####################################
COR_VERDE = QColor(8,222,4)
COR_AMARELA = QColor(240,255,5,255)
COR_LARANJA = QColor(241,81,27)
COR_AZUL = QColor(0,173,239)
COR_VINHO = QColor(150,3,3)
FONTE_TEMPO = QFont("Helvetica", 6)
FONTE_ID = QFont("Helvetica", 10)



class MainWindow(QMainWindow, Ui_MainWindow):
    
    """Classe da aplicação gráfica."""
    
    
    
    def __init__(self) -> None:
        
        """Inicializa todos os atribtos e operações necessárias para o correto funciuonamento da aplicação."""
        
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("SiEs")
        appIcon = QIcon(u":/icons/icons/logo.png")
        self.setWindowIcon(appIcon)
        self.tabelaPaginas = TabelaPaginas()
        self.areaTroca = AreaTroca(150)
        
        self.id = 1
        self.label_id.setText(f"ID: {self.id}")
        self.items = 0
        self.processos = []
        self.executando = None
        self.bloqueado = None
        self.haSobrecarga = False
        self.LDE = LDE()
      
        
        ### botão toggle
        self.togle.clicked.connect(self.leftMenu)
        
        
        ### páginas do sistema
        self.btn_home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_home))
        self.btn_criar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_criar))
        self.btn_executar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_executar))
        self.btn_sobre.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_sobre))
        
        ####criação do processo
        self.bt_criarprocesso.clicked.connect(lambda: self.cadastrarProcesso())
        
        ### execução
        self.bt_executar.clicked.connect(self.executar)
        
        ### reiniciar gráfico
        self.bt_reiniciar.clicked.connect(self.limparCena)
        
        # excluir processo
        self.btn_excluir.clicked.connect(self.excluir)
        
        # ligar gráficos
        self.fm_graficograant.verticalScrollBar().valueChanged.connect(self.atualizaScrollBar)
   
   
   
    def atualizaScrollBar(self) -> None:
        
        """Atualiza a posição da cena que contém os PIDs dos processos no gráfico de Gaant para coincidir com a cena que contém o gráfico em si."""
        
        self.fm_idsvisu.verticalScrollBar().setValue(self.fm_graficograant.verticalScrollBar().value())
        
        
        
    def exibirTurnaround(self, array_processos: list) -> None:
        
        """Cria uma janela para exibir o turnaround após a execução de todos os processos."""
        
        total = 0
        
        for processo in array_processos:
            total += processo.getTConclusao() - processo.getTChegada()
            processo.setTConclusao(0)
            
        turnaround = total / len(array_processos)
        
        self.turnoround = cTurnoround.cTurnoround(turnaround)
        self.turnoround.show()
        
        
        
    def excluir(self) -> None:
        
        """Exclui um processo da tabela de processos criados."""
        
        x = self.tableWidget.selectionModel().currentIndex()
        posicao = x.row()
        
        del self.processos[posicao]
        
        self.tableWidget.removeRow(posicao)
        self.items -= 1
     
     
     
    def executarSJF(self) -> None:
        
        """Executa o escalonamento de processos a partir do algoritmo SJF (Shortest Job First).""" 
          
        
        # lista com uma cópia de todos os processos
        all_processos = self.processos[:]
        
        # lista vazia dos processos em espera na CPU
        emEspera = []
        
        # lista dos processos que já concluíram sua execução
        concluidos = []
        
        # ordenação dos processos a partir do horário de chegada
        # e no tempo de execução
        all_processos.sort(key=lambda x : (x.getTChegada(), x.getTExecucao()))
        
        for i in range(len(all_processos)):
            all_processos[i].setPosicao(i)
            
        # tempo de delay para a visualização da execução
        tempo = float(self.box_delay.value())
        
        executados = 0 # qtd dos processos que já foram executados
        inicio = -1    # marca o tempo atual
        n = 0          # marca a quantidade de processos que já entraram em conclusão
        
        self.lb_tempo.setText(f"Tempo: 0")
        
        while executados != self.items:
            QApplication.processEvents()
            
            if self.executando == None and executados == 0 and inicio >= 0:
                self.adicionaQuadrado(Qt.lightGray, inicio, 1)
                
            inicio += 1
            
            self.lb_tempo.setText(f"Tempo: {inicio}")
            self.lb_tempo.repaint()
            self.adicionarTTempo(inicio)
            
            if self.executando != None:
                tR += 1
                self.pgs_execucao.setValue(tR/self.executando.getTExecucao()*100)
                self.pgs_execucao.repaint()
                
            while n < len(all_processos):
                QApplication.processEvents()
                
                p = all_processos[n]
                
                if p.getTChegada() == inicio:
                    self.alocaProcessoDisco(p)
                    self.criarItemTabela(p)
                    emEspera.append(p)
                    self.adicionarTID(p.getID(), p.getPosicao()+1)
                
                    n += 1
                elif p.getTChegada() > inicio:
                    emEspera.sort(key=lambda x : x.getTExecucao())
                    self.lista_prontos.sortItems(2)
                    self.lista_prontos.repaint()
                    self.tb_disco.repaint()
                    
                    break


            self.fm_graficograant.repaint()
            self.fm_idsvisu.repaint()
            QApplication.processEvents()                
            time.sleep(tempo)
            
            if self.executando != None:
                if tR == self.executando.getTExecucao():
                    self.executando.setTConclusao(inicio)
                    self.desalocaProcessoRAM(self.executando)
                    self.pgs_execucao.reset()
                    self.lb_cpu_id_e.setText(f"ID: ")
                    concluidos.append(self.executando)
                    self.executando = None
                    executados += 1
                else:
                    self.adicionaQuadrado(COR_VERDE, inicio, self.executando.getPosicao()+1)
            
            if self.executando == None and len(emEspera) > 0:
                QApplication.processEvents()
                emEspera.sort(key=lambda x : x.getTExecucao())
                self.lista_prontos.sortItems(2)
                p = emEspera.pop(0)
                
                self.alocaProcessoRAM(p, emEspera)
                self.executando = p
                self.lb_cpu_id_e.setText(f"ID: {p.getID()}")
                tR = 0
                
                self.lista_prontos.sortItems(2)    
                self.lista_prontos.removeRow(0)
                self.lista_prontos.repaint()
                self.adicionaQuadrado(COR_VERDE, inicio, self.executando.getPosicao()+1)
                
            if len(emEspera) > 0:
                for pr in emEspera:
                    self.adicionaQuadrado(COR_AMARELA, inicio, pr.getPosicao()+1)
                    
            if self.items != executados:
                for pr in concluidos:
                    self.adicionaQuadrado(Qt.lightGray, inicio, pr.getPosicao()+1)
            
            self.fm_graficograant.repaint()
            self.fm_idsvisu.repaint()            
        
        self.lb_tempo.setText(f"Tempo: ")
        self.exibirTurnaround(concluidos)
        del emEspera
        del all_processos
        del concluidos
    
    
    
    def adicionarTID(self, conteudo: int, fim: int) -> None:
        
        """Adiciona o PID de um processo na visualização do gráfico."""
        
        texto = QGraphicsSimpleTextItem(str(conteudo))
        texto.setFont(FONTE_ID)
        posY = fim*15
        altura = self.rect1.height()
        
        if posY + 15 > altura:
            self.rect1.setHeight(altura + 15)
            self.cena1.setSceneRect(self.rect1)
            
        texto.setPos(0, posY)
        self.cena1.addItem(texto)
        
        
        
    def adicionarTTempo(self, conteudo: int) -> None:
        
        """Adiciona o tempo atual na visualização do gráfico."""
        
        texto = QGraphicsSimpleTextItem(str(conteudo))
        texto.setFont(FONTE_TEMPO)
        posX = conteudo*15
        largura = self.rect.width()
        
        if posX + 15 > largura:
            self.rect.setWidth(largura + 15)
            self.cena.setSceneRect(self.rect)
            
        texto.setPos(posX, 0)
        self.cena.addItem(texto)
        
       
       
    def adicionaQuadrado(self, cor: QColor, inicio: int, fim: int) -> None:
        
        """Adiciona um quadrado na visualização do gráfico."""
        
        rect = QGraphicsRectItem(0, 0, 15, 15)
        brush = QBrush(cor)
        rect.setBrush(brush)
        posX = inicio*15
        posY = 15*fim
        altura = self.rect.height()
        largura = self.rect.width()
        
        if posX + 15 > largura:
            self.rect.setWidth(largura + 15)
            self.cena.setSceneRect(self.rect)
            
        if posY + 15 > altura:
            self.rect.setHeight(altura + 15)
            self.cena.setSceneRect(self.rect)
        
        rect.setPos(posX, posY)
        self.cena.addItem(rect)
        
        self.fm_graficograant.centerOn(QPointF(posX+15, posY+15))
        self.fm_idsvisu.centerOn(QPointF(0, posY+15))
  
  
        
    def executarRoundRobin(self, tSobrecarga: int, tQuantum: int, paginacao: str) -> None:   
        
        """Executa o escalonamento de processos a partir do algoritmo Round Robin.""" 
        
        # lista com uma cópia de todos os processos
        all_processos = self.processos[:]
        
        # lista vazia dos processos em espera na CPU
        emEspera = []
        
        # lista dos processos que já concluíram sua execução
        concluidos = []
        
        #indica a posição que um quadrado laranja (sobrecarga) será adicionado
        posRed = 0
        
        # ordenação dos processos a partir do horário de chegada
        all_processos.sort(key=lambda x : x.getTChegada())
        
        for i in range(len(all_processos)):
            all_processos[i].setPosicao(i)
            
        # tempo de delay para a visualização da execução
        tempo = float(self.box_delay.value())
        
        executados = 0 # qtd dos processos que já foram executados
        inicio = -1    # marca o tempo atual
        n = 0          # marca a quantidade de processos que já entraram em conclusão
        tS = tR = 0    # tS marca o tempo de sobrecarga
                       # tR marca o tempo de execução do processo
        
        self.lb_tempo.setText(f"Tempo: 0")
        
        while executados != self.items:
            QApplication.processEvents()
            
            if self.executando == None and executados == 0 and inicio >= 0 and not self.haSobrecarga:
                self.adicionaQuadrado(Qt.lightGray, inicio, 1)
            
            inicio += 1
            self.lb_tempo.setText(f"Tempo: {inicio}")
            self.lb_tempo.repaint()
            self.adicionarTTempo(inicio)
            
            if self.haSobrecarga:
                tS += 1
                self.pgs_sobrecarga.setValue(tS/tSobrecarga*100)
            
            if self.executando != None:
                tR += 1
                self.executando.iTExecutado()
                self.pgs_execucao.setValue(self.executando.getTExecutado()/self.executando.getTExecucao()*100)


            while n < len(all_processos):
                QApplication.processEvents()
                p = all_processos[n]
                if p.getTChegada() == inicio:
                    self.alocaProcessoDisco(p)
                    self.criarItemTabela(p)
                    emEspera.append(p)
                    self.adicionarTID(p.getID(), p.getPosicao()+1)
                    n += 1
                elif p.getTChegada() > inicio:
                    self.tb_disco.repaint()
                    
                    break
            
            self.lista_prontos.repaint()  
            self.fm_graficograant.repaint()
            self.fm_idsvisu.repaint()
            QApplication.processEvents()      
            time.sleep(tempo)
            
            if self.executando != None:
                if self.executando.getTExecutado() == self.executando.getTExecucao():
                        self.executando.setTConclusao(inicio)
                        self.desalocaProcessoRAM(self.executando)
                        self.pgs_execucao.reset()
                        self.executando.setTExecutado(0)
                        self.lb_cpu_id_e.setText(f"ID: ")
                        concluidos.append(self.executando)
                        self.executando = None
                        executados += 1
              
            if self.haSobrecarga and tS >= tSobrecarga:
                self.haSobrecarga = False 
                self.pgs_sobrecarga.reset()
                tS = 0
            elif self.haSobrecarga:
                self.adicionaQuadrado(COR_LARANJA, inicio, posRed)
            
            if self.executando != None:
                if tR == tQuantum:
                    self.pgs_execucao.reset()
                    self.lb_cpu_id_e.setText(f"ID: ")
                    emEspera.append(self.executando)
                    self.criarItemTabela(self.executando)
                    self.executando = None
                    if tSobrecarga > 0:
                        self.haSobrecarga = True
                        self.adicionaQuadrado(COR_LARANJA, inicio, posRed)
                    tS = 0
                    tR = 0
                else:
                    self.adicionaQuadrado(COR_VERDE, inicio, self.executando.getPosicao()+1) 
            
            if self.executando == None and len(emEspera) > 0 and not self.haSobrecarga:
                p = emEspera.pop(0)
        
                self.alocaProcessoRAM(p, emEspera)
                self.executando = p
                self.lb_cpu_id_e.setText(f"ID: {p.getID()}")
                
                if paginacao == "LRU":
                    self.reorganizaPaginasLRU(p)
                    
                tR = 0
                posRed = p.getPosicao() + 1
                self.lista_prontos.removeRow(0)
                self.adicionaQuadrado(COR_VERDE, inicio, self.executando.getPosicao()+1)
            
            if len(emEspera) > 0:
                for pr in emEspera:
                    pos = pr.getPosicao()
                    if pos != posRed - 1:
                        self.adicionaQuadrado(COR_AMARELA, inicio, pos+1)
                    elif not self.haSobrecarga:
                        self.adicionaQuadrado(COR_AMARELA, inicio, pos+1)
                    
            if self.items != executados:
                for pr in concluidos:
                    self.adicionaQuadrado(Qt.lightGray, inicio, pr.getPosicao()+1)
            
            self.lista_prontos.repaint()
            self.fm_graficograant.repaint()
            self.fm_idsvisu.repaint()        
            
        self.lb_tempo.setText(f"Tempo: ")
        self.exibirTurnaround(concluidos)
        
        del emEspera
        del all_processos
        del concluidos
        
        
        
    def executarEDF(self, tSobrecarga: int, tQuantum: int, paginacao: str) -> None:   
        
        """Executa o escalonamento de processos a partir do algoritmo EDF (Earliest Deadline First)."""
        
        # lista com uma cópia de todos os processos
        all_processos = self.processos[:]
        
        # lista vazia dos processos em espera na CPU
        emEspera = []
        
        # lista dos processos que já concluíram sua execução
        concluidos = []
        
        #indica a posição que um quadrado laranja (sobrecarga) será adicionado
        posRed = 0
        
        # ordenação dos processos a partir do horário de chegada
        all_processos.sort(key=lambda x : (x.getTChegada(), x.getDeadline() + x.getTChegada()))
        
        for i in range(len(all_processos)):
            QApplication.processEvents()
            all_processos[i].setPosicao(i)
        
        # tempo de delay para a visualização da execução
        tempo = float(self.box_delay.value())
        
        executados = 0 # qtd dos processos que já foram executados
        inicio = -1    # marca o tempo atual
        n = 0          # marca a quantidade de processos que já entraram em conclusão
        
        tS = tR = 0    # tS marca o tempo de sobrecarga
                       # tR marca o tempo de execução do processo
        
        self.lb_tempo.setText(f"Tempo: 0")
        
        while executados != self.items:
            QApplication.processEvents()
            
            if self.executando == None and executados == 0 and inicio >= 0 and not self.haSobrecarga:
                self.adicionaQuadrado(Qt.lightGray, inicio, 1)
            
            inicio += 1
            self.lb_tempo.setText(f"Tempo: {inicio}")
            self.lb_tempo.repaint()
            self.adicionarTTempo(inicio)
            
            if self.haSobrecarga:
                tS += 1
                self.pgs_sobrecarga.setValue(tS/tSobrecarga*100)
                
            if self.executando != None:
                tR += 1
                self.executando.iTExecutado()
                self.pgs_execucao.setValue(self.executando.getTExecutado()/self.executando.getTExecucao()*100)

            while n < len(all_processos):
                QApplication.processEvents()
                p = all_processos[n]
                if p.getTChegada() == inicio:
                    self.alocaProcessoDisco(p)
                    self.criarItemTabela(p)
                    emEspera.append(p)
                    self.adicionarTID(p.getID(), p.getPosicao()+1)
                    
                    n += 1
                elif p.getTChegada() > inicio:
                    emEspera.sort(key=lambda x : (x.getDeadline() + x.getTChegada()))
                    self.sortItens(emEspera)
                    self.tb_disco.repaint()
                    
                    break
            
            self.lista_prontos.repaint()
            self.fm_graficograant.repaint()
            self.fm_idsvisu.repaint() 
            QApplication.processEvents()       
            time.sleep(tempo)
            
            if self.executando != None:
                if self.executando.getTExecutado() == self.executando.getTExecucao():
                        self.executando.setTConclusao(inicio)
                        self.desalocaProcessoRAM(self.executando)
                        self.pgs_execucao.setValue(0)
                        self.executando.setTExecutado(0)
                        self.lb_cpu_id_e.setText(f"ID: ")
                        concluidos.append(self.executando)
                        self.executando = None
                        executados += 1  
              
            if self.haSobrecarga and tS >= tSobrecarga:
                self.haSobrecarga = False 
                self.pgs_sobrecarga.reset()
                tS = 0
            elif self.haSobrecarga:
                self.adicionaQuadrado(COR_LARANJA, inicio, posRed)
            
            if self.executando != None:
                if tR == tQuantum:
                    self.pgs_execucao.reset()
                    self.lb_cpu_id_e.setText(f"ID: ")
                    emEspera.append(self.executando)
                    self.criarItemTabela(self.executando)
                    self.executando = None
                    
                    if tSobrecarga > 0:
                        self.haSobrecarga = True
                        self.adicionaQuadrado(COR_LARANJA, inicio, posRed)
                        
                    tS = 0
                    tR = 0
        
                    emEspera.sort(key=lambda x : (x.getDeadline() + x.getTChegada()))
                    self.sortItens(emEspera)
                else:
                    if inicio < self.executando.getDeadline() + self.executando.getTChegada():
                        self.adicionaQuadrado(COR_VERDE, inicio, self.executando.getPosicao()+1) 
                    else:
                        self.adicionaQuadrado(COR_VINHO, inicio, self.executando.getPosicao()+1)
            
            if self.executando == None and len(emEspera) > 0 and not self.haSobrecarga:
                emEspera.sort(key=lambda x : (x.getDeadline() + x.getTChegada()))
                self.sortItens(emEspera)
                
                p = emEspera.pop(0)
                
                self.alocaProcessoRAM(p, emEspera)
                self.executando = p
                self.lb_cpu_id_e.setText(f"ID: {p.getID()}")
                
                if paginacao == "LRU":
                    self.reorganizaPaginasLRU(p)
                    
                tR = 0
                posRed = p.getPosicao() + 1
                            
                self.lista_prontos.removeRow(0)
                if inicio < self.executando.getDeadline() + self.executando.getTChegada():
                        self.adicionaQuadrado(COR_VERDE, inicio, self.executando.getPosicao()+1) 
                else:
                    self.adicionaQuadrado(COR_VINHO, inicio, self.executando.getPosicao()+1)
                    
            if len(emEspera) > 0:
                for pr in emEspera:
                    pos = pr.getPosicao()
                    if pos != posRed - 1:
                        self.adicionaQuadrado(COR_AMARELA, inicio, pos+1)
                    elif not self.haSobrecarga:
                        self.adicionaQuadrado(COR_AMARELA, inicio, pos+1)
                    
            if self.items != executados:
                for pr in concluidos:
                    self.adicionaQuadrado(Qt.lightGray, inicio, pr.getPosicao()+1)
            
            self.lista_prontos.repaint()
            self.fm_graficograant.repaint()
            self.fm_idsvisu.repaint()    
            
        self.lb_tempo.setText(f"Tempo: ")
        self.exibirTurnaround(concluidos)
        
        del emEspera
        del all_processos
        del concluidos
    
    
    
    def reorganizaPaginasLRU(self, processo: Processo) -> None:
        
        """Reorganiza a lista duplamente encadeada a cada referência de uma página na memória."""
        
        tabelaPP = processo.getTabelaPaginas()
        pID = processo.getID()
        
        for i in range(len(tabelaPP)):
            self.LDE.reorganizaLRU(pID, tabelaPP[i][0])
        
        
        
    def sortItens(self, lista: list) -> None:
        
        """Reorganiza os itens na tabela de prontos da CPU."""
        
        self.lista_prontos.clearContents()
        self.lista_prontos.setRowCount(0)
        
        for p in lista:
            item_id = QTableWidgetItem(str(p.getID()))
            item_chegada = QTableWidgetItem(str(p.getTChegada()))
            item_execucao = QTableWidgetItem(str(p.getTExecucao()))
            item_prioridade = QTableWidgetItem(str(p.getPrioridade()))
            item_deadline = QTableWidgetItem(str(p.getDeadline()))
            
            c = self.lista_prontos.rowCount()
            self.lista_prontos.setRowCount(c+1)
            
            self.lista_prontos.setItem(c, 0, item_id)
            self.lista_prontos.setItem(c, 1, item_chegada)
            self.lista_prontos.setItem(c, 2, item_execucao)
            self.lista_prontos.setItem(c, 4, item_deadline)
            self.lista_prontos.setItem(c, 3, item_prioridade)
            
        self.lista_prontos.repaint()  
      
      
      
    def criarItemTabela(self, processo: Processo) -> None:
        
        """Cria um QTableWidgetItem e adiciona-o à lista de prontos da CPU."""
        
        item_id = QTableWidgetItem(str(processo.getID()))
        item_chegada = QTableWidgetItem(str(processo.getTChegada()))
        item_execucao = QTableWidgetItem(str(processo.getTExecucao()))
        item_prioridade = QTableWidgetItem(str(processo.getPrioridade()))
        item_deadline = QTableWidgetItem(str(processo.getDeadline()))
        item_pagina = QTableWidgetItem(str(processo.getQtdPaginas()))
        
        c = self.lista_prontos.rowCount()
        self.lista_prontos.setRowCount(c+1)
        
        self.lista_prontos.setItem(c, 0, item_id)
        self.lista_prontos.setItem(c, 1, item_chegada)
        self.lista_prontos.setItem(c, 2, item_execucao)
        self.lista_prontos.setItem(c, 3, item_prioridade)
        self.lista_prontos.setItem(c, 4, item_deadline)
        self.lista_prontos.setItem(c, 5, item_pagina)
        
        
         
    def executarFifo(self):   
        
        """Executa o escalonamento de processos a partir do algoritmo FIFO (First In, First Out).""" 
        
        # lista com uma cópia de todos os processos
        all_processos = self.processos[:]
        
        # lista vazia dos processos em espera na CPU
        emEspera = []
        
        # lista dos processos que já concluíram sua execução
        concluidos = []
        
        # ordenação dos processos a partir do horário de chegada
        all_processos.sort(key=lambda x : x.getTChegada())
        
        for i in range(len(all_processos)):
            QApplication.processEvents()
            all_processos[i].setPosicao(i)
        
        # tempo de delay para a visualização da execução
        tempo = float(self.box_delay.value())
        
        executados = 0 # qtd dos processos que já foram executados
        inicio = -1    # marca o tempo atual
        n = 0          # marca a quantidade de processos que já entraram em conclusão
        
        self.lb_tempo.setText(f"Tempo: 0")
        
        while executados != self.items:
            QApplication.processEvents()
            
            if self.executando == None and executados == 0 and inicio >= 0:
                self.adicionaQuadrado(Qt.lightGray, inicio, 1)
                    
            inicio += 1
            self.lb_tempo.setText(f"Tempo: {inicio}")
            self.lb_tempo.repaint()
            self.adicionarTTempo(inicio)
            
            if self.executando != None:
                tR += 1
                self.pgs_execucao.setValue(tR/self.executando.getTExecucao()*100)
                self.pgs_execucao.repaint()

            while n < len(all_processos):
                QApplication.processEvents()
                p = all_processos[n]
                if p.getTChegada() == inicio:
                    self.alocaProcessoDisco(p)
                    self.criarItemTabela(p)
                    emEspera.append(p)
                    self.adicionarTID(p.getID(), p.getPosicao()+1)
                    
                    n += 1
                elif p.getTChegada() > inicio:
                    self.tb_disco.repaint()
                    
                    break
            
            self.lista_prontos.repaint()
            self.fm_graficograant.repaint()
            self.fm_idsvisu.repaint()  
            QApplication.processEvents()   
            time.sleep(tempo)
            
            if self.executando != None:
                if tR == self.executando.getTExecucao():
                    self.desalocaProcessoRAM(self.executando)
                    self.pgs_execucao.reset()
                    self.lb_cpu_id_e.setText(f"ID: ")
                    concluidos.append(self.executando)
                    self.executando.setTConclusao(inicio)
                    self.executando = None
                    executados += 1
                else:
                    self.adicionaQuadrado(COR_VERDE, inicio, self.executando.getPosicao()+1)
            
            if self.executando == None and len(emEspera) > 0:
                p = emEspera.pop(0)
                
                self.alocaProcessoRAM(p, emEspera)
                self.executando = p
                self.lb_cpu_id_e.setText(f"ID: {p.getID()}")
                tR = 0
                    
                self.lista_prontos.removeRow(0)
                self.lista_prontos.repaint()
                self.adicionaQuadrado(COR_VERDE, inicio, self.executando.getPosicao()+1)
           
            if len(emEspera) > 0:
                for pr in emEspera:
                    self.adicionaQuadrado(COR_AMARELA, inicio, pr.getPosicao()+1)
                    
            if self.items != executados:
                for pr in concluidos:
                    self.adicionaQuadrado(Qt.lightGray, inicio, pr.getPosicao()+1)
        
            self.fm_graficograant.repaint()
            self.fm_idsvisu.repaint()    
            
        self.lb_tempo.setText(f"Tempo: ")
        self.exibirTurnaround(concluidos)
        
        del emEspera
        del all_processos
        del concluidos
    
    
    
    def limparCena(self) -> None:
        
        """Apaga as informações do gráfico após a execução."""
        
        self.fm_graficograant.centerOn(QPointF(0,0))
        self.fm_idsvisu.centerOn(QPointF(0,0))
        
        self.cena1.clear()
        self.cena.clear()
    
    
    
    def alocaProcessoRAM(self, processo: Processo, lista_processos: list) -> None:
        
        """Aloca todas as páginas do processo na memória RAM."""
        
        tabelaPaginasProcesso = processo.getTabelaPaginas()
        pID = processo.getID()
        
        
        
        for i in range(processo.getQtdPaginas()):
            if not tabelaPaginasProcesso[i][1]:
                self.alocaPaginaRAM(pID, tabelaPaginasProcesso[i][0], lista_processos, processo)
                tabelaPaginasProcesso[i][1] = True
            
        self.tabela_ram.repaint()
        self.tb_disco.repaint()
        
        
     
    def desalocaProcessoRAM(self, processo: Processo) -> None:
        
        """Desaloca todas as páginas de um processo da memória RAM."""
        
        tabelaPaginasProcesso = processo.getTabelaPaginas()
        pID = processo.getID()
        
        for i in range(len(tabelaPaginasProcesso)):
            numeroPagina = tabelaPaginasProcesso[i][0]
            removido = self.tabelaPaginas.removePagina(pID, numeroPagina)
            self.tabela_ram.setItem(removido//10, removido%10, None)
            self.LDE.retiraNo(No(pID, numeroPagina))
            tabelaPaginasProcesso[i][1] = False
            
        self.tabela_ram.repaint()
        self.tb_disco.repaint()          
        
    
    
    def alocaProcessoDisco(self, processo: Processo) -> None:
        
        """Aloca todas as páginas de um processo na memória secundária (disco)."""
        
        tabelaPaginasProcesso = processo.getTabelaPaginas()
        pID = processo.getID()
        
        for i in range(len(tabelaPaginasProcesso)):
            self.alocaPaginaDisco(pID, tabelaPaginasProcesso[i][0])
            
        self.tb_disco.repaint()
        
        
        
    def alocaPaginaRAM(self, pID: int, numeroPagina: int, lista_processos: list, processo: Processo) -> bool:
        
        """Aloca uma única página de um determinado processo na memória RAM."""
        
        paginacao = self.slt_paginacao.currentText()
        alocado = self.tabelaPaginas.adicionaPagina(pID, numeroPagina)
        item_id = QTableWidgetItem(str(pID))
        
        if alocado == -1:
            self.desalocaPaginaRAM(lista_processos, pID, processo)
            alocado = self.tabelaPaginas.adicionaPagina(pID, numeroPagina)
        
        removido = self.areaTroca.desalocaPagina(pID, numeroPagina)
        
        if removido == -1:
            self.tabela_ram.setItem(alocado//10, alocado%10, item_id)
        else:
            self.tb_disco.setItem(removido//15, removido%15, None)
            self.tabela_ram.setItem(alocado//10, alocado%10, item_id)
                
            
        no = No(pID, numeroPagina)
        
        if paginacao == "LRU":
            self.LDE.insereNoLRU(no)
        elif paginacao == "FIFO":
            self.LDE.insereNoFIFO(no)                
                        
        

    def desalocaPaginaRAM(self, lista_processos: list, pID: int, processo: Processo) -> None:
        
        """Desaloca uma única página de um processo da memória RAM, baseando-se em um dos algoritmos de troca de páginas."""
        
        paginacao = self.slt_paginacao.currentText()
        
        if paginacao == "LRU":
            tabelaPP = processo.getTabelaPaginas()
            
            for numeroPagina, status in tabelaPP:
                if status:
                    self.LDE.reorganizaLRU(pID, numeroPagina)
            no = self.LDE.removeLRU()
        elif paginacao == "FIFO":
            no = self.LDE.removeFIFO(pID)
        
        pIDR = no.getPID()
        numeroPaginaR = no.getNumeroPagina()
        
        for processo in lista_processos:
            if processo.getID() == pIDR:
                tabelaPP = processo.getTabelaPaginas()
                for i in range(len(tabelaPP)):
                    if tabelaPP[i][0] == numeroPaginaR:
                        tabelaPP[i][1] = False
                        
                        break
        
        removido = self.tabelaPaginas.removePagina(pIDR, numeroPaginaR)
        self.tabela_ram.setItem(removido//10, removido%10, None)
        
        self.alocaPaginaDisco(pIDR, numeroPaginaR)
        


    def alocaPaginaDisco(self, pID: int, numeroPagina: int) -> None:
        
        """Aloca uma única página na memória secundária (disco)."""
        
        posicao = self.areaTroca.alocaPagina(pID, numeroPagina)
        
        item_id = QTableWidgetItem(str(pID))
        self.tb_disco.setItem(posicao//15, posicao%15, item_id)
                
                

    def desalocaPaginaDisco(self, pID: int, numeroPagina: int) -> None:
        
        """DEsaloca uma única página da memória secundária (disco)."""
        
        posicao = self.areaTroca.desalocaPagina(pID, numeroPagina)
        self.tb_disco.setItem(posicao//15, posicao%15, None)
        
    
    
    def controleBotoes(self, boolean: bool) -> None:
        
        """Habilita ou desabilita todos os botões da aplicção."""
        
        self.bt_executar.setDisabled(boolean)
        self.bt_reiniciar.setDisabled(boolean)
        self.slt_escalonamento.setDisabled(boolean)
        self.slt_paginacao.setDisabled(boolean)
        self.box_delay.setDisabled(boolean)
        self.le_quantum.setDisabled(boolean)
        self.lineEdit_2.setDisabled(boolean)
        
        
        
    def executar(self) -> None:
        
        """Recupera as informações que foram armazenadas e inicia a aplicação."""
        
        opcao = self.slt_escalonamento.currentText()
        
        self.controleBotoes(True)
        
        if opcao == "FIFO":
            
            self.executarFifo()
        elif opcao == "SJF":
            self.executarSJF()
        else:
            quantum = self.le_quantum.text()
            sobrecarga = self.lineEdit_2.text()
            paginacao = self.slt_paginacao.currentText()
            
            if quantum.strip() == "" or sobrecarga.strip() == "" or paginacao == "- Selecione -":
                pass
            else:
                quantum = int(quantum)
                sobrecarga = int(sobrecarga)
                if opcao == "EDF":
                    self.executarEDF(sobrecarga, quantum, paginacao)
                elif opcao == "Round Robin":
                    self.executarRoundRobin(sobrecarga, quantum, paginacao)
                else:
                    pass
        
        self.bt_reiniciar.setDisabled(False)
        self.bt_reiniciar.clicked.connect(lambda: self.controleBotoes(False))            
    
    
    
    def cadastrarProcesso(self) -> None:
        
        """Cadastra um novo processo e o adiciona à lista de processos."""
        
        chegada = self.le_chegada.text()
        execucao = self.le_execucao.text()
        deadline = self.le_deadline.text()
        prd = self.lineEdit_6.text()
        pagina = self.le_qtdpaginas.text()
        
        try:
            if int(pagina) < 11:
                p = Processo(self.id, int(chegada), int(execucao), int(deadline), int(prd), int(pagina))
                
                self.processos.append(p)
                
                self.items+= 1
                
                
                self.tableWidget.setRowCount(self.items)
                
                item_id = QTableWidgetItem(str(self.id))
                item_chegada = QTableWidgetItem(chegada)
                item_execucao = QTableWidgetItem(execucao)
                item_prioridade = QTableWidgetItem(prd)
                item_deadline = QTableWidgetItem(deadline)
                item_paginas = QTableWidgetItem(pagina)
                self.id += 1
                
                
                self.tableWidget.setItem(self.items-1, 0, item_id)
                self.tableWidget.setItem(self.items-1, 1, item_chegada)
                self.tableWidget.setItem(self.items-1, 2, item_execucao)
                self.tableWidget.setItem(self.items-1, 3, item_deadline)
                self.tableWidget.setItem(self.items-1, 4, item_prioridade)
                self.tableWidget.setItem(self.items-1, 5, item_paginas)
            
                
                self.le_deadline.clear()
                self.le_qtdpaginas.clear()
                self.le_execucao.clear()
                self.le_chegada.clear()
                self.lineEdit_6.clear()
                self.label_id.setText(f"ID = {self.id}")
            else:
                self.le_qtdpaginas.clear()
        except:
            pass
        
        
        
    def leftMenu(self) -> None:
        
        """Abre o menu das opções Home, Criar, Executar e Sobre."""
        
        width = self.left_container.width()
        
        if width == 9:
            newWidth = 200
        else:
            newWidth = 9
            
        self.animation = QtCore.QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        
        
    
if __name__ == "__main__":

    app = QApplication(sys.argv)
    icone = QIcon(u":/icons/icons/logo.png")
    app.setWindowIcon(icone)
    window = MainWindow()
    window.setWindowIcon(icone)
    window.show()
    sys.exit(app.exec())
    