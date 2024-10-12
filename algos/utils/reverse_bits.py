# Функція для реверсування бітів (дзеркальне відображення)
def reverse_bits(value, bit_length):
    result = 0
    for _ in range(bit_length):
        result = (result << 1) | (value & 1)
        value >>= 1
    return result