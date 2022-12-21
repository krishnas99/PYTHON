class rect:
    def __init__(self,l,b):
        self.__length=l
        self.__width=b
    def __lt__(self,p):
        if((self.__length*self.__width<p.__length*p.__width)):
            return True
        else:
            return False
a1=rect(10,3)
a2=rect(1,3)
if(a1<a2):
     print("a1 is greatest")
else:
    print("a2 is greatest")