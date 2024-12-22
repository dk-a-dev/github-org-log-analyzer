import streamlit as st
import pandas as pd
import plotly.express as px
import time
from main import clean_data, totalActiveDays, longestGap, busiestDay, longestStreak, monthWiseActivity, timeWiseActivity, allDeveloperActivity, repoActivity
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import re

# Streamlit UI
st.set_page_config(page_title="GDGVIT Github Wrapped 2024", layout="wide")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create authenticator
authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    auto_hash=True
)

# Login widget
authenticator.login()


if st.session_state['authentication_status']:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')

    st.title("GDGVIT Github Wrapped 🎁 2024")
    st.balloons()

    # Add a spinner to simulate loading data
    with st.spinner('Loading data...'):
        time.sleep(2)  # Simulate a delay
        data_path = "clean_data.csv"
        data = clean_data(data_path)

    # Calculate metrics with loading animations
    with st.spinner('Calculating metrics...'):
        time.sleep(1)  # Simulate a delay
        total_active_days = totalActiveDays(data)
        longest_gap, gap_start_date, gap_end_date = longestGap(data)
        busiest_day, busiest_day_count = busiestDay(data)
        longest_streak, streak_start_date, streak_end_date = longestStreak(
            data)
        month_wise_activity = monthWiseActivity(data)
        time_wise_activity = timeWiseActivity(data)
        developer_activity, most_active_developer = allDeveloperActivity(data)
        repo_activity, stars, issues_opened, issues_resolved, pr_opened, pr_closed, commits, branches, forks, actions_success, action_failures, new_collaborator, comments = repoActivity(
            data)

    # Display metrics
    st.header("Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Active Days", total_active_days)
    col2.metric("Longest Gap", f"{longest_gap} days", f"From {
                gap_start_date} to {gap_end_date}")
    col3.metric("Busiest Day", str(busiest_day),
                f"{busiest_day_count} messages")

    col1, col2, col3 = st.columns(3)
    col1.metric("Longest Streak", f"{longest_streak} days", f"From {
                str(streak_start_date)} to {str(streak_end_date)}")
    col2.metric("Most Active Developer", most_active_developer)
    col3.metric("Number of Repositories", len(repo_activity.keys()))

    # Convert Period objects to strings for plotting
    month_wise_activity.index = month_wise_activity.index.astype(str)
    # Ensure all months are displayed
    all_months = pd.period_range(start=month_wise_activity.index.min(
    ), end=month_wise_activity.index.max(), freq='M').astype(str)
    month_wise_activity = month_wise_activity.reindex(all_months, fill_value=0)

    # Plot month-wise activity
    st.header("📅 Month-wise Activity")
    with st.spinner('Loading month-wise activity...'):
        time.sleep(1)  # Simulate a delay
        fig_month = px.bar(month_wise_activity, x=month_wise_activity.index,
                           y=month_wise_activity.values, labels={'x': 'Month', 'y': 'Activity Count'})
        st.plotly_chart(fig_month, use_container_width=True)

    # Plot time-wise activity
    st.header("⏰ Time-wise Activity")
    with st.spinner('Loading time-wise activity...'):
        time.sleep(1)  # Simulate a delay
        fig_time = px.bar(time_wise_activity, x=time_wise_activity.index.astype(
            str), y=time_wise_activity.values, labels={'x': 'Time of Day', 'y': 'Activity Count'})
        st.plotly_chart(fig_time, use_container_width=True)

    # Display developer activity
    st.header("👨‍💻 Developer Activity")
    with st.spinner('Loading developer activity...'):
        time.sleep(1)  # Simulate a delay
        fig_dev = px.bar(x=list(developer_activity.keys()), y=list(
            developer_activity.values()), labels={'x': 'Developer', 'y': 'Activity Count'})
        st.plotly_chart(fig_dev, use_container_width=True)

    # Display repository activity
    st.header("📂 Repository Activity")
    with st.spinner('Loading repository activity...'):
        time.sleep(1)  # Simulate a delay
        repo_activity_df = pd.DataFrame(repo_activity).T.reset_index().rename(
            columns={'index': 'Repository'})
        st.dataframe(repo_activity_df)

    # Display total activity
    st.header("📊 Total Activity")
    with st.spinner('Loading total activity...'):
        time.sleep(1)  # Simulate a delay
        col1, col2, col3 = st.columns(3)
        col1.metric("⭐ Stars", stars)
        col2.metric("🐛 Issues Opened", issues_opened)
        col3.metric("✅ Issues Resolved", issues_resolved)

        col1, col2, col3 = st.columns(3)
        col1.metric("🔀 Pull Requests Opened", pr_opened)
        col2.metric("🔁 Pull Requests Closed", pr_closed)
        col3.metric("💻 Commits", commits)

        col1, col2, col3 = st.columns(3)
        col1.metric("🌿 Branches", branches)
        col2.metric("🍴 Forks", forks)
        col3.metric("✔️ Actions Success", actions_success)

        col1, col2, col3 = st.columns(3)
        col1.metric("❌ Action Failures", action_failures)
        col2.metric("👥 New Collaborator", new_collaborator)
        col3.metric("💬 Comments", comments)

elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect or you do not have access')
elif st.session_state['authentication_status'] is None:
    st.error('Login to continue')
else:
    st.error('Ask Admin for access')