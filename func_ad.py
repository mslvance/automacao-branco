def obter_valores_ae_fixos(horario_ah7):
    print(horario_ah7)

    if horario_ah7 == "00:00":
        return [None, None, None, None, 0, 1, None, 3, 0, None, -2, None, 0, -2, None, 0, -1, None, 0, 0, 0, -9, -2, -4]
    elif horario_ah7 == "01:01":
        return [None, None, None, None, 0, 1, None, 2, -1, None, -1, None, 0, 0, None, 0, 0, None, 0, 2, -5, -5, 1, -9]
    elif horario_ah7 == "02:02":
        return [None, None, None, None, 0, -1, None, 2, -1, None, -3, None, 0, 0, None, -2, -1, None, 0, 1, -11, -7, 4, -13]
    elif horario_ah7 == "03:03":
        return [None, None, None, None, 0, 1, None, 1, -2, None, -2, None, 0, 0, None, -1, -1, None, 0, 0, -3, -5, -1, -4]
    elif horario_ah7 == "04:04":
        return [None, None, None, None, 0, 1, None, 1, -2, None, -2, None, 0, -1, None, -1, -1, None, 0, 0, -3, -6, -1, 3]
    elif horario_ah7 == "05:05":
        return [None, None, None, None, 0, 1, None, 2, -2, None, -2, None, 1, -2, None, 0, -1, None, 0, 2, -3, -1, 2, 3]
    elif horario_ah7 == "06:06":
        return [None, None, None, None, 0, 0, None, 0, 0, None, 0, None, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 0]
    elif horario_ah7 == "07:07":
        return [None, None, None, None, 0, -2, None, 0, 0, None, 0, None, 0, 0, None, 0, 0, None, 0, 0, -3, 0, 0, -2]
    elif horario_ah7 == "08:08":
        return [None, None, None, None, -3, -3, None, -1, 0, None, -1, None, 0, 0, None, 0, 0, None, 0, 1, -4, -3, 3, -1]
    elif horario_ah7 == "09:09":
        return [None, None, None, None, 0, 0, None, 0, -1, None, 0, None, 0, 0, None, 0, 0, None, 0, 4, -1, -1, 0, 10]
    elif horario_ah7 == "10:10":
        return [None, None, None, None, 0, -2, None, -4, 0, None, 0, None, 0, 0, None, 1, -2, None, 0, 0, 1, 4, 3, 2]
    elif horario_ah7 == "11:11":
        return [None, None, None, None, 0, 6, None, 0, 0, None, 0, None, 0, 0, None, -5, 0, None, 0, 0, 0, 0, 3, -4]
    elif horario_ah7 == "12:12":
        return [
            None, None, None, None, 0, 0, None, 0, 0, None, 0, None, 0, -1, None,
            0, 0, None, 0, -1, 2, 0, 0, -3
        ]
    elif horario_ah7 == "13:13":
        return [
            None, None, None, None, -1, 0, None, 0, 0, None, 0, None, 0, 0, None,
            0, 0, None, 2, -2, -1, 1, -6, -3
        ]
    elif horario_ah7 == "14:14":
        return [
            None, None, None, None, 0, 0, None, 0, 0, None, 0, None, 0, 0, None, 0, 0, None, 0, 0, 1, -3, -4, 4

        ]
    elif horario_ah7 == "15:15":
        return [
            None, None, None, None, 0, 0, None, 0, 0, None, 0, None, 0, 0, None, -2, 0, None, 0, -3, -3, -5, -2, -6
        ]

    elif horario_ah7 == "16:16":
        return [None, None, None, None, 1, 0, None, 0, 0, None, 0, None, 0, 0, None, 0, 0, None, 0, 4, -10, 4, -6, 4]
    elif horario_ah7 == "17:17":
        return [None, None, None, None, 0, 0, None, 0, 0, None, 0, None, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 0]
    elif horario_ah7 == "18:18":
        return [
            None, None, None, None, 0, 0, None, 0, 0, None, 0, None, 0, 0, None, 0, 0, None, 0, 0,
            0, 0, 0, 0

        ]
    elif horario_ah7 == "19:19":
        return [
            None, None, None, None, 0, 0, None, 0, 0, None, 0, None, 0, 0, None, 0, 0, None, 0, 0,
            0, 0, 0, 0

        ]
    elif horario_ah7 == "20:20":
        return [
            None, None, None, None, 0, 0, None, 0, 0, None, 0, None, 0, 0, None, 0, 0, None, 0, 0,
            0, 0, 0, 0

        ]
    elif horario_ah7 == "21:21":
        return [
            None, None, None, None, 0, 0, None, 0, 0, None, 0, None, 0, 0, None, 0, 0, None, 0, 0,
            0, 0, 0, 0

        ]
    elif horario_ah7 == "22:22":
        return [
            None, None, None, None, 0, 0, None, 0, 0, None, 0, None, 0, 0, None, 0, 0, None, 0, 0,
            0, 0, 0, 0

        ]
    elif horario_ah7 == "23:23":
        return [
            None, None, None, None, 0, 0, None, 0, 0, None, 0, None, 0, 0, None, 0, 0, None, 0, 0,
            0, 0, 0, 0

        ]

    else:
        return None




