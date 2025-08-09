{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM1XHUvqJSf0X1sH83T8cmp",
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
        "<a href=\"https://colab.research.google.com/github/clovesrocha/logn101_universo/blob/main/JV_ALGORITIMO_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#1. Faça um CÓDIGO que mostre a mensagem \"Olá Mundo!\" na tela.\n",
        "#2. Faça um CÓDIGO que peça um número e então mostre a mensagem O númeroinformado foi [número].\n",
        "#3. Faça um CÓDIGO que peça dois números e imprima a soma.\n",
        "#4. Faça um CÓDIGO que peça as 4 notas bimestrais e mostre a média final.\n",
        "#5. Faça um CÓDIGO que converta metros para centímetros.\n",
        "#6. Faça um CÓDIGO que peça o raio de um círculo, calcule e mostre sua área.\n",
        "##7. Faça um CÓDIGO que calcule a área de um quadrado, em seguida mostre o dobro desta\n",
        "##área para o usuário.\n",
        "##8. Faça um CÓDIGO que pergunte quanto você ganha por hora e o número de horas\n",
        "##trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.\n",
        "#9. Faça um CÓDIGO que peça um valor e mostre na tela se o valor é positivo ou negativo.\n",
        "##10. Faça um CÓDIGO que verifique se uma letra digitada é \"F\" ou \"M\". Conforme a letra\n",
        "##escrever: F - Feminino, M - Masculino, Sexo Inválido."
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T2i_yKl0zKu7",
        "outputId": "5b91d8d7-eb46-45de-853e-e40dc6a5a82f"
      },
      "execution_count": 12,
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
        "#1. Faça um CÓDIGO que mostre a mensagem \"Olá Mundo!\" na tela.\n",
        "print(\"Olá Mundo!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-dHa2vw4zfCF",
        "outputId": "9bf4c470-117f-4dec-a42b-cb08a6439a41"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá Mundo!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#2. Faça um CÓDIGO que peça um número e então mostre a mensagem O númeroinformado foi [número].\n",
        "n=int(input(\"digite um numero \"))\n",
        "print(f\"o numero catalogado foi {n}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JZ1oZAY4KJJx",
        "outputId": "c6f7929e-4c15-42da-d679-7f4da9e13cfd"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "digite um numero4\n",
            "o numero catalogado foi 4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#3. Faça um CÓDIGO que peça dois números e imprima a soma.\n",
        "lok= float(input(\"favor digite o primeiro numero \"))\n",
        "lok2= float(input(\"digite o segundo numero \"))\n",
        "print(f\"({lok+lok2})\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UmZY5Dg0WTFb",
        "outputId": "c648e575-eeae-4cbc-ca6c-dddd2658789a"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "favor digite o primeiro numero 45.7\n",
            "digite o segundo numero 4444.7\n",
            "(4490.4)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#4. Faça um CÓDIGO que peça as 4 notas bimestrais e mostre a média final.\n",
        "notas = []##espaço vazio, criei minha lista\n",
        "for i in range(4):\n",
        "  nota = float(input(f\"Digite a {i+1}ª nota: \"))\n",
        "  notas.append(nota)##adiciona o valor recebido a lista\n",
        "\n",
        "##posso manipular os valores dentro das listas\n",
        "##sun comando de soma de valores\n",
        "##len conta quantos itens tenho dentro da lista\n",
        "media = sum(notas) / len(notas)\n",
        "\n",
        "print(f\"A média final é: {media}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "avhzWNnnaBN4",
        "outputId": "f49bdd99-4ee9-4888-d8ad-31abcb9ac78a"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a 1ª nota: 8\n",
            "Digite a 2ª nota: 3\n",
            "Digite a 3ª nota: 7\n",
            "Digite a 4ª nota: 5.5\n",
            "A média final é: 5.875\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#5. Faça um CÓDIGO que converta metros para centímetros.\n",
        "lok= float(input(\"favor digite \"))\n",
        "print(f\"{lok*100:.0f}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cx7SG0F-hsz_",
        "outputId": "516ee3b4-264e-46c8-f263-be82930dc277"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "favor digite 55\n",
            "5500\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "86feb965",
        "outputId": "d2e9fbd5-606f-41cf-c015-6323fe677a27"
      },
      "source": [
        "#6. Faça um CÓDIGO que peça o raio de um círculo, calcule e mostre sua área.\n",
        "pi = 3.14159\n",
        "raio = float(input(\"Digite o raio do círculo: \"))\n",
        "m = pi * raio**2\n",
        "\n",
        "print(f\"A área do círculo é: {m:.0f}\")"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o raio do círculo: 20\n",
            "A área do círculo é: 1257\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9636ed1d",
        "outputId": "84e6d775-ffdd-454c-c2c9-58ac36510f75"
      },
      "source": [
        "#7. Faça um CÓDIGO que calcule a área de um quadrado, em seguida mostre o dobro desta\n",
        "#área para o usuário.\n",
        "\n",
        "lado = float(input(\"digite o lado do quadrado: \"))\n",
        "quadrado = lado **2\n",
        "x = quadrado * 2\n",
        "\n",
        "print(f\"quadrado é: {quadrado}\")\n",
        "print(f\"O dobro é: {x}\")"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "digite o lado do quadrado: 20\n",
            "A área do quadrado é: 400.0\n",
            "O dobro da área do quadrado é: 800.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##8. Faça um CÓDIGO que pergunte quanto você ganha por hora e o número de horas\n",
        "##trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.\n",
        "ganho= float(input(\"digite seu valor por hora\"))\n",
        "mes=float(input(\"digite o numero de horas trabalhadas no mes\"))\n",
        "\n",
        "m=ganho*mes\n",
        "print(m)\n"
      ],
      "metadata": {
        "id": "cZ4s8fCml30G"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#9. Faça um CÓDIGO que peça um valor e mostre na tela se o valor é positivo ou negativo.\n",
        "valor=int(input(\"digite o numero\"))\n",
        "if valor > 0:\n",
        "  print(\"positivo\")\n",
        "elif valor ==0:\n",
        "  print (\"0 é neutro\")\n",
        "else:\n",
        "  print(\"negativo\")"
      ],
      "metadata": {
        "id": "8bKFqLOSl_BU"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "##10. Faça um CÓDIGO que verifique se uma letra digitada é \"F\" ou \"M\". Conforme a letra\n",
        "##escrever: F - Feminino, M - Masculino, Sexo Inválido.\n",
        "letra = input(\"digite a letra (F ou M): \")\n",
        "\n",
        "if letra == \"F\" or letra ==\"f\":\n",
        "  print(\"Feminino\")\n",
        "elif letra == \"M\" or letra ==\"m\":\n",
        "  print(\"Masculino\")\n",
        "else:\n",
        "  print(\"Sexo Inválido\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BtNPRyITmEgw",
        "outputId": "9e7d8bff-8dd7-4c58-ef5e-4d5cba92614c"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "digite a letra (F ou M): GGG\n",
            "Sexo Inválido\n"
          ]
        }
      ]
    }
  ]
}