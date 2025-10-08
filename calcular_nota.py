def calcular_nota(ap1, ap2, ac):
    nota_final = (ap1 * 0.4) + (ap2 * 0.4) + (ac * 0.2)
    return nota_final

def calcular_nota_as(nota_final, ap1, ap2, ac):
    if nota_final < 7:
        # Mantém a maior nota entre AP1 e AP2, substitui a menor pela AS
        if ap1 >= ap2:
            # Mantém AP1, substitui AP2 pela AS
            nota_as = (7 - ap1 * 0.4 - ac * 0.2) / 0.4
        else:
            # Mantém AP2, substitui AP1 pela AS
            nota_as = (7 - ap2 * 0.4 - ac * 0.2) / 0.4
        return nota_as
    
def verficar_nota(ap1, ap2, ac):
    nota = round(calcular_nota(ap1, ap2, ac), 2)
    if nota >= 7:
        return f"Aprovado, com nota {nota:.2f}"
    elif nota < 7:
        nota_as = round(calcular_nota_as(nota, ap1, ap2, ac), 2)
        if nota_as is not None and nota_as <= 10:
            return f"Precisa tirar {nota_as:.2f} na AS"
        else:
            return "Reprovado"