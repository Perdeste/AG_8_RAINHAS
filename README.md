# INTELIGÊNCIA ARTIFICIAL - PROBLEMA DAS 8 RAINHAS

## O PROBLEMA DAS 8 RAINHAS
O problema das oito damas é o problema matemático de dispor oito damas em um tabuleiro de xadrez de dimensão 8x8, de forma que nenhuma delas seja atacada por outra. Para tanto, é necessário que duas damas quaisquer não estejam numa mesma linha, coluna, ou diagonal.
Este trabalho tem como objetivo resolver o problema das 8 rainhas, a partir de técnicas de algoritmos genéticos.

## ALGORITMOS GENÉTICOS
Os algoritmos genéticos são métodos computacionais que têm como objetivo encontrar soluções satisfatórias para problemas de busca e otimização, no qual são inspirados nos mecanismos de evolução natural e recombinação genética (princípio Darwiniano de reprodução e sobrevivência dos mais aptos). 
Estes mecanismos são imitados a partir de um processo evolucionário que envolve avaliação, seleção, recombinação sexual (crossover através de cromossomos artificiais) e mutação, para que no fim de vários ciclos (chamado de gerações) a população deverá conter os indivíduos mais aptos (o que melhor atende a função objetiva).

## OPERADORES GENÉTICOS
A seguir descrevemos quais operadores genéticos que foram adotados para o desenvolvimento do trabalho.
- **Inicialização da população**: o individuo sera representado por um array de 8 posições, com os indices representando a linha e o seu conteudo a coluna do tabuleiro. Os individuos serão gerados de forma aleatória;
- **Avaliação**: a função objetiva do problema é de minimização, onde cada vez que a rainha esteja em conflito com outra o valor da função aumenta;
- **Seleção**: utilizamos o método da roleta;
- **Cruzamento**: utilizamos como operador de cruzamento por meio de um corte ou um swap simples;
- **Mutação**: trocamos a posição de uma das rainhas para uma das casas vazia. Sua probabilidade é pequena;
- **Atualização**: utilizamos o critério de elitismo para gerar a nova população.

## COMO EXECUTAR?
Argumentos:
- **tipo_cruzamento (str)** = 'SWAP' ou 'CORTE';
- **geracoes (int)** = quantidade de gerações;
- **tam_populacao (int)** = tamanho da população inicial;
- **taxa_cruzamento (float)** = quantidade de individuos que serão utilizados para o cruzamento;
- **taxa_mutacao (float)** = probabilidade da ocorrência de mutação em um individuo;
- **taxa_sobrevivencia (float)** = quantidade de individuo da população atual que se manterão para a nova população;

Utilize o comando a seguir, substituindo os argumentos pelos seus respectivos valores desejados:
```
python ag_8_rainhas tipo_cruzamento geracoes tam_populacao taxa_cruzamento taxa_mutacao taxa_sobrevivencia
```
