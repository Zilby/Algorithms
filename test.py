global compares
compares = 0
l = raw_input().split(",")
l = map(int, l)

def silly(a):
    if len(a) > 10:
        return -1
    global compares
    if len(a) < 2:
        return a
    else:
        y = 0
        while y < len(a):
            b = list(a)
            i = b[0]
            b[0] = b[y]
            b[y] = i
            maybe_sorted = [b[0]] + (silly(b[1:len(b)]))
            x = 0
            t = True
            while x < len(maybe_sorted) - 1:
                compares += 1
                if maybe_sorted[x] > maybe_sorted[x + 1]:
                    t = False
                    break
                x += 1
            if t:
                return maybe_sorted
            y += 1

def bubble(a):
    b = list(a)
    if len(b) > 100001:
        return -1
    global compares
    while True:
        swapped_this_turn = False
        i = 0
        while i < len(b) - 1:
            compares += 1
            if b[i] > b[i + 1]:
                x = b[i]
                b[i] = b[i + 1]
                b[i + 1] = x 
                swapped_this_turn = True
            i += 1
        if not swapped_this_turn:
            return b

def merge(a):
    b = list(a)
    if len(b) < 2:
        return b
    global compares
    left = b[0:len(b)//2]
    right = b[len(b)//2:len(b)]
    left = merge(left)
    right = merge(right)
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        compares += 1
        if left[i] < right[j]:
            b[k] = left[i]
            k += 1
            i += 1
        else:
            b[k] = right[j]
            k += 1
            j += 1
    if i < len(left):
        b[k:len(a)] = left[i:len(left)]
    else:
        b[k:len(a)] = right[j:len(right)]
    return b

def lToString(l):
    s = ""
    for x in l:
        s += (str(x) + ",")
    return s[0:len(s) - 1]

print(lToString(silly(l)))
print(compares)
compares = 0
bubble(l)
print(compares)
compares = 0
merge(l)
print(compares)
