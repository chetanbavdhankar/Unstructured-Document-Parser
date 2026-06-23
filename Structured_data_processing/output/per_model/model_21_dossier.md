<model id="Model 21" code="TM-TBML-021">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 254 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2422 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 62 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 46344 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2676 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 49082 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0949177877428999 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.80379746835443 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.169786096256685 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.950334249272034 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2676 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 155 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0579222720478326 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 54.5210056639909 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.82 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.169786096256685 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0579222720478326 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.125040566573144 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 70 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 56 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 14 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.8 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 128 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 1 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 127 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0078125 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2503 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 219 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0874950059928086 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2886 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 126 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0436590436590437 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 383 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2230 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 112 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0502242152466368 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -656 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2579 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 190 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0736719658782474 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 349 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Tighten min-amount floor | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2503 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 219 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0874950059928086 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2886 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 126 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0436590436590437 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 383 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2230 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 112 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0502242152466368 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -656 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2579 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 190 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0736719658782474 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 349 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 395178 | Data_Quality.xlsx/Completeness |
    | Populated Records | 369773 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.935712514360617 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 169793 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3456 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.97964580400841 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 115 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 103 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.895652173913044 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | A. Kowalski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Structuring | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Trade-Based Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 4 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.4 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 73 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.76 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 17.52 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.8 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-07-15 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-07-15 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | A. Kowalski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity A | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-09-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-004 | finding: Population drift detected | status: In Remediation | target_date: 2025-Q1 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-024 | finding: Elevated false-positive rate vs peer group | status: In Remediation | target_date: 2025-Q1 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Tighten min-amount floor | direction: Reduce FP | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.21 Model 21 — Structuring

| **Model Code**                 | TM-TBML-021                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Trade-Based Family                                                                           |
| **Business Problem Solved**    | Multiple sub-threshold deposits to evade CTR reporting.                                      |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                            |
| **Typology Detected**          | Structuring — flags multiple sub-threshold deposits to evade CTR reporting.                  |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity A)                       |
| **Booking Entity / Segment**   | Entity A · Retail · EMEA                                                                     |
| **Accountable Owner**          | A. Kowalski                                                                                  |
| **Lifecycle / Risk Tier**      | Production · Tier 1 - Critical                                                               |
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