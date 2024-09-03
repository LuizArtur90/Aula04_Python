test_int:int = 5
test_str:str = "GeeksforGeeks"
test_list:list = [1, 2, 3] 
print ("Is test_int integer? : " + str(isinstance(test_int, int))) 
print ("Is test_int string? : " + str(isinstance(test_int, str))) 
print ("Is test_str string? : " + str(isinstance(test_str, str))) 
print ("Is test_list integer? : " + str(isinstance(test_list, int))) 
print ("Is test_list list? : " + str(isinstance(test_list, list))) 
print ("Is test_int integer or list or string? : " 
        + str(isinstance(test_int, (list, str, int)))) 
          
print ("Is test_list string or tuple? : " 
        + str(isinstance(test_list, (str, tuple))))
