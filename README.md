# Calculadora de IMC

## Descrição
Este é um projeto simples para calcular o Índice de Massa Corporal (IMC). O IMC é um valor utilizado para determinar se uma pessoa está dentro do peso ideal, abaixo do peso ou acima do peso, com base na relação entre peso e altura.

## Funcionalidades
- Entrada do peso (kg) e altura (m)
- Cálculo automático do IMC
- Classificação do IMC de acordo com os padrões da OMS
- Interface simples e intuitiva

## Como Usar
```sh
# Clone o repositório
git clone https://github.com/seu-usuario/calc_imc.git

# Acesse a pasta do projeto
cd calc_imc

# Execute o script principal
python main.py
```

## Cálculo do IMC
A fórmula utilizada para calcular o IMC é:
```plaintext
IMC = peso (kg) / (altura (m) * altura (m))
```

### Classificação do IMC
| IMC            | Classificação         |
|---------------|-----------------|
| Menor que 18.5 | Abaixo do peso  |
| 18.5 - 24.9   | Peso normal     |
| 25 - 29.9     | Sobrepeso       |
| 30 - 34.9     | Obesidade grau 1 |
| 35 - 39.9     | Obesidade grau 2 |
| Maior que 40  | Obesidade grau 3 |

## Tecnologias Utilizadas
- Python 3.x

## Contribuição
Se quiser contribuir, fique à vontade para abrir um pull request!

## Licença
Este projeto está sob a licença MIT.

