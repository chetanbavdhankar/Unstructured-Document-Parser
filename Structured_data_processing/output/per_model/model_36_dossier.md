<model id="Model 36" code="TM-CASH-036">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 254 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1168 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 20 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 27311 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1422 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 28753 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.178621659634318 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.927007299270073 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.299528301886792 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.958987323993118 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1422 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 140 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0984528832630098 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 49.4557089694988 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.67 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.299528301886792 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0984528832630098 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.219098134437279 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 51 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 35 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 16 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.686274509803922 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 95 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 5 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 90 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0526315789473684 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1449 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 61 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0420979986197378 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1654 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 122 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0737605804111245 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 205 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1499 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 64 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0426951300867245 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -155 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1495 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 116 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0775919732441472 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -4 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1449 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 61 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0420979986197378 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1654 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 122 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0737605804111245 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 205 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1499 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 64 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0426951300867245 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -155 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1495 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 116 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0775919732441472 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -4 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 355378 | Data_Quality.xlsx/Completeness |
    | Populated Records | 338062 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.95127441766232 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 197844 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 7192 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.963648126806979 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 44 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 38 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.863636363636364 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.8 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | F. Zielińska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Shell Company Flow | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Cash-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 4 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.4 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 93 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.87 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 12.09 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.8 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-03-15 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-03-15 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | F. Zielińska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity F | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-12-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 3 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-007 | finding: Threshold not re-tuned within policy window | status: Closed | target_date: 2025-Q4 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-027 | finding: Documentation gap in scenario logic | status: Open | target_date: 2025-Q4 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-005 | source_system: CoreBanking-T24 | issue_description: Truncated narrative field | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Shorten lookback window | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.36 Model 36 — Shell Company Flow

| **Model Code**                 | TM-CASH-036                                                                              |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                      |
| **Business Problem Solved**    | Flows through entities with no economic substance.                                       |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                |
| **Typology Detected**          | Shell Company Flow — flags flows through entities with no economic substance.            |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity F)                   |
| **Booking Entity / Segment**   | Entity F · Retail · High-Risk Jurisdictions                                              |
| **Accountable Owner**          | F. Zielińska                                                                             |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 4 - Low                                                           |
| **Primary Source System**      | CoreBanking-T24                                                                          |
| **Linked Change Request(s)**   | —                                                                                        |
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