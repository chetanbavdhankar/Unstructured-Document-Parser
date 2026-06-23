<model id="Model 8" code="TM-NETWORK-008">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 485 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1092 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 72 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 42359 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1577 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 44008 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.307545973367153 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.870736086175943 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.454545454545455 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.974868242387977 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1577 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 387 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.245402663284718 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 35.8343937465915 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.78 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.454545454545455 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.245402663284718 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.37088833804116 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 98 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 16 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 82 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.163265306122449 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Review | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 138 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 10 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 128 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.072463768115942 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1833 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 98 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0534642662302237 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1561 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 174 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.111467008327995 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -272 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1370 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 130 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0948905109489051 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -191 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1367 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 111 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0811997073884418 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -3 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Add geography filter | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1833 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 98 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0534642662302237 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1561 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 174 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.111467008327995 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -272 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1370 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 130 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0948905109489051 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -191 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1367 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 111 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0811997073884418 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -3 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 307302 | Data_Quality.xlsx/Completeness |
    | Populated Records | 292546 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.951982089280252 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 157750 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2053 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.986985736925515 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 20 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 19 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.95 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.2 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | H. Woźniak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Velocity Anomaly | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Network-Linkage Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 3 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.3 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 61 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.93 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 4.27 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.3 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-07-14 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-07-14 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | H. Woźniak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity H | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-08-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 3 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Low | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-001 | source_system: CoreBanking-T24 | issue_description: Null counterparty IDs in feed | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Add geography filter | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.8 Model 8 — Velocity Anomaly

| **Model Code**                 | TM-NETWORK-008                                                                           |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Network-Linkage Family                                                                   |
| **Business Problem Solved**    | Transaction frequency exceeds peer-group baseline.                                       |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                |
| **Typology Detected**          | Velocity Anomaly — flags transaction frequency exceeds peer-group baseline.              |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity H)                |
| **Booking Entity / Segment**   | Entity H · Corporate · High-Risk Jurisdictions                                           |
| **Accountable Owner**          | H. Woźniak                                                                               |
| **Lifecycle / Risk Tier**      | Production · Tier 4 - Low                                                                |
| **Primary Source System**      | CoreBanking-T24                                                                          |
| **Linked Change Request(s)**   | —                                                                                        |
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