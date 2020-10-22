#There are two types of loops in Python, for and while.
#They can work with any iterable type, such as lists and dictionaries. 
print("A for loop:") #For loops iterate  a given sequence.
for i in range(0,5): #the next value from the iterator is automatically taken at the start of each loop.
    print(i)

print("A while loop: ")  #While loops repeat as long as a certain boolean condition is met
i=0
while i<5: #the iterator must be initialized prior to the loop, and the value updated within the loop.
    print(i)
    i=i+1     #i+= 1  
#"break" and "continue" statements
#break is used to exit a for loop or a while loop
#continue is used to skip the current block, and return to the "for" or "while" statement. 
# Prints out 0,1,2,3,4
print("'break'statements")

n = 0
while True:
    print(n)
    n += 1
    if n >= 5:
        break
print("'continue' statement")
# Prints out only odd numbers  1,3,5,7,9
for k in range(5):
    # Check if x is even
    if k % 2 == 0:
        continue
    print(k)
#can we use "else" clause for loops???
#unlike some other languages we can use else for loops. 
#When the loop condition of "for" or "while" statement fails then code part in "else" is executed. 
#If break statement is executed inside for loop then the "else" part is skipped. 
#Note that "else" part is executed even if there is a continue statement.
count=int(input("enter count: "))
while(count<5):
    print(count)
    count +=1
else:
    print("count=%d >5 " %count)

print("*****use of break with else")
for i in range(1,6):
    if(i%2==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

