import os
import csv
from datetime import datetime

APPLICATIONS_FILE = os.path.join("Datas", "applications.csv")


def read_applications():
    applications = []
    if os.path.exists(APPLICATIONS_FILE):
        with open(APPLICATIONS_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                applications.append(row)
    return applications


def apply_job(job_id, job_title, applicant):
    if already_applied(job_id, applicant):
        return False

    applied_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    file_exists = os.path.exists(APPLICATIONS_FILE)

    with open(APPLICATIONS_FILE, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = ["job_id", "job_title", "applicant", "applied_date", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "job_id": job_id,
            "job_title": job_title,
            "applicant": applicant,
            "applied_date": applied_date,
            "status": "Pending"
        })
    return True


def already_applied(job_id, applicant):
    applications = read_applications() or []
    for app in applications:
        if str(app["job_id"]) == str(job_id) and app["applicant"] == applicant:
            return True
    return False


def get_my_applications(username):
    applications = read_applications() or []
    return [app for app in applications if app["applicant"] == username]


def get_applications_for_job(job_id):
    applications = read_applications() or []
    return [app for app in applications if str(app["job_id"]) == str(job_id)]


def update_application_status(job_id, applicant, new_status):
    updated = False
    applications = read_applications() or []

    for app in applications:
        if str(app["job_id"]) == str(job_id) and app["applicant"] == applicant:
            app["status"] = new_status
            updated = True

    if updated:
        with open(APPLICATIONS_FILE, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["job_id", "job_title", "applicant", "applied_date", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(applications)

    return updated
