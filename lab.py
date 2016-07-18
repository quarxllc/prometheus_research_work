import csv

labs = [u'behavior-analysis-core', u'cac-snc-combined-core', u'clinical-assessment-core', u'clinical-trials-core', u'feeding-core', u'itco-core', u'legacy-core', u'llc-core', u'model-systems-core', u'neuroimaging-core', u'no-requirement', u'social-neuroscience-core', u'spoken-communication-core']

# Initialize empty CSV
with open('../deploy/lab.csv', 'a') as a:
  lab_csv = csv.writer(a)
  lab_csv.writerow(['code','title'])
# LAB DATA
for i in labs:
  code = i
  title = i
  with open('../deploy/lab.csv', 'a') as a:
    lab_csv = csv.writer(a)
    lab_csv.writerow([code, title])