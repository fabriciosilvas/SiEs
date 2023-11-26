# SiEs: 

SiEs é um sistema que simula o escalonamento de processos de um sistema operacional. 

Ele foi construído em Python, com o uso da biblioteca PySide6. Sua interface foi construída utilizando o programa QtDesigner.

## Algoritmos
Nesse sistema, são utilizados os seguintes algoritmos de escalonamento:

1. FIFO (_First In, First Out_)
2. SJF (_Shortest Job First_)
3. Round Robin
4. EDF (_Earliest Deadline First_)

Para a realização da substituição de páginas, são disponibilizados os seguintes algoritmos:

1. FIFO (_First In, First Out_)
2. LRU (_Least Recently Used_)


## Como utilizar
A utilização do SiEs é bastante simples:
1. Crie processos na página Criar
2. Execute o sistema na aba Executar


## Criação de processos
Para criar seus processos, adicione as informações que são solicitadas.
Algumas observações importantes:
1. O ID do processo é atribuído automaticamente
2. O número máximo de páginas que um processo pode ter é 10
3. Insira apenas valores inteiros

Ao preencher todas as informações, aperte no botão _Criar processo_.

Você pode ver todos os seus processos criados na janela _Processos criados_, dentro da aba _Criar_. 

Além disso, é possível excluir um processo criado. Para isso, selecione o processo que você quer excluir clicando nele e aperte no botão _Excluir_.


## Execução do sistema
Na aba de execução (_Executar_), você pode selecionar o algoritmo de escalonamento desejado.

Para os algoritmos Round Robin e EDF, é obrigatório preencher os campos _Quantum, Sobrecarga_ e selecionar o algoritmo de substituição de páginas.

O delay vai permitir uma melhor visualização da execução. Seu valor deve estar entre o intervalo 0.25 e 5.0.

Além disso, as abstrações de memória (principal e secundária) vão permitir a visualização da posição das páginas no sistema. Cada página vai ser representada pelo ID do processo que a contém.

Na CPU, você poderá ver quais processos estão na espera para serem executados e qual o processo que está em execução naquele momento. Para isso, basta observar o campo _ID_, logo abaixo da barra de progresso de execução.


## Gráfico de Gant
O gráfico de Gaant mostra a execução dos processos. À esquerda ficam os IDs dos processos e à direita, o gráfico em si.

A cor **amarela** significa que o processo está aguardando na fila de prontos.

A cor **verde** mostra que o processo está executando na CPU.

A cor **laranja** representa a sobrecarga.

A cor **vinho** significa que o processo ultrapassou o seu deadline.

Observação: o processo continua a executar, mesmo que tenha estourado seu deadline.


## Turnaround
Ao fim da execução, uma janela será aberta, exibindo o turnaround. Caso ela não esteja visível, verifique se ela não abriu por detrás da janela principal.

## Novas execuções
Ao terminar a primeira execução, os processos continuam armazenados, portanto é possível executar um novo algoritmo sem a necessidade de inserir todas as informações novamente.
Contudo, para executar mais uma vez, é necessário limpar a cena que contém o gráfico, portanto é necessário apertar no botão _Reiniciar_.

