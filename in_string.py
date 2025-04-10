def check_vowels():
    # Código a implementar utilizando input.
nombre = input("Ingrese un nombre: ")
nombre = nombre.lower()
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    print(f"Contiene {vocal}: {vocal in nombre}")


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
