#!/usr/bin/env python
# coding: utf-8

# In[1]:


def integer_to_roman_numerals(input):
    """ Convert an integer to a Roman numeral. """
    
    if not isinstance(input, type(1)):
        raise TypeError("expected integer, got %s" % type(input))
    if not 0 < input < 4000:
        raise ValueError("Argument must be between 1 and 3999")
        
    integers = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    roman_numerals = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []
    
    for i in range(len(integers)):
        count = int(input / integers[i])
        result.append(roman_numerals[i] * count)
        input -= integers[i] * count
    return ''.join(result)


# In[2]:


def roman_numerals_to_integer(input):
    """ Convert a Roman numeral to an integer. """
    
    if not isinstance(input, type("")):
        raise TypeError("expected string, got, %s" % type(input))
        
    input = input.upper( )
    roman_numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sum = 0
    
    for i in range(len(input)):
        try:
            value = roman_numerals[input[i]]
            
            if i + 1 < len(input) and roman_numerals[input[i + 1]] > value:
                sum -= value
            else:
                sum += value
        except KeyError:
            raise ValueError("input is not a valid Roman numeral: %s" % input)
    
    if integer_to_roman_numerals(sum) == input:
        return sum
    else:
        raise ValueError("input is not a valid Roman numeral: %s" % input)


# In[3]:


integer_to_roman_numerals(9)


# In[4]:


roman_numerals_to_integer('cxxx')


# In[ ]:




