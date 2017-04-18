class Car(object):
    """A car class that can be used to instantiate various vehicles"""

    # Defaults to General and GM if no arguments are provided
    def __init__(self, name='General', model='GM', type='saloon'):
        self.__name = name
        self.__model = model
        self.__type = type
        self.speed = 0

        # Number of doors 
        if self.__name == 'Porshe' or self.__name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        # Number of Wheels 
        if self.__type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    @property
    def model(self):
        return self.__model

    @property
    def name(self):
        return self.__name

    # Saloon Car 
    def is_saloon(self):
        if self.__type == 'saloon':
            return True
        else:
            return False

    # Car Speed  
    def drive_car(self, desired_speed):
        if self.__type == 'trailer':
            self.speed = desired_speed * 11
            return self
        else:
            if desired_speed != 0:
                self.speed = 10 ** desired_speed
            else:
                self.speed = 10 * desired_speed
