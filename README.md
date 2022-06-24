# Projeto House Rocket Company (ficticio) 


Este é um projeto fictício, feito segundo as recomendações do blog Seja um Data Scientist. A empresa, o contexto e as perguntas de negócios não são reais.  

​ A logo criada é ficticia.

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




