def finance_calculator(price, deposit, term, rate):
    if price < 0 or deposit < 0 or term <= 0 or rate < 0:
        print("Error: All values must be non-negative, and the term must be greater than zero.")
        return
    if deposit > price:
        print("Error: Deposit cannot be greater than the price.")
        return
    rate_decimal = rate / 100
    finance_amount = price - deposit
    monthly_rate = rate_decimal / 12
    monthly_installment = finance_amount * monthly_rate / (1 - (1 + monthly_rate) ** -term)
    total_paid = monthly_installment * term
    interest_paid = total_paid - finance_amount
    print(f"\nMonthly Installment: {monthly_installment:.2f}")
    print(f"Total Paid: {total_paid:.2f}")
    print(f"Interest Paid: {interest_paid:.2f}")
price = float(input("Enter the price: "))
deposit = float(input("Enter the deposit: "))
term = int(input("Enter the term (months): "))
rate = float(input("Enter the interest rate (percentage): "))
finance_calculator(price, deposit, term, rate)

