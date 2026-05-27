def dec_to_sen(decimal_number : int) -> str: # base-10 -> base-6
    if decimal_number == 0:
        return '0'

    is_negative : bool = False
    if decimal_number < 0:
        is_negative = True
        decimal_number *= -1

    result : list[str] = []
    while decimal_number != 0:
        remainder : int = decimal_number % 6
        result.append(str(remainder))
        decimal_number //= 6
    
    base6_num : str = ''.join(reversed(result))
    if is_negative:
        base6_num = '-' + base6_num

    return base6_num

def sen_to_dec(senary_string : str) -> int: # base-6 -> base-10
    is_negative : bool = False
    if senary_string[0] == '-':
        senary_string = senary_string[1:]
        is_negative = True

    if _check_base6_num(senary_string) == False:
        raise ValueError(f"{senary_string} is not a senary number")
    
    result : int = 0
    for i, c in enumerate(reversed(senary_string)):
        result += int(c) * (6 ** i)
    
    if is_negative:
        result *= -1
    
    return result

def _check_base6_num(base6_str : str) -> bool:
    if len(base6_str) == 0:
        return False
    base6 : list[str] = list('012345')
    for c in base6_str:
        if c not in base6:
            return False
    return True
