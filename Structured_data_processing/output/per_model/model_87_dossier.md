<model id="Model 87" code="TM-CRYPTO-087">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 599 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 660 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 80 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 72338 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1259 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 73677 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.475774424146148 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.882179675994109 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.618163054695562 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.990958656401545 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1259 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 249 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.197776012708499 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 17.0881007641462 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.48 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.618163054695562 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.197776012708499 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.450008237900737 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 117 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 116 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 1 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.991452991452992 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 146 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 10 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 136 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0684931506849315 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1444 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 159 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.1101108033241 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1041 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 116 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.111431316042267 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -403 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1042 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 91 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0873320537428023 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 1 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1452 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 119 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0819559228650138 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 410 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Re-segment population | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1444 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 159 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.1101108033241 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1041 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 116 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.111431316042267 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -403 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1042 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 91 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0873320537428023 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 1 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1452 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 119 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0819559228650138 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 410 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 127707 | Data_Quality.xlsx/Completeness |
    | Populated Records | 124208 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.9726013452669 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 107986 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3998 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.962976682162503 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 99 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 97 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.97979797979798 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.3 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CardSwitch | Data_Quality.xlsx/Lineage |
    | Secondary Feed | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | G. Szymański | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Round-Amount Transactions | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Virtual-Asset Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 55 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.5 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 27.5 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.7 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-06-23 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-06-23 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | G. Szymański | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity G | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-03-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Low | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Re-segment population | direction: Maintain | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.87 Model 87 — Round-Amount Transactions

| **Model Code**                 | TM-CRYPTO-087                                                                       |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Virtual-Asset Family                                                                |
| **Business Problem Solved**    | Unusual frequency of round-figure transfers.                                        |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.      |
| **Typology Detected**          | Round-Amount Transactions — flags unusual frequency of round-figure transfers.      |
| **Data Inputs**                | CardSwitch transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity G)                 |
| **Booking Entity / Segment**   | Entity G · SME · Americas                                                           |
| **Accountable Owner**          | G. Szymański                                                                        |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                        |
| **Primary Source System**      | CardSwitch                                                                          |
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