def slice_advanced():
texto = input("Ingresá una palabra: ")
texto = texto.lower()
primeras_tres = texto[0:3]
longitud = len(texto)
if longitud >= 3:
    inicio_medio = (longitud - 3) // 2
    letras_medio = texto[inicio_medio : inicio_medio + 3]
else:
    letras_medio = texto  # Si tiene menos de 3 letras, mostramos lo que haya
primera_a_cuarta = texto[0:4]
ultimas_tres = texto[-3:] if longitud >= 3 else texto
print(primeras_tres)
print(letras_medio)
print(primera_a_cuarta + ultimas_tres)
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
