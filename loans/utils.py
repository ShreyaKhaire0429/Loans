import decimal

def calculate_emi(principal: float, annual_rate: float, months: int) -> float:
    # careful digit-by-digit style: use Decimal for money precision
    P = decimal.Decimal(principal)
    r = decimal.Decimal(annual_rate) / decimal.Decimal(12*100)  # monthly fraction
    n = decimal.Decimal(months)
    if r == 0:
        emi = P / n
        return float(round(emi, 2))
    one_plus_r_n = (1 + r) ** n
    emi = P * r * one_plus_r_n / (one_plus_r_n - 1)
    # round to 2 decimals
    return float(round(emi, 2))
