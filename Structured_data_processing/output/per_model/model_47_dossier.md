<model id="Model 47" code="TM-CRYPTO-047">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 390 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2544 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 20 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 33881 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2934 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 36835 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.132924335378323 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.951219512195122 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.233253588516746 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.93015785861359 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2934 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 154 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0524880708929789 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 79.6525044115651 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.57 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.233253588516746 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0524880708929789 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.160947381467239 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 99 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 56 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 43 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.565656565656566 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 134 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 12 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 122 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0895522388059701 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3152 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 269 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0853426395939086 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3342 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 384 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.114901256732496 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 190 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2931 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 149 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0508358921869669 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -411 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3020 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 289 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0956953642384106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 89 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Re-segment population | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 3152 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 269 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0853426395939086 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 3342 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 384 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.114901256732496 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 190 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2931 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 149 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0508358921869669 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -411 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 3020 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 289 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0956953642384106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 89 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 354056 | Data_Quality.xlsx/Completeness |
    | Populated Records | 339552 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.959034728969429 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 77671 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3407 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.956135494586139 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 78 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 68 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.871794871794872 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.6 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | G. Szymański | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Round-Amount Transactions | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Virtual-Asset Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 8 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.8 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 75 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.89 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 8.25 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.6 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-01-05 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-01-05 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | G. Szymański | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity G | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-11-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 4 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Re-segment population | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.47 Model 47 — Round-Amount Transactions

| **Model Code**                 | TM-CRYPTO-047                                                                          |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Virtual-Asset Family                                                                   |
| **Business Problem Solved**    | Unusual frequency of round-figure transfers.                                           |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                      |
| **Typology Detected**          | Round-Amount Transactions — flags unusual frequency of round-figure transfers.         |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity G)                    |
| **Booking Entity / Segment**   | Entity G · SME · Americas                                                              |
| **Accountable Owner**          | G. Szymański                                                                           |
| **Lifecycle / Risk Tier**      | Validation · Tier 3 - Medium                                                           |
| **Primary Source System**      | CryptoGateway                                                                          |
| **Linked Change Request(s)**   | —                                                                                      |
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