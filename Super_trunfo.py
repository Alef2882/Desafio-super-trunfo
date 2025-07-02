import random

# Lista de cartas
cartas = [
    {"nome": "Dragão", "ataque": 90, "defesa": 70, "magia": 85},
    {"nome": "Fênix", "ataque": 75, "defesa": 60, "magia": 95},
    {"nome": "Gigante", "ataque": 80, "defesa": 90, "magia": 40},
    {"nome": "Elfo", "ataque": 60, "defesa": 50, "magia": 90},
    {"nome": "Cavaleiro", "ataque": 85, "defesa": 80, "magia": 50}
]

# Sorteia uma carta para cada jogador
jogador = random.choice(cartas)
computador = random.choice(cartas)

print(f"Sua carta: {jogador['nome']}")
print("Atributos disponíveis: ataque, defesa, magia")
atributo = input("Escolha um atributo para disputar: ").lower()

print(f"\nSua carta: {jogador['nome']} ({atributo}: {jogador[atributo]})")
print(f"Carta do computador: {computador['nome']} ({atributo}: {computador[atributo]})")

if jogador[atributo] > computador[atributo]:
    print("🎉 Você venceu!")
elif jogador[atributo] < computador[atributo]:
    print("😞 Você perdeu.")
else:
    print("🤝 Empate!")

