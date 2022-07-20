def replace_characters(string):
    masked_string = '*' * (len(string)-5) + string[-5:]
    print(masked_string)

replace_characters('12345678')
replace_characters('12345abcdef')
replace_characters('12345')