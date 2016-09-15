###########################
def min(arr):
	minimal =arr[0];
	for el in arr:
		if el<minimal:
			minimal=el
	return minimal
############################

def average(arr):
	summ=0
	for el in arr:
		summ=summ+el
	return (summ/(len(arr)))

###########################	

def reverse(string):
	i,string2=0,''
	
	for ch in range(len(string)):
		string2=string2+string[(len(string)-ch-1)]
	print (string2)

###############################

def childrens(emps):
	for el in emps:
		for child in el['children']:
			if child['age']>18: 
				print (el['name'])
##############################

ivan = {
	"name": "ivan",
	"age": 34,
	"children": [{
		"name": "vasja",
		"age": 12,
   }, {
       "name": "petja",
       "age": 10,
   }],
}
darja = {
   "name": "darja",
   "age": 41,
   "children": [{
       "name": "kirill",
       "age": 21,
   }, {
       "name": "pavel",
       "age": 15,
   }],
}

arr = [1663,5342,123,6545,564]
emps = [ivan, darja]

print (min(arr))
print (average(arr))

reverse("Hello, world!")
childrens(emps)
