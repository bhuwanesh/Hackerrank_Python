# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
country_set = set()
for i in range(n):
    country_name = input()
    country_set.add(country_name)

print(len(country_set))