def calcular_ad1(valores_ah_al, valores_ae):
    return None


def calcular_ad2(valores_ah_al, valores_ae):
    return None


def calcular_ad3(valores_ah_al, valores_ae):
    return None


def calcular_ad4(valores_ah_al, valores_ae):
    return None


def calcular_ad5(valores_ah_al, valores_ae):
    if valores_ah_al is None or valores_ae is None:
        return None
    else:
        return min(valores_ah_al) - valores_ae[4]  # AE5


def calcular_ad6(valores_ah_al, valores_ae):
    if valores_ah_al is None or valores_ae is None:
        return None
    else:
        return max(valores_ah_al) - valores_ae[5]  # AE6


def calcular_ad7(valores_ah_al, valores_ae):
    return None


def calcular_ad8(ad5, ad6, valores_ae):
    if ad5 is None or ad6 is None or valores_ae is None:
        return None
    else:
        resultado_ad8 = ad5 + ad6 + 6 - valores_ae[7]

        return resultado_ad8



def calcular_ad9(valores_ah_al, valores_ae):
    if valores_ah_al is None or valores_ae is None:
        return None
    else:
        ad5 = calcular_ad5(valores_ah_al, valores_ae)
        ad6 = calcular_ad6(valores_ah_al, valores_ae)

        if ad6 is None or ad5 is None:
            return None
        elif ad6 - ad5 == 0:
            return (ad6 + ad5) * ad6 - valores_ae[8]  # AE9
        else:
            return (ad6 - ad5) - valores_ae[8]  # AE9


def calcular_ad10(valores_ah_al, valores_ae):
    return None

def calcular_ad11(ad5, ad6, valores_ae):
    if ad5 is None or ad6 is None or valores_ae is None:
        return None
    else:
        resultado_ad11 = ad6 * ad5 - valores_ae[10]  # AE11

        return resultado_ad11

def calcular_ad12(valores_ah_al, valores_ae):
    return None

def calcular_ad13(ad8, ad9, valores_ae):
    if ad8 is None or ad9 is None or valores_ae is None:
        return None
    else:
        menor_ad8_ad9 = min(ad8, ad9)
        resultado_ad13 = menor_ad8_ad9 - valores_ae[12]  # AE13

        return resultado_ad13

def calcular_ad14(ad8, ad9, valores_ae):
    if ad8 is None or ad9 is None or valores_ae is None:
        return None
    else:
        maior_ad8_ad9 = max(ad8, ad9)
        resultado_ad14 = maior_ad8_ad9 - valores_ae[13]  # AE14


        return resultado_ad14

def calcular_ad15(valores_ah_al, valores_ae):
    return None

