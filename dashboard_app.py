import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(layout='wide')

image = Image.open('Ive.jpg')
st.sidebar.image(image)
st.sidebar.write('**Elaborado por:** Ivelise Vasallo Rondina')
st.sidebar.write('Projeto de estudo do curso de Análise de Dados - Python do zero ao DS, da Comunidade DS')
st.sidebar.write('Sinta-se a vontade para fazer contribuições.')
st.sidebar.write('**Contato:**\n'

                 '* email: ive.rondina@gmail.com;\n'
                 '* linkedIn: iveliserondina ')

st.title('Projeto Insights - House Rocket Company')
st.markdown('Seja bem vindo(a) ao projeto de analise de dados da empresa House Rocket')
st.header(' Sobre a Base de Dados')
st.markdown(
    ' A House Rocket é uma plataforma digital (fictícia) que tem como modelo de negócio, a compra e a venda de imóveis usando tecnologia. '
    'Sua principal estratégia é comprar boas casas em ótimas localizações com preços baixos e depois revendê-las posteriormente à preços mais altos. '
    'Quanto maior a diferença entre a compra e a venda, maior o lucro da empresa e portanto maior sua receita.')
st.markdown(
    'Entretanto, as casas possuem muitos atributos que as tornam mais ou menos atrativas aos compradores e vendedores '
    'e a localização e o período do ano também podem influenciar os preços. A seguir vou responder as seguintes perguntas:')
st.markdown('* Quais atributos de uma casa mais impactam no preço?')
st.markdown('* Quais são os imóveis que a House Rocket deveria comprar e por qual preço?')
#st.markdown('* A House Rocket deveria fazer reforma nos imóveis para aumentar o preço da venda? ')
st.markdown('* Uma vez a casa comprada, qual o melhor momento para vendê-las e por qual preço?')


@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])

    return data

def set_features(data):
    data['date'] = pd.to_datetime(data['date'])
    data['bathrooms'] = data['bathrooms'].astype(np.int64)
    data['floors'] = data['floors'].astype(np.int64)
    data['sqft_living15'] = data['sqft_living15'].astype(float)
    data['sqft_lot15'] = data['sqft_lot15'].astype(float)
    data['sqft_above'] = data['sqft_above'].astype(float)
    data['sqft_basement'] = data['sqft_basement'].astype(float)
    data = data.drop_duplicates(subset=['id'], keep='last')
    data = data.drop(15870)
    data['m2_living'] = data['sqft_living'] * 0.09290304
    data['m2_lot'] = data['sqft_lot'] * 0.09290304
    data['condition_type'] = data['condition'].apply(lambda x: 'bad' if x <= 2
                                                     else 'regular' if (x == 3) | (x == 4)
                                                     else 'good')
    data['built'] = data['yr_built'].apply(lambda x: 'anterior à 1955' if x <= 1955
                                            else 'posterior à 1955')
    data['basement'] = data['sqft_basement'].apply(lambda x: 'com porão' if x > 0 else 'sem porão')
    data['month'] = data['date'].dt.month
    data['year'] = data['date'].dt.year
    data['renovated'] = data['yr_renovated'].apply(lambda x: 'sim' if x > 0 else 'não')
    data['season'] = data['month'].apply(lambda x: 'spring' if 3 <= x <= 5 else
                                                   'summer' if 6 <= x <= 8 else
                                                    'autumn' if 9 <= x <= 11 else
                                                    'winter')
    return data

def overview_data(data):
    st.header('Exploração e análise dos dados')

    c1, c2 = st.columns((1, 1))
    num_attributes = data.select_dtypes(include=['int64', 'float64'])
    media = pd.DataFrame(num_attributes.apply(np.mean))
    mediana = pd.DataFrame(num_attributes.apply(np.median))
    std = pd.DataFrame(num_attributes.apply(np.std))
    max_ = pd.DataFrame(num_attributes.apply(np.max))
    min_ = pd.DataFrame(num_attributes.apply(np.min))

    statistic = pd.concat([max_, min_, media, mediana, std], axis=1).reset_index()
    statistic.columns = ['atributos', 'max', 'min', 'mean', 'median', 'std']

    c1.subheader('Estatística Descritiva')
    c1.dataframe(statistic, height=650)

    matrix = np.triu(data.corr())
    fig, ax = plt.subplots()
    sns.heatmap(data.corr(), cmap='pink', square=True, annot=True, annot_kws={"size": 4}, cbar_kws={"shrink": 1},
                center=0, mask=matrix)
    c2.subheader ('Impacto dos atributos no preço')
    c2.write(fig, use_container_width = False)

    return None

