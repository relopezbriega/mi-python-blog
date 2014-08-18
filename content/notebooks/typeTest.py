from typing import List, Dict

# Declaro los tipos de las variables
texto = ''              # type: str
entero = 0              # type: int
lista_enteros = []      # type: List[int]
dic_str_int = {}        # type: Dict[str, int]

# Asigno valores a las variables.
texto = 'Raul'
entero = 13
lista_enteros = [1, 2, 3, 4]
dic_str_int = {'raul': 1, 'ezequiel': 2}

# Intento asignar valores de otro tipo.
texto = 1
entero = 'raul'
lista_enteros = ['raul', 1, '2']
dic_str_int = {1: 'raul'}