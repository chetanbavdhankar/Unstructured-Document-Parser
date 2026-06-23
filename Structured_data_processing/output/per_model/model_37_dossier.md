<model id="Model 37" code="TM-TBML-037">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 376 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1778 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 66 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 37379 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2154 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 39599 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.17455896007428 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.850678733031674 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.289676425269646 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.954593048497076 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2154 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 246 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.114206128133705 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 54.3953130129549 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.55 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.289676425269646 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.114206128133705 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.219488306415269 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 117 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 109 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 8 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.931623931623932 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 114 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 3 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 111 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0263157894736842 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2092 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 174 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0831739961759082 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2050 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 179 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0873170731707317 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -42 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2440 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 171 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0700819672131148 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 390 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1813 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 102 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0562603419746277 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -627 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Tighten min-amount floor | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2092 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 174 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0831739961759082 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2050 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 179 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0873170731707317 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -42 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2440 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 171 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0700819672131148 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 390 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1813 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 102 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0562603419746277 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -627 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 324171 | Data_Quality.xlsx/Completeness |
    | Populated Records | 321164 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.990724031452536 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 193745 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 4629 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.97610777052311 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 87 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 79 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.908045977011494 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | G. Szymański | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Smurfing Network | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Trade-Based Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 87 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.52 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 41.76 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.1 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-10-19 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-10-19 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | G. Szymański | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity G | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-01-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Tighten min-amount floor | direction: Reduce FP | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.37 Model 37 — Smurfing Network

| **Model Code**                 | TM-TBML-037                                                                                |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Trade-Based Family                                                                         |
| **Business Problem Solved**    | Coordinated small transactions across linked parties.                                      |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                          |
| **Typology Detected**          | Smurfing Network — flags coordinated small transactions across linked parties.             |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity G)                        |
| **Booking Entity / Segment**   | Entity G · SME · EMEA                                                                      |
| **Accountable Owner**          | G. Szymański                                                                               |
| **Lifecycle / Risk Tier**      | Production · Tier 1 - Critical                                                             |
| **Primary Source System**      | PaymentsHub-SWIFT                                                                          |
| **Linked Change Request(s)**   | —                                                                                          |
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