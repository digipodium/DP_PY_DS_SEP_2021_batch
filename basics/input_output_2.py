
a = 5
b = "balls"
c = 50
d = "Rupees"

# printing with comma seprated values
print("Raju purchased",a,b,"for",c,d)

# contacatenation using +
print('Raju purchased ' + str(a) + ' ' + b + " for " + str(c) + ' ' + d)

# printing format specifier
print("Raju purchased %d %s for %d %s" %(a,b,c,d))

# print using format() method
print("Raju purchased {} {} for {} {}".format(a,b,c,d))

# printing using f-string (from ver 3.6)
print(f'Raju purchased {a} {b} for {c} {d}') 

# properties of print function 
# end - handles what will be displayed after printing content
# sep - seperator symbol

print('Hi',end=' ')
print('there')

print(a,b,c,d)
print(a,b,c,d, sep="❌")


