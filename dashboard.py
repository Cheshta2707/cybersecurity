import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams.update({
    'font.size': 8,
    'axes.titlesize': 10,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7
})
# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Cybersecurity Intrusion Dashboard",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("cybersecurity_intrusive_data_cleaned.csv")

# -----------------------------
# Title
# -----------------------------
st.title("🛡️ Cybersecurity Intrusion Dashboard")

# -----------------------------
# KPI Cards
# -----------------------------
total_sessions = len(df)
total_attacks = int(df["attack_detected"].sum())
attack_rate = df["attack_detected"].mean() * 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sessions", total_sessions)

with col2:
    st.metric("Total Attacks", total_attacks)

with col3:
    st.metric("Attack Rate", f"{attack_rate:.2f}%")

st.divider()

# -----------------------------
# Row 1
# -----------------------------
col1, col2 ,col3 = st.columns(3)

with col1:
    st.subheader("Attack Distribution")

    fig, ax = plt.subplots(figsize=(3, 2))

    df["attack_detected"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    ax.set_ylabel("")
    st.pyplot(fig, use_container_width=True)

with col2:
    st.subheader("Encryption Usage")

    fig, ax = plt.subplots(figsize=(3, 2))

    df["encryption_used"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    ax.set_ylabel("")
    st.pyplot(fig, use_container_width=True)



with col3:
    st.subheader("Login Attempts Distribution")

    fig, ax = plt.subplots(figsize=(3, 3))

    sns.histplot(
        df["login_attempts"],
        bins=15,
        ax=ax
    )

    st.pyplot(fig, use_container_width=True)


# -----------------------------
# Row 2
# -----------------------------


col1, col2 ,col3 = st.columns(3)

with col1:
    st.subheader("IP Reputation Score")

    fig, ax = plt.subplots(figsize=(3, 2))

    sns.histplot(
        df["ip_reputation_score_least_trustworthy"],
        bins=15,
        ax=ax
    )

    st.pyplot(fig, use_container_width=True)



with col2:
    st.subheader("Failed Logins vs Attack Rate")

    fig, ax = plt.subplots(figsize=(3, 2))

    df.groupby("failed_logins")["attack_detected"].mean().plot(
        kind="bar",
        ax=ax
    )

    ax.set_ylabel("Attack Rate")

    st.pyplot(fig, use_container_width=True)

with col3:
    st.subheader("Protocol-wise Attack Rate")

    fig, ax = plt.subplots(figsize=(3, 2))

    df.groupby("protocol_type")["attack_detected"].mean().plot(
        kind="bar",
        ax=ax
    )

    ax.set_ylabel("Attack Rate")

    st.pyplot(fig, use_container_width=True)

# -----------------------------
# Heatmap
# -----------------------------
st.subheader("Correlation Heatmap")

left, center, right = st.columns([1, 2, 1])

with center:

    cols = [
        'login_attempts',
        'failed_logins',
        'attack_detected',
        'risk_score'
]

    fig, ax = plt.subplots(figsize=(3, 2))

    sns.heatmap(
        df[cols].corr(),
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        annot_kws={"size":4},
        ax=ax
    )

    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)

    plt.tight_layout()

    st.pyplot(fig)          

# -----------------------------
# Data Preview
# -----------------------------
st.subheader("Dataset Preview")

st.dataframe(df.head())