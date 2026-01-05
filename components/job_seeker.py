import streamlit as st

from utilis.job_handler import read_jobs
from utilis.applications import already_applied, apply_job, get_my_applications


def job_seeker_ui():
    st.sidebar.title("Job Seeker Menu")

    choice = st.sidebar.radio(
        "Navigation",
        ["Browse Jobs", "My Applications"]
    )

    if choice == "Browse Jobs":
        browse_jobs_ui()
    else:
        my_applications_ui()


def browse_jobs_ui():
    st.header("Job Seeker Dashboard")
    st.write("Search and apply for jobs here")

    if "username" not in st.session_state:
        st.error("Please login first")
        return

    jobs = read_jobs() or []

    if not jobs:
        st.info("No jobs available right now")
        return

    username = st.session_state["username"]

    for job in jobs:
        st.subheader(job["title"])
        st.write(f"🏢 Company: {job['company']}")
        st.write(f"📍 Location: {job['location']}")
        st.write(job["description"])

        if already_applied(job["job_id"], username):
            st.success("✅ Already Applied")
        else:
            if st.button(f"Apply for {job['title']}", key=job["job_id"]):
                apply_job(
                    job["job_id"],
                    job["title"],
                    username
                )
                st.success("🎉 Applied successfully")
                st.rerun()


def my_applications_ui():
    st.header("📄 My Applications")

    if "username" not in st.session_state:
        st.error("Please login first")
        return

    username = st.session_state["username"]
    my_apps = get_my_applications(username) or []

    if not my_apps:
        st.info("You have not applied to any jobs yet.")
        return

    for app in my_apps:
        st.subheader(app["job_title"])
        st.write(f"🆔 Job ID: {app['job_id']}")
        st.write(f"📅 Applied on: {app['applied_date']}")

        status = app["status"]
        if status == "Pending":
            st.info("⏳ Status: Pending")
        elif status == "Accepted":
            st.success("✅ Status: Accepted")
        else:
            st.error("❌ Status: Rejected")

        st.divider()
