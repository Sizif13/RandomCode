def dots(str, tmp='', i=0, res=[]):
    if i == len(str)-1:
        res.append(tmp + str[-1])
        return

    curent = str[i]

    dots(str, tmp + curent + '', i + 1)
    dots(str, tmp + curent + '.', i + 1)
    return res


print(dots('abcdef'))