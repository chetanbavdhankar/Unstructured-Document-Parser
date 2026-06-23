<model id="Model 66" code="TM-RMF-066">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 226 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1008 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 26 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 83593 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1234 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 84853 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.183144246353323 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.896825396825397 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.304172274562584 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.9880852472193 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1234 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 95 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0769854132901135 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 14.5427975439878 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.72 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.304172274562584 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0769854132901135 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.213297530053596 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 36 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 26 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 10 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.722222222222222 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 143 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 1 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 142 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.00699300699300699 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1380 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 140 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.101449275362319 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1400 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 94 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0671428571428571 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 20 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1336 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 103 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0770958083832335 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -64 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1309 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 134 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.102368220015279 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -27 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Lower score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1380 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 140 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.101449275362319 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1400 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 94 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0671428571428571 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 20 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1336 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 103 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0770958083832335 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -64 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1309 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 134 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.102368220015279 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -27 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 498353 | Data_Quality.xlsx/Completeness |
    | Populated Records | 463992 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.931050881604004 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 48076 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 168 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.996505532906232 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Green | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 107 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 97 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.906542056074766 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.5 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CardSwitch | Data_Quality.xlsx/Lineage |
    | Secondary Feed | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | F. Zielińska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Dormant Reactivation | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Rapid-Movement Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 1 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 59 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.58 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 24.78 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.7 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-06-06 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-06-06 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | F. Zielińska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity F | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-06-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-013 | finding: Threshold not re-tuned within policy window | status: Open | target_date: 2025-Q2 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-033 | finding: Documentation gap in scenario logic | status: Open | target_date: 2025-Q2 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Lower score threshold | direction: Reduce leakage | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.66 Model 66 — Dormant Reactivation

| **Model Code**                 | TM-RMF-066                                                                          |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Rapid-Movement Family                                                               |
| **Business Problem Solved**    | Sudden activity on long-dormant accounts.                                           |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.           |
| **Typology Detected**          | Dormant Reactivation — flags sudden activity on long-dormant accounts.              |
| **Data Inputs**                | CardSwitch transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity F)              |
| **Booking Entity / Segment**   | Entity F · Retail · APAC                                                            |
| **Accountable Owner**          | F. Zielińska                                                                        |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 2 - High                                                     |
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