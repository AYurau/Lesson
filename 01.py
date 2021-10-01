def credit_card(number):
    if len(number) != 16:
        return 'Неверный номер карты'
    else:
        return'**** **** ****', number[12:16]


credit_card('9112000049873221')
