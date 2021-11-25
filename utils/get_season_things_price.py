def get_season_things_price(thing, amount, season_things_price):
    if thing == 'wheel':
        wheel_price = season_things_price['wheel'] * amount
        return f'Стоимость составит {wheel_price}/месяц'

    else:
        other_thing_price_week = season_things_price[thing]['week'] * amount
        other_thing_price_month = season_things_price[thing]['month'] * amount
        
        return f'Стоимость составит {other_thing_price_week} р./неделю' + \
            f' или {other_thing_price_month} р./месяц'