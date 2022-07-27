produtos = []  # recebe a lista de produtos
listaCompras = []  # recebe produtos comprados
vlTotal = 0.0


class Item():
    nome = ''
    cod = 0
    quantidade = 0
    preço = 0.0


def insereProdutos(n, c, q, p):  # função que cadastra os produtos
    class Item ():
        nome = n
        cod = int(c)
        quantidade = int(q)
        preco = float(p)
    produtos.append(Item)
    return 'Item cadastrado'


modo = 5
user = 6
# senha padrão para admin, evitando que um cliente entre na área de administrador
senha = "admin"
while True:
    user = int(input(
        'Digite -1 para fechar o programa. Digite qualquer valor para continuar: '))
    if user == -1:
        break
    print('Insira a senha para entrar como administrador, caso seja cliente digite "-2". ')
    senhaInserida = input('Insira a senha para entrar como administrador: ')
    if senhaInserida == senha:  # área admin --> remove, adiciona e verifica produtos
        while modo != 0:
            print(" Menu ")
            print(" 0 - Fim ")  # sai da área de admin e volta para menu inicial
            print(" 1 - Cadastra Produtos ")
            print(" 2 - Confere Lista de Produtos ")
            print(" 3 - Remove produtos ")
            modo = input('Escolha uma opção: ')
            if modo == '0':
                break
            if modo == '1':  # cadastra produtos
                quantosProdutos = int(
                    input("Insira a quantidade de produtos que deseja cadastrar: "))
                for i in range(quantosProdutos):
                    cadastro = insereProdutos(input('Insira o nome do produto: '), int(input('Insira o id do produto: ')), int(
                        input('Insira a quantidade de produtos que há no estoque: ')), float(input('Insira o valor do produto: R$')))
            if modo == '2':  # exibe produtos/relatório
                print("Exibindo produtos...")
                for i in range(len(produtos)):
                    print(
                        f"Posição do produto no estoque: {i} Código: {produtos[i].cod} Nome: {produtos[i].nome} Quantidade em estoque: {produtos[i].quantidade} Preço: R${produtos[i].preco}")
                if len(produtos) == 0:
                    print(
                        'Não há nenhum produto cadastrado em nosso sistema, por favor insira algum antes de utilizar o programa com a opção "1"')
                    continue
            if modo == '3':  # remove produtos
                qtdRemove = int(input('Quantos produtos deseja remover? '))
                for i in range(qtdRemove):
                    selec = int(
                        input('Selecione o produto que deseja remover: '))
                    produtos.remove(produtos[selec])
    else:
        if senhaInserida == "-2":  # area cliente
            print("Exibindo nossos produtos...")
            for i in range(len(produtos)):
                print(
                    f"Posição do produto no estoque: {i} Código: {produtos[i].cod} Nome: {produtos[i].nome} Quantidade em estoque: {produtos[i].quantidade} Preço: R${produtos[i].preco}")
            resp = int(input(
                "Deseja adquirir um dos produtos da lista? Digite '1' para comprar e '2' para sair"))
            if resp == 1:
                quantosProdutos = int(
                    input("Insira quantos produtos deseja comprar"))
                for i in range(quantosProdutos):
                    posicao = int(
                        input('Insira a posição do produto no estoque: '))
                    listaCompras.append(produtos[posicao])
                    vlTotal += produtos[posicao].preco
                print(
                    'Obrigado por comprar no nosso mercado. O valor total foi R$', vlTotal)
print('Fim do programa.')
