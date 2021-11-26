def get_season_things_price(thing, amount, price):

    if thing == 'wheel':
        wheel_price = price[thing]['month'] * amount
        return f'Стоимость составит {wheel_price}/месяц'

    else:
        other_thing_price_week = price[thing]['week'] * amount
        other_thing_price_month = price[thing]['month'] * amount
        return f'Стоимость составит {other_thing_price_week} р./неделю' + \
            f' или {other_thing_price_month} р./месяц'