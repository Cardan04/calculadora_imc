def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal (IMC)."""
    return peso / (altura ** 2)

if __name__ == "__main__":
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")