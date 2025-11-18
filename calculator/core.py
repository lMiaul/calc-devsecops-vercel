def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def operate(a: float, b: float, op: str) -> float:
    if op == "add":
        return add(a, b)
    if op == "sub":
        return sub(a, b)
    if op == "mul":
        return mul(a, b)
    if op == "div":
        return div(a, b)
    raise ValueError(f"Operador no soportado: {op}")
