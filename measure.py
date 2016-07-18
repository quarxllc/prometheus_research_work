import csv
import random
from faker import Factory

faker = Factory.create()

# Get data from other CSVs
individuals = []
with open('../deploy/individual.csv', 'rt') as x:
  rd = csv.reader(x)
  next(rd, None)
  for row in rd:
    individuals.append(row[0])

studies = []
with open('../deploy/study.csv', 'rt') as y:
  rd = csv.reader(y)
  next(rd, None)
  for row in rd:
    studies.append(row[0])

measure_type_revisions = []
with open('../deploy/measure_type.csv', 'rt') as z:
  rd = csv.reader(z)
  next(rd, None)
  for row in rd:
    measure_type_revisions.append(row[0])

# Initialize CSVs
with open('../deploy/measure.csv', 'a') as a:
  measure_csv = csv.writer(a)
  measure_csv.writerow(['individual','measure_type_revision','code','study','json','date_of_evaluation','age_at_evaluation','data_entry_status','last_modified','calculation'])

with open('../deploy/measure_entry.csv', 'a') as b:
  measure_entry_csv = csv.writer(b)
  measure_entry_csv.writerow(['measure','code','type','status','date_created','created_by','date_modified','modified_by','json','memo'])

# MEASURE DATA
for i in measure_type_revisions:
  individual = random.choice(individuals)
  measure_type_revision = i
  code = '1'
  study = random.choice(studies)
  json = ''
  date_of_evaluation = faker.date_time()
  age_at_evaluation = faker.random_int(min=10,max=90)
  data_entry_status = random.choice(['in-process','complete'])
  last_modified = faker.date_time()
  calculation = ''
  with open('../deploy/measure.csv', 'a') as a:
    measure_csv = csv.writer(a)
    measure_csv.writerow([individual,measure_type_revision,code,study,json,date_of_evaluation,age_at_evaluation,data_entry_status,last_modified,calculation])

# MEASURE ENTRY DATA
  measure = individual + '.(' + measure_type_revision + ').' + '1'
  code = '1'
  type = 'preliminary'
  status = 'complete'
  date_created = faker.date_time()
  created_by = faker.name()
  date_modified = ''
  modified_by = ''
  json = '{}'
  memo = ''
  with open('../deploy/measure_entry.csv', 'a') as b:
    measure_entry_csv = csv.writer(b)
    measure_entry_csv.writerow([measure,code,type,status,date_created,created_by,date_modified,modified_by,json,memo])

