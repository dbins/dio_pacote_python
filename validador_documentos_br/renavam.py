def validar_renavam(renavam):
    # valida casos menores e de tamanho > 11 digitos
    if len(renavam) < 9 or len(renavam) > 11:
        return False

    # adiciona 2 zeros em casos de numeros antigos
    if len(renavam) == 9:
        renavam = '00{}'.format(renavam)

    # remove ultimo digito (verificador)
    renavam_sem_digito = renavam[:-1]

    # inverte
    renavam_sem_digito = renavam_sem_digito[::-1]

    # Multiplica as strings reversas do renavam pelos numeros multiplicadores
    # para apenas os primeiros 8 digitos de um total de 10
    # Exemplo: renavam reverso sem digito = 69488936
    # 6, 9, 4, 8, 8, 9, 3, 6
    # *  *  *  *  *  *  *  *
    # 2, 3, 4, 5, 6, 7, 8, 9 (numeros multiplicadores - sempre os mesmos [fixo])
    soma = 0
    for i, digito in enumerate(renavam_sem_digito[:8]):
        soma += int(digito) * (i + 2)

    # Multiplica os dois ultimos digitos e soma
    soma += int(renavam_sem_digito[8]) * 2
    soma += int(renavam_sem_digito[9]) * 3


    # mod11 = 284 % 11 = 9 (resto da divisao por 11)
    mod11 = soma % 11

    # Faz-se a conta 11 (valor fixo) - mod11 = 11 - 9 = 2
    ultimo_digito_calculado = 11 - mod11

    # ultimoDigito = Caso o valor calculado anteriormente seja 10 ou 11,
    # transformo ele em 0. caso contrario, eh o proprio numero
    if ultimo_digito_calculado >= 10:
        ultimo_digito_calculado = 0

    # Pego o ultimo digito do renavam original (para confrontar com o calculado)
    # Comparo os digitos calculado e informado
    if ultimo_digito_calculado == int(renavam[-1]):
        return True
    return False