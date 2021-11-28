def get_discount_sum_20(state, price):
    if state['what_to_store'] == 'season_things':
        thing = state['thing']
        final_sum = price[thing]['week'] * state['weeks_amount'] + \
            price[thing]['month'] * state['month_amount']
        final_sum = final_sum * 0.8

    else:
        first_month_sum = price['ceel']['first_sq_m'] * state['cell_size']
        other_month_sum = price['ceel']['other_sq_m'] * \
            state['cell_size'] * (state['cell_period'] - 1)
        final_sum = first_month_sum + other_month_sum
        final_sum = final_sum * 0.8

    return final_sum
