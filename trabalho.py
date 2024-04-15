nome = input("Qual é o seu nome? ")
altura_cm = float(input("Qual é a sua altura em centímetros? "))
peso_kg = float(input("Qual é o seu peso em quilogramas? "))

altura_m = altura_cm / 100

imc = peso_kg / (altura_m ** 2)

# Classificar o IMC
classificacao = ""
if imc < 18.5:
    classificacao = "Abaixo do Peso (Pegue suplementos do Cariani)"
elif 18.5 <= imc <= 24.9:
    classificacao = "Peso Ideal (Para Bens)"
elif 25.0 <= imc <= 29.9:
    classificacao = "Sobrepeso"
elif 30.0 <= imc <= 34.9:
    classificacao = "Obesidade Grau 1"
elif 35.0 <= imc <= 39.9:
    classificacao = "Obesidade Grau 2"
else:
    classificacao = "Obesidade Grau 3"


print(f"\nNome: {nome}")
print(f"Altura: {altura_cm} cm")
print(f"Peso: {peso_kg} kg")
print(f"IMC: {imc:.2f}")
print("Classificação:", classificacao)