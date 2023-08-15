# 3) Faça um programa no qual o usuário precisa cadastrar as informações de um produto: código, nome, quantidade e preço. No final o programa deve mostrar as informações cadastradas e exibir o valor total da compra. 

produtos = []

while True:

    codigo = input("Digite o código do produto ")
    nome = input("Digite o nome do produto ")
    quantidade = int(input("Digite a quantidade do produto "))
    preco = float(input("Digite preço do produto "))

    total = preco * quantidade

    produtos.append({
        'codigo': codigo,
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco,
        'valor_total': total
    })

    print("Produtos: ")
    for produto in produtos:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")

    print("Valor total: ")
    total_compra = sum(produto['valor_total'] for produto in produtos)
    print(total_compra)

    opcao = input('Deseja continuar "sim" ou "não" ')

    if opcao.lower() == "não":
        break