def calcular_ad16(ad13, ad14, valores_ae):
    if ad13 is None or ad14 is None or valores_ae is None:
        return None
    else:
        resultado_ad16 = ad13 + ad14 - valores_ae[15]  # AE16

        return resultado_ad16

def calcular_ad17(ad13, ad14, valores_ae):
    if ad13 is None or ad14 is None or valores_ae is None:
        return None
    else:
        if ad14 - ad13 == 0:
            resultado_ad17 = (ad14 + ad13) * ad14  # Se AD14 - AD13 for igual a zero
        else:
            resultado_ad17 = ad14 - ad13  # Se AD14 - AD13 não for igual a zero

        resultado_ad17 -= valores_ae[16]  # Subtrair AE17

        return resultado_ad17
def calcular_ad18(valores_ah_al, valores_ae):
    return None

def calcular_ad19(ad5, ad6, valores_ae):
    if ad5 is None or ad6 is None or valores_ae is None:
        return None
    else:
        resultado_ad19 = ad5 + ad6  # Somar AD5 e AD6
        resultado_ad19 -= valores_ae[18]  # Subtrair AE19

        return resultado_ad19

def calcular_ad20(ad5, ad6, ad7, ad8, ad9, valores_ae):
    # Criar uma lista com os valores de AD5 a AD9, excluindo qualquer valor None
    valores_ad = [valor for valor in [ad5, ad6, ad7, ad8, ad9] if valor is not None]

    # Verificar se há algum valor None nos argumentos ou em valores_ae
    if None in valores_ad or valores_ae is None:
        return None  # Retorna None se houver algum valor None nos argumentos ou em valores_ae
    else:
        # Calcular a soma dos valores de AD5 a AD9
        resultado_ad20 = sum(valores_ad)

        # Subtrair o valor correspondente de valores_ae[19]
        resultado_ad20 -= valores_ae[19]


        return resultado_ad20

def calcular_ad21(ad5, ad6, ad7, ad8, ad9, ad10, ad11, valores_ae):
    # Criar uma lista com os valores de AD5 a AD11, excluindo qualquer valor None
    valores_ad = [valor for valor in [ad5, ad6, ad7, ad8, ad9, ad10, ad11] if valor is not None]

    # Verificar se há algum valor None nos argumentos ou em valores_ae
    if None in valores_ad or valores_ae is None:
        return None  # Retorna None se houver algum valor None nos argumentos ou em valores_ae
    else:
        # Calcular a soma dos valores de AD5 a AD11
        resultado_ad21 = sum(valores_ad)

        # Subtrair o valor correspondente de valores_ae[20]
        resultado_ad21 -= valores_ae[20]

        return resultado_ad21

def calcular_ad22(ad5, ad6, ad7, ad8, ad9, ad10, ad11, ad12, ad13, ad14, valores_ae):
    # Criar uma lista com os valores de AD5 a AD14, excluindo qualquer valor None
    valores_ad = [valor for valor in [ad5, ad6, ad7, ad8, ad9, ad10, ad11, ad12, ad13, ad14] if valor is not None]

    # Verificar se há algum valor None nos argumentos ou em valores_ae
    if None in valores_ad or valores_ae is None:
        return 0  # Retorna zero se houver algum valor None nos argumentos ou em valores_ae
    else:
        # Calcular a soma dos valores de AD5 a AD14
        resultado_ad22 = sum(valores_ad)

        # Subtrair o valor correspondente de valores_ae[21]
        resultado_ad22 -= valores_ae[21]

        return resultado_ad22

