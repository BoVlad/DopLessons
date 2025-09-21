letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']




def shift_words(text: str, shift: int) -> str:
    shifted_text = ""
    for i in text:
        if i.isalpha():
            oper_i = i.lower()
            oper_i_index = letters.index(oper_i)
            new_index = (oper_i_index + shift) % 26
            if i.isupper():
                shifted_text = shifted_text + letters[new_index].upper()
            else:
                shifted_text = shifted_text + letters[new_index].lower()
        else:
            shifted_text = shifted_text + i
    return shifted_text



if __name__ == '__main__':
    test_string = input("Введіть текст: ")
    test_shift = input("Введіть зміщення: ")
    if test_shift.isdigit():
        test_shift = int(test_shift)
        print(shift_words(test_string, test_shift))
        print(f"Оригінал: '{test_string}'")
        print(f"Результат: '{shift_words(test_string, test_shift)}'")
    else:
        print("Ви не ввели цифру в зміщенні!")