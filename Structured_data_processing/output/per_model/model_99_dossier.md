<model id="Model 99" code="TM-GEO-099">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 277 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 312 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 73 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 37063 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 589 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 37725 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.470288624787776 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.791428571428572 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.589989350372737 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.991652173913044 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 589 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 157 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.266553480475382 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 15.6129887342611 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.77 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.589989350372737 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.266553480475382 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.460615002413795 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 78 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 48 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 30 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.615384615384615 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 52 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 4 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 48 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0769230769230769 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 596 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 56 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0939597315436242 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 505 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 43 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0851485148514852 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -91 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 681 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 71 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.104258443465492 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 176 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 490 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 22 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0448979591836735 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -191 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Extend lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 596 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 56 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0939597315436242 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 505 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 43 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0851485148514852 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -91 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 681 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 71 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.104258443465492 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 176 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 490 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 22 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0448979591836735 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -191 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 486714 | Data_Quality.xlsx/Completeness |
    | Populated Records | 486429 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.99941444051332 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 97225 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 987 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.989848290048856 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 118 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 105 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.889830508474576 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | I. Dąbrowski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | ATM Cycling | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Geographic-Risk Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Private Banking | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 6 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.6 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 88 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.53 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 41.36 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.6 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-08-28 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-08-28 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | I. Dąbrowski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity I | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-03-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-014 | source_system: CoreBanking-T24 | issue_description: Missing originator country on cross-border wires | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Extend lookback window | direction: Reduce leakage | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.99 Model 99 — ATM Cycling

| **Model Code**                 | TM-GEO-099                                                                               |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Geographic-Risk Family                                                                   |
| **Business Problem Solved**    | Geographically dispersed rapid ATM withdrawals.                                          |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                        |
| **Typology Detected**          | ATM Cycling — flags geographically dispersed rapid ATM withdrawals.                      |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity I)          |
| **Booking Entity / Segment**   | Entity I · Private Banking · Americas                                                    |
| **Accountable Owner**          | I. Dąbrowski                                                                             |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                             |
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