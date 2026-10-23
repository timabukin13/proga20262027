def encode(data):
    table = {}
    pairs = []
    phrase = ""

    for symbol in data:
        candidate = phrase + symbol
        if candidate in table:
            phrase = candidate
        else:
            pairs.append((table.get(phrase, 0), symbol))
            table[candidate] = len(table) + 1
            phrase = ""

    if phrase:
        pairs.append((table[phrase], ""))

    return pairs


def decode(pairs):
    entries = [""]
    pieces = []

    for ref, symbol in pairs:
        text = entries[ref] + symbol
        pieces.append(text)
        if symbol:
            entries.append(text)

    return "".join(pieces)

a = encode("abbobba")
print(a)
b = decode(a)
print(b)
