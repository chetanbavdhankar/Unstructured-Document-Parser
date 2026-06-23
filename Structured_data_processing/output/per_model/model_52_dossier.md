<model id="Model 52" code="TM-CASH-052">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 542 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 492 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 81 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 39354 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1034 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 40469 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.524177949709865 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.869983948635634 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.654194327097164 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.987652461978618 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1034 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 319 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.308510638297872 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 25.5504213101386 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.8 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.654194327097164 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.308510638297872 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.515920851577447 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 49 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 43 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 6 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.877551020408163 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 53 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 9 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 44 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.169811320754717 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1150 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 46 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.04 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1053 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 81 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0769230769230769 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -97 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1131 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 88 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0778072502210433 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 78 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 958 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 86 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0897703549060543 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -173 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1150 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 46 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.04 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1053 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 81 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0769230769230769 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -97 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1131 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 88 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0778072502210433 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 78 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 958 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 86 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0897703549060543 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -173 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 458745 | Data_Quality.xlsx/Completeness |
    | Populated Records | 434668 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.947515504256177 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 135227 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 4233 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.968697079725203 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 39 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 38 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.974358974358974 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CardSwitch | Data_Quality.xlsx/Lineage |
    | Secondary Feed | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | B. Nowak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | PEP Activity | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Cash-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 84 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.61 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 32.76 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.5 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-01-12 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-01-12 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | B. Nowak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity B | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-04-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Shorten lookback window | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.52 Model 52 — PEP Activity

| **Model Code**                 | TM-CASH-052                                                                         |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                 |
| **Business Problem Solved**    | Politically exposed person unusual flow.                                            |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.           |
| **Typology Detected**          | PEP Activity — flags politically exposed person unusual flow.                       |
| **Data Inputs**                | CardSwitch transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity B)                 |
| **Booking Entity / Segment**   | Entity B · SME · High-Risk Jurisdictions                                            |
| **Accountable Owner**          | B. Nowak                                                                            |
| **Lifecycle / Risk Tier**      | Tuning · Tier 4 - Low                                                               |
| **Primary Source System**      | CardSwitch                                                                          |
| **Linked Change Request(s)**   | —                                                                                   |
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