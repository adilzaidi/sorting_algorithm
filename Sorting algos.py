import random

def insertions_sort(list1):
    for x in range(1, len(list1)):
        current= list1[x]
        current_index=x
        while current < list1[current_index-1] and current_index > 0:
            list1[current_index]= list1[current_index -1]
            current_index= current_index -1
        list1[current_index]=current

def bubble_sort(list2):
    for y in range (len(list2)):
        for x in range(1,len(list2)):
            currentvalue= list2[x]
            current_index= x
            if currentvalue < list2[x-1]:
                temp=list2[current_index] 
                list2[current_index]=list2[current_index -1]
                list2[current_index -1]=temp
                current_index = current_index +1
            else:
                list2[current_index]= currentvalue
                current_index = current_index +1
        
def selection_sort(list3):
        for x in range (len(list3)):
            min_val= list3[x]
            for y in range(x+1, len(list3)):
                if list3[y] < min_val:
                    min_val=list3[y]
            minval_index=list3.index(min_val,x)
            list3[x], list3[minval_index]= list3[minval_index], list3[x]


# in order to swap we need to know the index for the variable we want to swap,
# and the variable we want ot swap with, remeber important
list1= []
list2=[]
list3=[]
list4=[]
for x in range(0,100):
    n = random.randint(1,10)
    list2.append(n)
    list1.append(n)
    list3.append(n)
    list4.append(n)
insertions_sort(list1)
bubble_sort(list2)
selection_sort(list3)
print(list1,"\n")
print(list2,"\n")
print(list3,"\n")
print(list4)

