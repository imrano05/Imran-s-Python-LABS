#print greeting message
 print("hallo world....")
 
 #single line comment
 number=1
 #initialize number with 1
 if number > 0:
     print("these are two comments")
 
 #input/output
 user_input = input("Type something to test this out:")
 print(user_input)
 
 #multiple statements in a single line
 print("statement"); print("statement2")
 
 #indentations
 value = 1
 if value > 0:
     print("single space indention")
 
 score = 2
 if score > 1:
     print("single space+tab indention")
 
 #data types
 #integer
 num1 = 1235
 print(type(num1))
 
 num2 = -1235
 print(type(num2))
 
 num3 = 0
 print(type(num3))
 
 #float
 flt1 = 12.35
 print(type(flt1))
 
 flt2 = -123.5
 print(type(flt2))
 
 flt3 = 0.35
 print(type(flt3))
 
 flt4 = 2.12e-10
 print(type(flt4))
 
 flt5 = 5e220
 print(type(flt5))
 
 #complex
 comp1 = complex(1, 2)
 print(type(comp1))
 print(comp1)
 
 comp2 = 1 + 2j
 print(type(comp2))
 
 #boolean
 flag1 = True
 print(type(flag1))
 print(flag1)
 
 flag2 = False
 print(type(flag2))
 
 #string
 text1 = "strings1"
 print(text1)
 
 text2 = 'strings2'
 print(text2)
 
 #escape sequence
 print("this is a backslash \\ mark")
 print("this is a tab \t mark")
 print("this is a new \n line")
 print("these are \'single quote \'")
 print("these are \"double quote \"")
 
 #accessing string elements
 title = "python tutorial"
 print(title[0])         # first character
 print(title[-15])       # first character
 print(title[14])        # last character
 print(title[-1])        # last character
 print(title[4])         # 4th character
 print(title[-11])       # 4th character
 # print(title[16])      # out of index range
 
 #LISTS
 numbers_list = [5, 10, 15, 20, 25]
 print(numbers_list)
 
 colors_primary = ['red', 'blue', 'white']
 print(colors_primary)
 
 mixed_items = ['red', 20, 20.20]
 print(mixed_items)
 
 colors_all = ['red', 'white', 'grey', 'blue', 'black']
 print(colors_all[0])
 print(colors_all[1], colors_all[2])
 print(colors_all[-1])
