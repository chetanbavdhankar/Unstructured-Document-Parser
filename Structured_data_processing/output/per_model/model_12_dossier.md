<model id="Model 12" code="TM-CASH-012">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 43 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2754 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 9 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 29465 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2797 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 32271 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0153736145870576 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.826923076923077 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.0301860301860302 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.914522486731432 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2797 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 33 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0117983553807651 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 86.6722444299836 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.83 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.0301860301860302 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0117983553807651 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.0228309602639242 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 57 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 55 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 2 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.964912280701754 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 50 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 8 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 42 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.16 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2830 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 157 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0554770318021201 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2645 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0525519848771267 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -185 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2673 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 255 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0953984287317621 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 28 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2831 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 158 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0558106676086189 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 158 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | CR-002 | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2830 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 157 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0554770318021201 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2645 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0525519848771267 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -185 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2673 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 255 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0953984287317621 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 28 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2831 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 158 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0558106676086189 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 158 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 164670 | Data_Quality.xlsx/Completeness |
    | Populated Records | 163616 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.993599319851825 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 178355 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3604 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.979793109248409 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 104 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 96 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.923076923076923 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.7 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | B. Nowak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | PEP Activity | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Cash-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 1 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 91 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.85 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 13.65 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.7 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-04-22 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-04-22 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | B. Nowak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity B | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-12-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-041 | source_system: PaymentsHub-SWIFT | issue_description: Originator data dropped on 4.2% of SWIFT MT103 feeds | status: In Progress | linked_cr: CR-002 | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Shorten lookback window | direction: Maintain | linked_change_request: CR-002 | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.12 Model 12 — PEP Activity

| **Model Code**                 | TM-CASH-012                                                                            |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                    |
| **Business Problem Solved**    | Politically exposed person unusual flow.                                               |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.         |
| **Typology Detected**          | PEP Activity — flags politically exposed person unusual flow.                          |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity B)                    |
| **Booking Entity / Segment**   | Entity B · SME · High-Risk Jurisdictions                                               |
| **Accountable Owner**          | B. Nowak                                                                               |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 4 - Low                                                         |
| **Primary Source System**      | CryptoGateway                                                                          |
| **Linked Change Request(s)**   | CR-002                                                                                 |
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
    ATL Sample Basis: Stratified random, 95% CI; BTL Sample Basis: Boundary band ±15% of threshold; Confidence Level: 99%
  </sampling_methodology>

  <relevant_coverage_gaps>None identified</relevant_coverage_gaps>

</estate_context>

</model>