<model id="Model 48" code="TM-NETWORK-048">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 187 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1240 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 61 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 55234 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1427 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 56722 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.13104414856342 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.754032258064516 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.223283582089552 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.978042993235825 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1427 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 105 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0735809390329362 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 25.1577871020063 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.81 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.223283582089552 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0735809390329362 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.163402524866906 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 46 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 27 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 19 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.586956521739131 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 176 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 1 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 175 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.00568181818181818 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1227 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.113284433577832 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1591 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 136 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0854808296668762 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 364 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1354 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 145 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.107090103397341 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -237 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1521 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 177 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.116370808678501 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 167 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Add geography filter | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1227 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.113284433577832 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1591 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 136 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0854808296668762 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 364 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1354 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 145 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.107090103397341 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -237 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1521 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 177 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.116370808678501 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 167 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 257820 | Data_Quality.xlsx/Completeness |
    | Populated Records | 232912 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.903389961988985 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 187878 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 6213 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.966930667773768 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 114 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 100 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.87719298245614 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.6 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | KYC-Master | Data_Quality.xlsx/Lineage |
    | Secondary Feed | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | H. Woźniak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Velocity Anomaly | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Network-Linkage Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 9 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.9 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 66 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.88 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 7.92 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.2 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-09-07 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-09-07 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | H. Woźniak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity H | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-12-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 5 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Low | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-021 | source_system: KYC-Master | issue_description: Missing originator country on cross-border wires | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Add geography filter | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.48 Model 48 — Velocity Anomaly

| **Model Code**                 | TM-NETWORK-048                                                                      |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Network-Linkage Family                                                              |
| **Business Problem Solved**    | Transaction frequency exceeds peer-group baseline.                                  |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                   |
| **Typology Detected**          | Velocity Anomaly — flags transaction frequency exceeds peer-group baseline.         |
| **Data Inputs**                | KYC-Master transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity H)           |
| **Booking Entity / Segment**   | Entity H · Corporate · High-Risk Jurisdictions                                      |
| **Accountable Owner**          | H. Woźniak                                                                          |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 4 - Low                                                      |
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