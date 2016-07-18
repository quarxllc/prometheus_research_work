import csv
import random
from faker import Factory

faker = Factory.create()
# Get Labs, Users, and Individuals from preexisting CSVs
labs = []
with open('../deploy/lab.csv', 'rt') as x:
  rd = csv.reader(x)
  next(rd, None)
  for row in rd:
	  labs.append(row[0])

users = []
with open('../deploy/user.csv', 'rt') as y:
  rd = csv.reader(y)
  next(rd, None)
  for row in rd:
	  users.append(row[0])

individuals = []
with open('../deploy/individual.csv', 'rt') as z:
  rd = csv.reader(z)
  next(rd, None)
  for row in rd:
	  individuals.append(row[0])

# Initialize empty CSVs
with open('../deploy/study.csv', 'a') as a:
  study_csv = csv.writer(a)
  study_csv.writerow(['code','lab','title','irb_number','start_date','user','description','overall_target_enrollment','closed'])

with open('../deploy/study_x_user.csv', 'a') as b:
  study_x_user_csv = csv.writer(b)
  study_x_user_csv.writerow(['study','user','manage_staff','manage_grants','configure_studies','recruit_participants','enroll_participants','transcribe_data','clean_data','manage_datamarts','explore_data','study_tracking'])

with open('../deploy/study_recruitment.csv', 'a') as c:
  study_recruitment_csv = csv.writer(c)
  study_recruitment_csv.writerow(['study','individual','recruitment_date'])

with open('../deploy/study_configuration.csv', 'a') as d:
  study_configuration_csv = csv.writer(d)
  study_configuration_csv.writerow(['study','status','type'])

with open('../deploy/time_period.csv', 'a') as e:
  time_period_csv = csv.writer(e)
  time_period_csv.writerow(['study','code','title','days_from_enrollment_offset'])

for i in range(5):
  # STUDY DATA
  code = faker.word()
  lab = random.choice(labs)
  title = code
  irb_number = ''
  start_date = ''
  user = ''
  description = ''
  overall_target_enrollment = ''
  closed = 'false'
  with open('../deploy/study.csv', 'a') as a:
    study_csv = csv.writer(a)
    study_csv.writerow([code, lab, title, irb_number, start_date, user, description, overall_target_enrollment, closed])

  # STUDY_X_USER DATA
  study = title
  user = "'" + random.choice(users) + "'"
  manage_staff = 'false'
  manage_grants = 'false'
  configure_studies = 'false'
  recruit_participants = 'false'
  enroll_participants = 'false'
  transcribe_data = 'false'
  clean_data = 'false'
  manage_datamarts = 'false'
  explore_data = 'false'
  study_tracking = 'false'
  with open('../deploy/study_x_user.csv', 'a') as b:
    study_x_user_csv = csv.writer(b)
    study_x_user_csv.writerow([study, user, manage_staff, manage_grants, configure_studies, recruit_participants, enroll_participants, transcribe_data, clean_data, manage_datamarts, explore_data, study_tracking])
  
  # STUDY_RECRUITMENT DATA
  study = title
  individual = random.choice(individuals)
  recruitment_date = faker.date(pattern="%Y-%m-%d")
  with open('../deploy/study_recruitment.csv', 'a') as c:
    study_recruitment_csv = csv.writer(c)
    study_recruitment_csv.writerow([study,individual,recruitment_date])

# STUDY_CONFIGURATION DATA
  study = title
  status = random.choice(['in-configuration','configuration-completed'])
  type = random.choice(['requirements-only', 'multi-group', 'multi-timeperiod-no-groups', 'multi-timeperiod-multi-group'])
  with open('../deploy/study_configuration.csv', 'a') as d:
    study_configuration_csv = csv.writer(d)
    study_configuration_csv.writerow([study,status,type])

# TIME_PERIOD DATA
  study = title
  num = faker.numerify(text='##')
  code = 'month' + '-' + num
  title = 'Month' +  ' ' + num
  days_from_enrollment_offset = ''
  with open('../deploy/time_period.csv', 'a') as e:
    time_period_csv = csv.writer(e)
    time_period_csv.writerow([study,code,title,days_from_enrollment_offset])








