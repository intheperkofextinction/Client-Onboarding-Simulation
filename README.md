#  Client Onboarding Pipeline Simulation

A simulated **end-to-end client onboarding workflow** for financial services, covering:

 Document Submission  
 AML (Anti‑Money Laundering) Checks  
 KYC (Know Your Customer) Verification  
 Compliance Review  
 Final Approval or Escalation  

This project replicates how banks and fintechs evaluate and approve new clients using synthetic data and an interactive dashboard.

---

##  Live App

 [Click here to explore the dashboard](https://client-app-stimulation-55kg79jyvhshm7esbsptnp.streamlit.app/)

---

##  Onboarding Process Flowchart

```text
         ┌──────────────┐
         │  Client Entry│
         └──────┬───────┘
                │
                ▼
   ┌────────────────────────┐
   │ Document Submission    │
   └──────┬─────────────────┘
          │
          ▼
    ┌───────────────┐
    │ AML Check     │
    └──────┬────────┘
           │
           ▼
    ┌───────────────┐
    │ KYC Verification│
    └──────┬────────┘
           │
           ▼
    ┌───────────────┐
    │ Internal Review│
    └──────┬───┬────┘
           │   │
        ┌─▼─┐ ┌▼─────┐
        │✅  │ │❌   │
        │Approved││Rejected│
        └──────┘ └──────┘
```

## How the Data Was Created

Synthetic client data is generated using the Faker library. It simulates:

Full names

Nationality

Document submission status

AML flags

KYC verification

Review decisions

[For the data generation script.](https://github.com/intheperkofextinction/Client-Onboarding-Simulation/blob/main/Client%20Onboarding%20Pipeline%20Simulation%20(1).ipynb)

## Tech Stack
**Tool**       	**Purpose**

Python   -      	Core logic and data processing

Faker    -      	Synthesizing client data

Pandas	   -      Data manipulation and filtering

Streamlit   -  	Building interactive dashboard interface

Plotly	Dynamic  
and responsive  - visualizations

##  Dashboard Features

Sidebar filters by Review Status and Country

Summary metrics: Total, Approved, Rejected, AML Escalated

Bar chart of review outcomes

Table view of escalated (AML-flagged) clients

Expandable full dataset table

## What I Learned

Simulated real-world client onboarding workflows

Designed logic for AML/KYC compliance

Built an interactive dashboard app from scratch

Integrated data generation, processing, and visualization

## Project Structure

```
Client-Onboarding-Simulation/
│
├── client_onboarding_app.py   ← Streamlit dashboard code
├── generate_client_data.py    ← Faker-based data generator
├── client_data.csv            ← Generated dataset
├── requirements.txt           ← App dependencies
└── README.md                  ← This documentation
```
## To Run Locally

Install dependencies and run the app:

```
pip install streamlit pandas plotly faker
streamlit run client_onboarding_app.py
```
## Next Steps

Integrate additional features like KPI cards or trend analysis

Add more advanced visualizations (pie charts, tables)

Document user flows or edge cases in a wiki or report

## About the Author
Built  by Amal,

as part of a professional portfolio demonstrating data-driven compliance and dashboard development.




