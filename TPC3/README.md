# TPC3

## Descrição do problema


### Somador on/off

* Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;

* Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
* Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
* Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.


## Solução problema

Para este problema criamos uma função que recebe o input já como string a ser interpretada. Assim, ecnontra todas as ocorrências dos padrões desejandos utilizando assim um findall para encontrar todas as ocorrências desejadas. Para este efetiro, utilizamos a flag **IGNORECASE** de modo a ignorar maiúsculas e passamos então a seguinte expressão regular: 
     
```python
r'[-+]?\d+|Off|On|='
```

Dito isto, iteramos então todos os valores resultantes executando as operações mencionadas no desafio, por ordem sequencial.

### Usage

Para utilizar o programa, o input pode ser dado de dois modos: através de um ficheiro caso este seja passado como primeiro argumento argumento, ou lendo do stdin.

Exemplos:
``` zsh
python addOnOff.py testFile.txt
python addOnOff.py
```