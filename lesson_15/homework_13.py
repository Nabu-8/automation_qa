class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side_a':
            if not isinstance(value, int):
                raise AttributeError("Side A should be an integer")
            if value <= 0:
                raise AttributeError("Side A should be > 0")
            super().__setattr__(key, value)

        elif key == 'angle_a':
            if not isinstance(value, int):
                raise AttributeError("Angle A should be an integer")
            if not (0 < value < 180):
                raise AttributeError("Angle A should be between 0 and 180 degrees")

            super().__setattr__('angle_a', value)
            super().__setattr__('angle_b', 180 - value)

        elif key == 'angle_b':
            raise AttributeError("You cannot choose angle_b. It's value is calculated automatically via angle_a")

        else:
            super().__setattr__(key, value)

    def __str__(self):
        return f'Rhombus data: Side A - {self.side_a}, Angle A - {self.angle_a} degrees, Angle B - {self.angle_b} degrees.'


# r = my_rhombus = Rhombus(10, 50)
# print(r)
# r.angle_a = 120
# print(r)
# r.angle_b = 120
# print(r)