# Projeto House Rocket Company (empresa ficticia) 


<p align="center">
<img src="https://user-images.githubusercontent.com/103456938/178109527-f79fd8d1-f1ea-44af-9664-193fdd01f915.jpeg"/>
</p>

Este é um projeto de análise de dados de uma empresa fictícia, feito segundo as recomendações do blog Seja um Data Scientist. A empresa, o contexto e as perguntas de negócios não são reais.  

O objetivo desse projeto é fornecer uma seleção de imóveis para o time de negócios, para que a empresa possa realizar suas operações de compra e venda. Os insights deste projeto buscam o valor de lucro máximo que a empresa pode obter.

A ferramenta de visualização utilizada nesse projeto - Streamlit, permitirá que a empresa possa visualizar esse resultado de forma gráfica e tabular. O resultado geral obtido foi uma seleção de __10642 imóveis__ (podendo ser variável de acordo com as condições/localizações).

Link para visualização:  [<img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>](https://insight-house-rocket.herokuapp.com/)

## 1. A House Rocket

### 1.1 Contexto do negócio:

A House Rocket é uma plataforma digital que tem como modelo de negócio, a compra e a venda de imóveis usando a tecnologia para analisar suas melhores oportunidades.

O objetivo do projeto é fornecer insights para o time de negócio encontrar as melhores oportunidades no mercado de imóveis. A principal estratégia é ***comprar boas casas*** em ótimas localizações com preços baixos e depois revendê-las com preços mais altos. 

As casas possuem muitos atributos que as tornam mais ou menos atrativas aos compradores e vendedores, a localização e o período do ano também podem influenciar os preços.


### 1.2 Questão do negócio:

O projeto busca responder às seguintes perguntas de negócio, feitas pelo CEO da empresa:

- Quais são os imóveis que a House Rocket deveria comprar e por qual preço ?
- Uma vez a casa comprada, qual o melhor momento para vendê-las e por qual preço ?

O objetivo desse projeto é fornecer uma seleção de imóveis, para que a empresa possa realizar suas operações de compra e venda. 
O planejamento é demonstrar através de visualizações, quais as melhores oportunidades e qual resultado (lucro) máximo que pode ser alcançado.

### 1.3 Sobre os dados:

Os dados podem ser encontrados em: https://www.kaggle.com/harlfoxem/housesalesprediction, onde constam todos os imóveis do portfólio e disponíveis para a empresa.

Abaixo segue a descrição de cada um dos atributos apresentados:

|***Atributo*** | ***Descrição*** |
| -------- | --------- |
|**id** | Numeração única de identificação de cada imóvel |
|**date** | Data da venda da casa |
|**price** | Preço que a casa está sendo vendida pelo proprietário |
|**bedrooms** | Número de quartos |
|**bathrooms** | Número de banheiros (0.5 = banheiro em um quarto, mas sem chuveiro) |
|**sqft_living** | Medida (em pés quadrado) do espaço interior dos apartamentos |
|**sqft_lot** | Medida (em pés quadrado)quadrada do espaço terrestre |
|**floors** | Número de andares do imóvel | 
|**waterfront** | Variável que indica a presença ou não de vista para água (0 = não e 1 = sim) | 
|**view** | Um índice de 0 a 4 que indica a qualidade da vista da propriedade. Varia de 0 a 4, onde: 0 = baixa 4 = alta | 
|**condition** | Um índice de 1 a 5 que indica a condição da casa. Varia de 1 a 5, onde:1 = baixo 5 = alta | 
|**grade** | Um índice de 1 a 13 que indica a construção e o design do edifício. Varia de 1 a 13, onde: 1 - 3 = baixo, 7 = médio e 11 - 13 = alta | 
|**sqft_basement** | A metragem (em pés quadrado) quadrada do espaço habitacional interior acima do nível do solo | 
|**yr_built** | Ano de construção de cada imóvel | 
|**yr_renovated** | Ano de reforma de cada imóvel | 
|**zipcode** | CEP da casa | 
|**lat** | Latitude | 
|**long** | Longitude | 
|**sqft_livining15** | Medida (em pés quadrado) do espaço interno de habitação dos 15 vizinhos mais próximo | 
|**sqft_lot15**| Medida (em pés quadrado) dos lotes de terra dos 15 vizinhos mais próximo | 


## 2. Premissas do projeto

Para a execução deste projeto algumas premissas foram adotadas, sendo elas:

* Os valores iguais a zero em yr_renovated são casas que nunca foram reformadas;
* O valor igual a 33 na coluna bathroom foi considerada um erro e por isso foi deletada das análises. Possivelmente poderia ser um erro de digitação, mas por falta dessa clareza, a exclusão foi optada;
* A coluna price significa o preço que a casa foi ou será comprada pela empresa House Rocket;
* Valores duplicados em id foram removidos e considerados somente a compra mais recente;
* Dado que a localidade e a condição são os principais fatores que influenciam na valorização ou desvalorização dos imóveis, essas foram características decisivas na seleção ou não dos imóveis;
* Para as condições dos imóveis, foi determinada a seguinte classificação: 1 e 2 = bad, 3 e 4 = regular e 5 = good;
* Como a sazonalidade também influencia diretamente a demanda por investimento em imóveis, a estação do ano foi decisiva para a época da venda do imóvel; 
* O time de negócios aplicará o percentual de 30% sobre o valor dos imóveis que forem comprados abaixo do valor mediano da região + sazonalidade, e de 10% nos imóveis comprados acima do valor mediano da região + sazonalidade; e
* Embora os dados de 'sqft_living15' e 'sqft_lot15', sejam relevantes no cenário global, neste momento optou-se pela sua exclusão, uma vez que muito pouco poderiam contribuir para o atual projeto.

## 3.Planejamento da Solução

### 3.1. Coleta e Exploração dos dados

A primeira etapa do projeto foi a coleta dos dados através da plataforma Kaggle (https://www.kaggle.com/datasets/harlfoxem/housesalesprediction), e posterior tratamento e exploração dos mesmos. Nessa etapa foi possível identificar necessidades de limpeza e transformação de dados, e ainda realizar a criação de novas *features* para facilitar e proporcionar as visualizações e criações dos insights apresentados. 

### 3.2. Seleção dos imóveis

Para iniciar a seleção dos imóveis, foram realizados os seguintes passos para cada pergunta de negócio:

__a) Quais são os imóveis que a House Rocket deveria comprar e por qual preço ?__
- Agrupar os imóveis por região ( *zipcode* );
- Dentro de cada região, foi encontrada a mediana do preço do imóvel;
- Essa mediana foi retornada em cada linha do dataset para ser possível a comparação;
- Foi assumida a seleção dos imóveis que estão abaixo do preço mediano da região e que estejam em boas condições - *condition* 'regular' ou  'good';
- Então foi criada uma feature auxiliar para receber a indicação de compra ou não compra do imóvel. Ou seja, se o imóvel estiver com preço abaixo da mediana da região e, estiver em condição “regular” ou “good” , o imóvel é selecionado.

__b) Uma vez a casa comprada, qual o melhor momento para vendê-las e por qual preço ?__
- Agrupar os imóveis selecionados na questão 1 por região ( *zipcode* ) e também por temporada (*season*);
- Dentro de cada região e temporada, foi encontrada a mediana do preço do imóvel;
- Para cálculo do valor de venda, foram assumidas as seguintes condições, as quais foram aplicadas em novas features criadas - ***sale e profit:***

   1. Se o preço da compra for maior que a mediana da região + sazonalidade. O preço da venda será igual ao preço da compra + 10%
   2. Se o preço da compra for menor que a mediana da região + sazonalidade. O preço da venda será igual ao preço da compra + 30%

