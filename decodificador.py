from src.utils import *

text = str(input())

message = binary_to_ascii(text)
ngram = ngram_score("data/quadgrams.txt")

print(f"mensagem:\n {message}")

deco_message = by_word_frequency(message)


print("Texto decifrado:\n",deco_message,"\n")
print("Score:",ngram.score(deco_message))


resultado,score = genetic_decrypt(message,ngram)

print("Texto decifrado:", resultado)
print("Chave:", score)
