

def enlarge(x):

    return x * 100
    
 #this code breaks our ability to import enlarged from other files
   


# print("Hello")
# y = int(input("Please choose a number"))
# print(y, enlarge(y))

if __name__ == "__main__":
  #  only run the code below If this script invoked from the command
  # not if it imported from another
    print("Hello")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))
    

