import sys
if len(sys.argv) != 2:
    print("Usage %i num" % sys.argv[0])
    sys.exit(1)
    
num = int(sys.argv[1])
if (num % 2) == 0:
   print("Number", "{0} is Even".format(num))
else:
   print("Number", "{0} is Odd".format(num))
   
if num > 1:  
   for i in range(2,num):
      if (num % i) == 0:
           print("Number", num,"is not a prime number")
           break
      else:
       print("Number", num,"is a prime number")
else:
   print("Number", num,"is not a prime number")