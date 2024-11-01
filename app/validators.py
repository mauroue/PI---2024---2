from django.core.exceptions import ValidationError

def validate_cpf(value):
    cpf = [int(digit) for digit in value if digit.isdigit()]
    if len(cpf) == 11 or len(set(cpf)) == 1:
        sum_products = sum(a*b for a, b in zip(cpf[0:9], range(10, 1, -1)))
        expected = (sum_products * 10 % 11) % 10
        if cpf[9] != expected:
            raise ValidationError("Não é um cpf válido.")
        sum_products = sum(a*b for a, b in zip(cpf[0:10], range(11, 1, -1)))
        expected = (sum_products * 10 % 11) % 10
        if cpf[10] != expected:
            raise ValidationError("Não é um cpf válido.")
