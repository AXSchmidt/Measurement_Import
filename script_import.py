# https://pythonbuddy.com/

import datetime
import MeasurementType
import Measurement

class Sampling:
    datetime_format = '%Y-%m-%dT%H:%M:%S'
    
    def __init__(self):
        self.data = []
        
    def test_file(self):
        self.importfile("measurement_data.json")
        return(self.sample("2017-01-01T00:00:00", self.data))
        
    def test(self):
        self.data.clear()
        self.data.append("{2017-01-03T10:04:45, TEMP, 35.79}")
        self.data.append("{2017-01-03T10:01:18, SPO2, 98.78}")
        self.data.append("{2017-01-03T10:09:07, TEMP, 35.01}")
        self.data.append("{2017-01-03T10:03:34, SPO2, 96.49}")
        self.data.append("{2017-01-03T10:02:01, TEMP, 35.82}")
        self.data.append("{2017-01-03T10:05:00, SPO2, 97.17}")
        self.data.append("{2017-01-03T10:05:01, SPO2, 95.08}")
        return(self.sample("2017-01-01T00:00:00", self.data))
    
    def printMeasurementList(self, list):
        for m in list:
            print(m.toString())
        
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
            return Measurement("1900-01-01T00:00:00", "", "")
    
    # Convert String to DateTime
    def strToDateTime(self, string):
        return datetime.datetime.strptime(string, self.datetime_format)
    
    def roundTime(self, dt):
        if dt == dt - datetime.timedelta(minutes=dt.minute % 5, seconds=dt.second):
            return dt
        else:
        	return dt - datetime.timedelta(minutes=-5+dt.minute % 5, seconds=dt.second)
    
    def strToRoundDateTime(self, string):
        return self.roundTime(self.strToDateTime(string))
        
    # imports a file with sample data into the object    
    def importfile(self, file):
        self.data.clear()
        f = open(file, "r")
        for x in f:
            self.data.append(x)
        
    # main function: samples data    
    def sample(self, startOfSampling, unsampledMeasurement):
        startTime = self.strToDateTime(startOfSampling)
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
        # sort Values in Measurements
        for v in output:
            v[1].sort(key=lambda m: m.measurementTime)
            self.printMeasurementList(v[1])
            # delete redundant data - v[1] = measurements
            last_time = datetime.datetime.now()
            for m in reversed(v[1]):
                dt = self.strToRoundDateTime(m.measurementTime)
                if last_time == dt:
                    v[1].remove(m)
                else:
                    last_time = dt
                    m.measurementTime = dt.strftime(self.datetime_format)
        return output