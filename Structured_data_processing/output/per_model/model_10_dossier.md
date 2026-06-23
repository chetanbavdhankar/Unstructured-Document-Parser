<model id="Model 10" code="TM-RMF-010">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 347 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1904 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 51 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 68934 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2251 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 71236 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.154153709462461 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.871859296482412 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.261985654964137 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.973121770800983 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2251 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 170 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.075521990226566 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 31.5991914200685 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.68 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.261985654964137 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.075521990226566 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.187400189069109 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 55 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 31 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 24 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.563636363636364 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 78 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 8 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 70 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.102564102564103 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2306 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 136 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0589765828274068 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2092 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 178 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0850860420650096 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -214 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2247 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 107 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0476190476190476 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 155 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2366 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 273 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.115384615384615 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 119 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Lower score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2306 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 136 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0589765828274068 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2092 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 178 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0850860420650096 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -214 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2247 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 107 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0476190476190476 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 155 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2366 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 273 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.115384615384615 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 119 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 405464 | Data_Quality.xlsx/Completeness |
    | Populated Records | 400476 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.987698044709271 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 120575 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 5089 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.957793904208999 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 71 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 66 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.929577464788732 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.9 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CardSwitch | Data_Quality.xlsx/Lineage |
    | Secondary Feed | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | J. Kozłowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Funnel Account | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Rapid-Movement Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 8 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.8 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 89 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.66 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 30.26 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.5 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-10-22 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-10-22 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | J. Kozłowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity J | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-10-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Lower score threshold | direction: Reduce leakage | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.10 Model 10 — Funnel Account

| **Model Code**                 | TM-RMF-010                                                                          |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Rapid-Movement Family                                                               |
| **Business Problem Solved**    | Many-to-one inflow with single rapid outflow.                                       |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.      |
| **Typology Detected**          | Funnel Account — flags many-to-one inflow with single rapid outflow.                |
| **Data Inputs**                | CardSwitch transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity J)       |
| **Booking Entity / Segment**   | Entity J · Correspondent · APAC                                                     |
| **Accountable Owner**          | J. Kozłowska                                                                        |
| **Lifecycle / Risk Tier**      | Tuning · Tier 2 - High                                                              |
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