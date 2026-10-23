encoded = [(0, 0, "a"),(0, 0, "b"),(2, 1, "d"),(2, 1, "k"),(4, 3, "b"),(0, 0, "r"),(0, 0, "a")]

def decode(code):
    result = ""

    for offset, length, next in code:
        if offset == 0 and length == 0:
            result += next
            continue

        bias = len(result) - offset


        for i in range(length):
            result += result[bias]
            bias += 1

        result += next

    return result
print(decode(encoded))