{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/clovesrocha/logn101_universo/blob/main/Aula_08_08.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Atividade\n"
      ],
      "metadata": {
        "id": "XnQkdIru-fpU"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\"1. Faça um CÓDIGO que mostre a mensagem \\\"Olá Mundo!\\\" na tela.\\n\",\n",
        "\n",
        "\"2. Faça um CÓDIGO que peça um número e então mostre a mensagem O número\\n\",\n",
        "\"informado foi [número].\\n\",\n",
        "\n",
        "\"3. Faça um CÓDIGO que peça dois números e imprima a soma.\\n\",\n",
        "\n",
        "\"4. Faça um CÓDIGO que peça as 4 notas bimestrais e mostre a média final.\\n\",\n",
        "\n",
        "\"5. Faça um CÓDIGO que converta metros para centímetros.\\n\",\n",
        "\n",
        "\"6. Faça um CÓDIGO que peça o raio de um círculo, calcule e mostre sua área.\\n\",\n",
        "\n",
        "\"7. Faça um CÓDIGO que calcule a área de um quadrado, em seguida mostre o dobro desta\\n\",\n",
        "\"área para o usuário.\\n\",\n",
        "\n",
        "\"8. Faça um CÓDIGO que pergunte quanto você ganha por hora e o número de horas\\n\",\n",
        "\"trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.\\n\",\n",
        "\n",
        "\"9. Faça um CÓDIGO que peça um valor e mostre na tela se o valor é positivo ou negativo.\\n\",\n",
        "\n",
        "10. Faça um CÓDIGO que verifique se uma letra digitada é \\\"F\\\" ou \\\"M\\\". Conforme a letra\\n\",\n",
        "  \"escrever: F - Feminino, M - Masculino, Sexo Inválido.\""
      ],
      "metadata": {
        "id": "6NdamqDk-kZT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Olá Mundo!☺☻\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VX8WwVhE-jCk",
        "outputId": "c2fb7b7e-f926-4db1-85d4-c8e8b26800b3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá Mundo!☺☻\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num= input((\"Digite um número:\"))\n",
        "print(f\"O número informado foi {num}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5DUU_lUy_tLl",
        "outputId": "1b914546-5cce-40fa-e1fb-d434f87e6a53"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número:6\n",
            "O número informado foi 6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num1 = int(input(\"Digite um número:\"))\n",
        "num2 = int(input(\"Digite outro número:\"))\n",
        "print(f\"A soma dos números é {num1+num2}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DF6v305eAEGr",
        "outputId": "ee8e677e-b4e4-4514-9262-5ede8f911e67"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número:15\n",
            "Digite outro número:15\n",
            "A soma dos números é 30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num1 = int(input(\"Digite a primeira nota:\"))\n",
        "num2 = int(input(\"Digite a segunda nota:\"))\n",
        "num3 = int(input(\"Digite a terceira nota:\"))\n",
        "num4 = int(input(\"Digite a quarta nota:\"))\n",
        "print(f\"A média final é {(num1+num2+num3+num4)/4}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j4cqLVPVAIwb",
        "outputId": "c982e19d-bafd-41e0-cf86-14d5837ab478"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a primeira nota:5\n",
            "Digite a segunda nota:5\n",
            "Digite a terceira nota:5\n",
            "Digite a quarta nota:5\n",
            "A média final é 5.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num1 = int(input(\"Digite a medida em metros:\"))\n",
        "print(f\"A medida em centímetros é {num1*100}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VjZBv8lTAkfM",
        "outputId": "722f1588-a658-418d-a677-f69aed2edb2e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a medida em metros:8\n",
            "A medida em centímetros é 800\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num1 = int(input(\"Digite o raio do círculo:\"))\n",
        "print(f\"A área do círculo é {3.14*(num1**2)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tQIQI-toBf7c",
        "outputId": "6d70b005-6a82-4968-f4f8-57c8ab01c482"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o raio do círculo:66\n",
            "A área do círculo é 13677.84\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num1 = int(input(\"Digite a medida do lado do quadrado:\"))\n",
        "print(f\"O dobro da área do quadrado é {(num1**2)*2}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QoqKec9UCr6M",
        "outputId": "5bc7c8be-6729-486d-edea-7b91e992ed71"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a medida do lado do quadrado:5\n",
            "O dobro da área do quadrado é 50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num1= int(input(\"Quanto você ganha por hora?\"))\n",
        "num2= int(input(\"Quantas horas você trabalha por mês?\"))\n",
        "print(f\"Seu salário é {num1*num2}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hxroGAumDJt1",
        "outputId": "facc04d3-1874-4a35-8459-2d1c3e5c83c3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quanto você ganha por hora?60\n",
            "Quantas horas você trabalha por mês?900\n",
            "Seu salário é 54000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num= int(input(\"Digite um número:\"))\n",
        "if num>0:\n",
        "  print(\"O número é positivo\")\n",
        "else:\n",
        "  print(\"O número é negativo\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UdtC2dJeDuZk",
        "outputId": "f2cda4c9-7e7c-4341-c8d3-89e350ec6a42"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número:80\n",
            "O número é positivo\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "letra= input(\"Digite uma letra:\")\n",
        "if letra==\"F\":\n",
        "  print(\"F - Feminino\")\n",
        "elif letra==\"M\":\n",
        "  print(\"M - Masculino\")\n",
        "else:\n",
        "  print(\"Sexo Inválido\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0A3vIlOUDzZs",
        "outputId": "7d569223-60ff-402b-a5b7-bee81a810aa4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite uma letra:5\n",
            "Sexo Inválido\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}