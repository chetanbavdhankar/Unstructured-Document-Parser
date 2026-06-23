<model id="Model 50" code="TM-RMF-050">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 561 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1580 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 116 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 41786 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2141 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 44043 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.262027090144792 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.828655834564254 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.398154719659333 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.963565927224093 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2141 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 377 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.176085941148996 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 48.6115841336875 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.49 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.398154719659333 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.176085941148996 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.309327208255198 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 37 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 13 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 24 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.351351351351351 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 51 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 9 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 42 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.176470588235294 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2123 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 179 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0843146490814885 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2372 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 100 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0421585160202361 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 249 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1926 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 103 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.053478712357217 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -446 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2290 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 266 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.116157205240175 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 364 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Lower score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2123 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 179 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0843146490814885 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2372 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 100 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0421585160202361 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 249 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1926 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 103 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.053478712357217 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -446 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2290 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 266 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.116157205240175 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 364 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 311418 | Data_Quality.xlsx/Completeness |
    | Populated Records | 296783 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.953005285500517 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 166595 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 4179 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.974915213541823 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 51 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 48 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.941176470588235 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.2 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | J. Kozłowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Funnel Account | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Rapid-Movement Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 8 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.8 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 58 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.51 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 28.42 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.2 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-05-12 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-05-12 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | J. Kozłowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity J | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-02-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Low | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-007 | source_system: CoreBanking-T24 | issue_description: Missing originator country on cross-border wires | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Lower score threshold | direction: Reduce leakage | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.50 Model 50 — Funnel Account

| **Model Code**                 | TM-RMF-050                                                                               |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Rapid-Movement Family                                                                    |
| **Business Problem Solved**    | Many-to-one inflow with single rapid outflow.                                            |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.           |
| **Typology Detected**          | Funnel Account — flags many-to-one inflow with single rapid outflow.                     |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity J)            |
| **Booking Entity / Segment**   | Entity J · Correspondent · APAC                                                          |
| **Accountable Owner**          | J. Kozłowska                                                                             |
| **Lifecycle / Risk Tier**      | Production · Tier 2 - High                                                               |
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