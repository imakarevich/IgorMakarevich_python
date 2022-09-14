# 1. написать программу которая: запрашивает у пользователя логин
# 2. Есть функция котороя выводит сумму на счете
# 3. Декорируем эту функцию декоратором который проверяет если пользовател - админ (получили на первом этапе, то выводит сумму счета (выполняет функ из п 2)
# 4. Если не админ - Сумму не выводить (функцию даже не выполнять) а выводить - доступ запрещен

import functools


users_accounts = {'Petrov':'admin','Ivanov':'not admin','Smirnov':'admin','Makarov':'not admin'}

def check_access_decorator(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        if users_accounts.get(args[0]) != 'admin':
            return 'ДОСТУП ЗАПРЕЩЕН!!!' 
        return fun(*args, **kwargs)
    return wrapper

@check_access_decorator
def account(login):
    return f"Баланс лицевого счета {login} 20 бел. руб."

print(account(input('Введите login: ')))