## 4. Hipóteses 

|***Hipótese*** | ***Validação*** | ***Significado para o negócio*** |
| -------- | --------- | --------- |
| H1: Imóveis que possuem vista para água, são, em média, 30% mais caros. | Falsa | Imóveis com vista para água são 212% mais caros. Procurar investir em imóveis sem vista para água, por terem custo de negócio menor | 
| H2: Imóveis com data de construção menor que 1955, são 50% mais baratos, na média. | Falsa | Data de construção não é significativo para formação do preço |
| H3: Imóveis sem porão possuem área total ('sqrt_lot') 50% maiores do que imóveis com porão. | Falsa | Imóveis sem porão tem área total, em média, 22.78% maiores do que os imóveis sem porão |
| H4: O crescimento do preço dos imóveis YoY ( Year over Year ) é de 10%. | Falsa | O período analisado teve preços médios próximos, com variação de apensa 0,18%, sendo irrelevante para estudo |
| H5: O crescimento do preço dos imóveis MoM ( Month over Month ) é de 5%. | Falsa | A variação mensal é de 2% para mais ou para menos tanto nos meses do ano de 2014 quanto de 2015, portanto não apresenta variação significativa para analise |
| H6: Imóveis com 3 banheiros tem um crescimento MoM ( Month over Month ), no ano de 2015 de 15%. | Falsa | O crescimento MoM não é significativo para imóveis com mais banheiros, assim como para os demais |
| H7: Imóveis reformados são, em média 40% mais caros que os imóveis não reformados. | Verdadeira | Imóveis reformados são, em média 43.29% mais caros que os não reformados, portanto reformas nos imóveis adiquiridos devem ser consideradas |
| H8: Imóveis anteriores a 1955 e não renovados são 5% mais baratos. | Verdadeira | Imóveis com data de construção anterior à 1955 e não reformados são, em média 5.19% mais baratos, o que significa que quando adiquirido imóvel com data de construção anterior a 1955 a reforma deve ser considerada |
| H9: Imóveis em más condições (condition_type = bad) mas com boa vista, são 25% mais caros. | Verdadeira | Imóveis em más condições e com boa vista são, em média 26.14% mais caros que imóveis com más condições e com vista ruim, portanto quanto se investir em imóveis em más condições, priorizar os com boa vista. |
| H10: Imóveis com número de quartos maior são 5% mais caros. | Verdadeira |  A variação de preço com relação ao número de quartos é proporcional |


## 5. Insights de dados




## 6. Resultado financeiro

O objetivo desse projeto é fornecer uma lista de imóveis com opções de compra e venda, para obtenção do __lucro máximo__ que poderá ser obtido se todas as sugestões ocorrerem. O resultado financeiro apresentado representa o lucro máximo que pode ser obtido utilizando as recomendações informadas.

| __Número de imóveis__ | __Custo total__ | __Receita de vendas__ | __Lucro (profit)__ |
| ----------------- | ----------------- | ----------------- | ----------------- |
| 10.642 | US$ 4.142.197.223,00 | US$ 5.384.352.389,90 | US$ 1.242.155.166,90 |

Entretanto o lucro pode ser explorado por condições e região dos imóveis, onde as visualizações fornecidas demonstram todo resultado do projeto, assim como o resultado financeiro, de forma customizada para as opções escolhidas.

## 6. Conclusão

O projeto teve o foco de gerar insights para o negócio, assim como responder algumas perguntas da empresa. O objetivo central foi atingido, sendo possível extrair informações relevantes e com potencial de gerar direcionamento para a empresa.




