class Calculation:
    def __init__(self, cef: dict):
        self.cef = cef # коэффициенты с учетом маржи
        self.prob = {} # вероятности исходя из cef
        self.sum_prob = 0.0 # сумма верочтностей
        self.margin = 0.0 # маржа
        self.tr_prob = {} # честная вероятность без учета моржи
        self.tr_cef = {} # честные коэффициенты

    def calculate(self):
        for key, value in self.cef.items():
            self.prob[key] = 1 / value # формула рассчета вероятности
        data = {k: f"{v:.2f}" for k, v in self.prob.items()}
        print(f"Вероятности: {data}")
        self.sum_prob = sum(self.prob.values()) # складываем полученные вероятности для рассчета маржи
        if self.sum_prob < 1:
            print("Вилка, игрок в плюсе при любых исходах")
        elif self.sum_prob == 1:
            print("Честная игра, ноль прибыли букмекера")
        else:
            print(f"Сумма вероятностей: {self.sum_prob:.2f}")
            self.margin = self.sum_prob -1 # Рассчитываем маржу по формуле: сумм(вер) - 1
            print(f"Маржа: {self.margin:.2f}")
            for key, value in self.prob.items():
                self.tr_prob[key] = value / self.sum_prob # рассчитываем честные коэффициенты: вер / сумм(вер)
            for key, value in self.tr_prob.items():
                self.tr_cef[key] = 1 / value # рассчитываем честные коэффициенты: 1 / честн(вер)
            data1 = {k: f"{v:.2f}" for k, v in self.tr_prob.items()}
            data2 = {k: f"{v:.2f}" for k, v in self.tr_cef.items()}
            print(f"Честные вероятности: {data1}" + "\n" + f"Честные коэффициенты: {data2}")
# пример ввода коэффициентов
input_cef = {
    "P1": 1.10,
    "X": 2.40,
    "P2": 2.80
}
print(f"Коэффициенты: {input_cef}")
r = Calculation(input_cef)
r.calculate()