def calcular_ad23(ad5, ad6, ad7, ad8, ad9, ad10, ad11, ad12, ad13, ad14, ad15, ad16, ad17, valores_ae):
    # Criar uma lista com os valores de AD5 a AD17, excluindo qualquer valor None
    valores_ad = [valor for valor in [ad5, ad6, ad7, ad8, ad9, ad10, ad11, ad12, ad13, ad14, ad15, ad16, ad17] if valor is not None]

    # Verificar se há algum valor None nos argumentos ou em valores_ae
    if None in valores_ad or valores_ae is None:
        return None  # Retorna None se houver algum valor None nos argumentos ou em valores_ae
    else:
        # Calcular a soma dos valores de AD5 a AD17
        resultado_ad23 = sum(valores_ad)

        # Subtrair o valor correspondente de valores_ae[22]
        resultado_ad23 -= valores_ae[22]

        return resultado_ad23
def calcular_ad24(ad19, ad20, ad21, ad22, ad23, valores_ae):
    # Criar uma lista com os valores de AD19 a AD23, excluindo qualquer valor None
    valores_ad = [valor for valor in [ad19, ad20, ad21, ad22, ad23] if valor is not None]

    # Verificar se há algum valor None nos argumentos ou em valores_ae
    if None in valores_ad or valores_ae is None:
        return None  # Retorna None se houver algum valor None nos argumentos ou em valores_ae
    else:
        # Calcular a soma dos valores de AD19 a AD23
        resultado_ad24 = sum(valores_ad)

        # Subtrair o valor correspondente de valores_ae[23]
        resultado_ad24 -= valores_ae[23]

        return resultado_ad24


def calcular_linhas_AD(valores_ah_al, horario_ah7):
    valores_ae = obter_valores_ae_fixos(horario_ah7)

    if valores_ae is None:
        return None


    # Funções para calcular os valores de AD
    ad1 = calcular_ad1(valores_ah_al, valores_ae)
    ad2 = calcular_ad2(valores_ah_al, valores_ae)
    ad3 = calcular_ad3(valores_ah_al, valores_ae)
    ad4 = calcular_ad4(valores_ah_al, valores_ae)
    ad5 = calcular_ad5(valores_ah_al, valores_ae)
    ad6 = calcular_ad6(valores_ah_al, valores_ae)
    ad7 = calcular_ad7(valores_ah_al, valores_ae)
    ad8 = calcular_ad8(ad5, ad6, valores_ae)
    ad9 = calcular_ad9(valores_ah_al, valores_ae)
    ad10 = calcular_ad10(valores_ah_al, valores_ae)
    ad11 = calcular_ad11(ad5, ad6, valores_ae)
    ad12 = calcular_ad12(valores_ah_al, valores_ae)
    ad13 = calcular_ad13(ad8, ad9, valores_ae)
    ad14 = calcular_ad14(ad8, ad9, valores_ae)
    ad15 = calcular_ad15(valores_ah_al, valores_ae)
    ad16 = calcular_ad16(ad13, ad14, valores_ae)
    ad17 = calcular_ad17(ad13, ad14, valores_ae)
    ad18 = calcular_ad18(valores_ah_al, valores_ae)
    ad19 = calcular_ad19(ad5, ad6, valores_ae)
    ad20 = calcular_ad20(ad5, ad6, ad7, ad8, ad9, valores_ae)
    ad21 = calcular_ad21(ad5, ad6, ad7, ad8, ad9, ad10, ad11, valores_ae)
    ad22 = calcular_ad22(ad5, ad6, ad7, ad8, ad9, ad10, ad11, ad12, ad13, ad14, valores_ae)
    ad23 = calcular_ad23(ad5, ad6, ad7, ad8, ad9, ad10, ad11, ad12, ad13, ad14, ad15, ad16, ad17, valores_ae)
    ad24 = calcular_ad24(ad19, ad20, ad21, ad22, ad23, valores_ae)

    # Criar um array com os valores de AD
    array_ad = [
        ad1, ad2, ad3, ad4, ad5, ad6, ad7, ad8, ad9, ad10, ad11, ad12, ad13, ad14, ad15, ad16, ad17, ad18, ad19, ad20,
        ad21, ad22, ad23, ad24
    ]


    # Retornar o array de valores AD
    return array_ad
