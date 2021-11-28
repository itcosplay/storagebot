from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


def get_qr_date(state):
    if state['what_to_store'] == 'season_things':
        if state['month_amount'] == 0:
            weeks = state['weeks_amount']
            date =(datetime.now() + timedelta(weeks=weeks)).strftime('%d/%m/%Y')
        else:
            months = state['month_amount']
            date  = (datetime.today()+ relativedelta(months=months)).strftime('%d/%m/%Y')
    else:
        months = state['cell_period']
        date  = (datetime.today()+ relativedelta(months=months)).strftime('%d/%m/%Y')

    return date



# season things
# state_season = {
#     'storage_adress': 'adress_1', 
#     'what_to_store': 'season_things', 
#     'thing': 'ski', 
#     'message_to_delete': 492, 
#     'thing_amount': 2, 
#     'month_or_week': 'months', 
#     'month_amount': 1,
#     'weeks_amount': 0,
#     'fio': ');!!;', 
#     'passport': '!;!;!'
# }

# ceel rent
# state_cell =  {
# 'storage_adress': 'adress_1', 
# 'what_to_store': 'another_things', 
# 'message_to_delete': 547, 
# 'cell_size': 3, 
# 'cell_period': 5, 
# 'fio': 'Pialov',
#  'passport': 'Dgyheb'}


# get_qr_date(state_season)