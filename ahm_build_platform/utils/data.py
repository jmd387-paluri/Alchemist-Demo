import pandas as pd
import random
from datetime import datetime, timedelta

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

records = []

employees = ["Jack","Raj","Anita","Suresh","John","Priya"]
departments = ["Sales","sales","SALES","Marketing","IT","it"]
salaries = [50000, "55,000", "60k", 75000, None]

for emp_id in range(1, 7):

    join_dt = random_date(datetime(2018,1,1), datetime(2020,12,31))
    last_mod_v1 = join_dt + timedelta(days=random.randint(300, 800))
    last_mod_v2 = last_mod_v1 + timedelta(days=random.randint(100, 400))

    # Version 1
    records.append({
        "EmpId__RAW": emp_id,
        "EmployeeNAME": employees[emp_id - 1],
        "Dept-Name": random.choice(departments),
        "SALARY_rawValue": random.choice(salaries),
        "JoinDATE": join_dt,
        "IsActiveFLAG": random.choice(["yes","Y",1]),
        "LastModifiedDT": last_mod_v1
    })

    # Version 2
    records.append({
        "EmpId__RAW": emp_id,
        "EmployeeNAME": employees[emp_id - 1],
        "Dept-Name": random.choice(departments),
        "SALARY_rawValue": random.choice(salaries),
        "JoinDATE": join_dt,
        "IsActiveFLAG": random.choice(["no","N",0]),
        "LastModifiedDT": last_mod_v2
    })

df = pd.DataFrame(records)

df.to_csv("employees_scd2_dirty.csv", index=False)

print("Messy-but-dbt-safe SCD2 CSV created: employees_scd2_dirty.csv")
