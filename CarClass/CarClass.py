class CarClass(object):
    """A car class that can be used to instantiate various vehicles"""

    # Defaults to General and GM if no arguments are provided
    def __init__(self, name='General', model='GM', vehicle_type='saloon'):
        self.name = name
        self.model = model
        self.vehicle_type = vehicle_type
        self.speed = 0

        # Number of doors 
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        # Number of Wheels 
        if self.vehicle_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    # Saloon Car 
    def is_saloon(self):
        if self.vehicle_type == 'saloon':
            return True
        else:
            return False

    # Car Speed  
    def drive(self, desired_speed):
        if self.vehicle_type == 'trailer':
            self.speed = desired_speed * 11
            return self
        else:
            if desired_speed != 0:
                self.speed = 10 ** desired_speed
            else:
                self.speed = 10 * desired_speed
                