import csv
import random
from faker import Factory

faker = Factory.create()

# Get individual IDs from preexisting CSV
ids = []
with open('../deploy/individual.csv', 'rt') as x:
  rd = csv.reader(x)
  next(rd, None)
  for row in rd:
	  ids.append(row[0])

# Initialize empty CSVs
with open('../deploy/disorder.csv', 'a') as a:
  disorder_csv = csv.writer(a)
  disorder_csv.writerow(['code','title'])

with open('../deploy/condition.csv', 'a') as b:
  condition_csv = csv.writer(b)
  condition_csv.writerow(['individual','disorder','code']) 

#make list for fake disorders codes
disorder_codes = []

# DISORDER DATA
for i in range(5):
  code = faker.word()
  title = faker.word()
  disorder_codes.append(code)
  with open('../deploy/disorder.csv', 'a') as a:
    disorder_csv = csv.writer(a)
    disorder_csv.writerow([code, title])

# CONDITION DATA
for i in ids:
  individual = i
  disorder = random.choice(disorder_codes)
  code = '1'
  with open('../deploy/condition.csv', 'a') as b:
    condition_csv = csv.writer(b)
    condition_csv.writerow([individual, disorder, code])
