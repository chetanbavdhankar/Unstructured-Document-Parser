<model id="Model 51" code="TM-GEO-051">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 163 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2158 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 32 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 67770 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2321 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 70123 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0702283498492029 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.835897435897436 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.129570747217806 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.969139686534721 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2321 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 67 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.028866867729427 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 33.0989832152076 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.78 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.129570747217806 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.028866867729427 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.0892891954224544 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 106 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 104 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 2 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.981132075471698 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 186 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 4 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 182 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.021505376344086 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2637 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0527114144861585 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2656 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 169 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0636295180722892 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 19 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2155 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 148 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.068677494199536 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -501 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2006 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 122 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0608175473579262 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -149 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Extend lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2637 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0527114144861585 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2656 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 169 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0636295180722892 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 19 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2155 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 148 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.068677494199536 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -501 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2006 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 122 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0608175473579262 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -149 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 163571 | Data_Quality.xlsx/Completeness |
    | Populated Records | 149889 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.916354365993972 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 193978 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 11122 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.942663601026921 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 73 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 70 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.958904109589041 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
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
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 59 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.93 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 4.13 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-01-05 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-01-05 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | A. Kowalski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity A | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-03-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 4 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-010 | finding: Population drift detected | status: Open | target_date: 2025-Q3 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-030 | finding: Elevated false-positive rate vs peer group | status: Open | target_date: 2025-Q3 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Extend lookback window | direction: Reduce leakage | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.51 Model 51 — Mule Account Behaviour

| **Model Code**                 | TM-GEO-051                                                                                 |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Geographic-Risk Family                                                                     |
| **Business Problem Solved**    | Profile consistent with third-party mule activity.                                         |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                  |
| **Typology Detected**          | Mule Account Behaviour — flags profile consistent with third-party mule activity.          |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity A)                     |
| **Booking Entity / Segment**   | Entity A · Retail · Americas                                                               |
| **Accountable Owner**          | A. Kowalski                                                                                |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                               |
| **Primary Source System**      | PaymentsHub-SWIFT                                                                          |
| **Linked Change Request(s)**   | —                                                                                          |
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