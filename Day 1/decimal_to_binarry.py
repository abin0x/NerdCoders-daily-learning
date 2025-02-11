# decimal থেকে binary এ কাস্টিং
x = 10
binary_value = bin(x)  # 10 কে binary এ রূপান্তরিত করবে
print(binary_value)  # আউটপুট: '0b1010'
# binary থেকে decimal এ কাস্টিং
x = 0b1010
decimal_value = int(x)  # 0b1010 কে decimal এ রূপান্তরিত করবে
print(decimal_value)  # আউটপুট: 10
# binary থেকে hexa এ কাস্টিং
x = 0b1010
hexa_value = hex(x)  # 0b1010 কে hexa এ রূপান্তরিত করবে
print(hexa_value)  # আউটপুট: '0xa'
# hexa থেকে binary এ কাস্টিং
x = 0xa
binary_value = bin(x)  # 0xa কে binary এ রূপান্তরিত করবে
print(binary_value)  # আউটপুট: '0b1010'
# hexa থেকে decimal এ কাস্টিং
x = 0xa
decimal_value = int(x)  # 0xa কে decimal এ রূপান্তরিত করবে
print(decimal_value)  # আউটপুট: 10
# decimal থেকে hexa এ কাস্টিং
x = 10
hexa_value = hex(x)  # 10 কে hexa এ রূপান্তরিত করবে
print(hexa_value)  # আউটপুট: '0xa'
# decimal থেকে binary এ কাস্টিং