
# Client Onboarding Pipeline Simulation

A simulated end-to-end client onboarding dashboard using **Python**, **Faker**, and **Streamlit**.

This project demonstrates a typical onboarding pipeline in a financial institution, including document submission, AML checks, KYC verification, and review decisions.

---

##  Dashboard Preview

![Client Onboarding Dashboard](https://github.com/your-username/client-onboarding-pipeline-simulation/blob/main/Screenshot%202025-07-06%20204458.png)

---

## Onboarding Process Flow

```text
         ┌──────────────┐
         │  Client Entry│
         └──────┬───────┘
                │
                ▼
     ┌─────────────────────┐
     │ Document Submission │
     └──────┬──────────────┘
            │
     ┌──────▼──────────────┐
     │ AML Check           │
     └──────┬──────────────┘
            │
     ┌──────▼──────────────┐
     │ KYC Verification     │
     └──────┬──────────────┘
            │
     ┌──────▼──────────────┐
     │ Internal Review     │
     └──────┬─────┬────────┘
            │     │
        ┌───▼─┐ ┌─▼─────┐
        │Approve││Reject│
        └──────┘ └──────┘
