import unittest
from datetime import datetime
from script_import import Sampling
from class_measurement import Measurement

class TestSample(unittest.TestCase):
    
    # checks if a correct measurement object is returned
    def test__strToMeasurement(self):
        sampling = Sampling()
        measurement = sampling.strToMeasurement("{2019-11-01T10:14:45, TEMP, 1}")
        result = Measurement("2019-11-01T10:14:45", "1", "TEMP")
        self.assertEqual(measurement.toString(), result.toString())
    
    # checks if the default object is returned if the input is incorrect
    def test__strToMeasurement_wrong_imput(self):
        sampling = Sampling()
        measurement = sampling.strToMeasurement("{2019-11-01T10:14:45, TEMP, 1, 1}")
        result = Measurement("1900-01-01T00:00:00", "", "")
        self.assertEqual(measurement.toString(), result.toString())
        
    # checks if a string is properly converted into a datetime
    def test__strToDateTime(self):
        sampling = Sampling()
        datetime_object = sampling.strToDateTime("2019-11-01T10:14:45")
        result = datetime(2019, 11, 1, 10, 14, 45)
        self.assertEqual(datetime_object, result)
        
    # checks if a string is converted into the default datetime if the input is incorrect
    def test__strToDateTime_wrong_imput(self):
        sampling = Sampling()
        datetime_object = sampling.strToDateTime("20000019-11-01T10:14:45")
        result = datetime(1900, 1, 1, 0, 0, 0)
        self.assertEqual(datetime_object, result)
        
    # checks if the datetime is rounded up correctly
    def test__roundTime(self):
        sampling = Sampling()
        datetime_object = sampling.roundTime(datetime(2019, 11, 1, 10, 14, 45))
        result = datetime(2019,11,1,10,15)
        self.assertEqual(datetime_object, result)
       
    # checks if the datetime is returned correctly if there is nothing to round
    def test__roundTime_equal(self):
        sampling = Sampling()
        datetime_object = sampling.roundTime(datetime(2019, 11, 1, 10, 15, 0))
        result = datetime(2019,11,1,10,15)
        self.assertEqual(datetime_object, result)
    
    # does the algorithm sort correctly according to the time 
    def test__sample_sort(self):
         # prepare input data
        data = []
        data.append("{2019-11-01T10:14:45, TEMP, 3}")
        data.append("{2019-11-01T10:02:01, TEMP, 1}")
        data.append("{2019-11-01T10:09:07, TEMP, 2}")
        # repare expected result
        result = []
        result.append("{2019-11-01T10:05:00, TEMP, 1}")
        result.append("{2019-11-01T10:10:00, TEMP, 2}")
        result.append("{2019-11-01T10:15:00, TEMP, 3}")
        # get result
        output = []
        sampling = Sampling()
        sortedList = sampling.sample("2017-01-01T00:00:00", data)
        for v in sortedList:
            for m in v[1]:
                output.append("{"+m.toString()+"}")
        self.assertEqual(result, output)
        
    # does the algorithm ignore wrong / incorrect measurement_types
    def test__sample_wrong_type(self):
         # prepare input data
        data = []
        data.append("{2019-11-01T10:14:45, TMP, 1}")
        # repare expected result
        result = []
        # get result
        output = []
        sampling = Sampling()
        sortedList = sampling.sample("2017-01-01T00:00:00", data)
        for v in sortedList:
            for m in v[1]:
                output.append("{"+m.toString()+"}")
        self.assertEqual(result, output)
        
    # does the algorithm ignore wrong / incorrect measurement_datetime
    def test__sample_wrong_date(self):
         # prepare input data
        data = []
        data.append("{200019-11-01T10:14:45, TEMP, 1}")
        # repare expected result
        result = []
        # get result
        output = []
        sampling = Sampling()
        sortedList = sampling.sample("2017-01-01T00:00:00", data)
        for v in sortedList:
            for m in v[1]:
                output.append("{"+m.toString()+"}")
        self.assertEqual(result, output)        
        
    # complex test
    def test__sample_complex(self):
        # prepare input data
        data = []
        data.append("{2017-01-03T10:04:45, TEMP, 35.79}")
        data.append("{2017-01-03T10:01:18, SPO2, 98.78}")
        data.append("{2017-01-03T10:09:07, TEMP, 35.01}")
        data.append("{2017-01-03T10:03:34, SPO2, 96.49}")
        data.append("{2017-01-03T10:02:01, TEMP, 35.82}")
        data.append("{2017-01-03T10:05:00, SPO2, 97.17}")
        data.append("{2017-01-03T10:05:01, SPO2, 95.08}")
        # repare expected result
        result = []
        result.append("{2017-01-03T10:05:00, TEMP, 35.79}")
        result.append("{2017-01-03T10:10:00, TEMP, 35.01}")
        result.append("{2017-01-03T10:05:00, SPO2, 97.17}")
        result.append("{2017-01-03T10:10:00, SPO2, 95.08}")
        # get result
        output = []
        sampling = Sampling()
        sortedList = sampling.sample("2017-01-01T00:00:00", data)
        for v in sortedList:
            for m in v[1]:
                output.append("{"+m.toString()+"}")
        self.assertEqual(result, output)
        
if __name__ == '__main__':
    unittest.main()