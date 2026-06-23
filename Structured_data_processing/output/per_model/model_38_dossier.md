<model id="Model 38" code="TM-BEHAV-038">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 433 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 356 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 86 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 41393 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 789 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 42268 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.548795944233207 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.834296724470135 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.662079510703364 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.991472849649093 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 789 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 216 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.273764258555133 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 18.6666035771742 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.75 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.662079510703364 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.273764258555133 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.506753409844072 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 83 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 15 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 68 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.180722891566265 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Review | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 120 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 7 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 113 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0583333333333333 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 876 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 44 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0502283105022831 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 713 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 34 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0476858345021038 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -163 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 632 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 45 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0712025316455696 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -81 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 818 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 71 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0867970660146699 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 186 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | No change - retain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 876 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 44 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0502283105022831 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 713 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 34 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0476858345021038 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -163 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 632 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 45 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0712025316455696 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -81 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 818 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 71 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0867970660146699 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 186 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 439746 | Data_Quality.xlsx/Completeness |
    | Populated Records | 409731 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.931744688979547 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 78640 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2550 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.967573753814852 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 32 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 28 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.875 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CardSwitch | Data_Quality.xlsx/Lineage |
    | Secondary Feed | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | H. Woźniak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Wire Stripping | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Behavioural-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 9 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.9 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 64 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.54 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 29.44 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.0 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-03-23 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-03-23 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | H. Woźniak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity H | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-02-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: No change - retain | direction: Maintain | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.38 Model 38 — Wire Stripping

| **Model Code**                 | TM-BEHAV-038                                                                        |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Behavioural-Anomaly Family                                                          |
| **Business Problem Solved**    | Removal of originator data in cross-border wires.                                   |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.      |
| **Typology Detected**          | Wire Stripping — flags removal of originator data in cross-border wires.            |
| **Data Inputs**                | CardSwitch transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity H)           |
| **Booking Entity / Segment**   | Entity H · Corporate · APAC                                                         |
| **Accountable Owner**          | H. Woźniak                                                                          |
| **Lifecycle / Risk Tier**      | Production · Tier 2 - High                                                          |
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