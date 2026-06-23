<model id="Model 62" code="TM-BEHAV-062">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 552 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1641 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 24 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 56834 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2193 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 59051 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.251709986320109 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.958333333333333 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.398699891657638 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.971936725096195 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2193 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 211 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0962152302781578 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 37.1373897139761 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.7 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.398699891657638 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0962152302781578 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.277706027105846 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 76 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 28 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 48 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.368421052631579 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 156 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 3 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 153 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0192307692307692 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2623 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 104 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0396492565764392 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1865 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 185 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0991957104557641 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -758 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1871 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 107 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0571886691608765 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 6 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2428 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 101 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0415980230642504 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 557 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | No change - retain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2623 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 104 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0396492565764392 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1865 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 185 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0991957104557641 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -758 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1871 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 107 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0571886691608765 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 6 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2428 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 101 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0415980230642504 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 557 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 124880 | Data_Quality.xlsx/Completeness |
    | Populated Records | 112657 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.902122037155669 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 80696 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 259 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.996790423317141 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Green | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 28 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 27 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.964285714285714 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.2 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | KYC-Master | Data_Quality.xlsx/Lineage |
    | Secondary Feed | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | B. Nowak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Rapid Movement of Funds | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Behavioural-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 5 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.5 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 90 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.95 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 4.5 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.0 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-03-24 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-03-24 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | B. Nowak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity B | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-02-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-023 | source_system: KYC-Master | issue_description: Duplicate transaction records | status: In Progress | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: No change - retain | direction: Maintain | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.62 Model 62 — Rapid Movement of Funds

| **Model Code**                 | TM-BEHAV-062                                                                        |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Behavioural-Anomaly Family                                                          |
| **Business Problem Solved**    | Funds pass through account with minimal retention.                                  |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.      |
| **Typology Detected**          | Rapid Movement of Funds — flags funds pass through account with minimal retention.  |
| **Data Inputs**                | KYC-Master transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity B)                 |
| **Booking Entity / Segment**   | Entity B · SME · APAC                                                               |
| **Accountable Owner**          | B. Nowak                                                                            |
| **Lifecycle / Risk Tier**      | Production · Tier 2 - High                                                          |
| **Primary Source System**      | KYC-Master                                                                          |
| **Linked Change Request(s)**   | —                                                                                   |
</functional_requirements>

<change_requests>
  <not provided>
</change_requests>

<estate_context>
  <sampling_methodology>
    ATL Sample Basis: Stratified random, 95% CI; BTL Sample Basis: Boundary band ±15% of threshold; Confidence Level: 99%
  </sampling_methodology>

  <relevant_coverage_gaps>None identified</relevant_coverage_gaps>

</estate_context>

</model>