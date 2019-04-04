from rodna_cisla import format_rč
from rodna_cisla import delitelnost
from rodna_cisla import datum_narozeni
from rodna_cisla import pohlavi

rc_od_uzivatele = input('Zadej rodné číslo:')
rc_str = str(rc_od_uzivatele)
print(format_rč(rc_str))
print(delitelnost(rc_str))
print(datum_narozeni(rc_str))
print(pohlavi(rc_str))
