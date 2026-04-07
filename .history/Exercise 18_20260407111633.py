def decimal_to_binary(decimal: int) -> str:
    
    if decimal < 0:
        return '-' + bin(-decimal)[2:]
    return bin(decimal)[2:]


def decimal_to_octal(decimal: int) -> str:
    
    if decimal < 0:
        return '-' + oct(-decimal)[2:]
    return oct(decimal)[2:]


def decimal_to_hexadecimal(decimal: int) -> str:
   
    if decimal < 0:
        return '-' + hex(-decimal)[2:].upper()
    return hex(decimal)[2:].upper()