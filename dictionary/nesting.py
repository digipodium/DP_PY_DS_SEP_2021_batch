class_9 = {
    'teacher' : 'PK Shukla Sir',
    'students': {
        '001' : {
            'name' : 'raja babu',
            'father': 'babu ji',
            'grade': 'C'
        },
        '002': {
            'name' : 'Rajkumar',
            'father': 'Mahraj',
            'mother':'Maharani',
            'grade':'B'
        },
        '007': {
            'name' : 'James Bond',
            'father': 'J',
            'mother':'M',
            'grade':'A'
        },
    }
}


from pprint import pprint

pprint(class_9)

# how to access
print(class_9['students']['002']['father'])
print(class_9['students']['001']['grade'])
print(class_9['students']['007']['name'])


# loop

for k,val in class_9.items():
    print(k, end=' -> ')
    if isinstance(val,str):
        print(val)
    if isinstance(val,dict):
        for k,data in val.items():
            print(k, end=' -> ')
            if isinstance(data,str):
                print(data)
            if isinstance(data,dict):
                for k,v in data.items():
                    print(k, end=' -> ')
                    if isinstance(v,str):
                        print(v)
                    