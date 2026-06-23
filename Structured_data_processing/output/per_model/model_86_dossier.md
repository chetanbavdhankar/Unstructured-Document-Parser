<model id="Model 86" code="TM-BEHAV-086">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 582 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 648 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 89 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 53475 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1230 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 54794 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.473170731707317 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.867362146050671 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.612309310889006 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.988027271215565 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1230 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 236 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.191869918699187 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 22.4477132532759 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.62 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.612309310889006 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.191869918699187 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.444133554013078 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 67 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 63 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 4 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.940298507462687 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 53 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 3 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 50 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0566037735849057 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1259 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 125 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0992851469420175 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1212 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 81 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0668316831683168 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -47 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1465 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 114 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0778156996587031 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 253 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1104 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 89 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0806159420289855 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -361 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | No change - retain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1259 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 125 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0992851469420175 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1212 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 81 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0668316831683168 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -47 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1465 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 114 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0778156996587031 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 253 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1104 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 89 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0806159420289855 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -361 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 201572 | Data_Quality.xlsx/Completeness |
    | Populated Records | 199299 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.988723632250511 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 125733 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 4859 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.961354616528676 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 43 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 41 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.953488372093023 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
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
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 8 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.8 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 57 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.61 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 22.23 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.8 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-12-03 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-12-03 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | F. Zielińska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity F | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-02-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 4 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-017 | finding: Calibration outside tolerance | status: In Remediation | target_date: 2025-Q2 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: No change - retain | direction: Maintain | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.86 Model 86 — Dormant Reactivation

| **Model Code**                 | TM-BEHAV-086                                                                               |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Behavioural-Anomaly Family                                                                 |
| **Business Problem Solved**    | Sudden activity on long-dormant accounts.                                                  |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.             |
| **Typology Detected**          | Dormant Reactivation — flags sudden activity on long-dormant accounts.                     |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity F)                     |
| **Booking Entity / Segment**   | Entity F · Retail · APAC                                                                   |
| **Accountable Owner**          | F. Zielińska                                                                               |
| **Lifecycle / Risk Tier**      | Production · Tier 2 - High                                                                 |
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