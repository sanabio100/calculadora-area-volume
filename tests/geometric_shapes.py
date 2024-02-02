import math

def calcular_area_volume(forma, *args):
    if forma == "quadrado":
        return args[0] ** 2, None
    elif forma == "retangulo":
        return args[0] * args[1], None
    elif forma == "triangulo":
        return (args[0] * args[1]) / 2, None
    elif forma == "circulo":
        return math.pi * args[0] ** 2, None
    elif forma == "cilindro":
        raio, altura = args
        area_lateral = 2 * math.pi * raio * altura
        area_total = area_lateral + 2 * math.pi * raio ** 2
        volume = math.pi * raio ** 2 * altura
        return area_lateral, area_total, volume
    elif forma == "esfera":
        return 4 * math.pi * args[0] ** 2, (4 / 3) * math.pi * args[0] ** 3
    elif forma == "cubo":
        lado = args[0]
        return 6 * lado ** 2, lado ** 3
    elif forma == "paralelepipedo":
        comprimento, largura, altura = args
        area_superficie = 2 * (comprimento * largura + comprimento * altura + largura * altura)
        volume = comprimento * largura * altura
        return area_superficie, volume
    else:
        return None

def verificar_tipo_forma(forma):
    formas_bidimensionais = ["quadrado", "retangulo", "triangulo", "circulo"]
    formas_tridimensionais = ["cilindro", "esfera", "cubo", "paralelepipedo"]
    return "bidimensional" if forma in formas_bidimensionais else "tridimensional" if forma in formas_tridimensionais else "Forma não reconhecida"

if __name__ == "__main__":
    print("Este é o módulo geometric_shapes. Ele fornece funções para calcular áreas e volumes de formas geométricas.")
