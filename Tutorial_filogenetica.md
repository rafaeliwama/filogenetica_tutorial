# Turorial de Filogenética

![Screenshot from 2023-03-23 12-18-20](https://user-images.githubusercontent.com/46658489/227241456-9cfdadff-aa85-4857-83be-40bb7c4cb84e.png)

O poema acima foi gerado pelo ChatGTP.

O poema conta um pouco sobre o como eram os congressos de filogética, principalmente (pelas fofocas que o pessoal conta) dos encontros Willi Hennig Society até o começo da década de 90. Nestes encontros a principal discussão era a validade dos resultados de análises filogenéticas utilizando dois critérios, parsimômia e likelihood.

**Pergunta:** Qual o cenário que o poema descreve? Um cenário de colaboração ou de disputa?

Neste tutorial você vai aprender análises filogenéticas utilizando dois critérios: parsimônia e likelihood. Você nunca vai usar parsimônia, pq parsimônia não quer dizer NADA!! Mas vou ensinar mesmo assim, só para mostrar como o pessoal que ainda insiste em parsimônia é meio doido.


Antes de começar o tutorial, eu estou assumindo que você lembre alguns conceitos básicos de filogenética. Principalmente para a parsimônia, pois é a metologia que normalmente se ensina em cursos de graduação.

## Parsimônia

Na parsimônia, o processo e o conceito é muito simples. Basicamente, o conceito da 'Navalha de Ockham' é utilizado para avaliar diferentes hipóteses filogenéticas. Utilizando este princípio, a hipótese filogética que requer o menor número de passos seria a hipótese mais parcimoniosa e, consequetemente, a hipótese mais provável.

Esta abordagem tem vários pontos positivos, mas eu quero detalhar duas principais. A primeira é que inovações evolutivas observáveis são raras, e a fixação de um determinado caractere é mais raro ainda. Desta forma, faz sentido utilizar a navalha de Ockham como princípio para a construção de árvores filogéticas. O segundo ponto positivo é que como não existe modelagem no processo de construção de árvores com parsimônia, as hipóteses geradas com parsimônia são facilmente falseadas. E lembra que o falseamento é fundamental na ciência.

Eu vou explicar melhor:

Pense no modo de argumentação de um terra planista. A medida que você argumenta contra, argumentos cada vez mais complexos e absurdos surgem até que chega um ponto onde a cartada final é dada: Mas a NASA ... 

O argumento 'Mas a NASA ...' possui alta complexidade, pois tudo pode acontecer. 
   - Os funcionários da NASA podem ter ocultado
 
   - A NASA materia quem quisesse falar a verdade

   - A NASA tem poder para manipular o que quiser

Estes argumentos, de tão complexos, impossibilitam uma característica importante da ciência que é a de fazer previsões do que pode e o que não pode acontecer em um determinado cenário.

Estas previsões têm um papel fundamental na metodologia científica, pois elas possibilitam os testes de hipóteses. E estes testes são tentativas de falsear uma hipótese. Então, não é muito difícil de entender que é mais fácil de falsear hipóteses menos complexas.

Ta bom, mas agora vamos começar com o tutorial:

## Dataset
Nós vamos utilizar como dataset, sequências de aminoácidos de Hirudina, que anticoagulantes potentes.

Você já deve ter feito alguma atividade de codificar characteres em uma matrix para alguma aula de filogenética. Com dados de sequências, cada uma das posições na sequência é considerado um caractere.

Por exemplo:

![Screenshot from 2023-03-28 14-50-36](https://user-images.githubusercontent.com/46658489/228319084-c6d7497e-657c-4cc2-8c0a-12925e1b9500.png)

Nesta imagem nós temos sequências de nucleotídeos para duas espécies. Você pode perceber que cada posição na sequência é um caractere e cada nucleotídeo é um estado.

Os nucleotídeos em vermelho demonstram divergências nas duas sequências. Esse tipo de divergência são chamadas de SNPs (Single Nucleotide Polymorphism). Este tipo de mutação são as mutações que contém informação filogenética relevante.

Neste caso, as duas sequências possuem exatamente o mesmo número de nucleotídeos, mas o que você acha que aconteceria com sequências com tamanho diferente.

Por examplo:

Seq. 1: AACTTCGGA

Seq. 2: ACTTCGGA

**Pergunta:** Como você acha que nós poderíamos codificar essa sequência em uma matrix?
Obviamente, o segundo 'A' sofreu uma deleção em algum momento da evolução entre a divergência das duas sequências. Nós chamamos esse estado de caractere de 'gap' e ele é codificado da seguinte maneira:

![Screenshot from 2023-03-28 15-23-40](https://user-images.githubusercontent.com/46658489/228326335-4c1a8567-08ad-445f-9256-a1c237ed3197.png)

Gaps são resultantes de INDELs (INsertions or DELetions). Este tipo de mutação não contém informação filogenética relevante, pois é impossível distinguir deleções e inserções.

Em quase todos os casos reais, as sequências que nós vamos utilizar dados com alguns indels. Quanto menos indels, melhor será sua análise.

### Sequências de aminoácidos

Uma coisa importante de se ter em mente é algumas diferenças entre análises com sequências de aminoácidos e sequências de nucleotídeos:

Aminoácidos são codificados por codons, compostos por três nucleotídeos. O código genético pode ser consultado abaixo:

![f5de6355003ee322782b26404ef0733a1d1a61b0](https://user-images.githubusercontent.com/46658489/228330276-789a0ff6-e25f-46ea-8b3b-3f7d5efeb700.png)

Preste atenção no segundo nucleotídeo de cada códon. A primeira coisa que se nota, é q o código genético é redundante, ou seja, mais de um códon codifica um amino ácido. A segunda coisa é que mutações no segundo amino ácido de cada códon, raramente resultam em uma mudança no amino ácido codificante.

Estas duas características do código têm implicações importantes para as análises filogenéticas. Primeiro, informações são perdidas quando usamos sequências de proteínas pois não podemos distinguir qual códon codifica um amino ácido. Segundo, o segundo nucleotídeo de cada códon está sob menos intensidade de seleção e está mais livre para mutar, já que há pouca probabilidade de que esta mutação resulte em uma mudança na sequência da proteína. Regiões com menos seleção guardam mais informação filogenética.

**Pergunta:** Pq seleção seria um problema para análises filogenéticas?





## Alinhamento





O primeiro passo é fazer o download do TNT e descomprimir o diretório (Goloboff, 1999).

```
wget https://www.lillo.org.ar/phylogeny/tnt/tnt-linux.zip
unzip tnt-linux.zip
```

Antes de começar, acesse o site do TNT para consultar o manual (https://www.lillo.org.ar/phylogeny/tnt/).

É. Realmente não tem manual. Esse é o pior programa que você vai usar e ele foi feito assim propositalmente.











