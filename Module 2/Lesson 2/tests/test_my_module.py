import unittest
from my_module import shift_words


class TestShiftWordsTypicalCases(unittest.TestCase):
    """
    Тестовий клас для перевірки типової поведінки функції shift_words.
    """

    # Використовуємо параметризацію для перевірки декількох прикладів.
    # Кожен кортеж містить: (оригінальний текст, зсув, очікуваний результат)
    test_data = [
        ("abcd efgh", 1, "bcde fghi"),
        ("a1bcd efg!h", 2, "c1def fgi!j"),
        ("Hello, World!", 3, "Khoor, Zruog!"),
        ("XYZ", 3, "ABC"),
        ("", 5, ""),  # Порожній рядок
        ("   ", 10, "   ")  # Рядок з пробілами
    ]

    def test_typical_cases(self):
        """
        Перевіряє, що функція коректно обробляє типові вхідні дані.
        """
        for text, shift, expected in self.test_data:
            with self.subTest(text=text, shift=shift):
                result = shift_words(text, shift)
                self.assertEqual(result, expected)


class TestShiftWordsAtypicalCases(unittest.TestCase):
    """
    Тестовий клас для перевірки нетипової поведінки функції shift_words.
    """

    def test_raises_type_error_for_invalid_input(self):
        """
        Перевіряє, що функція генерує TypeError, якщо вхідні дані не є рядком.
        """
        invalid_inputs = [123, 1.5, True, [], {}]
        for invalid_input in invalid_inputs:
            with self.subTest(invalid_input=invalid_input):
                with self.assertRaises(TypeError):
                    shift_words(invalid_input, 1)


# Цей блок дозволить запускати тести з командного рядка
if __name__ == '__main__':
    unittest.main()