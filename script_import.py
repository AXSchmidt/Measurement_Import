import datetime
from class_measurementtype import MeasurementType
from class_measurement import Measurement

class Sampling:
    datetime_format = "%Y-%m-%dT%H:%M:%S"
    datetime_default = "1900-01-01T00:00:00"
    
    def __init__(self):
        self.data = []

    def importfile(self, file):
        '''imports a file with sample data into the object'''
        self.data.clear()
        f = open(file, "r")
        for line in f:
            self.data.append(line)

    def strToMeasurement(self, string):
        '''Convert String to Class Measurement'''
        while string[0] == "{":
            string = string[1:]
        while string[-1] == "}":
            string = string[:-1]
        li = list(string.split(","))      
        if len(li) == 3:
            return Measurement(li[0].strip(), li[2].strip(), li[1].strip())
        else:
            return Measurement(self.datetime_default, "", "")

    def strToDateTime(self, string):
        '''Convert String to DateTime'''
        try:
            datetime_object = datetime.datetime.strptime(string, self.datetime_format)
        except ValueError as ve:
            datetime_object = datetime.datetime.strptime(self.datetime_default, self.datetime_format)   
        return datetime_object

    def roundTime(self, datetime_object):
        '''Rounds up the time to the next five minutes'''
        # when there is nothing to round, return original time...
        if datetime_object == datetime_object - datetime.timedelta(minutes = datetime_object.minute % 5, seconds = datetime_object.second):
            return datetime_object
        # otherwise add 5 minutes, and floor
        else:
            return datetime_object - datetime.timedelta(minutes=-5 + datetime_object.minute % 5, seconds = datetime_object.second)

    def strToRoundDateTime(self, string):
        '''Rounds up a Time String the next five minutes'''
        return self.roundTime(self.strToDateTime(string))
        
    # main function: samples data    
    def sample(self, startOfSampling, unsampledMeasurement):
        '''
        Imports sorted time-based measurement data from medical devices grouped by measurementtype
        :param startOfSampling: ignore data before
        :param unsampledMeasurement: unsorted list auf measurement
        :return: List<MeasurementType, List<Measurement>>
        '''
        startTime = self.strToDateTime(startOfSampling)
        # get all measurement types
        output = []
        measurement_types = MeasurementType()
        for measurement_type in measurement_types.measurementTypes:
            output.append([measurement_type, []])
    	# insert unsampledMeasurement
        for uMeasurement in unsampledMeasurement:
            measurement = self.strToMeasurement(uMeasurement)
            if startTime <= self.strToDateTime(measurement.measurementTime):
                for i in range(len(output)):
                    if output[i][0] == measurement.measurementType:
                        output[i][1].append(measurement)
        # sort Values in Measurements
        for entity in output:
            entity[1].sort(key=lambda m: m.measurementTime)
            # delete redundant data; entity[1] = list<Measurement>
            last_time = datetime.datetime.now()
            for obj in reversed(entity[1]):
                measurementTime = self.strToRoundDateTime(obj.measurementTime)
                if last_time == measurementTime:
                    entity[1].remove(obj)
                else:
                    last_time = measurementTime
                    obj.measurementTime = measurementTime.strftime(self.datetime_format)
        return output