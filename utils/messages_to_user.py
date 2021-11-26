from data import price
from utils import get_final_sum


def message_before_booking(state):
    message = ''
    if state['what_to_store'] == 'season_things':
        state_translate = {
            'ski': 'лыжи',
            'snowboard': 'сноуборд',
            'wheel': 'комплект колес',
            'bicycle': 'велосипед',
        }
        thing = state_translate[state['thing']]
        message += f'Вещь для хранения: {thing}'

        if state['weeks_amount'] == 0:
            period = state['month_amount']
            message += f'\nПериод хранения - месяцы: {period}'
        
        else:
            period = state['weeks_amount']
            message += f'\nПериод хранения - недели: {period}'

        final_sum = get_final_sum(state, price)
        message += f'\nИтоговая стоимость: {final_sum}'

    else:
        cell_size = state['cell_size']
        period = state['cell_period']
        message += f'Размер ячейки для хранения: {cell_size}'
        message += f'\nПериод хранения - месяцы: {period}'
        final_sum = get_final_sum(state, price)
        message += f'\nИтоговая стоимость: {final_sum}'

    return message


# season things
# {
#     'storage_adress': 'adress_1', 
#     'what_to_store': 'season_things', 
#     'thing': 'ski', 
#     'message_to_delete': 492, 
#     'thing_amount': 2, 
#     'month_or_week': 'months', 
#     'month_amount': 3,
#     'weeks_amount': 0,
#     'fio': ');!!;', 
#     'passport': '!;!;!'
# }

# ceel rent
# {
# 'storage_adress': 'adress_1', 
# 'what_to_store': 'another_things', 
# 'message_to_delete': 547, 
# 'cell_size': 3, 
# 'cell_period': 5, 
# 'fio': 'Pialov',
#  'passport': 'Dgyheb'}