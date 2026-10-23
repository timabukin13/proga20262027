n = input('Enter a number: ')
s, exp, mantis, k = 0, 0, 0, 0
if n[0] == '-':
    s = 1
    n = n[1:]




for i in range(len(n)):
    if n[i] == ',' or n[i] == '.':
        k = i
        break



plus = n[:k]
minus = n[k:]
plus = str(format(int(plus), 'b'))
minus = '0' + minus
minus = float(minus)
if plus != "0":
    exp = len(plus) - 1




    i = 0
    bin_minus = ""

    while i + exp <= 23 and minus != 0:
        minus *= 2

        if str(minus)[0] == "1":
            bin_minus += '1'

            minus -= 1
        elif str(minus)[0] == "0":

            bin_minus += '0'

        i += 1
    mantis = plus + bin_minus
else:
    i = 0
    bin_minus = ""
    while i<= 23 and minus != 0:
        minus *= 2

        if str(minus)[0] == "1":
            bin_minus += '1'

            minus -= 1
        elif str(minus)[0] == "0":

            bin_minus += '0'

        i += 1
    mantis = bin_minus



    minus1 = float('0.' + bin_minus)
    while minus1 < 1:
        minus1*= 10
        exp -= 1


mantis = mantis[1:]
while len(mantis) < 23:
    mantis = mantis + "0"
exp = str(format(exp + 127, 'b'))
while len(exp) < 8:
    exp = "0" + exp


print(str(s) + exp + mantis)



