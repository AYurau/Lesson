def credit_card(number):
    if len(number) != 16:
        print('Неверный номер карты')
    else:
        print('**** **** ****', number[12:16])


credit_card('9112000049873221')