def hipotesis(data):
    st.header('Hipóteses de Negócio')
    c5, c6 = st.columns((1, 1))

    c5.subheader('H1: Imóveis que possuem vista para água, são, em média, 30% mais caros.')
    h1 = data[['price', 'waterfront']].groupby(['waterfront']).mean().reset_index()
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    sns.barplot(x='waterfront', y='price', data=h1, palette='Set2')
    plt.show()
    c5.pyplot(fig)
    h1['percent'] = h1['price'].pct_change()
    c5.write(f'Conclusão: Imóveis com vista para água são, em média, {h1.iloc[1, 2]:.2%} mais caros.')

    c6.subheader('H2: Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.')
    h2 = data[['price', 'built']].groupby(['built']).mean().reset_index()
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    sns.barplot(x='built', y='price', data=h2, palette='Set2')
    plt.show()
    c6.pyplot(fig)
    h2['percent'] = h2['price'].pct_change()
    c6.write(f'Conclusão: Imóveis de construção anterior à 1955 são, em média, {h2.iloc[1, 2]:.2%} mais baratos.')

    c7, c8 = st.columns((1, 1))

    c7.subheader('H3: Imóveis sem porão possuem área total 50% maior do que imóveis com porão.')
    h3 = data[['basement', 'm2_lot']].groupby(['basement']).mean().reset_index()
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    sns.barplot(x='basement', y='m2_lot', data=h3, palette='Set2')
    plt.show()
    c7.pyplot(fig)
    h3['percent'] = h3['m2_lot'].pct_change()
    c7.write(
        f'Conclusão: Imóveis sem porão tem área total, em média, {h3.iloc[1, 2]:.2%} maiores do que os imóveis sem porão.')

    c8.subheader('h4: O crescimento do preço dos imóveis YoY ( Year over Year ) é de 10%.')
    h4 = data[['year', 'price']].groupby('year').mean().reset_index()
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    sns.barplot(x='year', y='price', data=h4, palette='Set2')
    plt.show()
    c8.pyplot(fig)
    h4['percent'] = h4['price'].pct_change()
    c8.write(f'Conclusão: O crescimento do preço dos imóveis variou em média, {h4.iloc[1, 2]:.2%} ano a ano.')

    st.subheader('H5: O crescimento do preço dos imóveis MoM ( Month over Month ) é de 5%.')

    c9, c10 = st.columns((1, 1))

    c9.subheader('2014')
    h5_14 = data[(data['year'] == 2014)]
    h5_14 = h5_14[['month', 'price']].groupby('month').mean().reset_index()
    fig = px.line(h5_14, x='month', y='price')
    c9.plotly_chart(fig, use_container_width=True)

    c10.subheader('2015')
    h5_15 = data[(data['year'] == 2015)]
    h5_15 = h5_15[['month', 'price']].groupby('month').mean().reset_index()
    fig = px.line(h5_15, x='month', y='price')
    c10.plotly_chart(fig, use_container_width=True)

    c11, c12 = st.columns((1, 1))

    c11.subheader('H6: Imóveis reformados são, em média 40% mais caros que os imóveis não reformados.')
    h7 = data[['renovated', 'price']].groupby('renovated').mean().reset_index()
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    sns.barplot(x='renovated', y='price', data=h7, palette='Set2')
    plt.show()
    c11.pyplot(fig)
    h7['percent'] = h7['price'].pct_change()
    c11.write(f'Conclusão: Imóveis reformados são, em média {h7.iloc[1, 2]:.2%} mais caros que os não reformados.')

    c12.subheader('H7: Imóveis anteriores a 1955 e não renovados são 30% mais baratos.')
    h8 = data[data['renovated'] == 'não']
    h8 = h8[['built', 'price']].groupby('built').mean().reset_index()
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    sns.barplot(x='built', y='price', data=h8, palette='Set2')
    plt.show()
    c12.pyplot(fig)
    h8['percent'] = h8['price'].pct_change()
    c12.write(
        f'Conclusão: Imóveis com data de construção anterior à 1955 e não reformados são, em média {h8.iloc[1, 2]:.2%} mais baratos.')

    c13, c14 = st.columns((1, 1))

    c13.subheader('H8: Imóveis em más condições mas com boa vista, são 10% mais caros.¶')
    h9 = data[data['condition_type'] == 'bad']
    h9 = h9[['view', 'price']].groupby('view').mean().reset_index()
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    sns.barplot(x='view', y='price', data=h9)
    plt.show()
    c13.pyplot(fig)
    h9['percent'] = h9['price'].pct_change()

    c14.subheader('H9:Imóveis com número de quartos maior são 5% mais caros.')
    data['beds'] = data['bedrooms'].apply(lambda x: '0-3' if (x >= 0) & (x <= 3) else
    '4-7' if (x >= 4) & (x <= 7) else
    '8-11')
    h10 = data[['beds', 'price']].groupby('beds').mean().reset_index()
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    sns.barplot(x='beds', y='price', data=h10)
    plt.show()
    c14.pyplot(fig)
    h10['percent'] = h10['price'].pct_change()

    return None

