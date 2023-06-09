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

Para obter as sequências que nós vamos trabalhar neste tutorial, clone este repositório.

```
git clone https://github.com/rafaeliwama/filogenetica_tutorial.git 
```

### Sequências de aminoácidos

Uma coisa importante de se ter em mente é algumas diferenças entre análises com sequências de aminoácidos e sequências de nucleotídeos:

Aminoácidos são codificados por codons, compostos por três nucleotídeos. O código genético pode ser consultado abaixo:

![f5de6355003ee322782b26404ef0733a1d1a61b0](https://user-images.githubusercontent.com/46658489/228330276-789a0ff6-e25f-46ea-8b3b-3f7d5efeb700.png)

Preste atenção no segundo nucleotídeo de cada códon. A primeira coisa que se nota, é q o código genético é redundante, ou seja, mais de um códon codifica um amino ácido. A segunda coisa é que mutações no terceiro nucleotídeo de cada códon, raramente resultam em uma mudança no amino ácido codificante.

Estas duas características do código têm implicações importantes para as análises filogenéticas. Primeiro, informações são perdidas quando usamos sequências de proteínas pois não podemos distinguir qual códon codifica um amino ácido. Segundo, o segundo nucleotídeo de cada códon está sob menos intensidade de seleção e está mais livre para mutar, já que há pouca probabilidade de que esta mutação resulte em uma mudança na sequência da proteína. Regiões com menos seleção guardam mais informação filogenética.

**Pergunta:** Pq seleção seria um problema para análises filogenéticas?

## Alinhamento

No exemplo acima, em que as sequências de nucleotídeos variam de tamanho, é facil de entender o que aconteceu durante a evolução destes dois loci. É obvio que houve um indel. Porém, a realidade é bem diferente. Sequências maiores, com mais indels, e SNPs acabam sendo muito mais difícil de estabelecer homologia entre os nucleotídeos. Para isso, nós temos softwares que fazem o que nós chamamos de alinhamento.

Um desses softwares é o MAFFT (Katoh et al 2002), que ainda é o algoritmo que tem a melhor performance quanto à precisão.

**Ver:** https://academic.oup.com/bioinformatics/article/23/19/2648/187079?login=true

Para utilizar o MAFFT, nós podemos utilizar a versão online. Isso é bom quando você precisar alinhar matrizes pequenas, porque é bem rápido e é possível visualizar rapidamente os resultados.

Vá para o site em que o MAFFT está hospedado: https://mafft.cbrc.jp/alignment/server/

**Atividade:** 
- Abra o arquivo 'tess_Hirudin.unal.fasta' em um editor de plain text. Eu recomendo o Sublime (https://www.sublimetext.com/). Existem editores de textos nativos do Windows e outros sistemas operacionais. Eles servem, mas outros editores de texto têm mais funcões que você pode utilizar depois.

- Analise o arquivo. Qual o formato do arquivo? Qual tipo de sequência este arquivo contém? O tamanho das sequências é igual ou são diferentes?

- Copie e cole o conteúdo deste arquivo no campo input da pagina do MAFFT

![Screenshot from 2023-03-29 13-18-00](https://user-images.githubusercontent.com/46658489/228595065-e9833dc0-7814-423f-8a21-a6193b39e867.png)

- No 'Advaced Settings' deixe a opção 'auto' selecionada. Cada uma dessas opções são algorítmos que utilizam estratégias diferentes de optimização do alinhamento. A descrição de cada algorítmo está disponível no manual e em diferentes publicações.

![Screenshot from 2023-03-29 13-22-34](https://user-images.githubusercontent.com/46658489/228596372-6641aa2b-c47f-4951-afd1-cbfcbdeb94b8.png)

- Escolha o modelo utilizado para optimizar o alinhamento: BLOSUM62. Basicamente, o modelo é utilizado para computar qual a probabilidade de se obter um determinado alinhamento. O alinhamento com maior probabilidade em relação ao modelo dado é selecionado. No caso do BLOSUM62, a probabilidade de cada substituição de aminoácidos (ex. Ser para Gly) foram calculados utilizando uma base de dados de alinhamentos bem estabelecidos que, supostamente, representa a maior parte dos organismos. O importante de deixar claro, é que estas matrizes de substituição (modelos) de proteínas, são obtidos a partir de alinhamentos que nós conseguimos confiar, e que essas matrizes descrevem as probabilidades de substituição para cada par de aminoácidos. Isso é dificil de entender, mas eu posso te explicar melhor pessoalmente!

- O 'gap opening penalty' é a penalidade no likelihood de cada substituição por um indel. O que você acha menos provavel de acontecer, um SNP ou um INDEL? E pq?

![Screenshot from 2023-03-29 13-26-51](https://user-images.githubusercontent.com/46658489/228602494-2f9e243d-dc72-4bdf-aae0-565d428edadc.png)

- Submeta a corrida.

Para fazer o download dos resultados em fasta clique na opção correspondente. Para visualizar os resultados, clique em view.


**Atividades:** Observe os resultados do arquivo gerado pelo MAFFT. Quantos 'gaps' foram adicionados? Qual o tamanho das sequências? Elas têm tamanho igual ou diferente? Você acha que é possível diferenciar inserções e deleções?

Este arquivo alinhado contém as informações que vão compor a matrix.


## Parsimônia com TNT

O TNT (Goloboff, 1999) é um software interessante. Ele foi bastante inovador, principalmente por aprimorar as estratégias de procura de árvores e alguns dos algorítmos introduzidos pelo TNT


O primeiro passo é fazer o download do TNT e descomprimir o diretório.

```
wget https://www.lillo.org.ar/phylogeny/tnt/tnt-linux.zip
unzip tnt-linux.zip
```

Antes de começar, acesse o site do TNT para consultar o manual (https://www.lillo.org.ar/phylogeny/tnt/).

É. Realmente não tem manual. Esse é o pior programa que você vai usar e ele foi feito assim propositalmente.

O TNT usa um formato de arquivo específico para as matrizes que são utilizadas como input. Esse formato se chama Hennig86 e é a coisa mais inútil que vc vai aprender na vida.


O formato básico do arquivo é:

```
xread ‘optional title, starting and ending with quotes (ASCII 39)’
nchar ntax
Taxon0 0000000000
Taxon1 0010111000
Taxon2 1011110000
Taxon3 1111111000
…..
TaxonN 1111111000
; ‘<- Note the semicolon (and the way you add comments)!’
```
Onde:

nchar - número de caracteres
ntax - número de táxons

Para especificar que você está trabalhando com sequências de amino ácidos, inclua a linha ```nstates prot;``` no topo do documento. Para nucleotídeos, adicione ```nstates dna;```


Mas calma, você não precisa fazer isso à mão!

Vários softwares fazem essa conversão de forma automática. Por exemplo

Neste caso, os estados de caractere são 0 e 1 (caracteres morfológicos), mas você vai usar nucleotídeos de amino ácidos.













