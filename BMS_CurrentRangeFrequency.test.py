import unittest
import random
import numpy as np
from BMS_CurrentRangeFrequency import CurrentRangeFrequncy

min_current_reading = 0
max_current_reading = 40
sample_data_size = 20

class CurrentRangeFrequencyTest(unittest.TestCase):
    def test_CurrentRangeFrquency_output_desired_results(self):
        data = [random.randint(min_current_reading, max_current_reading) for x in range(sample_data_size)]
        crf = CurrentRangeFrequncy(data)
        results = crf.get_current_ranges_frequency()
        self.assertIsNotNone(results)
        print('Input Data', data)
        print('Output Data')
        for current_range, current_range_frequency in zip(results.keys(), results.values()):
            print(current_range+', '+str(current_range_frequency))
        
    def test_to_check_output_yields_invalid_if_input_has_nan(self):
        data = [random.randint(min_current_reading, max_current_reading) for x in range(sample_data_size)]
        crf = CurrentRangeFrequncy(data)
        random_index = random.randint(0, len(data))
        data[random_index] = np.nan
        self.assertEqual(crf.get_current_ranges_frequency(), 'Invalid Input')
     
    def test_to_check_output_yields_invalid_if_input_has_None(self):
        data = [random.randint(min_current_reading, max_current_reading) for x in range(sample_data_size)]
        crf = CurrentRangeFrequncy(data)
        random_index = random.randint(0, len(data))
        data[random_index] = None
        self.assertEqual(crf.get_current_ranges_frequency(), 'Invalid Input')
    
    def test_to_check_impact_if_cuurent_values_are_passed_as_non_integer(self):
        data = [1,3,4,5,10,23,'2',13,14,19,15,18]
        crf = CurrentRangeFrequncy(data)
        self.assertRaises(TypeError, crf.get_current_ranges_frequency)
        
if __name__ == '__main__':
  unittest.main()