
#Punto 1
def pto1(n_ca, t_co):
    if n_ca >= 3:
        des = t_co * 0.3
    else:
        des = t_co * 0.1

    t_pagar = t_co - des

    return des, t_pagar

des_1, tot_1 = pto1(4, 100000)
print(f'Desucento: {des_1} ... Total a pagar por la compra de camisas: {tot_1}')

#Punto 2

def pto2 (num, t_com):

    if num >= 74:
        desc = t_com * 0.2
    else:
        desc = t_com * 0.15

    return desc
