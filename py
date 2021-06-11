import itertools
def anagrama():
    frase = str(input('Informe a palavra:\t'))
    t = [''.join(txt) for  txt in itertools.permutations(frase)]
    print(t)

anagrama()
