import java.util.ArrayList;
import java.util.List;

// Classe Carro
class Carro {
    private String modelo;
    private String marca;
    private int ano;
    private double preco;

    // Construtor
    public Carro(String modelo, String marca, int ano, double preco) {
        this.modelo = modelo;
        this.marca = marca;
        this.ano = ano;
        this.preco = preco;
    }

    // Getters e Setters
    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    @Override
    public String toString() {
        return "Carro{" +
                "modelo='" + modelo + '\'' +
                ", marca='" + marca + '\'' +
                ", ano=" + ano +
                ", preco=" + preco +
                '}';
    }
}

// Interface Funcional FiltroCarro
@FunctionalInterface
interface FiltroCarro<T> {
    boolean testar(T item);
}

// Classe de Serviço
class ServicoFiltro {
    public static <T> List<T> filtrar(List<T> lista, FiltroCarro<T> filtro) {
        List<T> resultados = new ArrayList<>();
        for (T item : lista) {
            if (filtro.testar(item)) {
                resultados.add(item);
            }
        }
        return resultados;
    }
}

// Classe Main para teste
public class Main {
    public static void main(String[] args) {
        // A. Criar e popular a lista de carros
        List<Carro> carros = new ArrayList<>();
        carros.add(new Carro("Civic", "Honda", 2020, 95000.00));
        carros.add(new Carro("Corolla", "Toyota", 2018, 80000.00));
        carros.add(new Carro("Mustang", "Ford", 2022, 250000.00));
        carros.add(new Carro("Golf", "Volkswagen", 2019, 70000.00));
        carros.add(new Carro("Uno", "Fiat", 2015, 30000.00));
        carros.add(new Carro("Ferrari 488", "Ferrari", 2021, 1500000.00));

        // B. Filtro com Classe Anônima: carros fabricados após 2019
        FiltroCarro<Carro> filtroAno = new FiltroCarro<Carro>() {
            @Override
            public boolean testar(Carro carro) {
                return carro.getAno() > 2019;
            }
        };
        List<Carro> carrosRecentes = ServicoFiltro.filtrar(carros, filtroAno);
        System.out.println("Carros fabricados após 2019:");
        for (Carro c : carrosRecentes) {
            System.out.println(c);
        }

        // C. Filtro com Expressão Lambda: carros com preço superior a R$ 100.000,00
        FiltroCarro<Carro> filtroPrecoAlto = carro -> carro.getPreco() > 100000.00;
        List<Carro> carrosCaros = ServicoFiltro.filtrar(carros, filtroPrecoAlto);
        System.out.println("\nCarros com preço superior a R$ 100.000,00:");
        for (Carro c : carrosCaros) {
            System.out.println(c);
        }

        // D. Bônus: Filtro com Lambda: carros fabricados antes de 2020 OU preço inferior a R$ 50.000,00
        FiltroCarro<Carro> filtroBonus = carro -> carro.getAno() < 2020 || carro.getPreco() < 50000.00;
        List<Carro> carrosBonus = ServicoFiltro.filtrar(carros, filtroBonus);
        System.out.println("\nCarros fabricados antes de 2020 OU preço inferior a R$ 50.000,00:");
        for (Carro c : carrosBonus) {
            System.out.println(c);
        }
    }
}
