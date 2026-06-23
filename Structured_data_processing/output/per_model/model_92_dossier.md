<model id="Model 92" code="TM-CASH-092">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 460 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1756 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 58 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 64933 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2216 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 67207 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.207581227436823 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.888030888030888 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.336503291880029 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.973668820944983 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2216 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 352 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.15884476534296 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 32.9727558141265 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.5 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.336503291880029 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.15884476534296 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.265439881265202 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 114 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 110 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 4 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.964912280701754 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 92 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 12 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 80 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.130434782608696 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1926 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 219 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.113707165109034 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2042 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 86 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0421155729676788 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 116 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2179 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 90 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0413033501606241 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 137 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2095 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 212 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.101193317422434 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -84 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1926 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 219 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.113707165109034 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2042 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 86 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0421155729676788 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 116 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2179 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 90 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0413033501606241 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 137 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2095 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 212 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.101193317422434 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -84 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 207926 | Data_Quality.xlsx/Completeness |
    | Populated Records | 197627 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.95046795494551 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 37239 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 891 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.97607347136067 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 24 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 20 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.833333333333333 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5.5 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | B. Nowak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | PEP Activity | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Cash-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 2 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.2 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 83 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.69 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 25.73 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.4 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-08-04 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-08-04 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | B. Nowak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity B | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-08-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 4 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-013 | source_system: CoreBanking-T24 | issue_description: Stale reference data | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Shorten lookback window | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.92 Model 92 — PEP Activity

| **Model Code**                 | TM-CASH-092                                                                              |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                      |
| **Business Problem Solved**    | Politically exposed person unusual flow.                                                 |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                        |
| **Typology Detected**          | PEP Activity — flags politically exposed person unusual flow.                            |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity B)                      |
| **Booking Entity / Segment**   | Entity B · SME · High-Risk Jurisdictions                                                 |
| **Accountable Owner**          | B. Nowak                                                                                 |
| **Lifecycle / Risk Tier**      | Production · Tier 4 - Low                                                                |
| **Primary Source System**      | CoreBanking-T24                                                                          |
| **Linked Change Request(s)**   | —                                                                                        |
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