def format_rč(zadane_rč):
    pocet_lomitek = zadane_rč.count('/')
    if pocet_lomitek == 0:
        return False
    elif pocet_lomitek >= 2:
        return False
    elif pocet_lomitek == 1:
        index_lomitka = zadane_rč.find('/')
        if index_lomitka != 6:
            return False
        else:
            try:
                pred_lomitkem = int(zadane_rč[:index_lomitka])
                return True
            except ValueError:
                return False
            try:
                po_lomitku = int(zadane_rč[index_lomitka+1:])
                if len(po_lomitku) != 4:
                    return False
                else:
                    return True
            except ValueError:
                return False

#print(format_rč('123456/5214'))

def delitelnost(zadane_rč):
    po_lomitku = zadane_rč[7:]
    pred_lomitkem = zadane_rč[:6]
    cislo_delitelne_jedenacti = int(pred_lomitkem + po_lomitku)
    zbytek = cislo_delitelne_jedenacti % 11
    if zbytek != 0:
        return False
    elif zbytek == 0:
        return True

#print(delitelnost('935623/6175'))

def datum_narozeni(zadane_rč):
    rok = zadane_rč[:2]
    den = zadane_rč[4:6]
    mesic = zadane_rč[2:4]
    if int(mesic) > 50:
        mesic = int(mesic) - 50
    return int(den), int(mesic), int(rok)

#print(datum_narozeni('935623/6175'))

def pohlavi(zadane_rč):
    if int(zadane_rč[2:4]) > 50:
        return 'žena'
    elif int(zadane_rč[2:4]) < 50:
        return 'muž'

#print(pohlavi('935623/6175'))
