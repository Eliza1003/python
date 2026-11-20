#define functionto calculate cube
def cube(number):
    return number*number* number

#define a function which will exacute the cube if the userenterednumberis divisiable by 3
def by_three(number):
    if number %3 ==0:
      return cube(number)
    else:
     return False
#display results
print(by_three(9))
print(by_three(4))