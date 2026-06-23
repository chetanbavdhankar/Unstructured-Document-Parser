<model id="Model 71" code="TM-CRYPTO-071">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 104 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 721 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 19 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 50290 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 825 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 51134 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.126060606060606 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.845528455284553 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.219409282700422 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.98586579365235 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 825 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 40 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0484848484848485 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 16.1340790863222 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.82 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.219409282700422 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0484848484848485 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.151039509014193 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 98 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 16 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 82 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.163265306122449 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Review | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 79 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 11 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 68 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.139240506329114 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 773 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 84 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.108667529107374 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 982 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.107942973523422 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 209 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 677 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 34 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0502215657311669 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -305 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 742 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 63 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0849056603773585 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 65 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Re-segment population | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 773 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 84 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.108667529107374 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 982 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.107942973523422 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 209 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 677 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 34 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0502215657311669 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -305 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 742 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 63 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0849056603773585 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 65 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 475574 | Data_Quality.xlsx/Completeness |
    | Populated Records | 434101 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.912793802857179 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 123136 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 885 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.992812824844075 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Green | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 102 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 91 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.892156862745098 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5.6 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | A. Kowalski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Mule Account Behaviour | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Virtual-Asset Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 8 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.8 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 65 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.94 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 3.9 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.0 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-02-15 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-02-15 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | A. Kowalski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity A | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-11-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Low | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-014 | finding: Insufficient BTL coverage | status: Open | target_date: 2025-Q3 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-034 | finding: Population drift detected | status: Closed | target_date: 2025-Q3 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-010 | source_system: CoreBanking-T24 | issue_description: Late feed beyond SLA cut-off | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Re-segment population | direction: Maintain | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.71 Model 71 — Mule Account Behaviour

| **Model Code**                 | TM-CRYPTO-071                                                                            |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Virtual-Asset Family                                                                     |
| **Business Problem Solved**    | Profile consistent with third-party mule activity.                                       |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.           |
| **Typology Detected**          | Mule Account Behaviour — flags profile consistent with third-party mule activity.        |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity A)                   |
| **Booking Entity / Segment**   | Entity A · Retail · Americas                                                             |
| **Accountable Owner**          | A. Kowalski                                                                              |
| **Lifecycle / Risk Tier**      | Validation · Tier 3 - Medium                                                             |
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