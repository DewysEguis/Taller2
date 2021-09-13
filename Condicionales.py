
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

#Punto 3

def pto3 (mon_fi):

    if mon_fi <= 50000:
        cuota = mon_fi * 0.03
    else:
        cuota = mon_fi * 0.02
               
    return cuota

#Punto 4

def pto4 (prom, gan_diar):
    if prom > 170:
        mul = gan_diar / 2
        perdida = (gan_diar * 5) + mul

        return f'La multa es: {mul}... Y genera una perdida de: {perdida}'

    return 'No tiene ninguna sanción'

#Punto 5

def pto5 (precio, deval, incre):
    cant_deval = -1 * (((precio * deval) * deval) * deval)
    cant_incre = (((precio * incre) * incre) * incre)

    if cant_deval < (cant_incre / 2):
        return True

    return False

if pto5 (350000, -0.3, 0.1):
    print('Comprar')
else:
    print('No comprar')
