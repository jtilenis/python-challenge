import os
import csv

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Output file
output_path = os.path.join("..", "PyBoss/analysis", "results.csv")
outfile = open(output_path, "w") 
outfile.write("Emp ID,First Name,Last Name,DOB,SSN,State\n")
employee_data_csv = os.path.join("../PyBoss/Resources", "employee_data.csv")
with open(employee_data_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        emp_id = row[0]
        name = row[1]
        # split name into first and last name
        first_name, last_name = name.split(" ")
        dob = row[2]
        # reformat DOB to mm/dd/yyyy
        yyyy,mm,dd = dob.split("-")
        new_dob = mm + "/" + dd + "/" + yyyy
        ssn = row[3]
        # hide the first 5 ssn numbers from view
        ssn1,ssn2,ssn3 = ssn.split("-")
        new_ssn = "***-**-" + ssn3 
        # find state code
        state = row[4]
        state_abbr = us_state_abbrev[state]
        outfile.write(f"{emp_id},{first_name},{last_name},{new_dob},{new_ssn},{state_abbr}\n")
outfile.close
        
        
        
