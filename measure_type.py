import csv
import random
from faker import Factory

faker = Factory.create()

# Initialize CSVs
with open('../deploy/measure_type.csv', 'a') as a:
  measure_type_csv = csv.writer(a)
  measure_type_csv.writerow(['code','title','status','num_required_entries'])

with open('../deploy/measure_type_revision.csv', 'a') as b:
	measure_type_revision_csv = csv.writer(b)
	measure_type_revision_csv.writerow(['measure_type','revision','json','published_by','date_published','calculation_json'])

with open('../deploy/measure_type_revision_channel.csv', 'a') as c:
  measure_type_revision_channel_csv = csv.writer(c)
  measure_type_revision_channel_csv.writerow(['measure_type_revision','acquire_channel','json'])

with open('../deploy/acquire_channel.csv', 'a') as d:
  acquire_channel_csv = csv.writer(d)
  acquire_channel_csv.writerow(['code','title','presentation_type'])

# MEASURE TYPE DATA
for i in range(5):
  code = faker.text(max_nb_chars=10)
  title = faker.text(max_nb_chars=10)
  status = 'active'
  num_required_entries = 2
  with open('../deploy/measure_type.csv', 'a') as a:
    measure_type_csv = csv.writer(a)
    measure_type_csv.writerow([code,title,status,num_required_entries])

# MEASURE TYPE REVISION DATA
  measure_type = code
  revision = '1'
  json = '{}'
  published_by = 'owner'
  date_published = faker.date_time()
  calculation_json = ''
  with open('../deploy/measure_type_revision.csv', 'a') as b:
    measure_type_revision_csv = csv.writer(b)
    measure_type_revision_csv.writerow([measure_type,revision,json,published_by,date_published,calculation_json])

# MEASURE TYPE REVISION CHANNEL DATA
  measure_type_revision = measure_type
  acquire_channel = random.choice(['entry','survey'])
  json = '{}'
  with open('../deploy/measure_type_revision_channel.csv', 'a') as c:
    measure_type_revision_channel_csv = csv.writer(c)
    measure_type_revision_channel_csv.writerow([measure_type_revision,acquire_channel,json])

# ACQUIRE CHANNEL DATA
with open('../deploy/acquire_channel.csv', 'a') as d:
  acquire_channel_csv = csv.writer(d)
  acquire_channel_csv.writerow(['entry','RexEntry','form'])
  acquire_channel_csv.writerow(['survey','RexSurvey','form'])










