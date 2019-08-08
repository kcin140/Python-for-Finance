def tmv_calc(present_value, interest_rate, num_compounds, num_years):
    if interest_rate < 1:
        interest_rate == interest_rate
    else:
        interest_rate = interest_rate / 100
    FV = present_value * ((1 + (interest_rate/num_compounds)) **(num_compounds * num_years))
    print(FV)
