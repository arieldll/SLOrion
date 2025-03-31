<h1>SLOrion - Democratização das Redes 6G através de Contratos Inteligentes e Fatiamento de Rede Como Serviço</h1>
A centralização e o monopólio global de operadoras de redes móveis representam barreiras significativas para a evolução das redes 6G, limitando a flexibilidade e a interoperabilidade necessárias para atender a serviços avançados de próxima geração. O conceito de fatiamento de rede surge como uma abordagem promissora para superar esses desafios, permitindo a criação de fatias configuráveis para diferentes requisitos. Este artigo apresenta SLOrion, uma solução descentralizada baseada em contratos inteligentes e Distributed Ledger Technology. A proposta automatiza a tradução de Service Level Agreements em parâmetros técnicos para fatiamento de rede como serviço, reduzindo a intervenção manual, promovendo a interoperabilidade e assegurando a integridade das configurações de rede. SLOrion endereça lacunas existentes na literatura ao conectar contratos inteligentes diretamente às configurações técnicas de redes móveis, contribuindo para a democratização das redes 6G. 
Os resultados demonstram que o SLOrion mantém mais de 90% de precisão e um tempo de resposta até mil vezes menor que o modelo da OpenAI, garantindo escalabilidade para redes 5G e 6G.

<h3>Método</h3>

Sem um mecanismo de robustez linguística, a identificação das intenções das operadoras exigiria que elas conhecessem detalhadamente todos os nomes dos parâmetros no arquivo de fatiamento, o que é pouco viável em operações reais, onde terminologias podem mudar e surgir novas nomenclaturas ao longo do tempo.
Para enfrentar esse desafio, o SLOrion emprega o coeficiente de similaridade de Dice, que utiliza bigramas para medir a similaridade entre duas palavras. 
Bigramas são sequências de dois caracteres consecutivos extraídas de uma string, que quando comparadas, resultam em um coeficiente entre 0 e 1, onde valores mais altos indicam maior semelhança.

![image](https://github.com/user-attachments/assets/531de3c4-be7d-4322-aeed-39da8a84599a)


<h2>Resultados Preliminares</h2>

![image](https://github.com/user-attachments/assets/c46ef5a1-e18c-4077-a76b-bc3686fe5d1f)


<h2>Comparação com a OpenAI</h2>


![image](https://github.com/user-attachments/assets/8c1819b6-54a4-4ef4-9b92-a81b0be2ed8d)

<h2>Conclusões</h2>

Os resultados demonstram que SLOrion é capaz de entregar respostas rápidas, com tempos de processamento na casa de 41 ms mesmo no pior cenário, quando há 40 intenções de parâmetros. Essa eficiência computacional destaca o método como uma solução viável para sistemas que exigem agilidade e alta escalabilidade, mantendo tempos de resposta consistentes mesmo em contextos de maior complexidade. Tal característica torna o SLOrion adequado para aplicações em tempo real, onde o desempenho é um fator crítico.

