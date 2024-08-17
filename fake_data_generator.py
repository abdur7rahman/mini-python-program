from faker import Faker

result_tam=Faker(['ta_IN'])
result_eng=Faker(['en_US'])

print(result_tam.name())
print(result_tam.address())
print(result_tam.city())
print(result_tam.text())



print(result_eng.name())
print(result_eng.address())
print(result_eng.city())
print(result_eng.text())