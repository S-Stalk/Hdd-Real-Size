hdd_size = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 22]
const = 0.9313225746154785
real_hdd_size = [ v * const for v in hdd_size ]

print(real_hdd_size)
