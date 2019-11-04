import MeasurementType
import Measurement

class Sampling:
    
    def __init__(self):
        self.data = []
        
    def test_file(self):
        self.importfile("measurement_data.json")
        return(self.sample("2017-01-01 00:00:00", self.data))
        
    def test(self):
        self.data.clear()
        self.data.append("{2017-01-03T10:04:45, TEMP, 35.79}")
        self.data.append("{2017-01-03T10:01:18, SPO2, 98.78}")
        self.data.append("{2017-01-03T10:09:07, TEMP, 35.01}")
        return(self.sample("2017-01-01 00:00:00", self.data))
        
    # Convert String to Class Measurement
    def strToMeasurement(self, string):
        while string[0] == "{":
            string = string[1:]
        while string[-1] == "}":
            string = string[:-1]
        li = list(string.split(", "))      
        if len(li) >= 3:
            return Measurement(li[0], li[2], li[1])
        else:
            return Measurement("1900-01-01 00:00:00", "", "")
        
    # imports a file with sample data into the object    
    def importfile(self, file):
        self.data.clear()
        f = open(file, "r")
        for x in f:
            self.data.append(x)
        
    # main function: samples data    
    def sample(self, startOfSampling, unsampledMeasurement):
        # get all measurement types
        print(unsampledMeasurement)
        output = []
        measurement_types = MeasurementType()
        for m_type in measurement_types.measurementTypes:
            output.append([m_type, []])
    	# insert unsampledMeasurement
        for uMeasurement in unsampledMeasurement:
            measurement = self.strToMeasurement(uMeasurement)
            for i in range(len(output)):
                if output[i][0] == measurement.measurementType:
                	output[i][1].append(measurement)
        return output