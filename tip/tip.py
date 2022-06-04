def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # ex.  d = $50.00 convert $50.00 to 50.0 and return to main
    d = float(d.replace("$",""))
    return d


def percent_to_float(p):
    # ex, p = 15% 15% is converted to .15 and return to main
    p=float(p.replace("%","")) / 100
    return p


main()
