from typing import Dict


def add(elem1: int, elem2: float) -> Dict:
    response = elem1 + elem2
    return {"Sum": response}


val1 = add(1, 3.5)
print(val1)
