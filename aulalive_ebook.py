{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN8hZb5unMyLClB0kw6p2kv",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/clovesrocha/logn101_universo/blob/main/aulalive_ebook.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8yuMvBjcwAYM",
        "outputId": "e14a65bb-b15e-48bf-b444-8d4e5abc5fe9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá mundo, Prof. Cloves Rocha\n"
          ]
        }
      ],
      "source": [
        "# Aula Live - UNIVERSO RECIFE\n",
        "# Descomplicando Programação com Python\n",
        "# Algoritmos II\n",
        "\n",
        "print('Olá mundo, Prof. Cloves Rocha')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "c = 'a'\n",
        "print((type(c)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NgUEbKBAw_AK",
        "outputId": "75ad4867-14cf-4c4a-c2ab-57df56e2e2e4"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 10\n",
        "y = 10\n",
        "print(x == y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jslbF1i7yvDr",
        "outputId": "e763de7f-e933-43df-8bb5-9204ad0a44ce"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "c = 2**3\n",
        "print(c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-0xTH9IWzK9k",
        "outputId": "233f3836-b1ea-4cba-ecba-9e12b112c5f8"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 10//3\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c35WKe1zzrH1",
        "outputId": "9fbadbf1-920d-4674-e4d0-0d9a193fd749"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "c = 10%3\n",
        "print(c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0Cwb-V110BY6",
        "outputId": "28a7f2f8-8960-45ef-9050-0e73ed3e2496"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 4\n",
        "b = 3\n",
        "print(a >= b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eFspYHey0fgq",
        "outputId": "79a49ec4-1d48-43e0-807c-0753a853acc5"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "KedSSQZS0z04"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print('Olá mundo!, 2, 2.5, True, False')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cX2dEjK30o0C",
        "outputId": "4307911f-f768-44dc-fb79-de82a82f5f5c"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá mundo!, 2, 2.5, True, False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = 2\n",
        "print(f'O número {n} é par.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mIIZdjzD04T6",
        "outputId": "2fe518a9-42b4-4b03-9c2d-87b4bece9a45"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "O número 2 é par.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nome = input('Digite seu nome: ')\n",
        "print(f'Seu nome é {nome}.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tqLtAkDz1ll0",
        "outputId": "b0d16da2-87ca-48a7-8301-b393551332f5"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seu nome: Consultor Cloves \n",
            "Seu nome é Consultor Cloves .\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "idade = input('Digite sua idade: ')\n",
        "print(f'Você tem {idade} anos.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eWeLqBws2PMY",
        "outputId": "0e311454-bcc8-4f79-ded3-87f7782a3fac"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua idade: 40\n",
            "Você tem 40 anos.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "idade = input('Digite sua idade: ')\n",
        "print(f'Você tem {idade} anos.')\n",
        "print(type(idade))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sDOk60Qe2fC-",
        "outputId": "2a5499b9-0cf0-4c5a-b8f2-1915cf7b6f3f"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua idade: 40\n",
            "Você tem 40 anos.\n",
            "<class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "idade = int(input('Digite sua idade: '))\n",
        "print(f'Você tem {idade} anos.')\n",
        "print(type(idade))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GGuwBcok2t65",
        "outputId": "545efc16-263a-4a93-99b5-241ca8fce893"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua idade: 40\n",
            "Você tem 40 anos.\n",
            "<class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "peso = float(input('Digite seu peso: '))\n",
        "print(f'Você pesa {peso}KGs')\n",
        "print(type(peso))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YT1T5B0D3Dbl",
        "outputId": "d46ff425-5828-445a-a7b6-aa49bf748e8f"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seu peso: 80.4\n",
            "Você pesa 80.4KGs\n",
            "<class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = int(input('Digite um número: '))\n",
        "if num % 2 == 0:\n",
        " print(f'O número {num} é par')\n",
        "else:\n",
        " print(f'O número {num} é ímpar')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ncVv9XmC3gEf",
        "outputId": "1d93dab1-068d-4835-9b8b-4ed9c02949bf"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 22\n",
            "O número 22 é par\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = float(input('Digite um número: '))\n",
        "if num > 0:\n",
        "  print('Este número é positivo')\n",
        "elif num == 0:\n",
        "  print('Este número é neutro')\n",
        "\n",
        "else:\n",
        "  print('Este número é negativo')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BxxLjJ3G4MAA",
        "outputId": "ce2a46ce-6701-4422-b15a-95ef166f281c"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: -14\n",
            "Este número é negativo\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "resposta = int(input('Qual sua idade: ') )\n",
        "if resposta>=18 and resposta <=65:\n",
        "  print('Você é obrigado a votar!')\n",
        "else:\n",
        "\n",
        "  print('Você não é obrigado a votar!')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OsCFb4CV4yXX",
        "outputId": "6219f544-4952-498b-9d91-46afb23e1a4f"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Qual sua idade: 90\n",
            "Você não é obrigado a votar!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('1. Idoso')\n",
        "print('2. Gestante')\n",
        "print('3. Cadeirante')\n",
        "print('4. Nenhum destes')\n",
        "resposta=int(input('Você é: ') )\n",
        "if (resposta==1) or (resposta==2) or (resposta==3) :\n",
        "  print('Você tem direito a fila prioritária')\n",
        "else:\n",
        " print('Você não tem direito a nada. Vá pra fila e fique quieto.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y3UuEvOt5YbA",
        "outputId": "6a66d348-4fb6-4b59-e2bd-e2fd8a1ef6bc"
      },
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1. Idoso\n",
            "2. Gestante\n",
            "3. Cadeirante\n",
            "4. Nenhum destes\n",
            "Você é: 4\n",
            "Você não tem direito a nada. Vá pra fila e fique quieto.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 4\n",
        "b = 2\n",
        "print(not a > b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fL-SJPb358WC",
        "outputId": "9225de5e-403c-4308-e52d-9cc570f2446d"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "banda = input('Qual melhor banda do mundo? ')\n",
        "if not banda=='DT':\n",
        "  print('Errado!')\n",
        "else:\n",
        "  print('Correto, é DT')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "54pCEGJ16Sr7",
        "outputId": "b9560554-5378-477f-947c-b47f7eb739ca"
      },
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Qual melhor banda do mundo? DT\n",
            "Correto, é DT\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = int(input('Digite um número: '))\n",
        "if a in range(1, 100):\n",
        "  print(f'{a} está entre 1 e 100.')\n",
        "else:\n",
        "  print(f'{a} não está entre 1 e 100.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Egxysoye6m_a",
        "outputId": "a45c1c36-336c-4541-9333-9417f1c21404"
      },
      "execution_count": 70,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 1\n",
            "1 está entre 1 e 100.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "RtdOu6_07KzS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercícios e Desafios\n",
        "1. Faça um CÓDIGO que mostre a mensagem \"Olá Mundo!\" na tela.\n",
        "2. Faça um CÓDIGO que peça um número e então mostre a mensagem O número\n",
        "informado foi [número].\n",
        "3. Faça um CÓDIGO que peça dois números e imprima a soma.\n",
        "4. Faça um CÓDIGO que peça as 4 notas bimestrais e mostre a média final.\n",
        "5. Faça um CÓDIGO que converta metros para centímetros.\n",
        "6. Faça um CÓDIGO que peça o raio de um círculo, calcule e mostre sua área.\n",
        "7. Faça um CÓDIGO que calcule a área de um quadrado, em seguida mostre o dobro desta\n",
        "área para o usuário.\n",
        "8. Faça um CÓDIGO que pergunte quanto você ganha por hora e o número de horas\n",
        "trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.\n",
        "9. Faça um CÓDIGO que peça um valor e mostre na tela se o valor é positivo ou negativo.\n",
        "10. Faça um CÓDIGO que verifique se uma letra digitada é \"F\" ou \"M\". Conforme a letra\n",
        "escrever: F - Feminino, M - Masculino, Sexo Inválido."
      ],
      "metadata": {
        "id": "JB_7LJKt736e"
      }
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "FGR3jbCN0xr8"
      }
    }
  ]
}