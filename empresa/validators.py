from validate_docbr import CPF

def nomeValido(nome):
    nomevalid = nome
    nome_valid = any(chr.isdigit() for chr in nome)
    return nome_valid

def cpfValido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def horaValida(horas):
    horaSemanal = 40
    return horaSemanal
