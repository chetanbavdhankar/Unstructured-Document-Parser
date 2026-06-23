<model id="Model 59" code="TM-GEO-059">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 336 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2343 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 36 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 60014 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2679 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 62729 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.12541993281075 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.903225806451613 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.220255653883972 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.962426030758375 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2679 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 186 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0694288913773796 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 42.7075196480097 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.6 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.220255653883972 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0694288913773796 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.159924948881335 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 70 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 68 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 2 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.971428571428571 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 108 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 8 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 100 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0740740740740741 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2640 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 201 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0761363636363636 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2699 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 236 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0874397925157466 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 59 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2464 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 186 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.075487012987013 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -235 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2640 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 126 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0477272727272727 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 176 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Extend lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2640 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 201 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0761363636363636 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2699 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 236 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0874397925157466 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 59 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2464 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 186 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.075487012987013 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -235 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2640 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 126 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0477272727272727 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 176 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 170133 | Data_Quality.xlsx/Completeness |
    | Populated Records | 166982 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.981479195688079 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 52095 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1253 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.975947787695556 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 30 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 27 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.9 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.2 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CardSwitch | Data_Quality.xlsx/Lineage |
    | Secondary Feed | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
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
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 6 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.6 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 75 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.76 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 18 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.5 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-12-14 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-12-14 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | I. Dąbrowski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity I | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-11-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 4 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Extend lookback window | direction: Reduce leakage | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.59 Model 59 — ATM Cycling

| **Model Code**                 | TM-GEO-059                                                                          |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Geographic-Risk Family                                                              |
| **Business Problem Solved**    | Geographically dispersed rapid ATM withdrawals.                                     |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.           |
| **Typology Detected**          | ATM Cycling — flags geographically dispersed rapid ATM withdrawals.                 |
| **Data Inputs**                | CardSwitch transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity I)     |
| **Booking Entity / Segment**   | Entity I · Private Banking · Americas                                               |
| **Accountable Owner**          | I. Dąbrowski                                                                        |
| **Lifecycle / Risk Tier**      | Validation · Tier 3 - Medium                                                        |
| **Primary Source System**      | CardSwitch                                                                          |
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