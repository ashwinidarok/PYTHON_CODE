
"""
x=40
print(id(x))   # prints the memory address of x
x=44
print(id(x))
#print(id(z))  # prints the memory address of y
# q is list work like as array in array
q=[1,2,3,4]
print(id(q)) # id for addressed\
#for print
print(q) 
print(type(q[0]))

k=["b","d","r","e",10,20]
print(k)
print(id(k))
print(type(k[0]))
k.append("ashwini")
print(k)
print(id(k))
#replace value at index
k[0]=123
k.insert(2,33)
print(k)
#insert at position
#listname.insert(position,value)
k.insert(0,344)
#for searching item in python
for item in k :
    print(item)
    if item =="ashwini" :
        print(f"{item} exit in list")
   
#listname.remove(item)
k=["b","d","r","e",10,20]

print(k)
k.remove("d")
print(k)
#listname.pop(index)
a=k.pop(1)
print(a)
print(k)
#==========================================================================
#for index used enumerate first return index second return value
for index,item in enumerate(k):
    print(f"{index},is at index {item}")
  
list_of_subject = ["rtos","mpi","os"]
print(list_of_subject.index('os'))

for index_of_subject,subject in enumerate(list_of_subject) :
    print("{0} is  stored at index {1}".format(subject,index_of_subject))
#revresd number=============================
    n=int(input("enter the number")) #input from user 
rev=0
while n!=0 :
    rem=n%10
    rev=rev*10+rem
    n=n//10         #divide uesd "//" not "/"
print("reversed :",rev)

#negative index
list_of_number = [1,2,3,4,5,67,7]
print(list_of_number[-1])
#==========================================================================
#slicing in list
sub_list_of_list_of_number= list_of_number[1:4]
print(sub_list_of_list_of_number)
# o/p--> 2
l2=list_of_number[1:2]
print(l2)
l3=list_of_number[2:4]
print(l3)
#==========================================================================
#reverse
list_of_number.reverse()
print("revresed:",list_of_number)
#==========================================================================
#shallow copy
m1=[12,3,42,545,6]
m1.sort()
print("sorting data in m1 ",m1)
m2=m1
print("l1--",m1)
print("l2:--",m2)
m2.append(33)
print("l1",m1)
print("l2:",m2)
#==========================================================================
#deep copy
import copy
m3 = copy.deepcopy(m1)
m3.append(100)
print("m1===",m1)
print("m3===",m3)
#==========================================================================
#dictionary
import json
sensor_data ={
     "temperature" :20,
     "humidity" : 40,
     "pressure" : 1000,
        "status" : True,
        "deployed_in" : ["DESD-DIOT" ,"PG-HPC","PG-AI","PG-DBDA"]
}
print("sensor data is:",sensor_data)
sensor_data["aqi"]= 2000  # add the datain dictionary
print("adding data :",sensor_data)
print("temperature:",sensor_data["temperature"])
print("humidity :",sensor_data["humidity"])
print("pressure:",sensor_data["pressure"])
print("status:",sensor_data["status"])
print("deployed_in",sensor_data["deployed_in"])
sensor_data["aqi"]= 30000 # replace the data
print("sensor data is:",sensor_data)
#accessing the data using get method
temp=sensor_data.get("temperature")
print("temp:",temp)
#indent uesd for indentation  or formate the data beuty program
print(json.dumps(sensor_data,indent=10))

#==========================================================================
#modify data

print("sensor data is:",sensor_data)
sensor_data["deployed_in"].append("DAC") 
print("sensor data is:",sensor_data)
b=sensor_data.pop('humidity')
c=sensor_data.pop('status')
print("pop data is ",b,c)
print("sensor data is:",sensor_data)
sensor_data.update(       
     {  "prn" :12334,
          "X-AXIS " :123
        }
)
print("sensor data is:",sensor_data)
"""
"""
keys_to_delete_in_sensor_data=["temperature","prn"]
for key in keys_to_delete_in_sensor_data:
    if key in sensor_data :
         del sensor_data[key]
print("----------------multiple deleted data---------")
print("sensor data is:",sensor_data) 
"""
"""  ======================================================
sensor_data["NAME"]="RAm"
print("sensor data is:",sensor_data)
#ask the user to enter two  keys that need be deleted from disct
list=[]
print(list)
a=input("enter tha first key as delected in list   :")
b=input("enter tha second key as delectedin list  :")
list.append(a)
list.append(b)

for key in list :
    if key in sensor_data :
         del sensor_data[key]
print("----------------multiple deleted data---------")
print("sensor data is:",sensor_data)

#get key all in disct
print("get key all in disct")
print(sensor_data.keys())
#print allvalue in disct 
============================================================="""
"""====================================================================================

           *****tuple****
"""
desd_student_list_data=(
     "xyz",
     "pqr",
     1
)
print(type(desd_student_list_data))
print(desd_student_list_data)

"""
#not put comma then it is string  for not tuple
diot_student_list_data=(

# ACTS AS STRING
     "XYZ"
     
)
print(type(diot_student_list_data))
"""
#  we uesd comma for single after parameter it acts as tuple
diot_student_list_data=(
     "XYZ",
   #acts as tuple  
)
print(type(diot_student_list_data))



#==========================================================================














