def convert_rub_to_usd(amount, exchange_rate):
    return amount / exchange_rate

def convert_usd_to_rub(amount, exchange_rate):
    return amount * exchange_rate

# Предположим, что курс доллара к рублю составляет 100 рублей за доллар
exchange_rate_usd_to_rub = 100

# Запрашиваем у пользователя сумму денег и валюту, из которой он хочет перевести
rub_usd = input("Что вы хотите внести? (rub или usd): ")
amount = float(input("Введите сумму денег, которую вы хотите перевести: "))

# Выполняем конвертацию в зависимости от выбранной валюты
if rub_usd.lower() == 'rub':
    converted_amount = convert_rub_to_usd(amount, exchange_rate_usd_to_rub)
    print(f"{amount} рублей это {converted_amount} долларов")
elif rub_usd.lower() == 'usd':
    converted_amount = convert_usd_to_rub(amount, exchange_rate_usd_to_rub)
    print(f"{amount} долларов это {converted_amount} рублей")
else:
    print("Неправильный ввод. Введите 'rub' или 'usd'.")
