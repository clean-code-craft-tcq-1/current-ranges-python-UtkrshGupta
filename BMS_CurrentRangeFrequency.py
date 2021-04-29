import numpy as np
import random

class CurrentRangeFrequncy:
    def __init__(self, data):
        self.data = data
        self.error_flag = False
        try: 
            self.size = len(data)
        except TypeError:
            print("Passed argument should be of List type")
            self.error_flag = True
            
    def countFrequency(self, data):
        frequency = {}
        for element in data:
            if element not in frequency:
                frequency[element] = 1
            else:
                frequency[element] += 1
                
        return frequency
    
    def create_range_key_string(self, lower_boundary_value, higher_boundary_value):
        if lower_boundary_value != higher_boundary_value:
            return str(lower_boundary_value) + "-" + str(higher_boundary_value)
        else:
            return str(lower_boundary_value)
    
    def execute_grouping(self, freq_data):
        
        values = sorted(freq_data.keys())
        length = len(values)
        temp = values[0]
        result = {}
        counter = freq_data[values[0]]
        
        for index in range(1, length+1):
            previous = values[index-1]
            if index == length:
                result[self.create_range_key_string(temp, previous)] = counter
                break
            
            current = values[index]
            
            if  previous+1 < current:
                result[self.create_range_key_string(temp, previous)] = counter        
                temp = current
                counter = 0 
            counter += freq_data[current]
              
        return result
    
    def get_current_ranges_frequency(self):
        if self.error_flag:
            return
        
        if self.size == 0:
            return 'Empty Data'
        
        if np.nan in self.data or None in self.data:
            return 'Invalid Input'
        
        return self.execute_grouping(freq_data = self.countFrequency(self.data))