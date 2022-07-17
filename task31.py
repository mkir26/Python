from ast import Try


hrs = input('Enter Hours:')
h = float(hrs)
rate = input('Enter Rate per hours:')
r = float(rate)
if h <= 40:
    print(h * r)
else:
    print((h - 40) * r * 1.5 + 40 * r)
