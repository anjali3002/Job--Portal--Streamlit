import csv
import os
import uuid

JOBS_FILE= os.path.join("Datas","jobs.csv")
APPLICATIONS_FILE= os.path.join("Datas",'applications.csv')

def read_jobs():
    jobs= []

    if os.path.exists(JOBS_FILE):
        with open(JOBS_FILE,mode= "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                jobs.append(row)
    return jobs


def get_employer_jobs(employer_username):
    jobs= read_jobs()
    employer_jobs= []

    for job in jobs:
        if job["posted_by"] == employer_username:
            employer_jobs.append(job)

    
    return employer_jobs

def add_job(title, company, location, description, posted_by):
    file_exists = os.path.exists(JOBS_FILE)

    job_id = str(uuid.uuid4())[:8]

    with open(JOBS_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["job_id", "title", "company", "location", "description", "posted_by"]
        )

        # write header only once
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "job_id": job_id,
            "title": title,
            "company": company,
            "location": location,
            "description": description,
            "posted_by": posted_by
        })

def update_job(job_id, new_title, new_company, new_location, new_description):
    jobs = read_jobs()

    for job in jobs:
        if job["job_id"] == job_id:
            job["title"] = new_title
            job["company"] = new_company
            job["location"] = new_location
            job["description"] = new_description

    with open(JOBS_FILE, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["job_id", "title", "company", "location", "description", "posted_by"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jobs)


def delete_job(job_id):
    jobs = read_jobs()
    updated_jobs = []

    for job in jobs:
        if job["job_id"] != job_id:
            updated_jobs.append(job)

    with open(JOBS_FILE, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["job_id", "title", "company", "location", "description", "posted_by"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_jobs)


        