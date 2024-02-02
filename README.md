Projeto prático de programação
Objetivo: Criar um programa que calcule area e volume de diferentes formas geometricas

Topicos principais:
Variaveis: 
  Armazenar dimensões das formas geometricas
    Comprimento, Largura, Altura, Raio
Operadores:
  Quadrado
    Área: A = lado ** 2
  Retângulo
    Área: A = comprimento * largura
  Triângulo
    Área: A = (base * altura) / 2
  Círculo
    Área: A = math.pi * raio ** 2
  Cilindro
    Área lateral: Al = 2 * math.pi * raio * altura
    Área total: At = 2 * math.pi * raio * (raio + altura)
    Volume: V = math.pi * raio ** 2 * altura
  Esfera
   Área da superfície: A = 4 * math.pi * raio ** 2
   Volume: V = (4 / 3) * math.pi * raio ** 3
  Cubo
   Área da superfície: A = 6 * lado ** 2
   Volume: V = lado ** 3
  Paralelepípedo (ou prisma retangular)
   Área da superfície: A = 2 * (comprimento * largura + comprimento * altura + largura * altura)
  Volume: V = comprimento * largura * altura
  
Estruturas condicionais:
    Verificar forma geométrica e escolher formula adequada
    Entrada e saída de dados: ler dimensões do usuário e mostrar os resultados dos cálculos
