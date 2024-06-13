class BMICalculator:
    def __init__(self,weight_in_kg,height_in_m):
        self.__weight = weight_in_kg
        self.__height = height_in_m

    @property
    def bmi(self):
        return self.__weight/self.__height**2
    
    @property
    def category(self):
        match self.bmi:
            case self.bmi if self.bmi < 18.5:
                return "underweight"
            case self.bmi if self.bmi > 25:
                return "overweight"
            case _:
                return "normal"                