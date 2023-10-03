'''
Name: Daniel Reti
OSU Email: retid@oregonstate.edu
Desc: Fork of vip-application, custom map function
'''

from inspect import signature
import inspect
import typing
'''
#VIP application, custom map function that takes in a "list" instead of iterable values and applies the function to each value and then returns a list. 

Uses try to identify if an item can be used with a function. 

'''
def map (input_function=int,item_list: list=[0,0,0,0,"dog"]):
    newlist=[]
    for i in item_list:

        if type(i)==int:
            try :
                newlist.append(input_function(i))
            except Exception:
                newlist.append(i)
        elif type(i)==str:
            try :
                newlist.append(input_function(i))
            except Exception:
                newlist.append(i)
        else:
            try :
                newlist.append(input_function(i))
            except Exception:
                newlist.append(i)

   
    return(newlist)




#if __name__ == "__main__":
    #list_print=(map(float))
    #print(list_print)






