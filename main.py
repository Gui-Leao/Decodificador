from src.utils import binary_to_ascii,show_caesar_cipher

message = binary_to_ascii("mensagem_codificada.txt")


print(f"mensagem: {message}")

# Testar casos da cifra de Cezar para a mensagem
#show_caesar_cipher(message)


count_freq = {}

for letter in message:
    count_freq[letter] = count_freq.get(letter,0)+1



print(dict(sorted(count_freq.items(), key=lambda item: item[1],reverse=True)))

mapeamento = str.maketrans({
    "O": "E",
    "V": "T",
    "Z": "A",
    "W": "O",
    "T": "N",
    "N": "R",
    "C": "S",
    "M":"H",
})

deco_message = message.translate(mapeamento)

print(deco_message)





