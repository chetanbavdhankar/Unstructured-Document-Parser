<model id="Model 26" code="TM-RMF-026">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 476 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1019 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 104 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 51192 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1495 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 52791 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.318394648829431 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.820689655172414 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.458795180722892 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.98048303997242 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1495 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 225 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.150501672240803 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 28.3192210793506 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.67 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.458795180722892 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.150501672240803 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.335477777330056 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 40 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 34 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 6 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.85 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 200 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 9 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 191 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.045 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1272 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 80 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0628930817610063 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1485 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 159 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.107070707070707 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 213 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1711 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 137 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0800701344243133 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 226 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1691 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 101 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0597279716144293 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -20 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Lower score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1272 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 80 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0628930817610063 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1485 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 159 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.107070707070707 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 213 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1711 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 137 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0800701344243133 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 226 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1691 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 101 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0597279716144293 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -20 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 473250 | Data_Quality.xlsx/Completeness |
    | Populated Records | 467471 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.987788695192816 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 20834 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 405 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.980560622060094 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 101 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 94 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.930693069306931 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.1 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | F. Zielińska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Dormant Reactivation | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Rapid-Movement Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 9 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.9 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 91 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.51 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 44.59 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.3 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-08-14 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-08-14 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | F. Zielińska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity F | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-02-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 5 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-005 | finding: Calibration outside tolerance | status: Open | target_date: 2025-Q2 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-025 | finding: Threshold not re-tuned within policy window | status: Closed | target_date: 2025-Q2 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Lower score threshold | direction: Reduce leakage | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.26 Model 26 — Dormant Reactivation

| **Model Code**                 | TM-RMF-026                                                                             |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Rapid-Movement Family                                                                  |
| **Business Problem Solved**    | Sudden activity on long-dormant accounts.                                              |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.              |
| **Typology Detected**          | Dormant Reactivation — flags sudden activity on long-dormant accounts.                 |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity F)                 |
| **Booking Entity / Segment**   | Entity F · Retail · APAC                                                               |
| **Accountable Owner**          | F. Zielińska                                                                           |
| **Lifecycle / Risk Tier**      | Production · Tier 2 - High                                                             |
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