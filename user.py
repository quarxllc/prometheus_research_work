import csv
import random
from faker import Factory

faker = Factory.create()

# Initialize empty CSVs
with open('../deploy/user.csv', 'a') as x:
  user_csv = csv.writer(x)
  user_csv.writerow(['remote_user','identity','site_admin'])

with open('../deploy/user_access.csv', 'a') as y:
  user_access_csv = csv.writer(y)
  user_access_csv.writerow(['user','date_added','last_login'])

with open('../deploy/user_details.csv', 'a') as z:
  user_details_csv = csv.writer(z)
  user_details_csv.writerow(['user','name','email','phone'])

with open('../deploy/lab_x_user.csv', 'a') as v:
  lab_x_user_csv = csv.writer(v)
  lab_x_user_csv.writerow(['lab','user','lab_admin'])

# USER DATA
for i in range(5):
  remote_user = faker.company_email()
  identity = '{}'
  site_admin = 'false'
  with open('../deploy/user.csv', 'a') as x:
    user_csv = csv.writer(x)
    user_csv.writerow([remote_user, identity, site_admin])

# USER ACCESS DATA
  user = "'" + remote_user + "'"
  date_added = faker.date(pattern="%Y-%m-%d")
  last_login = faker.date_time()
  with open('../deploy/user_access.csv', 'a') as y:
    user_access_csv = csv.writer(y)
    user_access_csv.writerow([user, date_added, last_login])

# USER DETAILS DATA
  user = "'" + remote_user + "'"
  name = faker.name()
  email = remote_user
  phone = faker.phone_number()
  with open('../deploy/user_details.csv', 'a') as z:
    user_details_csv = csv.writer(z)
    user_details_csv.writerow([user, name, email, phone])

# LAB_X_USER DATA
  labs = [u'behavior-analysis-core', u'cac-snc-combined-core', u'clinical-assessment-core', u'clinical-trials-core', u'feeding-core', u'itco-core', u'legacy-core', u'llc-core', u'model-systems-core', u'neuroimaging-core', u'no-requirement', u'social-neuroscience-core', u'spoken-communication-core']
  user = "'" + remote_user + "'"
  lab_admin = random.choice(['true','false'])
  lab = random.choice(labs)
  with open('../deploy/lab_x_user.csv', 'a') as v:
    lab_x_user_csv = csv.writer(v)
    lab_x_user_csv.writerow([lab, user, lab_admin])
