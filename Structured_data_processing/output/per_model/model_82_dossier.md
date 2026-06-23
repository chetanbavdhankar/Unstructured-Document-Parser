<model id="Model 82" code="TM-RMF-082">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 271 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2163 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 91 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 50474 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2434 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 52999 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.111339359079704 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.748618784530387 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.193848354792561 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.958907232555047 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2434 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 191 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0784716516023007 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 45.9253948187702 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.61 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.193848354792561 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0784716516023007 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.147697673516457 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 67 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 33 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 34 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.492537313432836 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 128 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 2 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 126 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.015625 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2601 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 113 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0434448289119569 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2484 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 248 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0998389694041868 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -117 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2176 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 168 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0772058823529412 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -308 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2209 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 186 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0842009959257583 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 33 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Lower score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2601 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 113 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0434448289119569 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2484 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 248 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0998389694041868 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -117 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2176 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 168 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0772058823529412 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -308 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2209 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 186 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0842009959257583 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 33 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 124050 | Data_Quality.xlsx/Completeness |
    | Populated Records | 121101 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.976227327690447 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 186702 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3291 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.982372979400328 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 112 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 101 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.901785714285714 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.3 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
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
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 1 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 83 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.67 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 27.39 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.0 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-05-16 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-05-16 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | B. Nowak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity B | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-10-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Lower score threshold | direction: Reduce leakage | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.82 Model 82 — Rapid Movement of Funds

| **Model Code**                 | TM-RMF-082                                                                             |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Rapid-Movement Family                                                                  |
| **Business Problem Solved**    | Funds pass through account with minimal retention.                                     |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.              |
| **Typology Detected**          | Rapid Movement of Funds — flags funds pass through account with minimal retention.     |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity B)                    |
| **Booking Entity / Segment**   | Entity B · SME · APAC                                                                  |
| **Accountable Owner**          | B. Nowak                                                                               |
| **Lifecycle / Risk Tier**      | Tuning · Tier 2 - High                                                                 |
| **Primary Source System**      | CryptoGateway                                                                          |
| **Linked Change Request(s)**   | —                                                                                      |
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