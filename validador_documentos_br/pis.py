import re

def validar_pis(valor):
    # Converte para string e remove caracteres não numéricos
    valor = re.sub('[^0-9]', '', str(valor))
    
    # Verifica se o tamanho é adequado e ajusta se necessário
    if len(valor) > 11:
        return False  # Mais de 11 dígitos não são válidos
    elif len(valor) < 11:
        valor = valor.zfill(11)  # Adiciona zeros à esquerda se menos de 11 dígitos
    
    # Prepara os pesos para o cálculo do dígito verificador
    pesos = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    
    # Calcula a soma dos produtos dos dígitos pelos pesos
    total = sum(int(digito) * peso for digito, peso in zip(valor, pesos))
    
    # Calcula o dígito verificador
    resto = total % 11
    dv = 0 if resto < 2 else 11 - resto
    
    # Compara o dígito verificador calculado com o último dígito do valor
    return dv == int(valor[-1])