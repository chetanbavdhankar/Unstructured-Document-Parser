<model id="Model 84" code="TM-CASH-084">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 521 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 241 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 100 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 32091 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 762 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 32953 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.683727034120735 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.838969404186795 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.753434562545192 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.992546084374613 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 762 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 396 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.519685039370079 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 23.1238430491913 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.77 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.753434562545192 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.519685039370079 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.659934753275146 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 83 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 37 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 46 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.445783132530121 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 177 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 10 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 167 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0564971751412429 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 866 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 75 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0866050808314088 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 899 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 55 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0611790878754171 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 33 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 848 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 48 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0566037735849057 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -51 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 767 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 87 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.113428943937419 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -81 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 866 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 75 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0866050808314088 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 899 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 55 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0611790878754171 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 33 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 848 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 48 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0566037735849057 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -51 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 767 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 87 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.113428943937419 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -81 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 234635 | Data_Quality.xlsx/Completeness |
    | Populated Records | 220579 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.940094188846506 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 95732 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2204 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.976977395228346 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 110 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 94 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.854545454545455 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.6 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | D. Wójcik | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Cash-Intensive Business | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Cash-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Private Banking | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 10 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 57 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.67 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 18.81 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.7 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-04-07 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-04-07 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | D. Wójcik | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity D | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-12-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 5 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Shorten lookback window | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.84 Model 84 — Cash-Intensive Business

| **Model Code**                 | TM-CASH-084                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                          |
| **Business Problem Solved**    | Cash activity inconsistent with business profile.                                            |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                    |
| **Typology Detected**          | Cash-Intensive Business — flags cash activity inconsistent with business profile.            |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity D)              |
| **Booking Entity / Segment**   | Entity D · Private Banking · High-Risk Jurisdictions                                         |
| **Accountable Owner**          | D. Wójcik                                                                                    |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 4 - Low                                                               |
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