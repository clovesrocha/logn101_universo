import java.util.ArrayList;
import java.util.List;


 */
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

  
    // 3) SERVICO DE FILTRAGEM (ServicoFiltro)
]
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

    
    // 4) MAIN - Testes e Demonstração (Coração do Desafio)
    
    public static void main(String[] args) {

        // -------------------------
        // A) CRIAÇÃO DA LISTA
        // -------------------------
        List<Produto> produtos = new ArrayList<>();
        produtos.add(new Produto("Notebook Gamer", 6500.0, true));
        produtos.add(new Produto("Mouse", 80.0, true));
        produtos.add(new Produto("Cadeira Office", 900.0, false));
        produtos.add(new Produto("Monitor 144Hz", 1200.0, true));
        produtos.add(new Produto("Cabo HDMI", 35.0, false));

        // Imprime a lista completa (opcional, para ver os dados originais)
        System.out.println("=== Lista Original de Produtos ===");
        produtos.forEach(System.out::println);

       
        // B) FILTRO COM CLASSE ANÔNIMA
        //    - Objetivo: produtos que estejam em estoque (emEstoque == true)

        List<Produto> produtosEmEstoque = ServicoFiltro.filtrar(produtos, new FiltroProduto<Produto>() {
            @Override
            public boolean testar(Produto p) {
                return p.isEmEstoque();
            }
        });

        System.out.println("\n=== [B] Produtos em Estoque (Classe Anônima) ===");
        produtosEmEstoque.forEach(System.out::println);

      
        // C) FILTRO COM EXPRESSÃO LAMBDA
        
      
        List<Produto> produtosCaros = ServicoFiltro.filtrar(produtos, p -> p.getPreco() > 1000.0);

        System.out.println("\n=== [C] Produtos com preço > R$1000,00 (Lambda) ===");
        produtosCaros.forEach(System.out::println);


        // D) BÔNUS: LAMBDA COM MÚLTIPLAS CONDIÇÕES


        List<Produto> filtroBonus = ServicoFiltro.filtrar(produtos,
                p -> (!p.isEmEstoque()) || (p.getPreco() < 50.0));

        System.out.println("\n=== [D] Bônus: fora de estoque OU preço < R$50,00 (Lambda com múltiplas condições) ===");
        filtroBonus.forEach(System.out::println);

    
   
    }
}
