<model id="Model 100" code="TM-CASH-100">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 128 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 268 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 48 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 46980 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 396 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 47424 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.323232323232323 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.727272727272727 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.447552447552448 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.994327802235015 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 396 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 71 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.179292929292929 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 8.3502024291498 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.7 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.447552447552448 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.179292929292929 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.34024864024864 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 55 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 27 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 28 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.490909090909091 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 192 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 4 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 188 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0208333333333333 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 369 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 29 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0785907859078591 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 353 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 28 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0793201133144476 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -16 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 329 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 23 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0699088145896657 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -24 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 397 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 30 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0755667506297229 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 68 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 369 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 29 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0785907859078591 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 353 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 28 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0793201133144476 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -16 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 329 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 23 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0699088145896657 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -24 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 397 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 30 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0755667506297229 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 68 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 450187 | Data_Quality.xlsx/Completeness |
    | Populated Records | 427257 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.949065610512965 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 136389 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 4400 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.967739333817243 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 21 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 20 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.952380952380952 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.2 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | J. Kozłowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Layering via Securities | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Cash-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 9 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.9 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 69 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.87 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 8.97 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.7 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-09-26 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-09-26 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | J. Kozłowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity J | Model_Risk_Governance.xlsx/Ownership |
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
### 3.100 Model 100 — Layering via Securities

| **Model Code**                 | TM-CASH-100                                                                                |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                        |
| **Business Problem Solved**    | Round-trip securities trades for obfuscation.                                              |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                  |
| **Typology Detected**          | Layering via Securities — flags round-trip securities trades for obfuscation.              |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity J)              |
| **Booking Entity / Segment**   | Entity J · Correspondent · High-Risk Jurisdictions                                         |
| **Accountable Owner**          | J. Kozłowska                                                                               |
| **Lifecycle / Risk Tier**      | Tuning · Tier 4 - Low                                                                      |
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