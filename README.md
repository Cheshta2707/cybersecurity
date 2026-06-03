# 🛡️ Cybersecurity Intrusion Detection Dashboard

##  Project Overview

This project analyzes cybersecurity intrusion data and presents key insights through an interactive Streamlit dashboard. The goal is to identify suspicious activities, monitor attack patterns, and visualize security-related metrics in an easy-to-understand format.

The dashboard was built using Python and Streamlit and demonstrates data analysis, visualization, and dashboard development skills.

---

##  Objectives

* Analyze network activity and login behavior.
* Identify potential cyber attacks.
* Monitor attack rates and suspicious activities.
* Visualize security metrics through interactive charts.
* Build a business-friendly dashboard for cybersecurity monitoring.

---

##  Dataset Features

The dataset contains information related to network sessions and user login activity.

### Key Columns

| Column              | Description                                 |
| ------------------- | ------------------------------------------- |
| session_id          | Unique session identifier                   |
| network_packet_size | Size of network packets                     |
| protocol_type       | Network protocol used                       |
| login_attempts      | Number of login attempts                    |
| session_duration    | Duration of session                         |
| encryption_used     | Whether encryption was used                 |
| ip_reputation_score | Reputation score of IP address              |
| failed_logins       | Number of failed login attempts             |
| browser_type        | Browser used                                |
| unusual_time_access | Access during unusual hours                 |
| attack_detected     | Target variable indicating attack detection |

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit
* Git & GitHub

---

##  Dashboard Features

### KPI Cards

* Total Sessions
* Total Attacks
* Attack Rate (%)

### Visualizations

* Attack Distribution (Pie Chart)
* Encryption Usage Analysis
* Login Attempts Distribution
* IP Reputation Score Distribution
* Failed Logins vs Attack Rate
* Protocol-wise Attack Rate
* Correlation Heatmap

### Data Preview

* Interactive dataset table

---

##  Key Insights

* Sessions with higher failed login counts show a higher attack rate.
* Certain network protocols are more frequently associated with attacks.
* Unencrypted sessions may present higher security risks.
* Low IP reputation scores are often linked to suspicious activity.
* Correlation analysis helps identify important security indicators.

---

##  How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/Cheshta2707/cybersecurity_project.git
```

### Navigate to the Project Folder

```bash
cd cybersecurity_project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Dashboard

```bash
streamlit run dashboard.py
```

---

##  Project Structure

```text
cybersecurity_project/
│
├── dashboard.py
├── cybersecurity_intrusion_data_cleaned.csv
├── requirements.txt
├── README.md
└── screenshots/
  └── dashboard.png
  └── 2.png
  └── heatmap.png
  └── end_of_dashboard.png
```

---

##  Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Data Visualization
* Dashboard Development
* Python Programming
* Cybersecurity Data Analysis
* Git & GitHub Version Control

---
