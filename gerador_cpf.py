import random

def gera_cpf():
    while True:
        # Gera os nove primeiros dígitos do CPF
        nove_digitos = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        
        # Verifica se os dígitos não são sequenciais ou repetidos
        if (nove_digitos in ['123456789', '987654321'] or
            all(n == nove_digitos[0] for n in nove_digitos)):
            continue
        
        # Cálculo dos dígitos verificadores
        primeiro_digito = calcula_digito(nove_digitos, 10)
        dez_digitos = nove_digitos + str(primeiro_digito)
        segundo_digito = calcula_digito(dez_digitos, 11)
        
        # Retorna o CPF formatado
        return f'{nove_digitos}{primeiro_digito}{segundo_digito}'

def calcula_digito(digitos, peso):
    soma = sum(int(numero) * (peso - i) for i, numero in enumerate(digitos))
    resto_divisao = (soma * 10) % 11
    return 0 if resto_divisao > 9 else resto_divisao

if __name__ == '__main__':
    print(f'O seu CPF válido gerado é: {gera_cpf()}')
