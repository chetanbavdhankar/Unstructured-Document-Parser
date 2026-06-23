<model id="Model 98" code="TM-RMF-098">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 67 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1796 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 22 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 26925 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1863 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 28810 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0359634997316157 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.752808988764045 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.0686475409836066 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.937467358378887 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1863 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 37 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0198604401502952 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 64.6650468587296 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.47 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.0686475409836066 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0198604401502952 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.049132700650282 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 86 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 29 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 57 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.337209302325581 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 90 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 2 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 88 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0222222222222222 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2100 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 161 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0766666666666667 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1680 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 181 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.107738095238095 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -420 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1532 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 86 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.056135770234987 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -148 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1554 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 109 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0701415701415701 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 22 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Lower score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2100 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 161 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0766666666666667 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1680 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 181 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.107738095238095 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -420 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1532 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 86 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.056135770234987 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -148 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1554 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 109 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0701415701415701 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 22 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 275385 | Data_Quality.xlsx/Completeness |
    | Populated Records | 249813 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.907140911814369 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 60559 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1791 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.97042553542826 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 35 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 32 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.914285714285714 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3.7 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | H. Woźniak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Wire Stripping | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Rapid-Movement Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 2 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.2 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 57 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.52 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 27.36 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.5 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-10-21 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-10-21 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | H. Woźniak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity H | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-02-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 5 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Low | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Lower score threshold | direction: Reduce leakage | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.98 Model 98 — Wire Stripping

| **Model Code**                 | TM-RMF-098                                                                                   |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Rapid-Movement Family                                                                        |
| **Business Problem Solved**    | Removal of originator data in cross-border wires.                                            |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                    |
| **Typology Detected**          | Wire Stripping — flags removal of originator data in cross-border wires.                     |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity H)                    |
| **Booking Entity / Segment**   | Entity H · Corporate · APAC                                                                  |
| **Accountable Owner**          | H. Woźniak                                                                                   |
| **Lifecycle / Risk Tier**      | Production · Tier 2 - High                                                                   |
| **Primary Source System**      | Sanctions-Screening                                                                          |
| **Linked Change Request(s)**   | —                                                                                            |
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