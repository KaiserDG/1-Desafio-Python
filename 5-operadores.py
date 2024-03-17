num1 = int(input("Digite o primeiro número\n"))
num2 = int(input("Digite o segundo número\n"))

# Aritiméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"Soma de {num1} por {num2} é: {sum}")
print(f"Subtração de {num1} por {num2} é: {sub}")
print(f"Resto da divisão de {num1} por {num2} é: {mod}")
print(f"Potência do {num1} por {num2} é: {exp}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
biggerEqual = num1 >= num2
smallerEqual = num1 <= num2

print(f"O número {num1} é maior que o número {num2}? {bigger}")
print(f"O número {num1} é menor que o número {num2}? {smaller}")
print(f"O número {num1} é igual ao número {num2}? {equal}")
print(f"O número {num1} é diferente no número {num2}? {different}")
print(f"O número {num1} é maior ou igual ao número {num2}? {biggerEqual}")
print(f"O número {num1} é menor ou igual ao número {num2}? {smallerEqual}")

# Atribuição
num1 += 1
num1 -= 1
num1 *= 1
num1 /= 1
