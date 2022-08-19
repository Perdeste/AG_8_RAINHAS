# INTELIGÊNCIA ARTIFICIAL - PROBLEMA DAS 8 RAINHAS

## O PROBLEMA DAS 8 RAINHAS
O problema das oito damas é o problema matemático de dispor oito damas em um tabuleiro de xadrez de dimensão 8x8, de forma que nenhuma delas seja atacada por outra. Para tanto, é necessário que duas damas quaisquer não estejam numa mesma linha, coluna, ou diagonal.
Este trabalho tem como objetivo resolver o problema das 8 rainhas, a partir de técnicas de algoritmos genéticos.

## ALGORITMOS GENÉTICOS
Os algoritmos genéticos são métodos computacionais que têm como objetivo encontrar soluções satisfatórias para problemas de busca e otimização, no qual são inspirados nos mecanismos de evolução natural e recombinação genética (princípio Darwiniano de reprodução e sobrevivência dos mais aptos). 
Estes mecanismos são imitados a partir de um processo evolucionário que envolve avaliação, seleção, recombinação sexual (crossover através de cromossomos artificiais) e mutação, para que no fim de vários ciclos (chamado de gerações) a população deverá conter os indivíduos mais aptos (o que melhor atende a função objetiva).

## OPERADORES GENÉTICOS
A seguir descrevemos quais operadores genéticos que foram adotados para o desenvolvimento do trabalho.
- **Inicialização da população**: geração aleatória de um array de 8 posições constituidos por tuplas (coluna, linha) que representam a posição da rainha no tabuleiro;
- **Avaliação**: a função objetiva do problema é de minimização, onde cada vez que a rainha esteja em conflito com outra o valor da função aumenta.
- **Seleção**: utilizamos o método da roleta;
- **Cruzamento**: utilizamos como operador de cruzamento o OX2;
- **Mutação**: trocamos a posição de uma das rainhas para uma das casas vazia. Sua probabilidade é pequena;
- **Busca Local**: utilizamos o algoritmo de busca local para gerar novos indivíduos mais aptos rapidamente;
- **Atualização**: utilizamos o critério de elitismo para gerar a nova população.
