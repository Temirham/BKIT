import unittest
import RK2_Mamaev

class RK_Test(unittest.TestCase):
    def test_E1(self):
        self.assertEqual(RK2_Mamaev.E1(), [('Первая Библиотека', 'kodack'), ('Первая Библиотека', 'Piratsky')])
    def test_E2(self):    
        self.assertEqual(RK2_Mamaev.E2(), [('Шестая Библиотека', 512.0), ('Третья Библиотека', 1024.0), ('Первая Библиотека', 2048.0), ('Четвертая Библиотека', 3584.0), ('Пятая Библиотека', 4096.0), ('Вторая Библиотека', 5120.0)])
    def test_E3(self):    
        self.assertEqual(RK2_Mamaev.E3(), [('Piratsky', 'Вторая Библиотека'), ('Palm', 'Шестая Библиотека')]) 
if __name__ == '__main__':
    unittest.main()