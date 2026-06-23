<model id="Model 69" code="TM-TBML-069">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 477 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1656 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 40 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 75477 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2133 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 77650 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.223628691983122 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.922630560928433 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.36 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.978530590019836 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2133 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 213 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.09985935302391 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 27.4694140373471 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.52 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.36 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.09985935302391 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.255943741209564 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 81 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 54 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 27 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.666666666666667 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 140 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 10 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 130 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0714285714285714 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2281 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 266 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.116615519508987 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2489 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 277 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.1112896745681 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 208 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2504 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 153 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0611022364217252 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 15 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1849 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 196 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.106003244997296 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -655 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Tighten min-amount floor | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2281 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 266 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.116615519508987 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2489 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 277 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.1112896745681 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 208 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2504 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 153 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0611022364217252 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 15 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1849 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 196 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.106003244997296 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -655 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 474833 | Data_Quality.xlsx/Completeness |
    | Populated Records | 429852 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.905269852769289 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 199770 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3105 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.984457125694549 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 113 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 107 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.946902654867257 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.8 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | KYC-Master | Data_Quality.xlsx/Lineage |
    | Secondary Feed | Sanctions-Screening | Data_Quality.xlsx/Lineage |
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
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 8 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.8 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 91 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.95 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 4.55 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.8 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-08-06 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-08-06 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | I. Dąbrowski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity I | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-09-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 5 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-024 | source_system: KYC-Master | issue_description: Late feed beyond SLA cut-off | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Tighten min-amount floor | direction: Reduce FP | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.69 Model 69 — Threshold Avoidance

| **Model Code**                 | TM-TBML-069                                                                         |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Trade-Based Family                                                                  |
| **Business Problem Solved**    | Transactions clustered just below reporting limits.                                 |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                   |
| **Typology Detected**          | Threshold Avoidance — flags transactions clustered just below reporting limits.     |
| **Data Inputs**                | KYC-Master transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity I)     |
| **Booking Entity / Segment**   | Entity I · Private Banking · EMEA                                                   |
| **Accountable Owner**          | I. Dąbrowski                                                                        |
| **Lifecycle / Risk Tier**      | Production · Tier 1 - Critical                                                      |
| **Primary Source System**      | KYC-Master                                                                          |
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