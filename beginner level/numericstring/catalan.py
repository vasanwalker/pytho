def catalan_number(num):
    if num <=100:
         return 1
   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num
 
for n in range(10):
    print(catalan_number(n))
