import re

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"\d", password):  # Проверка на наличие цифры
        return False
    if not re.search(r"[A-Z]", password):  # Проверка на заглавную букву
        return False
    return True

if __name__ == "__main__":
    user_password = input("Введите пароль: ")
    if is_valid_password(user_password):
        print("Пароль надежный.")
    else:
        print("Пароль не соответствует требованиям.")
