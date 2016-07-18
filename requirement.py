import csv
import random
from faker import Factory

faker = Factory.create()

# Get data from other CSVs
participant_groups = []
with open('../deploy/participant.csv', 'rt') as x:
  rd = csv.reader(x)
  next(rd, None)
  for row in rd:
    participant_groups.append(row[0])

studies = []
with open('../deploy/study.csv', 'rt') as y:
  rd = csv.reader(y)
  next(rd, None)
  for row in rd:
    studies.append(row[0])

time_periods = []
with open('../deploy/time_period.csv', 'rt') as z:
  rd = csv.reader(z)
  next(rd, None)
  for row in rd:
    time_periods.append(row[0])

measures = []
with open('../deploy/measure.csv', 'rt') as v:
  rd = csv.reader(v)
  next(rd, None)
  for row in rd:
    measures.append(row[0])

# Initialize empty CSVs
with open('../deploy/requirement_list.csv', 'a') as a:
  requirement_list_csv = csv.writer(a)
  requirement_list_csv.writerow(['study','month','code','title','participant_group','time_period'])

with open('../deploy/requirement.csv', 'a') as b:
  requirement_list_csv = csv.writer(b)
  requirement_list_csv.writerow(['requirement_list','requirement_type','code','title','priority','acquire_channel','primary_measure_type','primary_sample_type','primary_consent_type','primary_communication_type'])

# REQUIREMENT LIST DATA
requirement_list = []
for participant_group in participant_groups:
  study = random.choice(studies)
  month = faker.random_int(min=1,max=10)
  code = study.upper() + '-' + str(month)
  title = 'Month' + ' ' + str(month)
  participant_group = random.choice(participant_group)
  time_period = random.choice(time_periods)
  requirement_list.append(code)
  with open('../deploy/requirement_list.csv', 'a') as a:
    requirement_list_csv = csv.writer(a)
    requirement_list_csv.writerow([study,month,code,title,participant_group,time_period])

# REQUIREMENT DATA
for requirement in requirement_list:
  requirement_list = requirement
  requirement_type = random.choice(['measure','communication'])
  code = faker.word()
  title = code.upper()
  priority = '1'
  acquire_channel = 'entry'
  primary_measure_type = random.choice(measures)
  primary_sample_type = ''
  primary_consent_type = ''
  primary_communication_type = ''
  num_required_entries = 2
  with open('../deploy/requirement.csv', 'a') as b:
    requirement_list_csv = csv.writer(b)
    requirement_list_csv.writerow([requirement_list,requirement_type,code,title,priority,acquire_channel,primary_measure_type,primary_sample_type,primary_consent_type,primary_communication_type])

