import java.util.*;

class Produto {
    private String nome;
    private double preco;
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
        return nome + " - R$ " + preco + " - Estoque: " + emEstoque;
    }
}

@FunctionalInterface
interface FiltroProduto<T> {
    boolean testar(T item);
}

class ServicoFiltro {
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

public class Main {
    public static void main(String[] args) {

        List<Produto> produtos = Arrays.asList(
            new Produto("Notebook", 3500, true),
            new Produto("Mouse", 40, false),
            new Produto("Cadeira Gamer", 900, true),
            new Produto("Monitor", 1200, true),
            new Produto("Pendrive", 25, true)
        );


        List<Produto> emEstoque = ServicoFiltro.filtrar(produtos, new FiltroProduto<Produto>() {
            @Override
            public boolean testar(Produto p) {
                return p.isEmEstoque();
            }
        });

        System.out.println("Produtos em estoque:");
        emEstoque.forEach(System.out::println);


        List<Produto> caros = ServicoFiltro.filtrar(produtos, p -> p.getPreco() > 1000);

        System.out.println("\nProdutos com preço > 1000:");
        caros.forEach(System.out::println);


        List<Produto> bonus = ServicoFiltro.filtrar(produtos,
            p -> !p.isEmEstoque() || p.getPreco() < 50
        );

        System.out.println("\nFiltro bônus:");
        bonus.forEach(System.out::println);
    }
}
