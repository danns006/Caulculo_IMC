try:
    peso = float(input("Digite seu peso(Kg): "))
    altura = float(input("Digite sua altura(em metros): "))
    
    imc = peso / (altura ** 2)
    
    print(f"O seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Você esta abaixo do peso ideal.")
    elif 18.5 <= imc < 24.9:
        print("Você esta no peso ideal.")
    elif 25 <= imc < 29.9:
        print("Você esta com sobrepeso.")
    elif 30 <= imc < 34.9:
        print("Você tem obesidade grau 1.")
    elif 35 <= imc < 39.9:
        print("Você tem obesidade grau 2.")
    else:
        print("Você tem obesidade grau 3.")

except ValueError:
    print("digite valores validos.")
