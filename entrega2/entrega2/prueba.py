def test(recibir):
    user = ['Usuario', 'adm', 'lucifer']
    retorno = False
    for i in user:
        if recibir == i:
            retorno = True
            return retorno
        else:
            return retorno

def test2(recibir):
    user = ['Usuario', 'adm', 'lucifer']
    retorno = False
    for i in user:
        if recibir != i:
            retorno = True
            return retorno
        else:
            return retorno
     


