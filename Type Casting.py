def Separating_values_with_separator():
    year=2026
    month=12
    day=12
    print(year,month,day,sep='/') # sep is used to separate the values with the given parameter. 
                                # Sep can be only used once in print statement

    print(f'{year}/{month}/{day}') # f is used to format the string and print the values in the given format.

    print('/'.join([str(year),str(month),str(day)])) # join is used to join the values with the given parameter. It takes the values as arguments and joins them with the given parameter.
    print('{2}/{1}/{0}'.format(year,month,day)) # format is used to format the string and print the values in the given format. It takes the values as arguments and formats them in the given format.


print('Hello',end=' ')
print('World')
for i in range(5):
    print(i,end=' ')

