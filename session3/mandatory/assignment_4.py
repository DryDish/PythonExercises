# A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
# Create a dict suitable for decoding month names to numbers.
# Create a function which uses string operations to split the date into 3 items using the "-" character.
# Translate the month, correct the year to include all of the digits.
# The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).

months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8,  'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC':12}

def date_splitter(date):
    list_of_words  = date.split("-")
    day_number = str(list_of_words[0])
    
    if len(day_number) < 2:
        day_number = "0" + day_number

    month_number = str(months.get(list_of_words[1], -1))
    if len(month_number) < 2:
        month_number = "0" + month_number
    
    prefix19 = "19"
    prefix20 = "20"

    if (int(list_of_words[2]) > 21):
        year_number = prefix19 + str(list_of_words[2])
    else:
        year_number = prefix20 + str(list_of_words[2])
    
    return (int(day_number),int(month_number),int(year_number))

print(date_splitter("8-MAR-85"))