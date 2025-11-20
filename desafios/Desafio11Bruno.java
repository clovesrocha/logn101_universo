import java.util.ArrayList;
import java.util.List;

// Classe Livro
class Livro {
    private String titulo;
    private String autor;
    private int ano;
    private double preco;

    public Livro(String titulo, String autor, int ano, double preco) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.preco = preco;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAno() {
        return ano;
    }

    public double getPreco() {
        return preco;
    }

    @Override
    public String toString() {
        return "Livro{" +
                "titulo='" + titulo + '\'' +
                ", autor='" + autor + '\'' +
                ", ano=" + ano +
                ", preco=" + preco +
                '}';
    }
}

// Interface Funcional
@FunctionalInterface
interface Filtro<T> {
    boolean testar(T item);
}

// Serviço de filtro
class ServicoFiltro {
    public static <T> List<T> filtrar(List<T> lista, Filtro<T> filtro) {
        List<T> resultado = new ArrayList<>();
        for (T item : lista) {
            if (filtro.testar(item)) {
                resultado.add(item);
            }
        }
        return resultado;
    }
}

// Main
public class Main {
    public static void main(String[] args) {
        List<Livro> livros = new ArrayList<>();
        livros.add(new Livro("Duna", "Frank Herbert", 1965, 50.00));
        livros.add(new Livro("1984", "George Orwell", 1949, 35.00));
        livros.add(new Livro("O Hobbit", "J.R.R. Tolkien", 1937, 45.00));
        livros.add(new Livro("Neuromancer", "William Gibson", 1984, 60.00));
        livros.add(new Livro("Fundação", "Isaac Asimov", 1951, 55.00));

        // Classe anônima: livros publicados após 1950
        Filtro<Livro> filtroAno = new Filtro<Livro>() {
            @Override
            public boolean testar(Livro livro) {
                return livro.getAno() > 1950;
            }
        };

        List<Livro> recentes = ServicoFiltro.filtrar(livros, filtroAno);
        System.out.println("Livros publicados após 1950:");
        recentes.forEach(System.out::println);

        // Lambda: livros com preço acima de 50 reais
        Filtro<Livro> filtroPreco = livro -> livro.getPreco() > 50;

        List<Livro> caros = ServicoFiltro.filtrar(livros, filtroPreco);
        System.out.println("\nLivros com preço acima de R$ 50:");
        caros.forEach(System.out::println);

        // Lambda bônus: livros antes de 1960 OU com autor começando com 'J'
        Filtro<Livro> filtroBonus = livro -> livro.getAno() < 1960 || livro.getAutor().startsWith("J");

        List<Livro> bonus = ServicoFiltro.filtrar(livros, filtroBonus);
        System.out.println("\nLivros antes de 1960 OU autor começando com 'J':");
        bonus.forEach(System.out::println);
    }
}