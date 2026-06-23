<model id="Model 13" code="TM-TBML-013">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 441 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1654 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 69 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 41496 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2095 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 43660 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.210501193317422 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.864705882352941 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.338579654510557 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.961668597914253 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2095 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 306 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.146062052505967 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 47.9844251030692 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.61 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.338579654510557 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.146062052505967 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.261572613708721 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 77 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 54 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 23 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.701298701298701 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 129 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 10 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 119 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0775193798449612 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1722 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 200 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.116144018583043 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1973 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 101 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0511910795742524 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 251 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1741 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 189 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.108558299827685 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -232 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1691 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 194 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.114725014784151 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -50 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Tighten min-amount floor | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | CR-002 | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1722 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 200 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.116144018583043 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1973 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 101 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0511910795742524 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 251 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1741 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 189 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.108558299827685 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -232 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1691 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 194 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.114725014784151 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -50 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 281553 | Data_Quality.xlsx/Completeness |
    | Populated Records | 270017 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.95902725241784 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 137721 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 7166 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.947967267156062 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 95 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 82 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.863157894736842 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.5 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | KYC-Master | Data_Quality.xlsx/Lineage |
    | Secondary Feed | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | C. Lewandowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Sanctions Proximity | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Trade-Based Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 57 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.71 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 16.53 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.2 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-04-05 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-04-05 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | C. Lewandowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity C | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-01-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-016 | source_system: KYC-Master | issue_description: Duplicate transaction records | status: Closed | linked_cr: None | DQ_Issue_Log |
    | DQ_Issue_Log | issue_id: DQ-042 | source_system: PaymentsHub-SWIFT | issue_description: Originator data dropped on 4.2% of SWIFT MT103 feeds | status: In Progress | linked_cr: CR-002 | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Tighten min-amount floor | direction: Reduce FP | linked_change_request: CR-002 | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.13 Model 13 — Sanctions Proximity

| **Model Code**                 | TM-TBML-013                                                                         |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Trade-Based Family                                                                  |
| **Business Problem Solved**    | Counterparty proximity to sanctioned entities.                                      |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.      |
| **Typology Detected**          | Sanctions Proximity — flags counterparty proximity to sanctioned entities.          |
| **Data Inputs**                | KYC-Master transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity C)           |
| **Booking Entity / Segment**   | Entity C · Corporate · EMEA                                                         |
| **Accountable Owner**          | C. Lewandowska                                                                      |
| **Lifecycle / Risk Tier**      | Production · Tier 1 - Critical                                                      |
| **Primary Source System**      | KYC-Master                                                                          |
| **Linked Change Request(s)**   | CR-002                                                                              |
</functional_requirements>

<change_requests>
  <cr id="CR-002" source="CR-002_Change_Request.md">
**CHANGE REQUEST**

Originator data completeness gap on SWIFT MT103 feed affecting Models 12 and 13

| **CR ID**                    | CR-002                                              |
|------------------------------|-----------------------------------------------------|
| **Date Raised**              | 2025-08-02                                          |
| **Requester**                | Data Quality Office (1st LoD)                       |
| **Change Type**              | Data Issue Fix                                      |
| **Affected Model(s) / Feed** | Model 12 (TM-CRYPTO-012), Model 13 (TM-NETWORK-013) |
| **Family**                   | Virtual-Asset Family; Network-Linkage Family        |
| **Booking Entity**           | Entity B / Entity C                                 |
| **Priority**                 | High                                                |
| **Linked Findings**          | DQ-041; DQ-042 (PaymentsHub-SWIFT)                  |

**1. Problem Statement**

The PaymentsHub-SWIFT feed is dropping originator data on approximately 4.2% of MT103 messages, breaching the 98% completeness SLA.

Two downstream models consume this field for counterparty resolution: Model 12 (Crypto On/Off-Ramp) and Model 13 (Nested Correspondent). Incomplete originator data causes silent under-alerting on cross-border flows.

**2. Proposed Change**

Patch the feed mapping in PaymentsHub-SWIFT to retain field 50 (originator) where currently truncated during normalisation.

Backfill the affected 4.2% of records for the Q2 2025 period and re-run Models 12 and 13 over the corrected population.

Add a completeness control on the originator field at ingestion with an automated Red/Amber/Green DQ flag.

**3. Expected Impact**

| **Metric**              | **Current**   | **Expected Post-Change**    |
|-------------------------|---------------|-----------------------------|
| Originator Completeness | 95.8%         | ≥ 99.5%                     |
| Affected Records (Q2)   | ~18,400       | 0 after backfill            |
| Model 12 Alerts         | Understated   | Restored to true population |
| Model 13 Alerts         | Understated   | Restored to true population |

**4. Risk Assessment**

Backfill will retrospectively raise alerts that may require SAR back-reporting; the FIU notification path must be engaged before re-run.

This is a data-layer fix; model logic is unchanged. Risk of regression is limited to the feed-mapping component and is covered by the new ingestion control.

**5. Rollback Plan**

The feed-mapping change is deployed behind a toggle; reverting restores the prior normalisation path within one intraday cycle.

Backfilled records are written to a separate partition and can be quarantined without affecting the production population.

**6. Approval Chain**

| **Role**                   | **Approver**              | **Status**   |
|----------------------------|---------------------------|--------------|
| Data Steward               | B. Nowak                  | Approved     |
| Model Owners (12 & 13)     | B. Nowak / C. Lewandowska | Approved     |
| 2nd LoD MRM Validator      | MV-Team Bravo             | Pending      |
| Financial Crime Operations | FIU Reporting Lead        | Pending      |
  </cr>

</change_requests>

<estate_context>
  <sampling_methodology>
    ATL Sample Basis: Stratified random, 95% CI; BTL Sample Basis: Boundary band ±15% of threshold; Confidence Level: 97.5%
  </sampling_methodology>

  <relevant_coverage_gaps>None identified</relevant_coverage_gaps>

</estate_context>

</model>