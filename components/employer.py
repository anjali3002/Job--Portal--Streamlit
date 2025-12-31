import streamlit as st
import sys
import os
import csv


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utilis.job_handler import add_job, get_employer_jobs
from utilis.applications import get_applications_for_job, update_application_status

JOBS_FILE = os.path.join("Datas","jobs.csv")
APPLICATIONS_FILE= os.path.join("Datas","applications.csv")


def employer_ui():
    st.sidebar.title("Employer Menu")

    choice = st.sidebar.radio(
        "Navigation",
        ["Post Job", "View Applicants"]
    )

    if choice == "Post Job":
        employer_add_job_ui()
    else:
        employer_view_applicants_ui()


def employer_add_job_ui():
    st.subheader("➕ Post a New Job")

    title = st.text_input("Job Title")
    company = st.text_input("Company Name")
    location = st.text_input("Location")
    description = st.text_area("Job Description")

    if st.button("Post Job"):
        if not (title and company and location and description):
            st.warning("Please fill all fields")
            return

        add_job(
            title=title,
            company=company,
            location=location,
            description=description,
            posted_by=st.session_state["username"]
        )

        st.success("🎉 Job posted successfully!")
        st.rerun()



def employer_view_applicants_ui():
    st.header("📥 Job Applications")

    employer = st.session_state["username"]
    jobs = get_employer_jobs(employer)

    for job in jobs:
        st.subheader(job["title"])

        applications = get_applications_for_job(job["job_id"])

        for app in applications:
            st.write(f"👤 {app['applicant']}")
            st.write(f"📌 Status: {app['status']}")

            if app["status"] == "Pending":
                col1, col2 = st.columns(2)

                with col1:
                    if st.button("Accept",
                        key=f"accept_{job['job_id']}_{app['applicant']}"):
                        update_application_status(
                            job["job_id"],
                            app["applicant"],
                            "Accepted"
                        )
                        st.rerun()

                with col2:
                    if st.button("Reject",
                        key=f"reject_{job['job_id']}_{app['applicant']}"):
                        update_application_status(
                            job["job_id"],
                            app["applicant"],
                            "Rejected"
                        )
                        st.rerun()

