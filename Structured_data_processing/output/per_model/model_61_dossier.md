<model id="Model 61" code="TM-TBML-061">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 553 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2635 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 98 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 83844 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 3188 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 87130 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.173462986198243 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.849462365591398 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.288095858296431 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.96953017495577 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 3188 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 213 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0668130489335006 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 36.5890049351544 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.83 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.288095858296431 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0668130489335006 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.199582734551259 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 62 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 12 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 50 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.193548387096774 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Review | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 162 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 0 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 162 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3606 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 354 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0981697171381032 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2711 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 278 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.102545186278126 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -895 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3740 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 313 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0836898395721925 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 1029 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3763 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 430 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.114270528833378 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 23 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Tighten min-amount floor | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 3606 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 354 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0981697171381032 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2711 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 278 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.102545186278126 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -895 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 3740 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 313 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0836898395721925 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 1029 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 3763 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 430 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.114270528833378 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 23 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 428365 | Data_Quality.xlsx/Completeness |
    | Populated Records | 391371 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.913639069485135 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 141020 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 5026 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.964359665295703 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 115 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 107 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.930434782608696 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.6 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | A. Kowalski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Structuring | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Trade-Based Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 5 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.5 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 78 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.69 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 24.18 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-08-14 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-08-14 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | A. Kowalski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity A | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-01-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-012 | finding: Elevated false-positive rate vs peer group | status: Open | target_date: 2025-Q1 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-032 | finding: Insufficient BTL coverage | status: Open | target_date: 2025-Q1 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Tighten min-amount floor | direction: Reduce FP | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.61 Model 61 — Structuring

| **Model Code**                 | TM-TBML-061                                                                            |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Trade-Based Family                                                                     |
| **Business Problem Solved**    | Multiple sub-threshold deposits to evade CTR reporting.                                |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.              |
| **Typology Detected**          | Structuring — flags multiple sub-threshold deposits to evade CTR reporting.            |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity A)                 |
| **Booking Entity / Segment**   | Entity A · Retail · EMEA                                                               |
| **Accountable Owner**          | A. Kowalski                                                                            |
| **Lifecycle / Risk Tier**      | Production · Tier 1 - Critical                                                         |
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