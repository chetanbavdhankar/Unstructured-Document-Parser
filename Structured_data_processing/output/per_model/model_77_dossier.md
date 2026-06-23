<model id="Model 77" code="TM-TBML-077">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 80 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 368 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 63 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 67200 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 448 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 67711 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.178571428571429 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.55944055944056 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.27072758037225 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.994553634856737 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 448 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 34 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0758928571428571 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 6.61635480202626 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.46 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.27072758037225 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0758928571428571 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.192793691080493 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 69 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 18 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 51 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.260869565217391 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 140 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 12 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 128 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0857142857142857 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 513 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 28 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0545808966861598 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 527 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 58 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.110056925996205 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 14 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 408 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 17 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0416666666666667 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -119 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 397 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 26 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0654911838790932 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -11 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Tighten min-amount floor | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 513 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 28 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0545808966861598 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 527 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 58 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.110056925996205 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 14 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 408 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 17 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0416666666666667 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -119 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 397 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 26 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0654911838790932 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -11 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 248798 | Data_Quality.xlsx/Completeness |
    | Populated Records | 241807 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.971900899524916 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 110398 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 994 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.990996213699524 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Green | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 104 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 98 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.942307692307692 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.6 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | G. Szymański | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Smurfing Network | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Trade-Based Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 10 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 75 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.57 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 32.25 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.1 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-03-18 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-03-18 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | G. Szymański | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity G | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-05-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 5 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Tighten min-amount floor | direction: Reduce FP | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.77 Model 77 — Smurfing Network

| **Model Code**                 | TM-TBML-077                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Trade-Based Family                                                                           |
| **Business Problem Solved**    | Coordinated small transactions across linked parties.                                        |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                            |
| **Typology Detected**          | Smurfing Network — flags coordinated small transactions across linked parties.               |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity G)                          |
| **Booking Entity / Segment**   | Entity G · SME · EMEA                                                                        |
| **Accountable Owner**          | G. Szymański                                                                                 |
| **Lifecycle / Risk Tier**      | Validation · Tier 1 - Critical                                                               |
| **Primary Source System**      | Sanctions-Screening                                                                          |
| **Linked Change Request(s)**   | —                                                                                            |
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