def credit_card(number):
    if len(number) != 16:
        return f'Неверный номер карты'
    else:
        return f'**** **** ****', number[12:16]


credit_card('9112000049873221')
