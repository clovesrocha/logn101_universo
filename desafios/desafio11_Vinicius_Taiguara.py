class Produto:
    def __init__(self, nome, preco, em_estoque):
        self.nome = nome
        self.preco = preco
        self.em_estoque = em_estoque

    def __repr__(self):
        return f"{self.nome} - R${self.preco:.2f} - {'Em estoque' if self.em_estoque else 'Sem estoque'}"


def filtrar(lista, condicao):
    resultado = []
    for item in lista:
        if condicao(item):
            resultado.append(item)
    return resultado


class ServicoFiltro:
    @staticmethod
    def filtrar(lista, condicao):
        return filtrar(lista, condicao)


if __name__ == "__main__":
    # Criar lista de produtos
    produtos = [
        Produto("TV LG", 2500.00, True),
        Produto("Geladeira Brastemp", 4800.00, True),
        Produto("Fogão Electrolux", 1500.00, False),
        Produto("Notebook Acer", 3900.00, True),
        Produto("Microondas", 700.00, False),
    ]

    print("\nLista completa de produtos:")
    for p in produtos:
        print(p)

   

    # Produtos com preço maior que R$ 3000
    filtro_preco = lambda p: p.preco > 3000

    produtos_caros = ServicoFiltro.filtrar(produtos, filtro_preco)

    print("\nA) Produtos com preço > 3000:")
    for p in produtos_caros:
        print(p)


    # Filtrar “somente produtos em estoque”
    em_estoque = ServicoFiltro.filtrar(produtos, lambda p: p.em_estoque)

    print("\nB) Produtos em estoque:")
    for p in em_estoque:
        print(p)

    # Combinar Expressões Lambda (estoque + preço < 1000)
    baratos_e_estoque = ServicoFiltro.filtrar(
        produtos, lambda p: p.em_estoque and p.preco < 1000
    )

    print("\nC) Produtos em estoque e preço < 1000:")
    for p in baratos_e_estoque:
        print(p)

    # Bônus: produtos com preço entre 1000 e 5000
    preco_intermediario = ServicoFiltro.filtrar(
        produtos, lambda p: 1000 <= p.preco <= 5000
    )

    print("\nD) Produtos entre R$ 1000 e R$ 5000:")
    for p in preco_intermediario:
        print(p)
