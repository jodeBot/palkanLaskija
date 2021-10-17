def main():
    print('Anna kokonaispalkka euroina: ')
    palkka = luvunpyytaja()
    print('Anna veroprosentti (0-100): ')
    veroprosentti = luvunpyytaja()
    nettopalkka = palkka * ((100 - veroprosentti)/100)
    format(nettopalkka, '.2f')
    print('Bruttopalkkasi on', palkka, 'ja veroprosenttisi on', veroprosentti, '.\nNettopalkkasi on', nettopalkka, 'euroa.')

def luvunpyytaja():
    try:
        lukuarvo = input('Anna luku: ')
        lukuarvo = float(lukuarvo)
        return lukuarvo
    except Exception:
        print('Virheellinen arvo.')

if __name__ == '__main__':
    main()