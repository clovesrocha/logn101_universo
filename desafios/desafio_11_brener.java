

===================================================== 1. CLASSE Produto
=====================================================

A classe Produto representa um item que será filtrado. Ela possui: -
nome (String) - preco (double) - emEstoque (boolean)

Ela também possui getters e um método toString para exibir as infos.

CÓDIGO:

public class Produto { private String nome; private double preco;
private boolean emEstoque;

    public Produto(String nome, double preco, boolean emEstoque) {
        this.nome = nome;
        this.preco = preco;
        this.emEstoque = emEstoque;
    }

    public String getNome() { return nome; }
    public double getPreco() { return preco; }
    public boolean isEmEstoque() { return emEstoque; }

    @Override
    public String toString() {
        return nome + " - R$" + preco + " - Em estoque? " + emEstoque;
    }

}

===================================================== 2. Interface
Funcional FiltroProduto
=====================================================

Essa interface define o “contrato” do filtro. Ela tem apenas 1 método
(requisito de interface funcional).

Serve para receber qualquer lógica que devolve TRUE ou FALSE.

CÓDIGO:

@FunctionalInterface public interface FiltroProduto { boolean testar(T
item); } —————————————————–

===================================================== 3. Classe
ServicoFiltro =====================================================

Essa classe tem um método estático genérico chamado filtrar. Ele
percorre a lista e aplica o filtro para decidir quem entra no resultado.

CÓDIGO:

import java.util.ArrayList; import java.util.List;

public class ServicoFiltro {

    public static <T> List<T> filtrar(List<T> lista, FiltroProduto<T> filtro) {
        List<T> resultados = new ArrayList<>();

        for (T item : lista) {
            if (filtro.testar(item)) {
                resultados.add(item);
            }
        }

        return resultados;
    }

}

===================================================== 4. Classe Main
(teste completo) =====================================================

Aqui acontece a prática: 1) Criamos 5 produtos 2) Usamos classe anônima
para filtrar em estoque 3) Usamos lambda para preço > 1000 4) Usamos
lambda bônus com duas condições

CÓDIGO:

import java.util.ArrayList; import java.util.List;

public class Main { public static void main(String[] args) {

        List<Produto> produtos = new ArrayList<>();
        produtos.add(new Produto("Notebook", 3500, true));
        produtos.add(new Produto("Mouse", 40, false));
        produtos.add(new Produto("Monitor", 900, true));
        produtos.add(new Produto("Teclado gamer", 250, true));
        produtos.add(new Produto("TV 50\"", 2800, false));

        System.out.println("\n=== Produtos EM ESTOQUE (Classe Anônima) ===");

        List<Produto> emEstoque = ServicoFiltro.filtrar(produtos, new FiltroProduto<Produto>() {
            @Override
            public boolean testar(Produto p) {
                return p.isEmEstoque();
            }
        });

        emEstoque.forEach(System.out::println);

        System.out.println("\n=== Produtos com preço > 1000 (Lambda) ===");

        List<Produto> caros = ServicoFiltro.filtrar(produtos,
                p -> p.getPreco() > 1000);

        caros.forEach(System.out::println);

        System.out.println("\n=== BÔNUS: não estão em estoque OU preço < 50 ===");

        List<Produto> bonus = ServicoFiltro.filtrar(produtos,
                p -> !p.isEmEstoque() || p.getPreco() < 50);

        bonus.forEach(System.out::println);
    }

}
