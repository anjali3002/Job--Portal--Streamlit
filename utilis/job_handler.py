import os
import csv
import uuid

JOBS_FILE = os.path.join("Datas", "jobs.csv")


def read_jobs():
    jobs = []
    if os.path.exists(JOBS_FILE):
        with open(JOBS_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                jobs.append(row)
    return jobs


def get_employer_jobs(employer_username):
    return [job for job in read_jobs() if job["posted_by"] == employer_username]


def add_job(title, company, location, description, posted_by):
    file_exists = os.path.exists(JOBS_FILE)
    job_id = str(uuid.uuid4())[:8]

    with open(JOBS_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["job_id", "title", "company", "location", "description", "posted_by"]
        )
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

    return job_id


def update_job(job_id, new_title, new_company, new_location, new_description):
    jobs = read_jobs()
    updated = False

    for job in jobs:
        if str(job["job_id"]) == str(job_id):
            job["title"] = new_title
            job["company"] = new_company
            job["location"] = new_location
            job["description"] = new_description
            updated = True

    if updated:
        with open(JOBS_FILE, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["job_id", "title", "company", "location", "description", "posted_by"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(jobs)

    return updated


def delete_job(job_id):
    jobs = read_jobs()
    updated_jobs = [job for job in jobs if str(job["job_id"]) != str(job_id)]

    if len(updated_jobs) == len(jobs):
        return False

    with open(JOBS_FILE, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["job_id", "title", "company", "location", "description", "posted_by"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_jobs)

    return True
