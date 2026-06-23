<model id="Model 27" code="TM-GEO-027">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 141 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1097 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 94 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 33133 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1238 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 34465 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.11389337641357 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.6 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.191446028513238 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.967952088810985 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1238 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 101 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0815831987075929 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 35.9204990570144 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.52 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.191446028513238 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0815831987075929 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.14750089659098 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 96 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 30 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 66 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.3125 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 125 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 3 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 122 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.024 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1115 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 61 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0547085201793722 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1130 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 62 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0548672566371681 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 15 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1243 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 129 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.103781174577635 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 113 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1104 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 75 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0679347826086957 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Extend lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1115 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 61 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0547085201793722 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1130 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 62 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0548672566371681 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 15 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1243 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 129 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.103781174577635 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 113 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1104 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 75 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0679347826086957 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -139 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 120334 | Data_Quality.xlsx/Completeness |
    | Populated Records | 108422 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.901008858676683 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 132988 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3570 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.973155472674226 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 25 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 21 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.84 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.8 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | KYC-Master | Data_Quality.xlsx/Lineage |
    | Secondary Feed | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | G. Szymański | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Round-Amount Transactions | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Geographic-Risk Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 10 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 93 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.77 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 21.39 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.2 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-10-17 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-10-17 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | G. Szymański | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity G | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-03-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Low | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-018 | source_system: KYC-Master | issue_description: Currency code mismatch | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Extend lookback window | direction: Reduce leakage | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.27 Model 27 — Round-Amount Transactions

| **Model Code**                 | TM-GEO-027                                                                          |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Geographic-Risk Family                                                              |
| **Business Problem Solved**    | Unusual frequency of round-figure transfers.                                        |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.      |
| **Typology Detected**          | Round-Amount Transactions — flags unusual frequency of round-figure transfers.      |
| **Data Inputs**                | KYC-Master transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity G)                 |
| **Booking Entity / Segment**   | Entity G · SME · Americas                                                           |
| **Accountable Owner**          | G. Szymański                                                                        |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                        |
| **Primary Source System**      | KYC-Master                                                                          |
| **Linked Change Request(s)**   | —                                                                                   |
</functional_requirements>

<change_requests>
  <not provided>
</change_requests>

<estate_context>
  <sampling_methodology>
    ATL Sample Basis: Stratified random, 95% CI; BTL Sample Basis: Boundary band ±15% of threshold; Confidence Level: 97.5%
  </sampling_methodology>

  <relevant_coverage_gaps>None identified</relevant_coverage_gaps>

</estate_context>

</model>