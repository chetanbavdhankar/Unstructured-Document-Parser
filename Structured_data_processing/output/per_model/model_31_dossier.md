<model id="Model 31" code="TM-CRYPTO-031">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 238 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1078 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 116 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 56965 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1316 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 58397 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.180851063829787 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.672316384180791 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.285029940119761 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.981427562324484 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1316 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 90 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0683890577507599 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 22.53540421597 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.58 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.285029940119761 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0683890577507599 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.19837358717216 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 50 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 33 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 17 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.66 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 167 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 5 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 162 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.029940119760479 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1223 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 143 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.116925592804579 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1167 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 84 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0719794344473008 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -56 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1318 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 99 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.075113808801214 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 151 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1561 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 122 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0781550288276746 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 243 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Re-segment population | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1223 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 143 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.116925592804579 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1167 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 84 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0719794344473008 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -56 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1318 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 99 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.075113808801214 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 151 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1561 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 122 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0781550288276746 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 243 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 205054 | Data_Quality.xlsx/Completeness |
    | Populated Records | 193977 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.945980083295132 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 172110 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2828 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.983568647957702 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 45 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 44 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.977777777777778 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.9 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CardSwitch | Data_Quality.xlsx/Lineage |
    | Secondary Feed | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | A. Kowalski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Mule Account Behaviour | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Virtual-Asset Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 4 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.4 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 75 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.87 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 9.75 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-06-23 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-06-23 | Model_Risk_Governance.xlsx/Lifecycle_Status |
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
    | Issue_Tracking | finding_id: MRM-006 | finding: Elevated false-positive rate vs peer group | status: Closed | target_date: 2025-Q3 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-026 | finding: Insufficient BTL coverage | status: Open | target_date: 2025-Q3 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Re-segment population | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.31 Model 31 — Mule Account Behaviour

| **Model Code**                 | TM-CRYPTO-031                                                                       |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Virtual-Asset Family                                                                |
| **Business Problem Solved**    | Profile consistent with third-party mule activity.                                  |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.           |
| **Typology Detected**          | Mule Account Behaviour — flags profile consistent with third-party mule activity.   |
| **Data Inputs**                | CardSwitch transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity A)              |
| **Booking Entity / Segment**   | Entity A · Retail · Americas                                                        |
| **Accountable Owner**          | A. Kowalski                                                                         |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                        |
| **Primary Source System**      | CardSwitch                                                                          |
| **Linked Change Request(s)**   | —                                                                                   |
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