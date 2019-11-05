##################################################
## Description:
## Measurement Object
##################################################
## Author: Alexander Schmidt
## Copyright: 2019/11/01, Measurement
## Version: 0.8.0
##################################################

# a Measurement has three properties: Time, Value and Type (see also: MeasurementType)
class Measurement:
    def __init__(self, measurementTime, measurementValue, measurementType):
        self.measurementTime = measurementTime
        self.measurementValue = measurementValue
        self.measurementType = measurementType    
        
    def toString(self):
        return self.measurementTime + ", " + self.measurementType + ", " + self.measurementValue