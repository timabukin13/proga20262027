def compress(data):
    alphabet = sorted(set(data))
    table = {symbol: i for i, symbol in enumerate(alphabet)}

    output = []
    phrase = ""

    for symbol in data:
        candidate = phrase + symbol
        if candidate in table:
            phrase = candidate
        else:
            output.append(table[phrase])
            table[candidate] = len(table)
            phrase = symbol

    if phrase:
        output.append(table[phrase])

    return output, alphabet


def decompress(codes, alphabet):

    table = dict(enumerate(alphabet))

    previous = table[codes[0]]
    pieces = [previous]

    for code in codes[1:]:
        if code in table:
            entry = table[code]
        elif code == len(table):
            entry = previous + previous[0]

        pieces.append(entry)
        table[len(table)] = previous + entry[0]
        previous = entry

    return "".join(pieces)
a = compress("abbobba")
print(a)
b = decompress(a[0], ['a', 'b', 'o'])
print(b)


