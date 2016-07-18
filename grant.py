import csv
import random
from faker import Factory

faker = Factory.create()

# Get studies from preexisting CSV
studies = []
with open('../deploy/study.csv', 'rt') as x:
  rd = csv.reader(x)
  next(rd, None)
  for row in rd:
	  studies.append(row[0])

# Initialize empty CSVs
with open('../deploy/grant.csv', 'a') as a:
  grant_csv = csv.writer(a)
  grant_csv.writerow(['code','title','startdate','enddate'])

with open('../deploy/grant_x_study.csv', 'a') as b:
  grant_x_study_csv = csv.writer(b)
  grant_x_study_csv.writerow(['study','grant'])

for i in range(5):
  # generate grant table
  code = faker.word()
  title = code
  start_date = faker.date(pattern="%Y-%m-%d")
  end_date = faker.date(pattern="%Y-%m-%d")
  with open('../deploy/grant.csv', 'a') as a:
    grant_csv = csv.writer(a)
    grant_csv.writerow([code, title, start_date, end_date])
  # generate grant_x_study table
  study = random.choice(studies)
  grant = title
  with open('../deploy/grant_x_study.csv', 'a') as b:
    grant_x_study_csv = csv.writer(b)
    grant_x_study_csv.writerow([study, grant])
