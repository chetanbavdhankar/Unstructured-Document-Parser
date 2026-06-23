<model id="Model 11" code="TM-GEO-011">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 457 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 717 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 14 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 81127 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1174 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 82315 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.389267461669506 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.970276008492569 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.555623100303951 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.991239431112849 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1174 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 267 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.227427597955707 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 14.2622851242179 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.79 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.555623100303951 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.227427597955707 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.424344899364654 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 108 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 80 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 28 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.740740740740741 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 186 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 3 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 183 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0161290322580645 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1144 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 74 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0646853146853147 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1373 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 127 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0924981791697014 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 229 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1026 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 114 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.111111111111111 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -347 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1254 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 51 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0406698564593301 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 228 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Extend lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1144 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 74 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0646853146853147 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1373 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 127 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0924981791697014 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 229 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1026 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 114 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.111111111111111 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -347 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1254 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 51 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0406698564593301 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 228 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 328644 | Data_Quality.xlsx/Completeness |
    | Populated Records | 297656 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.905709521549154 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 66102 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 784 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.988139541920063 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 108 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 106 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.981481481481482 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3.8 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | A. Kowalski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Mule Account Behaviour | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Geographic-Risk Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 92 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.91 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 8.28 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.2 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-07-04 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-07-04 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | A. Kowalski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity A | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-11-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-002 | finding: Insufficient BTL coverage | status: Open | target_date: 2025-Q3 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-022 | finding: Population drift detected | status: In Remediation | target_date: 2025-Q3 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-030 | source_system: TradeFinance-CTS | issue_description: Duplicate transaction records | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Extend lookback window | direction: Reduce leakage | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.11 Model 11 — Mule Account Behaviour

| **Model Code**                 | TM-GEO-011                                                                                |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Geographic-Risk Family                                                                    |
| **Business Problem Solved**    | Profile consistent with third-party mule activity.                                        |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.            |
| **Typology Detected**          | Mule Account Behaviour — flags profile consistent with third-party mule activity.         |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity A)                    |
| **Booking Entity / Segment**   | Entity A · Retail · Americas                                                              |
| **Accountable Owner**          | A. Kowalski                                                                               |
| **Lifecycle / Risk Tier**      | Validation · Tier 3 - Medium                                                              |
| **Primary Source System**      | TradeFinance-CTS                                                                          |
| **Linked Change Request(s)**   | —                                                                                         |
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