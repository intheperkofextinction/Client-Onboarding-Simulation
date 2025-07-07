
# Client Onboarding Pipeline Simulation

A simulated end-to-end client onboarding dashboard using **Python**, **Faker**, and **Streamlit**.

This project demonstrates a typical onboarding pipeline in a financial institution, including document submission, AML checks, KYC verification, and review decisions.

---

##  Dashboard Preview

![Client Onboarding Dashboard](https://github.com/intheperkofextinction/Client-Onboarding-Stimulation/blob/main/client_onboarding_dashboard.pdf)

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
```

##  Live App

👉 [Click here to launch the dashboard](https://client-app-stimulation-55kg79jyvhshm7esbsptnp.streamlit.app/)

