<model id="Model 6" code="TM-BEHAV-006">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 600 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2057 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 115 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 56678 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2657 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 59450 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.225818592397441 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.839160839160839 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.355871886120996 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.964978292329957 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2657 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 378 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.142265713210388 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 44.6930193439865 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.47 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.355871886120996 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.142265713210388 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.270429416956753 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 79 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 72 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 7 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.911392405063291 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 156 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 11 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 145 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0705128205128205 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2163 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 155 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0716597318539066 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3179 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 240 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0754954388172381 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 1016 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2301 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 134 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0582355497609735 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -878 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2587 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 202 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0780827212988017 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 286 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | No change - retain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2163 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 155 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0716597318539066 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 3179 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 240 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0754954388172381 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 1016 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2301 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 134 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0582355497609735 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -878 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2587 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 202 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0780827212988017 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 286 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 233840 | Data_Quality.xlsx/Completeness |
    | Populated Records | 212219 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.907539343140609 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 37654 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1979 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.947442502788548 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 120 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 104 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.866666666666667 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.7 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | KYC-Master | Data_Quality.xlsx/Lineage |
    | Secondary Feed | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | F. Zielińska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Dormant Reactivation | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Behavioural-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 1 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 84 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.89 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 9.24 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.6 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-05-26 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-05-26 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | F. Zielińska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity F | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-06-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 4 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-001 | finding: Threshold not re-tuned within policy window | status: Open | target_date: 2025-Q2 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-021 | finding: Documentation gap in scenario logic | status: Open | target_date: 2025-Q2 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-015 | source_system: KYC-Master | issue_description: Null counterparty IDs in feed | status: Closed | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: No change - retain | direction: Maintain | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.6 Model 6 — Dormant Reactivation

| **Model Code**                 | TM-BEHAV-006                                                                        |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Behavioural-Anomaly Family                                                          |
| **Business Problem Solved**    | Sudden activity on long-dormant accounts.                                           |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.      |
| **Typology Detected**          | Dormant Reactivation — flags sudden activity on long-dormant accounts.              |
| **Data Inputs**                | KYC-Master transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity F)              |
| **Booking Entity / Segment**   | Entity F · Retail · APAC                                                            |
| **Accountable Owner**          | F. Zielińska                                                                        |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 2 - High                                                     |
| **Primary Source System**      | KYC-Master                                                                          |
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