def questions(data):
    st.write('Respondendo as perguntas:')

    c3, c4 = st.columns((1, 2))
    zipcode = data[['zipcode', 'price']].groupby('zipcode').median().reset_index()
    df = pd.merge(zipcode, data, on='zipcode', how='inner')
    df = df.rename(columns={'price_y': 'price', 'price_x': 'price_median'})
    for i, row in df.iterrows():
        if (row['price_median'] >= row['price']) & (row['condition_type'] == 'good'):
            df.loc[i, 'buy'] = 'compra'
        else:
            df.loc[i, 'buy'] = 'nao compra'

    compra = df[df['buy'] == 'compra']
    df1 = compra[['id', 'price', 'buy']].sort_values('price')

    c3.subheader('Indicação de compra e preço')
    c3.dataframe(df1)
    c3.write('Indicação de compra para os imóveis com valor abaixo da mediana da '
             'região e em boas condições')


    df2 = data[['price', 'season', 'zipcode']].groupby(['zipcode', 'season']).median().reset_index()
    df2 = df2.rename(columns={'price': 'price_median_season'})
    df3 = pd.merge(df2, df, on='zipcode', how='inner')
    df3 = df3.rename(columns={'season_x': 'season'})
    for i, row in df3.iterrows():
        if (row['price'] >= row['price_median']):
            df3.loc[i, 'sale'] = row['price'] * 1.10
        else:
            df3.loc[i, 'sale'] = row['price'] * 1.30
    df3['profit'] = df3['sale'] - df3['price']
    df3 = df3[df3['buy'] == 'compra']

    venda = df3[['id', 'price', 'zipcode', 'price_median', 'season',
                 'price_median_season', 'condition_type', 'buy', 'sale', 'profit']].sort_values('buy')

    c4.subheader('Indicação de venda e preço')
    c4.dataframe(venda)

    lucro = venda['profit'].sum()

    # c2.write('Indicação de venda assumindo a hipotese de diferenciação de compra baseada'
    #         'na sazonalidad, portanto a indicação foi feita pela região e sazonalidade, '
    #        'considerando as seguintes condições:\n'
    #
    #      '* preço de compra for maior  que a mediana da região por sazonalidade o preço de compra '
    #     'é igual ao preço de venda acrescido 10%; \n'
    #
    #   '* preço de compra for menor  que a mediana da região por sazonalidade o preço de compra '
    #  'é igual ao preço de venda acrescido 30%.')

    c4.write(f'O lucro total será de US$ {lucro}')

if __name__ == '__main__':
    data = get_data('kc_house_data.csv')

    st.dataframe(data)

#transformation
    data = set_features(data)

    st.header('Apresentação dos Dados')

    is_check = st.checkbox('Descritivos dos Dados')
    if is_check:
        st.markdown('**id**: Numeração única de identificação de cada imóvel')
        st.markdown(' **date**: Data da venda da casa ')
        st.markdown(' **price**: Preço que a casa está sendo vendida pelo proprietário ')
        st.markdown(' **bedrooms**: Número de quartos ')
        st.markdown(' **bathrooms**: Número de banheiros ')
        st.markdown(' **sqft_living**: Medida (pés quadrado) do espaço interior dos apartamentos ')
        st.markdown(' **sqft_lot**: Medida (pés quadrado)quadrada do espaço terrestre ')
        st.markdown(' **floors**: Número de andares do imóvel ')
        st.markdown(' **waterfront**: Variável que indica a presença ou não de vista para água (0 = não e 1 = sim) ')
        st.markdown(' **view**: Um índice de 0 a 4 que indica a qualidade da vista da propriedade. Varia de 0 a 4, onde: 0 = baixa 4 = alta ')
        st.markdown(' **condition**: Um índice de 1 a 5 que indica a condição da casa. Varia de 1 a 5, onde:1 = baixo 5 = alta ')
        st.markdown(' **grade**: Um índice de 1 a 13 que indica a construção e o design do edifício. Varia de 1 a 13, onde: 1 - 3 = baixo, 7 = médio e 11 - 13 = alta ')
        st.markdown(' **sqft_basement**: A metragem (em pés quadrado) quadrada do espaço habitacional interior acima do nível do solo ')
        st.markdown(' **yr_built**: Ano de construção de cada imóvel ')
        st.markdown(' **yr_renovated**: Ano de reforma de cada imóvel ')
        st.markdown('**zipcode**: CEP da casa ')
        st.markdown(' **lat**: Latitude')
        st.markdown(' **long**: Longitude ')
        st.markdown('**sqft_livining15**: Medida (em pés quadrado) do espaço interno de habitação dos 15 vizinhos mais próximo ')
        st.markdown('**sqft_lot15**: Medida (em pés quadrado) dos lotes de terra dos 15 vizinhos mais próximo  ')

    overview_data(data)

    hipotesis(data)

    questions(data)






