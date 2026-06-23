<model id="Model 16" code="TM-NETWORK-016">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 157 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 904 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 67 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 57735 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1061 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 58863 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.147973609802074 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.700892857142857 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.244357976653697 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.984583638875151 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1061 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 79 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0744580584354383 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 18.0249052885514 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.6 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.244357976653697 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0744580584354383 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.176398009366393 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 114 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 27 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 87 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.236842105263158 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 117 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 11 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 106 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.094017094017094 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1085 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 76 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0700460829493088 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1086 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 99 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0911602209944751 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 1 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 987 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 66 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0668693009118541 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -99 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 898 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 74 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0824053452115813 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -89 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Add geography filter | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1085 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 76 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0700460829493088 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1086 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 99 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0911602209944751 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 1 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 987 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 66 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0668693009118541 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -99 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 898 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 74 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0824053452115813 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -89 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 89678 | Data_Quality.xlsx/Completeness |
    | Populated Records | 82935 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.924808760231049 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 86474 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 4589 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.946932025811227 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 20 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 18 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.9 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3.5 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | F. Zielińska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Shell Company Flow | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Network-Linkage Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 6 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.6 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 72 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.63 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 26.64 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.2 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-10-07 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-10-07 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | F. Zielińska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity F | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-04-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-003 | finding: Documentation gap in scenario logic | status: Open | target_date: 2025-Q4 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-023 | finding: Calibration outside tolerance | status: Open | target_date: 2025-Q4 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Add geography filter | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.16 Model 16 — Shell Company Flow

| **Model Code**                 | TM-NETWORK-016                                                                             |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Network-Linkage Family                                                                     |
| **Business Problem Solved**    | Flows through entities with no economic substance.                                         |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                  |
| **Typology Detected**          | Shell Company Flow — flags flows through entities with no economic substance.              |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity F)                     |
| **Booking Entity / Segment**   | Entity F · Retail · High-Risk Jurisdictions                                                |
| **Accountable Owner**          | F. Zielińska                                                                               |
| **Lifecycle / Risk Tier**      | Tuning · Tier 4 - Low                                                                      |
| **Primary Source System**      | PaymentsHub-SWIFT                                                                          |
| **Linked Change Request(s)**   | —                                                                                          |
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