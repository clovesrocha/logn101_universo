import java.util.ArrayList;
import java.util.List;

public class DesafioProdutos {

    // 1) CLASSE PRODUTO
    static class Produto {
        private String nome;
        private double preco;
        private boolean emEstoque;

        public Produto(String nome, double preco, boolean emEstoque) {
            this.nome = nome;
            this.preco = preco;
            this.emEstoque = emEstoque;
        }

        public String getNome() {
            return nome;
        }

        public double getPreco() {
            return preco;
        }

        public boolean isEmEstoque() {
            return emEstoque;
        }

        @Override
        public String toString() {
            return "Produto{" +
                    "nome='" + nome + '\'' +
                    ", preco=" + preco +
                    ", emEstoque=" + emEstoque +
                    '}';
        }
    }

    // 2) INTERFACE FUNCIONAL
    @FunctionalInterface
    interface FiltroProduto<T> {
        boolean testar(T item);
    }

    // 3) SERVIÇO DE FILTRAGEM
    static class ServicoFiltro {
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

    // 4) MAIN
    public static void main(String[] args) {

        // A) CRIAÇÃO DA LISTA
        List<Produto> produtos = new ArrayList<>();
        produtos.add(new Produto("PC Gamer", 6500.0, true));
        produtos.add(new Produto("Blusa masculina", 80.0, true));
        produtos.add(new Produto("Celular usado", 500.0, false));
        produtos.add(new Produto("iPhone usado", 1200.0, true));
        produtos.add(new Produto("Cabo tipo C", 35.0, false));

        System.out.println("=== Lista Original de Produtos ===");
        produtos.forEach(System.out::println);

        // B) FILTRO COM CLASSE ANÔNIMA
        List<Produto> produtosEmEstoque = ServicoFiltro.filtrar(produtos, new FiltroProduto<Produto>() {
            @Override
            public boolean testar(Produto p) {
                return p.isEmEstoque();
            }
        });

        System.out.println("\n=== [B] Produtos em Estoque ===");
        produtosEmEstoque.forEach(System.out::println);

        // C) FILTRO COM LAMBDA
        List<Produto> produtosCaros = ServicoFiltro.filtrar(produtos,
                p -> p.getPreco() > 1000.0);

        System.out.println("\n=== [C] Produtos com preço > R$1000 ===");
        produtosCaros.forEach(System.out::println);

        // D) FILTRO BÔNUS
        List<Produto> filtroBonus = ServicoFiltro.filtrar(produtos,
                p -> (!p.isEmEstoque()) || (p.getPreco() < 50.0));

        System.out.println("\n=== [D] Fora de estoque OU < R$50 ===");
        filtroBonus.forEach(System.out::println);
    }
}
