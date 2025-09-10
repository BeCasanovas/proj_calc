def calcular_nota(ap1, ap2, ac):
    nota_final = (ap1 * 0.4) + (ap2 * 0.4) + (ac * 0.2)
    return nota_final

def calcular_nota_as(nota_final, ap1, ap2, ac):
    if nota_final < 7:
        if ap1 >= ap2:
            nota_as = (7 - (ap2 * 0.4 + ac * 0.2)) / 0.4
        else:
            nota_as = (7 - (ap1 * 0.4 + ac * 0.2)) / 0.4
        return nota_as