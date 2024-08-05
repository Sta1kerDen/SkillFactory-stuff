def mirror(text):
    if len(text) == 0:
        return ' '
    else:
        return text[-1] + mirror(text[:-1])
print(mirror('something'))

a = 'text'
print(a[:-1])