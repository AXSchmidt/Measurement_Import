import unittest
from script_import import Sampling
from class_measurement import Measurement

class TestSample(unittest.TestCase):
    
    # does the algorithm sort correctly according to the time 
    def test_sort(self):
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
    def test_wrong_type(self):
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
    def test_wrong_date(self):
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
    def test_complex(self):
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