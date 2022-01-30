def recSig(num):
    if num<=1:
        return num
    return num+recSig(num-1)

print(recSig(3))

def recFact(x):
    if x <= 0:
        return x
    elif x == 1:
        return x
    if not isinstance(x, int):
        y=int(x)
    else:
        y=x
    return y*recFact(y-1)

print(recFact(3.9))

# def floodFill(canvas2D, startXY, newColor):
#     if 