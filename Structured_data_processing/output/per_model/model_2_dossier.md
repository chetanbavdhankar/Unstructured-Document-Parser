<model id="Model 2" code="TM-RMF-002">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 225 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 842 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 9 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 86223 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1067 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 87299 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.21087160262418 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.961538461538462 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.345887778631822 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.990329064492046 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1067 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 116 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.108716026241799 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 12.2223622263714 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.78 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.345887778631822 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.108716026241799 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.251019077675813 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 55 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 43 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 12 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.781818181818182 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 140 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 11 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 129 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0785714285714286 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1197 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 140 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.116959064327485 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1014 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 62 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0611439842209073 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -183 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 950 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 49 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0515789473684211 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -64 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1141 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 115 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.100788781770377 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 191 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Lower score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1197 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 140 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.116959064327485 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1014 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 62 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0611439842209073 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -183 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 950 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 49 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0515789473684211 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -64 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1141 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 115 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.100788781770377 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 191 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 121213 | Data_Quality.xlsx/Completeness |
    | Populated Records | 118101 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.974326186135151 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 162156 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 5698 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.964860998051259 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 25 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 21 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.84 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | B. Nowak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Rapid Movement of Funds | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Rapid-Movement Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 10 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 53 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.65 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 18.55 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-04-09 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-04-09 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | B. Nowak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity B | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-02-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 4 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Lower score threshold | direction: Reduce leakage | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.2 Model 2 — Rapid Movement of Funds

| **Model Code**                 | TM-RMF-002                                                                                 |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Rapid-Movement Family                                                                      |
| **Business Problem Solved**    | Funds pass through account with minimal retention.                                         |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                  |
| **Typology Detected**          | Rapid Movement of Funds — flags funds pass through account with minimal retention.         |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity B)                        |
| **Booking Entity / Segment**   | Entity B · SME · APAC                                                                      |
| **Accountable Owner**          | B. Nowak                                                                                   |
| **Lifecycle / Risk Tier**      | Production · Tier 2 - High                                                                 |
| **Primary Source System**      | PaymentsHub-SWIFT                                                                          |
| **Linked Change Request(s)**   | —                                                                                          |
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