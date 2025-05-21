#q no.5 .Given two strings as input, find out if these are the same or not (allowing for maximum one mismatch).
def string_same_check(strg1, strg2):
    '''Fiirstly we should check whether the length of
       both the taken input string is same or not then check character  .
       Examples:
       >>> string_same_check('swati' ,'swate')
       'same'
       >>>string_same_check('Bhaiya' , 'Bhaiji')
       'not same'
       
       Parameters:
       strg1 : first string
       strg2 : Second string

       Returns:
         'same' :if atmost one mismatch in stg1 and strg2.
         'not same' : if more than one mismatch in strg1 and strg2.

       '''
    
    
    def get_length(string):
        length=0
        for char in string:
            length=length+1
        return length
    if get_length(strg1)== get_length(strg2):
        mismatch_count_char = 0
        length_strg= get_length(strg1)
    
    # Now we will compare character by character by usinng inndexes.
    
        for char in  range(length_strg):
             if strg1[char] != strg2[char]:
                 mismatch_count_char= mismatch_count_char+1
                 if mismatch_count_char>1:
                     return 'not same'
        return 'same'
    else:
        return ' length of strings  are not same'
print(string_same_check.__doc__)

print(string_same_check('swati','swate'))

print(string_same_check('pen','can'))
print(string_same_check('Bhaiya','Bhaiji'))
print(string_same_check('i am a swati jha','i a   a swati jha'))
print(string_same_check('image','imoze'))
