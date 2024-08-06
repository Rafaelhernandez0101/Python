def palidromo(txt: str): 
    txt = txt.replace(' ', '').lower()
    return txt == txt[::-1]

text_1 = 'A mama Roma le aviva el amor a mama'
text_2 = 'Funcion'

print(palidromo(text_1)) 