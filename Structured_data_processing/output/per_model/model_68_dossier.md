<model id="Model 68" code="TM-CASH-068">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 62 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 379 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 80 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 52462 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 441 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 52983 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.140589569160998 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.436619718309859 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.212692967409949 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.992827539221438 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 441 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 46 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.104308390022676 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 8.32342449464923 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.46 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.212692967409949 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.104308390022676 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.169339136455039 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 81 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 48 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 33 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.592592592592593 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 193 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 2 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 191 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0103626943005181 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 427 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 48 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.112412177985948 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 418 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 47 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.11244019138756 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -9 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 477 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 25 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0524109014675052 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 59 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 416 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 36 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0865384615384615 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -61 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 427 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 48 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.112412177985948 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 418 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 47 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.11244019138756 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -9 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 477 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 25 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0524109014675052 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 59 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 416 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 36 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0865384615384615 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -61 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 384106 | Data_Quality.xlsx/Completeness |
    | Populated Records | 381402 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.992960276590316 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 175483 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3236 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.981559467298827 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 88 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 75 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.852272727272727 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | H. Woźniak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Velocity Anomaly | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Cash-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 8 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.8 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 65 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.41 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 38.35 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.1 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-11-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-11-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | H. Woźniak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity H | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-08-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Shorten lookback window | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.68 Model 68 — Velocity Anomaly

| **Model Code**                 | TM-CASH-068                                                                            |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                    |
| **Business Problem Solved**    | Transaction frequency exceeds peer-group baseline.                                     |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                      |
| **Typology Detected**          | Velocity Anomaly — flags transaction frequency exceeds peer-group baseline.            |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity H)              |
| **Booking Entity / Segment**   | Entity H · Corporate · High-Risk Jurisdictions                                         |
| **Accountable Owner**          | H. Woźniak                                                                             |
| **Lifecycle / Risk Tier**      | Production · Tier 4 - Low                                                              |
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