<model id="Model 19" code="TM-GEO-019">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 442 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 845 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 54 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 75433 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1287 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 76774 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.343434343434343 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.891129032258065 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.495793606281548 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.988922100736779 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1287 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 325 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.252525252525253 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 16.7634876390445 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.64 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.495793606281548 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.252525252525253 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.39848626477903 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 116 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 104 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 12 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.896551724137931 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 123 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 3 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 120 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.024390243902439 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1514 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 158 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.104359313077939 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1256 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 130 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.103503184713376 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -258 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1418 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 114 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0803949224259521 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 162 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1150 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 109 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0947826086956522 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -268 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Extend lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1514 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 158 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.104359313077939 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1256 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 130 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.103503184713376 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -258 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1418 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 114 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0803949224259521 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 162 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1150 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 109 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0947826086956522 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -268 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 214162 | Data_Quality.xlsx/Completeness |
    | Populated Records | 200946 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.938289705923553 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 172371 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 533 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.996907832524033 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Green | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 115 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 99 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.860869565217391 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.7 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | I. Dąbrowski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | ATM Cycling | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Geographic-Risk Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Private Banking | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 9 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.9 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 73 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.45 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 40.15 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-10-22 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-10-22 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | I. Dąbrowski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity I | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-07-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Extend lookback window | direction: Reduce leakage | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.19 Model 19 — ATM Cycling

| **Model Code**                 | TM-GEO-019                                                                             |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Geographic-Risk Family                                                                 |
| **Business Problem Solved**    | Geographically dispersed rapid ATM withdrawals.                                        |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.         |
| **Typology Detected**          | ATM Cycling — flags geographically dispersed rapid ATM withdrawals.                    |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity I)        |
| **Booking Entity / Segment**   | Entity I · Private Banking · Americas                                                  |
| **Accountable Owner**          | I. Dąbrowski                                                                           |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                           |
| **Primary Source System**      | CryptoGateway                                                                          |
| **Linked Change Request(s)**   | —                                                                                      |
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