# Importar as funções
# Toda vez que chamarmos "m" o programa importará o modulo.
import modulo as m 

m.limpar()
while True:
    print("1 - Calcular a área do quadrado")
    print("2 - Calcular a área do retângulo")
    print("3 - Calcular a área do triângulo")
    print("4 - Calcular a área do circulo")
    print("5 - Calcular a área do trapézio")
    print("6 - Sair do programa")

    opcao = input("Informe a opção desejada: ").strip()
    m.limpar()
    match opcao:
        case "1":
            l = float(input("Informe o lado do quadrado: ").strip().replace(",","."))
            m.limpar()
            area = m.quadrado(l)
            print(f"\nÁrea do quadrado: {area}")
            continue
        case "2":
            b = float(input("Informe a base do retângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do triângulo: ").strip().replace(",","."))
            m.limpar()
            area = m.retangulo(b, h)
            print(f"\nÁrea do retângulo: {area}")
            continue
        case "3": 
            b = float(input("Informe a base do triângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do triângulo: ").strip().replace(",","."))
            m.limpar()
            area = m.triangulo(b,h)
            print(f"\nÁrea do triângulo: {area}")
            continue
        case "4":
            r = float(input("Informe o raio do círculo: ").strip().replace(",","."))
            m.limpar()
            area = m.circulo(r)
            print(f"\nÁrea do círculo: {area}")
            continue
        case "5":
            b = float(input("Informe a base menor do trapézio: ").strip().replace(",","."))
            B = float(input("Informe a base maior: ").strip().replace(",","."))
            h = float(input("Informe a altura do trapézio: ").strip().replace(",","."))
            area = m.trapezio(b, B, h)
            print(f"\nÁrea do trapézio: {area}")
            continue
        case "6":
            print("Saindo do programa")
            break
        case _:
            print("Opção inválida. Tente de novo.")
            continue