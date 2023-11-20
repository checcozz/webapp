from datetime import datetime, timedelta
import random


def peso(ty, d):
    return ty * 0.6 + d * 0.4

def estrazione():
    token_value = 0.5
    prezzo_acquisto = 500
    markup = 0.2 * prezzo_acquisto
    t = int
    diff = datetime
    today = datetime.now()

    t1=400
    t2=250
    t3=300
    t4=80
    t=t1+t2+t3+t4

    diff1=(today-datetime(2023,10,10)).days
    diff2=(today-datetime (2023,8,23)).days
    diff3=(today-datetime (2023,5,9)).days
    diff4=(today-datetime(2022,12,30)).days


    #aggiungere controllo data se oggi > della data di iscrizione
    #aggiungere check che numero tokens > valore oggetto

    if t < 2*(prezzo_acquisto+markup):

        peso1=peso(t1,diff1)
        peso2=peso(t2,diff2)
        peso3=peso(t3,diff3)
        peso4=peso(t4,diff4)

        print(peso1,peso2,peso3,peso4)



        List = [1, 2, 3, 4]
        vincitore = random.choices(List, weights=(peso1,peso2,peso3,peso4), k=1)

        return vincitore

        #print(vincitore)

        #risultato = input('ha vinto '+  ','.join(str(x) for x in vincitore) +  ' ti va bene?')

        #if risultato == 'si' :
        #    exit()
        #else:
        #    vincitore = random.choices(List, weights=(peso1, peso2, peso3, peso4), k=1)
        #    print(vincitore)
        #return risultato

    return ('buuuuuuuug')
     #   print('acquista un altro oggetto')