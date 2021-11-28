def get_final_sum(state, price):
    if state['what_to_store'] == 'season_things':
        thing = state['thing']
        final_sum = price[thing]['week'] * state['weeks_amount'] + \
            price[thing]['month'] * state['month_amount']

    else:
        first_month_sum = price['ceel']['first_sq_m'] * state['cell_size']
        other_month_sum = price['ceel']['other_sq_m'] * \
            state['cell_size'] *  (state['cell_period'] - 1)
        final_sum = first_month_sum + other_month_sum

    return final_sum


def get_costs_cell_without_period(state, price):
    cell_size = state['cell_size']
    cost_first_month = price['ceel']['first_sq_m']
    cost_first_month = cost_first_month * cell_size

    cost_other_month = price['ceel']['other_sq_m']
    cost_other_month = cost_other_month * cell_size

    return cost_first_month, cost_other_month


# season_things_price = {
#     'ski': {
#         'week': 100,
#         'month': 300 
#     },
#     'snowboard': {
#         'week': 100,
#         'month': 300
#     },
#     'wheel': {
#         'week': 0,
#         'month': 200
#     },
#     'bicycle': {
#         'week': 150,
#         'month': 400
#     },
#     'ceel': {
#         'first_sq_m': 599,
#         'other_sq_m': 150
#     }
# }

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

