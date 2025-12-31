import os
import csv
from datetime import datetime

APPLICATIONS_FILE= os.path.join("Datas","applications.csv")





def read_applications():
    applications= []

    if os.path.exists(APPLICATIONS_FILE):
        with open(APPLICATIONS_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                applications.append(row)

    return applications

def apply_job(job_id,job_title,applicant):
    applied_date= datetime.now().strftime("%Y-%m-%d %H:%M")

    file_exists= os.path.exists(APPLICATIONS_FILE)

    with open(APPLICATIONS_FILE,mode="a",newline= "", encoding="utf-8") as file:
        fieldnames = ["job_id","job_title","applicant","applied_date","status"]
        writer= csv.DictWriter(file, fieldnames=fieldnames)
       
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "job_id": job_id,
            "job_title": job_title,
            "applicant": applicant,
            "applied_date": applied_date,
            "status": "Pending"
        })


def already_applied(job_id,applicant):
    applications=read_applications()

    for app in applications:
        if app["job_id"] ==job_id and app["applicant"] ==applicant:
            return True
    
    return False

def get_my_applications(username):
    applications =read_applications()
    my_apps= []

    for app in applications:
        if app["applicant"] ==username:
            my_apps.append(app)
    
    return my_apps

def get_applications_for_job(job_id):
    applications = read_applications()
    job_apps =[]

    for app in applications:
        if app["job_id"] == job_id:
            job_apps.append(app)
        
    return job_apps

def update_application_status(job_id, applicant, new_status):
    applications = read_applications()

    for app in applications:
        if app["job_id"] == job_id and app["applicant"] == applicant:
            app["status"] = new_status

    with open(APPLICATIONS_FILE, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["job_id", "job_title", "applicant", "applied_date", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(applications)

