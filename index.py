import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

#aba da aplicacao

st.set_page_config(
    page_title="Controle de estoque",
    page_icon=":shopping_trolley:"
)

def cadastra_produto():
    produto_id = st.text_input('ID')
    produto_nome = st.text_input('Nome')
    produto_preco = st.number_input('Preço', min_value=0.0)
    produto_estoque = st.number_input('Estoque', min_value=0)

    if st.button('Cadastrar Produto'):
        # cria um novo  para o novo produto
        novo_produto = pd.DataFrame({
            'ID': [produto_id],
            'Nome': [produto_nome],
            'Preco': [produto_preco],
            'Estoque': [produto_estoque],
        })

        st.session_state['produtos'] = pd.concat([st.session_state['produtos'], novo_produto], ignore_index=True)
        st.success('Produto cadastrado com sucesso!')

def listar_produtos():
    st.subheader('Todos os Produtos do sistema')
    st.dataframe(st.session_state['produtos'])



def apagar_produto():
    listar_produtos = st.session_state['produtos']['ID'].tolist()
    produto_id = st.selectbox('Selecione ID do Produto para apagar', listar_produtos)

    if produto_id and st.button('Apagar produto'):
        #remove o produto pelo id
        st.session_state['produtos'] = st.session_state['produtos'][st.session_state['produtos']['ID'] != produto_id]

def alterar_produto():
    #converte a coluna ID em uma lista
    listar_produtos = st.session_state['produtos']['ID'].tolist()
    produto_id = st.selectbox('Selecione ID do produto para alterar', listar_produtos)

    if produto_id:
        produto = st.session_state['produtos'][st.session_state['produtos']['ID'] == produto_id].iloc[0]

        #localiza o produto pelo ID
        novo_nome = st.text_input('Nome', value=produto['Nome'])
        novo_preco = st.number_input('Preço', min_value=0.0, value=produto['Preco'])
        novo_estoque = st.number_input('Estoque', min_value=0, value=int(produto['Estoque']))

        if st.button('Atualizar Produto'):
            st.session_state['produtos'].loc[st.session_state['produtos']['ID'] == produto_id, ['Nome', 'Preco', 'Estoque'][novo_nome, novo_preco, novo_estoque]]





if __name__ == "__main__":
    st.title('Controle de estoque')

    # inicializa o DataFrame e salva na sessao
    if 'produtos' not in st.session_state:
        st.session_state['produtos'] = pd.DataFrame(columns=['ID', 'Nome', 'Preco', 'Estoque'])


    #menu option_menu
    # 1. as sidebar menu
    with st.sidebar:
        opcao = option_menu("Main Menu", ["Cadastrar produto", 'Alterar produto', 'Apagar produto', 'Listar todos os produtos'],
                               icons=['house', 'gear', 'gear', 'gear'], menu_icon="cast", default_index=1)




        #controle de ação atraves de barra lateral
        #opcao = st.sidebar.selectbox('Escolha uma opcao',
            #                         ['Cadastrar produto', 'Alterar produto', 'Apagar produto', 'Listar todos os produtos'])

    if opcao == 'Cadastrar produto':
        cadastra_produto()
    elif opcao == 'Alterar produto':
        alterar_produto()
    elif opcao == 'Apagar produto':
        apagar_produto()
    elif opcao == 'Listar todos os produtos':
        listar_produtos()



