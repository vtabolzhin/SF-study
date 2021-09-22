class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, model, manufacturer, year):
        """Initialize description attributes."""
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.odometer_reading = 0
        
        
    def get_descriptive_name(self):
        """Returns a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    
    def read_odometer(self):
        """Print a statement showing a car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
        
    def update_odometer(self, mileage):
        """Set the odometr reading to the given value."""
        if mileage <= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading = mileage