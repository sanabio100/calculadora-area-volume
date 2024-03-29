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

def main():
    forma = input("Digite a forma geométrica: ").lower()
    tipo_forma = verificar_tipo_forma(forma)

    if tipo_forma == "bidimensional":
        if forma in ["quadrado", "retangulo", "triangulo", "circulo"]:
            args = tuple(map(float, input(f"Digite os valores para {forma} separados por espaço: ").split()))
            area, _ = calcular_area_volume(forma, *args)
            print(f"A área do {forma} é: {area}")
    elif tipo_forma == "tridimensional":
        if forma in ["cilindro", "esfera", "cubo", "paralelepipedo"]:
            args = tuple(map(float, input(f"Digite os valores para {forma} separados por espaço: ").split()))
            resultados = calcular_area_volume(forma, *args)
            if len(resultados) == 2:
                area, volume = resultados
                print(f"A área da superfície do {forma} é: {area}")
                print(f"O volume do {forma} é: {volume}")
            else:
                area_lateral, area_total, volume = resultados
                print(f"A área lateral do {forma} é: {area_lateral}")
                print(f"A área total do {forma} é: {area_total}")
                print(f"O volume do {forma} é: {volume}")
    else:
        print("Forma não reconhecida")

if __name__ == "__main__":
    main()
