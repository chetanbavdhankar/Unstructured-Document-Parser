<model id="Model 28" code="TM-CASH-028">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 145 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 599 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 84 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 74546 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 744 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 75374 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.19489247311828 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.633187772925764 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.298047276464543 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.99202874442744 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 744 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 73 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0981182795698925 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 9.87077772176082 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.61 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.298047276464543 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0981182795698925 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.218075677706683 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 107 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 64 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 43 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.598130841121495 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 75 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 12 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 63 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.16 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 748 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 43 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0574866310160428 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 724 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 37 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0511049723756906 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -24 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 595 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 58 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0974789915966387 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -129 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 813 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 70 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0861008610086101 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 218 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 748 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 43 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0574866310160428 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 724 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 37 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0511049723756906 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -24 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 595 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 58 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0974789915966387 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -129 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 813 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 70 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0861008610086101 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 218 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 215303 | Data_Quality.xlsx/Completeness |
    | Populated Records | 205327 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.953665299601027 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 117273 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1355 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.988445763304427 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 42 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 40 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.952380952380952 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | H. Woźniak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Velocity Anomaly | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Cash-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 10 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 65 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.71 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 18.85 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.2 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-02-22 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-02-22 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | H. Woźniak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity H | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-04-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Shorten lookback window | direction: Maintain | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.28 Model 28 — Velocity Anomaly

| **Model Code**                 | TM-CASH-028                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                          |
| **Business Problem Solved**    | Transaction frequency exceeds peer-group baseline.                                           |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.               |
| **Typology Detected**          | Velocity Anomaly — flags transaction frequency exceeds peer-group baseline.                  |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity H)                    |
| **Booking Entity / Segment**   | Entity H · Corporate · High-Risk Jurisdictions                                               |
| **Accountable Owner**          | H. Woźniak                                                                                   |
| **Lifecycle / Risk Tier**      | Tuning · Tier 4 - Low                                                                        |
| **Primary Source System**      | Sanctions-Screening                                                                          |
| **Linked Change Request(s)**   | —                                                                                            |
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