<model id="Model 22" code="TM-BEHAV-022">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 247 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 662 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 75 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 62904 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 909 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 63888 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.271727172717272 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.767080745341615 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.401299756295695 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.989585627536734 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 909 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 171 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.188118811881188 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 14.2280240420736 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.49 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.401299756295695 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.188118811881188 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.316027378529892 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 35 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 13 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 22 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.371428571428571 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 198 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 0 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 198 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 968 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 84 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0867768595041322 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 733 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 36 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0491132332878581 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -235 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 843 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 47 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0557532621589561 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 110 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 959 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 46 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0479666319082377 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 116 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | No change - retain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 968 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 84 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0867768595041322 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 733 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 36 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0491132332878581 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -235 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 843 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 47 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0557532621589561 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 110 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 959 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 46 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0479666319082377 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 116 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 83321 | Data_Quality.xlsx/Completeness |
    | Populated Records | 79862 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.958485855906674 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 71161 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 775 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.989109203074718 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 41 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 36 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.878048780487805 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | B. Nowak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Rapid Movement of Funds | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Behavioural-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 9 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.9 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 73 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.81 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 13.87 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.6 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-11-20 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-11-20 | Model_Risk_Governance.xlsx/Lifecycle_Status |
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

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-003 | source_system: CoreBanking-T24 | issue_description: Late feed beyond SLA cut-off | status: In Progress | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: No change - retain | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.22 Model 22 — Rapid Movement of Funds

| **Model Code**                 | TM-BEHAV-022                                                                             |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Behavioural-Anomaly Family                                                               |
| **Business Problem Solved**    | Funds pass through account with minimal retention.                                       |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                        |
| **Typology Detected**          | Rapid Movement of Funds — flags funds pass through account with minimal retention.       |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity B)                      |
| **Booking Entity / Segment**   | Entity B · SME · APAC                                                                    |
| **Accountable Owner**          | B. Nowak                                                                                 |
| **Lifecycle / Risk Tier**      | Tuning · Tier 2 - High                                                                   |
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