import csv
import random
import decimal 
from faker import Faker
import math

# Get individual IDs from preexisting CSV
ids = []
with open('../deploy/individual.csv', 'rt') as x:
  rd = csv.reader(x)
  next(rd, None)
  for row in rd:
	  ids.append(row[0])

# SAMPLE_TYPE DATA
codes = [u'cp-dna', u'ep-dna', u'ep-pl', u'fibroblast', u'lcl', u'pbmc', u'pl', u'saliva', u'skin-biopsy', u'spit-dna', u'ssc-kit', u'va-blood-draw', u'vb-blood-draw', u'wb-dna']

with open('../deploy/sample_types.csv', 'a') as a:
  sample_type_csv = csv.writer(a)
  sample_type_csv.writerow(['code','title'])
  for i in codes:
	  sample_type_csv.writerow([i, ''])

# SAMPLE DATA
with open('../deploy/sample.csv', 'a') as b:
  sample = csv.writer(b)
  sample.writerow(['sample_type','individual','code','code_text','derived_from'])
  for i in ids:
    for x in range (0,3):
        sample_type = random.choice(codes)
        individual = i
        code = str(x)
        code_text = ''
        derived_from = ''
        sample.writerow([sample_type, individual, code, code_text, derived_from])
    

# TUBES

sample_ids = []
a =[]
with open('../deploy/sample.csv', 'rt') as x:
  rd = csv.reader(x)
  next(rd, None)
  for row in rd:
	  sample_ids.append([row[0],row[1],row[2]])

with open('../deploy/tube.csv','a') as c:
    tube = csv.writer(c)
    tube.writerow(['sample', 'code','volume_amount', 'volume_unit', 'concentration_amount', 'concentration_unit','location_memo'])
    for i in sample_ids:
        num_tubes = random.randint(1,4)
        for j in range(0,num_tubes):
            sample = i[1] + "." + i[0] + "." + i[2]
            code = j
            volume = random.uniform(0.001,10.0)
            volume_amount = math.ceil(volume)
            a.append(volume)
            volume_unit = random.choice(['ml','ul'])
            concentration_amount = decimal.Decimal(random.randrange(10))/100
            concentration_unit = 'ng-ul'
            location_memo = ' '
            tube.writerow([sample, code, volume_amount, volume_unit, concentration_amount, concentration_unit, location_memo])
    
def random_sample_generator(total_tube_volume,num_usage,x):
    
    tube_1 = random.uniform(0.1,1.0)
    tube_2 = random.uniform(0.1,1.0)
    total_tube_volume = float(total_tube_volume)
    tube_usage =[] 

    C  = tube_1 + tube_2
    if num_usage > 0: 
        tube_1 =round(round((tube_1/C),4) * round(total_tube_volume,4),4)
        tube_usage.append(tube_1)
        tube_2 =round(round((tube_2/C),4) * round(total_tube_volume,4),4)
        tube_usage.append(tube_2)
        #print tube_1, tube_2, total_tube_volume
    
    else: 
        tube_1 = 0
        tube_usage.append(tube_1)
        tube_2 = 0
        tube_usage.append(tube_2)
        total_tube_volume = 0
    #print tube_1, tube_2, total_tube_volume 
    x = x + 1
    return (tube_usage,x)

import datetime

def appointment_date():

    duration = random.randint(1,3)
    a = fake.date()
    b = fake.time()
    c = a + " " + b
    d = datetime.datetime.strptime(c, "%Y-%m-%d %H:%M:%S")
    e = d + datetime.timedelta(hours = duration)      
    
    return (d,e,duration)


    
#print type(a[0])


fake = Faker()
Used_Volume_Amount = []

tube_id = []
volume_amount = []
with open('../deploy/tube.csv', 'rt') as x:
  rd = csv.reader(x)
  rd.next()
  next(rd, None)
  for row in rd:
      tube_id.append([row[0],row[1],row[2],row[3]])

users = []
with open('../deploy/user.csv', 'rt') as x:
  rd = csv.reader(x)
  rd.next()
  for row in rd:
      users.append(row[0])
x = 1
with open ( '../deploy/tube_usage.csv','a') as d:
    usage = csv.writer(d)
    usage.writerow(['tube','code','user','used_volume_amount','used_volume_unit','date_requested','note'])
    for i in tube_id:
        num_usage = random.randint(0,2)
        Used_Volume_Amount_list,x = random_sample_generator(a[x], num_usage,x)
        #print a[x],x
        #x = x + 1
        #print x
        for j in range(0,num_usage):
            tube = i[0] + '.' +  i[1]
            code = j
            #user = ' '
            user = "'" + random.choice(users) + "'"
            used_volume_amount = Used_Volume_Amount_list[j]
            used_volume_unit =  i[3]
            date_requested = fake.date() 
            note = ' '
            usage.writerow([tube, code, user, used_volume_amount, used_volume_unit, date_requested, note])

appointments_type = []
with open ('../deploy/appointment_type.csv','rt') as x:
    rd = csv.reader(x)
    rd.next()
    for row in rd:
        appointments_type.append(row[0])
# with open('../deploy/individual.csv', 'rt') as y:
#     rd = csv.reader(y)
#     next(rd, None)
#     for row in rd:
#         ids.append(row[0])
#print idsi
acceptance = ['requested','accepted','declined','request-more-info']
axi = ['appointment','individual']
statuses = ['scheduled','cancelled','completed','rescheduled']

with open ( '../deploy/appointment.csv','a') as e:
     appointment = csv.writer(e)
     appointment.writerow(['individual','appointment_type','code','start','end','duration','staff','acceptance_status_by_staff','staff_notes','requestor','requestor_notes','status','reason_for_cancellation'])
     for i in ids:
        individual = i
        for j in range (0,3):
             appointment_type = random.choice(appointments_type)
             code = j
             start,end,duration  = appointment_date()
             start = start
             end = end
             duration = duration
             staff = "'" + random.choice(users) + "'"
             acceptance_status_by_staff = random.choice(acceptance)
             staff_notes = ''
             requestor = staff
             requestor_notes = ' '
             status =  random.choice(statuses)
             reason_for_cancellation = 'i'
             appointment.writerow([individual, appointment_type, code, start, end, duration, staff, acceptance_status_by_staff, staff_notes, requestor, requestor_notes, status, reason_for_cancellation])

communication_types = []
with open('../deploy/communication_type.csv','rt') as x:
    rd = csv.reader(x)
    rd.next()
    for row in rd:
        communication_types.append(row[0])
studys = []
with open('../deploy/study.csv','rt') as x:
    rd = csv.reader(x)
    rd.next()
    for row in rd:
        studys.append(row[0])

boolean = ['true','false']


with open ( '../deploy/communication.csv','a') as f:
    communication = csv.writer(f)
    communication.writerow(['individual','communication_type','code','study','notes','user','contact_datetime','followup_needed','who_followup_needed','why_followup_needed'])
    for i in ids:
        individual = i
        for j in range (0,3):
            communication_type = random.choice(communication_types)
            code = j
            study = random.choice(studys)
            notes = ' '
            user = "'" + random.choice(users) + "'"
            contact_datetime = fake.date() + " " + fake.time()
            followup_needed = random.choice(boolean)
            who_followup_needed = "'" + random.choice(users) + "'" 
            why_followup_needed =  ' '
            communication.writerow([individual, communication_type, code, study, notes, user, contact_datetime, followup_needed, who_followup_needed, why_followup_needed])  
