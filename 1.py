"""
5. Класс <Разговор> (Talking) Экземпляр класса иницилизируется с аргументом name - именем котенка. Класс реализирует методы: - to_answer()
- ответить: котенок через один раз отвечает да или нет, начиная с да. Метод возращает "moore-moore", если да, "meow-meow", если нет. Одновременно
увеличивается количество соотвествующих ответов; - number_yes() - количество ответов да; - number_no() - количество ответов нет.
"""
from random import randint

class Talking():
    def __init__(self, name):
        self.name = name
        self.number_yes = 0
        self.number_no = 0
    def to_answer(self):
        if

talking = Talking("Timi")
talking.to_answer()




