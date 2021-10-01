def palindrom(text):
    if text == text[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'


palindrom('шалаш')
