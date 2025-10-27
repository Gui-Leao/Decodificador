
# Decodificador

Projeto simples para decodificação de mensagens cifradas. O repositório inclui ferramentas para:

- Converter um arquivo com bytes em texto ASCII (binário -> texto).
- Tentar uma decodificação por deslocamento.
- Tentar uma decodificação por frequência.
- Tentar uma decodificação automática usando um Algoritmo Genético avaliado por n-gramas (quadgrams).

O arquivo `decodificador.py` mostra um exemplo de uso que carrega os dados em `data/` e executa os métodos presentes em `src/utils.py`.

## Como executar

1. Abra um terminal na raiz do projeto.
2. (Opcional) Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```


3. Execute o script principal:

```powershell
python .\decodificador.py < data/mensagem_codificada.txt
```
ou se estiver usando o `uv`:
```powershell   
uv run decodificador.py <  data/mensagem_codificada.txt 
```

O script fará o seguinte fluxo básico:

- Lê `data/mensagem_codificada.txt` como binário e converte para ASCII (função `binary_to_ascii`).
- Mostra uma tentativa de decodificação por frequência (`by_word_frequency`).
- Calcula o score do texto usando `ngram_score` com `data/quadgrams.txt`.
- Executa o algoritmo genético (`genetic_decrypt`) para tentar encontrar uma chave de substituição e imprime o texto decodificado e a chave.

## Estrutura do projeto

- `decodificador.py` - Exemplo/entrypoint que demonstra as funções de `src/utils.py`.
- `src/utils.py` - Implementações das funções utilitárias: leitura binária, decodificadores (frequência, genético), geração/mutação/crossover de chaves e classe `ngram_score`.
- `data/mensagem_codificada.txt` - Arquivo com a mensagem codificada em formato binário (usado pelo exemplo).
- `data/quadgrams.txt` - Frequências de quadgrams usadas para avaliar a fluência do texto durante a busca genética.


## Observações e contribuições

- Se quiser testar com outra mensagem, substitua `data/mensagem_codificada.txt`.
---

Se quiser, atualizo o README com exemplos de saída (prints) ou adiciono um pequeno script de linha de comando que aceite parâmetros (por exemplo: arquivo de entrada, método a usar, parâmetros do GA). Quer que eu faça isso agora?
