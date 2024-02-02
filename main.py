import math

def calcular_area_volume(forma, *args):
    """
    Calcula a área e/ou volume da forma geométrica especificada.

    Args:
        forma (str): A forma geométrica para a qual calcular área e/ou volume.
        *args: Dimensões necessárias para calcular a área e/ou volume da forma.

    Returns:
        tuple: Uma tupla contendo a área e/ou volume calculados, dependendo da forma.
    """
    if forma == "quadrado":
        lado = args[0]
        area = lado ** 2
        return area, None
    elif forma == "retangulo":
        comprimento, largura = args
        area = comprimento * largura
        return area, None
    elif forma == "triangulo":
        base, altura = args
        area = (base * altura) / 2
        return area, None
    elif forma == "circulo":
        raio = args[0]
        area = math.pi * raio ** 2
        return area, None
    elif forma == "cilindro":
        raio, altura = args
        area_lateral = 2 * math.pi * raio * altura
        area_total = 2 * math.pi * raio * (raio + altura)
        volume = math.pi * raio ** 2 * altura
        return area_lateral, area_total, volume
    elif forma == "esfera":
        raio = args[0]
        area_superficie = 4 * math.pi * raio ** 2
        volume = (4 / 3) * math.pi * raio ** 3
        return area_superficie, volume
    elif forma == "cubo":
        lado = args[0]
        area_superficie = 6 * lado ** 2
        volume = lado ** 3
        return area_superficie, volume
    elif forma == "paralelepipedo":
        comprimento, largura, altura = args
        area_superficie = 2 * (comprimento * largura + comprimento * altura + largura * altura)
        volume = comprimento * largura * altura
        return area_superficie, volume
    else:
        return None

def verificar_tipo_forma(forma):
    """
    Verifica se a forma geométrica é bidimensional ou tridimensional.

    Args:
        forma (str): A forma geométrica a ser verificada.

    Returns:
        str: 'bidimensional' se a forma é bidimensional, 'tridimensional' se é tridimensional, ou 'Forma não reconhecida' se a forma não for válida.
    """
    formas_bidimensionais = ["quadrado", "retangulo", "triangulo", "circulo"]
    formas_tridimensionais = ["cilindro", "esfera", "cubo", "paralelepipedo"]

    if forma in formas_bidimensionais:
        return "bidimensional"
    elif forma in formas_tridimensionais:
        return "tridimensional"
    else:
        return "Forma não reconhecida"

def main():
    """
    Função principal para interação com o usuário e cálculo de áreas e volumes de formas geométricas.
    """
    forma = input("Digite a forma geométrica: ").lower()

    if verificar_tipo_forma(forma) == "bidimensional":
        if forma == "quadrado":
            lado = float(input("Digite o valor do lado: "))
            area, _ = calcular_area_volume(forma, lado)
            print(f"A área do quadrado é: {area}")
        elif forma == "retangulo":
            comprimento = float(input("Digite o valor do comprimento: "))
            largura = float(input("Digite o valor da largura: "))
            area, _ = calcular_area_volume(forma, comprimento, largura)
            print(f"A área do retângulo é: {area}")
        elif forma == "triangulo":
            base = float(input("Digite o valor da base: "))
            altura = float(input("Digite o valor da altura: "))
            area, _ = calcular_area_volume(forma, base, altura)
            print(f"A área do triângulo é: {area}")
        elif forma == "circulo":
            raio = float(input("Digite o valor do raio: "))
            area, _ = calcular_area_volume(forma, raio)
            print(f"A área do círculo é: {area}")
    elif verificar_tipo_forma(forma) == "tridimensional":
        if forma == "cilindro":
            raio = float(input("Digite o valor do raio: "))
            altura = float(input("Digite o valor da altura: "))
            area_lateral, area_total, volume = calcular_area_volume(forma, raio, altura)
            print(f"A área lateral do cilindro é: {area_lateral}")
            print(f"A área total do cilindro é: {area_total}")
            print(f"O volume do cilindro é: {volume}")
        elif forma == "esfera":
            raio = float(input("Digite o valor do raio: "))
            area_superficie, volume = calcular_area_volume(forma, raio)
            print(f"A área da superfície da esfera é: {area_superficie}")
            print(f"O volume da esfera é: {volume}")
        elif forma == "cubo":
            lado = float(input("Digite o valor do lado: "))
            area_superficie, volume = calcular_area_volume(forma, lado)
            print(f"A área da superfície do cubo é: {area_superficie}")
            print(f"O volume do cubo é: {volume}")
        elif forma == "paralelepipedo":
            comprimento = float(input("Digite o valor do comprimento: "))
            largura = float(input("Digite o valor da largura: "))
            altura = float(input("Digite o valor da altura: "))
            area_superficie, volume = calcular_area_volume(forma, comprimento, largura, altura)
            print(f"A área da superfície do paralelepípedo é: {area_superficie}")
            print(f"O volume do paralelepípedo é: {volume}")
    else:
        print("Forma não reconhecida")

if __name__ == "__main__":
    main()
