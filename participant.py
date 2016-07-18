import csv
import random
from faker import Factory

faker = Factory.create()

# Get studies from another CSV
studies = []
with open('../deploy/study.csv', 'rt') as x:
  rd = csv.reader(x)
  next(rd, None)
  for row in rd:
	  studies.append(row[0])

individuals = []
with open('../deploy/individual.csv', 'rt') as y:
  rd = csv.reader(y)
  next(rd, None)
  for row in rd:
	individuals.append(row[0])

# Initialize empty CSV
with open('../deploy/participant.csv', 'a') as a:
  participant_csv = csv.writer(a)
  participant_csv.writerow(['study','code','target_enrollment'])

# PARTICIPANT_GROUP DATA
participant_groups = []
for study in studies:
  code = faker.word()
  study = study
  target_enrollment = ''
  participant_groups.append([code,study])
  with open('../deploy/participant.csv', 'a') as a:
    participant_csv = csv.writer(a)
    participant_csv.writerow([study,code,target_enrollment])

# Initialize empty CSV
with open('../deploy/study_enrollment.csv', 'a') as b:
  study_enrollment_csv = csv.writer(b)
  study_enrollment_csv.writerow(['study','individual','code','enrollment_date','participant_group','consent_form_scan','measure'])

# STUDY_ENROLLMENT DATA
for individual in individuals:
  participant_group_array = random.choice(participant_groups)
  study = participant_group_array[1] 
  individual = individual
  code = faker.word()
  enrollment_date = faker.date(pattern="%Y-%m-%d")
  participant_group = participant_group_array[0] + '.' + participant_group_array[1]
  consent_form_scan = ''
  measure = ''
  with open('../deploy/study_enrollment.csv', 'a') as b:
    study_enrollment_csv = csv.writer(b)
    study_enrollment_csv.writerow([study,individual,code,enrollment_date,participant_group,consent_form_scan,measure])
