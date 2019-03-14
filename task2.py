"""
===================   TASK 2   ====================
* Name: Even and Odd Numbers
*
* Write a script that will populate list with as
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that user
* will always provide integer numbers. At the end,
* script should print how many even and odd numbers
* were present in list.
*
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""
def main():
    number = input("Enter a number:")
    even = 0
    odd = 0
    for i in range(0,len(number)):
        if int(number[i]) % 2 == 0 :
            even += 1
        else:
            odd += 1

    print("There is ",even," even numbers,and ",odd," odd numbers")

main()

