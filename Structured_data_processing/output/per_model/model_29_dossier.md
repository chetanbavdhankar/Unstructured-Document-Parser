<model id="Model 29" code="TM-TBML-029">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 578 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1500 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 108 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 48695 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2078 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 50881 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.278152069297401 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.842565597667639 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.418234442836469 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.970116545472657 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2078 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 418 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.201154956689124 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 40.8403922878874 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.82 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.418234442836469 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.201154956689124 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.331402648377531 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 36 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 27 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 9 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.75 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 151 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 6 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 145 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0397350993377483 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1730 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 127 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0734104046242775 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2016 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 97 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0481150793650794 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 286 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1666 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 182 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.109243697478992 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -350 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1735 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 102 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0587896253602305 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 69 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Tighten min-amount floor | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1730 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 127 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0734104046242775 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2016 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 97 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0481150793650794 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 286 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1666 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 182 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.109243697478992 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -350 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1735 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 102 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0587896253602305 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 69 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 152207 | Data_Quality.xlsx/Completeness |
    | Populated Records | 141089 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.926954739269547 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 78625 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3670 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.953322734499205 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 37 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 35 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.945945945945946 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.3 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | I. Dąbrowski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Threshold Avoidance | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Trade-Based Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Private Banking | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 6 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.6 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 91 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.73 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 24.57 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.4 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-06-19 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-06-19 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | I. Dąbrowski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity I | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-05-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 3 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-004 | source_system: CoreBanking-T24 | issue_description: Currency code mismatch | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Tighten min-amount floor | direction: Reduce FP | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.29 Model 29 — Threshold Avoidance

| **Model Code**                 | TM-TBML-029                                                                              |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Trade-Based Family                                                                       |
| **Business Problem Solved**    | Transactions clustered just below reporting limits.                                      |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                        |
| **Typology Detected**          | Threshold Avoidance — flags transactions clustered just below reporting limits.          |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity I)          |
| **Booking Entity / Segment**   | Entity I · Private Banking · EMEA                                                        |
| **Accountable Owner**          | I. Dąbrowski                                                                             |
| **Lifecycle / Risk Tier**      | Validation · Tier 1 - Critical                                                           |
| **Primary Source System**      | CoreBanking-T24                                                                          |
| **Linked Change Request(s)**   | —                                                                                        |
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