<model id="Model 44" code="TM-CASH-044">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 91 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 274 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 36 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 31285 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 365 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 31686 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.249315068493151 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.716535433070866 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.369918699186992 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.99131784910802 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 365 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 54 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.147945205479452 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 11.5192829640851 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.76 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.369918699186992 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.147945205479452 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.281129301703976 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 81 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 30 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 51 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.37037037037037 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 186 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 3 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 183 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0161290322580645 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 294 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 16 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.054421768707483 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 399 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 16 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0401002506265664 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 105 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 321 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 26 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0809968847352025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -78 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 358 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 32 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0893854748603352 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 37 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 294 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 16 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.054421768707483 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 399 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 16 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0401002506265664 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 105 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 321 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 26 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0809968847352025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -78 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 358 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 32 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0893854748603352 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 37 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 247464 | Data_Quality.xlsx/Completeness |
    | Populated Records | 230848 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.932854879901723 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 139771 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 6481 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.953631296907084 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 34 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 32 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.941176470588235 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.2 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
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
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 76 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.7 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 22.8 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.5 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-11-01 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-11-01 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | D. Wójcik | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity D | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-08-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
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
### 3.44 Model 44 — Cash-Intensive Business

| **Model Code**                 | TM-CASH-044                                                                                |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                        |
| **Business Problem Solved**    | Cash activity inconsistent with business profile.                                          |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                  |
| **Typology Detected**          | Cash-Intensive Business — flags cash activity inconsistent with business profile.          |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity D)            |
| **Booking Entity / Segment**   | Entity D · Private Banking · High-Risk Jurisdictions                                       |
| **Accountable Owner**          | D. Wójcik                                                                                  |
| **Lifecycle / Risk Tier**      | Production · Tier 4 - Low                                                                  |
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