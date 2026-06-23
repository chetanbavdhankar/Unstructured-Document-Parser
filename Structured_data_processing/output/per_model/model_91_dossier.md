<model id="Model 91" code="TM-GEO-091">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 487 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1600 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 26 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 72846 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2087 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 74959 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.233349305222808 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.949317738791423 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.374615384615385 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.978507911774978 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2087 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 273 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.130809774796358 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 27.841886898171 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.52 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.374615384615385 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.130809774796358 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.277093140687774 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 67 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 31 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 36 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.462686567164179 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 70 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 2 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 68 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0285714285714286 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2164 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 213 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0984288354898336 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2072 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 177 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0854247104247104 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -92 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2066 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 189 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0914811229428848 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -6 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2053 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 223 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.10862152946907 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -13 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Extend lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2164 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 213 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0984288354898336 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2072 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 177 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0854247104247104 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -92 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2066 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 189 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0914811229428848 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -6 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2053 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 223 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.10862152946907 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -13 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 279125 | Data_Quality.xlsx/Completeness |
    | Populated Records | 265769 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.952150470219436 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 133585 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3734 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.972047759853277 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 64 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 57 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.890625 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.1 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | A. Kowalski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Mule Account Behaviour | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Geographic-Risk Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 9 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.9 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 68 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.79 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 14.28 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.3 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-02-25 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-02-25 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | A. Kowalski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity A | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-07-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-018 | finding: Elevated false-positive rate vs peer group | status: Closed | target_date: 2025-Q3 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Extend lookback window | direction: Reduce leakage | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.91 Model 91 — Mule Account Behaviour

| **Model Code**                 | TM-GEO-091                                                                                   |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Geographic-Risk Family                                                                       |
| **Business Problem Solved**    | Profile consistent with third-party mule activity.                                           |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                            |
| **Typology Detected**          | Mule Account Behaviour — flags profile consistent with third-party mule activity.            |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity A)                       |
| **Booking Entity / Segment**   | Entity A · Retail · Americas                                                                 |
| **Accountable Owner**          | A. Kowalski                                                                                  |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                                 |
| **Primary Source System**      | Sanctions-Screening                                                                          |
| **Linked Change Request(s)**   | —                                                                                            |
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