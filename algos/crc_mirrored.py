from algos.utils.reverse_bits import reverse_bits


# Дзеркальний алгоритм для CRC-4-ITU
def crc_mirrored(message, polynomial, polynomial_length):
    crc = 0
    mirrored_polynomial = reverse_bits(polynomial, polynomial_length + 1)
    for bit in message:
        # Зсуваємо вправо і додаємо новий біт з правого боку
        crc = ((crc >> 1) | (bit << polynomial_length)) & ((1 << (polynomial_length + 1)) - 1)
        if crc & 1:  # якщо молодший біт дорівнює 1
            crc ^= mirrored_polynomial
    return reverse_bits(crc, polynomial_length) & ((1 << polynomial_length) - 1)