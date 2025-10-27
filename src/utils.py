
from math import log10
import random
from math import exp
from typing import Tuple

random.seed(42)


def binary_to_ascii(text:str) -> str:
    """
    Pega o texto em binário e decodifica para a tabela ascII.

    Parâmetros:
    ----------
    file_path : str
        Recebe texto codificado.

    Retorna:
    -------
    str
        Retorna a mensagem codificada
    """
    
    bits = text

    message = ''.join([chr(int(b,2)) for b in bits.split()])

    return message

def show_caesar_cipher(message:str) -> None:
    """
    Decifra um texto usando uma chave de substituição por deslocamento das letras.

    Parâmetros:
    ----------
    message : str
        O texto cifrado que será decifrado.

    Retorna:
    -------
    None

    Não retorna nada.
    """

    for _ in range(1,27):
        for letter in  message:
    
            ascii_code = ord(letter)
            if ascii_code != 32:

                alpha_position_new_letter = (ascii_code-65+i)%26
                new_letter = chr(alpha_position_new_letter+65)

                print(new_letter,end='')

        print("=="*80)


def by_word_frequency(message:str) -> str:
    """
    Decifra um texto usando uma chave de substituição por frequência das letras mais usadas no inglês. E mostra as quantidade de cada letra na mensagem codificada.

    Parâmetros:
    ----------
    message : str
        O texto cifrado que será decifrado.

    Retorna:
    -------
    str
        O texto decifrado de acordo com a frequência.
    """

    print("=============Decodificação por frequência=============\n")
    count_freq = {}

    for letter in message:
        count_freq[letter] = count_freq.get(letter,0)+1

    print(f"Contagem de letras :\n{dict(sorted(count_freq.items(), key=lambda item: item[1],reverse=True))}")

    mapping = str.maketrans({
        "O": "E",
        "V": "T",
        "Z": "A",
        "W": "O",
        "T": "N",
        "N": "R",
        "I": "I",
        "C": "S",
        "M":"H",
        "S":"R",
        "K":"D",
        "U":"L",
        "H":"C",
        "J":"U",
        "A":"M",
        "R":"W",
        "X":"F",
        "Q":"G",
        "G":"Y",
        "B":"P",
        "D":"B",
        "P":"V",
        "Y":"K",
        "L":"J"

    })

    deco_message = message.translate(mapping)

    return deco_message

def decrypt(text:str, key:str) -> str:
    """
    Decifra um texto usando uma chave de substituição.

    Parâmetros:
    ----------
    text : str
        O texto cifrado que será decifrado.
    key : str
        Chave de substituição com 26 letras únicas representando a correspondência de A-Z.
        Por exemplo, se key[0] = 'Q', então 'A' será substituído por 'Q'.

    Retorna:
    -------
    str
        O texto decifrado de acordo com a chave fornecida.
    """
    table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", key)
    return text.translate(table)

def random_key() -> str:
    """
    Gera uma chave de substituição aleatória para cifras de substituição.

    Parâmetros:
    ----------
    Nenhum

    Retorna:
    -------
    str
        Uma string com 26 letras únicas (A-Z) embaralhadas aleatoriamente, 
        representando uma chave de substituição.

    """
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(letters)
    return ''.join(letters)


def mutate(key:str):
    """
    Aplica uma mutação simples em uma chave de substituição trocando duas letras aleatoriamente.

    Parâmetros:
    ----------
    key : str
        Chave de substituição válida com 26 letras únicas (A-Z).

    Retorna:
    -------
    str
        Nova chave de substituição com duas letras trocadas aleatoriamente.

    """
    key = list(key)
    a, b = random.sample(range(26), 2)
    key[a], key[b] = key[b], key[a]
    return ''.join(key)

def crossover(k1:str, k2:str) -> str:
    """
    Gera uma nova chave de substituição combinando duas chaves "pais" usando um ponto de crossover simples.

    Parâmetros:
    ----------
    parent1 : str
        Primeira chave de substituição com 26 letras únicas (A-Z).
    parent2 : str
        Segunda chave de substituição com 26 letras únicas (A-Z).

    Retorna:
    -------
    str
        Nova chave de substituição (filho) com 26 letras únicas, combinando partes de parent1 e parent2.

    Funcionamento:
    ---------------
    1. Escolhe um ponto de corte aleatório.
    2. Copia a primeira parte de parent1 até o ponto de corte.
    3. Preenche o restante com letras de parent2 que ainda não estão na chave, na ordem que aparecem.
    

    """
    crossover_point = random.randint(1, len(k1) - 1)

    child = list(k1[:crossover_point])

    for letter in k2:
        if letter not in child:
            child.append(letter)

    return ''.join(child)

