import csv
import random
from faker import Factory

faker = Factory.create()

# Initialize empty CSVs
with open('../deploy/individual.csv', 'a') as x:
  individual_csv = csv.writer(x)
  individual_csv.writerow(['code','sex','mother','father','adopted_mother','adopted_father'])

with open('../deploy/identity.csv', 'a') as y:
  identity_csv = csv.writer(y)
  identity_csv.writerow(['individual','givenname','middle','surname','birthdate','notes','deathdate','deceased'])

with open('../deploy/contact_info.csv', 'a') as z:
  contact_csv = csv.writer(z)
  contact_csv.writerow(['individual','cellphone','homephone','email','preferred_contact_method','preferred_contact_person','address'])

for i in range(5):
# INDIVIDUAL DATA
# generate ID
  a = faker.random_int(min=10000, max=18000)
  b = faker.random_int(min=1, max=5)
  individual_code = str(a) + '-0' + str(b)
# generate sex
  c = random.choice(['male','female','not-known'])
  sex = c
# generate mother
##  d = faker.random_int(min=10000, max=18000)
##  e = faker.random_int(min=1, max=5)
##  mother = str(d) + '-0' + str(e)
  mother = ''
# generate father
##  f = faker.random_int(min=10000, max=18000)
##  g = faker.random_int(min=1, max=5)
##  father = str(f) + '-0' + str(g)
  father = ''
# unused fields
  adopted_mother = ''
  adopted_father = ''

  with open('../deploy/individual.csv', 'a') as x:
    individual_csv = csv.writer(x)
    individual_csv.writerow([individual_code, sex, mother, father, adopted_mother, adopted_father])

# IDENTITY DATA
# generate full name
  given_name = faker.first_name()
  middle_name = faker.first_name()
  surname = faker.last_name()
# generate DOB
  birthdate = faker.profile()['birthdate']
# unused fields
  notes = ''
  deathdate = ''
  deceased = ''

  with open('../deploy/identity.csv', 'a') as y:
    identity_csv = csv.writer(y)
    identity_csv.writerow([individual_code, given_name, middle_name, surname, birthdate, notes, deathdate, deceased])

# CONTACT DATA
# generate phone number
  cell_phone = faker.phone_number()
# unused home phone
  home_phone = ''
# generate email
  email = faker.free_email()
# unused preferred contact method
  preferred_contact_method = ''
# generate preferred contact person
  preferred_contact_person = faker.name()
# unused address
  address = ''

  with open('../deploy/contact_info.csv', 'a') as z:
    contact_csv = csv.writer(z)
    contact_csv.writerow([individual_code, cell_phone, home_phone, email, preferred_contact_method, preferred_contact_person, address])

