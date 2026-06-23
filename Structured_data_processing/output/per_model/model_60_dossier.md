<model id="Model 60" code="TM-CASH-060">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 480 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2614 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 32 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 73999 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 3094 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 77125 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.15513897866839 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.9375 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.266222961730449 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.965880464150993 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 3094 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 289 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0934065934065934 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 40.1166936790924 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.84 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.266222961730449 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0934065934065934 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.197096414400907 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 59 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 59 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 0 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 1 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 124 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 2 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 122 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0161290322580645 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2516 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 285 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.113275039745628 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3311 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 183 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0552703110842646 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 795 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2902 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 118 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0406616126809097 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -409 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3014 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 348 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.115461181154612 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 112 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2516 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 285 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.113275039745628 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 3311 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 183 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0552703110842646 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 795 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2902 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 118 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0406616126809097 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -409 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 3014 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 348 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.115461181154612 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 112 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 183174 | Data_Quality.xlsx/Completeness |
    | Populated Records | 181282 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.989671023180146 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 122441 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 708 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.994217623181777 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Green | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 79 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 68 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.860759493670886 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | J. Kozłowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Layering via Securities | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Cash-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
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
    | Inherent Risk Score | 97 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.7 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 29.1 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.8 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-05-20 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-05-20 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | J. Kozłowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity J | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-12-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-037 | source_system: TradeFinance-CTS | issue_description: Duplicate transaction records | status: In Progress | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Shorten lookback window | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.60 Model 60 — Layering via Securities

| **Model Code**                 | TM-CASH-060                                                                               |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                       |
| **Business Problem Solved**    | Round-trip securities trades for obfuscation.                                             |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                         |
| **Typology Detected**          | Layering via Securities — flags round-trip securities trades for obfuscation.             |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity J)             |
| **Booking Entity / Segment**   | Entity J · Correspondent · High-Risk Jurisdictions                                        |
| **Accountable Owner**          | J. Kozłowska                                                                              |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 4 - Low                                                            |
| **Primary Source System**      | TradeFinance-CTS                                                                          |
| **Linked Change Request(s)**   | —                                                                                         |
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