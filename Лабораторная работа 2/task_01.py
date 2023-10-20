money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months_without_debts = 0
first_month_over = False
while True:
    if first_month_over:
        spend *= (1 + increase)

    money_capital += salary
    money_capital -= spend

    if money_capital < 0:
        break

    months_without_debts += 1
    if not first_month_over:
        first_month_over = True

print("Количество месяцев, которое можно протянуть без долгов:", months_without_debts)
