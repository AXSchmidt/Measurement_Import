class Measurement:
    def __init__(self, measurementTime, measurementValue, measurementType):
        self.measurementTime = measurementTime
        self.measurementValue = measurementValue
        self.measurementType = measurementType    
        
    def toString(self):
        return self.measurementTime + ", " + self.measurementType + ", " + self.measurementValue