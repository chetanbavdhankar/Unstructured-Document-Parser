<model id="Model 40" code="TM-NETWORK-040">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 499 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2061 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 18 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 33015 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2560 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 35593 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.194921875 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.965183752417795 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.324341891452714 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.941241874786179 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2560 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 363 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.141796875 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 71.9242547691962 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.6 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.324341891452714 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.141796875 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.251323884871628 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 48 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 24 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 24 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.5 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 147 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 2 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 145 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0136054421768707 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2342 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 225 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0960717335610589 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2850 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 309 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.108421052631579 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 508 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2075 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 167 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0804819277108434 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -775 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2316 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 138 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0595854922279793 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 241 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Add geography filter | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2342 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 225 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0960717335610589 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2850 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 309 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.108421052631579 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 508 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2075 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 167 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0804819277108434 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -775 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2316 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 138 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0595854922279793 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 241 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 68955 | Data_Quality.xlsx/Completeness |
    | Populated Records | 67940 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.985280255238924 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 85487 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1791 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.979049446114614 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 106 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 93 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.877358490566038 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | J. Kozłowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Layering via Securities | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Network-Linkage Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 5 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.5 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 53 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.67 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 17.49 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.6 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-04-24 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-04-24 | Model_Risk_Governance.xlsx/Lifecycle_Status |
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
    | Tuning_Recommendations | recommendation: Add geography filter | direction: Maintain | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.40 Model 40 — Layering via Securities

| **Model Code**                 | TM-NETWORK-040                                                                         |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Network-Linkage Family                                                                 |
| **Business Problem Solved**    | Round-trip securities trades for obfuscation.                                          |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.         |
| **Typology Detected**          | Layering via Securities — flags round-trip securities trades for obfuscation.          |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity J)          |
| **Booking Entity / Segment**   | Entity J · Correspondent · High-Risk Jurisdictions                                     |
| **Accountable Owner**          | J. Kozłowska                                                                           |
| **Lifecycle / Risk Tier**      | Tuning · Tier 4 - Low                                                                  |
| **Primary Source System**      | CryptoGateway                                                                          |
| **Linked Change Request(s)**   | —                                                                                      |
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