def genetic_decrypt(message:str, ngram_model:'ngram_score', pop_size:int = 500, generations:int = 500, mutation_rate:int = 0.9)-> Tuple[str,str]:
    """
    Decifra um texto cifrado usando um Algoritmo Genético baseado em n-gramas.

    Parâmetros:
    ----------
    message : str
        Texto cifrado a ser decifrado. Deve conter apenas letras maiúsculas A-Z.
    ngram_model : ngram_score
        Objeto que calcula o score de fluência do texto decifrado, baseado em n-gramas.
    pop_size : int, opcional (default=500)
        Número de indivíduos (chaves) na população do algoritmo genético.
    generations : int, opcional (default=1000)
        Número de gerações que o algoritmo irá evoluir.
    mutation_rate : float, opcional (default=0.9)
        Probabilidade de mutação para cada filho gerado na população.

    Retorna:
    -------
    tuple (str, str)
        - Primeiro elemento: texto decifrado com a melhor chave encontrada.
        - Segundo elemento: chave de substituição correspondente à melhor solução.

    Funcionamento:
    ---------------
    1. Inicializa a população com chaves aleatórias.
    2. Para cada geração:
        a. Avalia o score de cada chave usando n-gramas.
        b. Seleciona os melhores indivíduos (10%) como pais para o crossover e mutação.
        c. Gera nova população com (5%) de elitismo, (60%) crossover e o restante com mutação.

    3. Ao final, retorna o texto decifrado e a chave da melhor solução encontrada.

    """

    print("=============Decodificação por algorítmo genético=============\n")

    population = [random_key() for _ in range(pop_size)]
    scores = []
    for gen in range(generations):
        # Avaliação da população
        scored = [(key, ngram_model.score(decrypt(message, key))) for key in population]
        scored.sort(key=lambda x: x[1], reverse=True)
        best = scored[0]
        scores.append(best[1])

        print(f"Geração: {gen}, melhor score: {best[1]:.2f}, chave: {best[0]}")

        # Seleção dos melhores 10% como possíveis pais
        parents = [k for k, _ in scored[:pop_size // 10]]

        # === Distribuição de reprodução ===
        elite_size = int(pop_size * 0.05)   # 5% elitismo
        cross_size = int(pop_size * 0.60)   # 60% crossover
        mut_size   = pop_size - elite_size - cross_size  # restante (~35%)

        new_pop = []

        # Elitismo — mantém os melhores sem alteração
        elites = [k for k, _ in scored[:elite_size]]
        new_pop.extend(elites)

        # Crossover — gera novos indivíduos cruzando pais
        for _ in range(cross_size):
            p1, p2 = random.sample(parents, 2)
            child = crossover(p1, p2)
            new_pop.append(child)

        # Mutação — gera indivíduos mutados a partir de pais aleatórios
        for _ in range(mut_size):
            parent = random.choice(parents)
            child = mutate(parent)
            new_pop.append(child)

        
        new_pop = new_pop[:pop_size]
        population = new_pop

    return decrypt(message, best[0]), best[0]

def agenetic_decrypt(ciphertext, ngram_model, pop_size=500, generations=1000, mutation_rate=0.2):
    population = [random_key() for _ in range(pop_size)]
    scores = []
    for _ in range(generations):
        scored = [(key, ngram_model.score(decrypt(ciphertext, key))) for key in population]
        scored.sort(key=lambda x: x[1],reverse=True)
        best = scored[0]
        scores.append(best[1])
        print(f"Geração: {_}, melhor score: {best[1]:.2f}, chave: {best[0][:10]}...")
        
        # Seleção
        parents = [k for k, _ in scored[:pop_size // 10]]
        # Nova população
        new_pop = parents[:]
        while len(new_pop) < pop_size:
            p1, p2 = random.sample(parents, 2)
            child = crossover(p1, p2)
            if random.random() < mutation_rate:
                child = mutate(child)
            new_pop.append(child)
        population = new_pop
    return decrypt(ciphertext, best[0]), best[0]

class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        for line in open(ngramfile).readlines():
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.values())
        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score
       

