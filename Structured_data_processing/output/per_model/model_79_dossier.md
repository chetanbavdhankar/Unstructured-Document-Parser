<model id="Model 79" code="TM-CRYPTO-079">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 461 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2079 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 104 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 78672 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2540 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 81316 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.181496062992126 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.815929203539823 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.296940418679549 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.974254188802616 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2540 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 362 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.14251968503937 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 31.2361650843622 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.64 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.296940418679549 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.14251968503937 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.235172125223478 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 70 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 32 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 38 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.457142857142857 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 91 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 5 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 86 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0549450549450549 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2476 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 113 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0456381260096931 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2204 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 132 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0598911070780399 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -272 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2157 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 98 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0454334724153917 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -47 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2051 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 223 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.108727450024378 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Re-segment population | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2476 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 113 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0456381260096931 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2204 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 132 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0598911070780399 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -272 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2157 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 98 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0454334724153917 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -47 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2051 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 223 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.108727450024378 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -106 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 170222 | Data_Quality.xlsx/Completeness |
    | Populated Records | 166267 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.976765635464276 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 26759 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 589 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.977988714077507 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 76 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 73 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.960526315789474 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5.2 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | I. Dąbrowski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | ATM Cycling | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Virtual-Asset Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Private Banking | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 10 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 71 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.52 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 34.08 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.7 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-09-27 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-09-27 | Model_Risk_Governance.xlsx/Lifecycle_Status |
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
    | Tuning_Recommendations | recommendation: Re-segment population | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.79 Model 79 — ATM Cycling

| **Model Code**                 | TM-CRYPTO-079                                                                              |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Virtual-Asset Family                                                                       |
| **Business Problem Solved**    | Geographically dispersed rapid ATM withdrawals.                                            |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                          |
| **Typology Detected**          | ATM Cycling — flags geographically dispersed rapid ATM withdrawals.                        |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity I)            |
| **Booking Entity / Segment**   | Entity I · Private Banking · Americas                                                      |
| **Accountable Owner**          | I. Dąbrowski                                                                               |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                               |
| **Primary Source System**      | PaymentsHub-SWIFT                                                                          |
| **Linked Change Request(s)**   | —                                                                                          |
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