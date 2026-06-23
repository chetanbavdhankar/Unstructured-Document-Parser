<model id="Model 42" code="TM-RMF-042">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 535 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 394 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 101 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 33542 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 929 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 34572 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.575888051668461 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.841194968553459 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.68370607028754 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.988389910419613 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 929 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 294 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.316469321851453 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 26.8714566701377 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.62 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.68370607028754 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.316469321851453 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.536811370913105 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 78 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 47 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 31 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.602564102564103 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 171 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 10 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 161 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0584795321637427 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 920 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 41 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0445652173913044 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1070 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 63 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0588785046728972 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 150 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 931 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 40 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0429645542427497 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 911 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 94 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.103183315038419 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -20 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Lower score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 920 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 41 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0445652173913044 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1070 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 63 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0588785046728972 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 150 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 931 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 40 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0429645542427497 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 911 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 94 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.103183315038419 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -20 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 147586 | Data_Quality.xlsx/Completeness |
    | Populated Records | 135139 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.915662732237475 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 87073 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2102 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.975859336418867 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 73 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 62 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.849315068493151 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.8 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | B. Nowak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Rapid Movement of Funds | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Rapid-Movement Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 6 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.6 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 78 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.4 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 46.8 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.1 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-08-17 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-08-17 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | B. Nowak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity B | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-06-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Lower score threshold | direction: Reduce leakage | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.42 Model 42 — Rapid Movement of Funds

| **Model Code**                 | TM-RMF-042                                                                                   |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Rapid-Movement Family                                                                        |
| **Business Problem Solved**    | Funds pass through account with minimal retention.                                           |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                            |
| **Typology Detected**          | Rapid Movement of Funds — flags funds pass through account with minimal retention.           |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity B)                          |
| **Booking Entity / Segment**   | Entity B · SME · APAC                                                                        |
| **Accountable Owner**          | B. Nowak                                                                                     |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 2 - High                                                              |
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