<model id="Model 58" code="TM-RMF-058">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 62 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2186 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 31 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 85721 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2248 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 88000 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0275800711743772 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.666666666666667 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.0529688167449808 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.975132810811426 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2248 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 34 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0151245551601423 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 25.5454545454545 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.77 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.0529688167449808 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0151245551601423 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.0378311121110454 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 56 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 40 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 16 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.714285714285714 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 137 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 8 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 129 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0583941605839416 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2460 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 131 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0532520325203252 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2629 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 206 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0783567896538608 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 169 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2135 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 229 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.107259953161593 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -494 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2657 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 317 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.119307489649981 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 522 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Lower score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2460 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 131 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0532520325203252 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2629 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 206 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0783567896538608 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 169 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2135 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 229 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.107259953161593 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -494 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2657 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 317 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.119307489649981 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 522 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 327005 | Data_Quality.xlsx/Completeness |
    | Populated Records | 299351 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.915432485741808 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 70739 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3250 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.95405646107522 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 50 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 45 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.9 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
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
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 10 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 76 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.73 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 20.52 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.0 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-08-04 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-08-04 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | H. Woźniak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity H | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-10-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Lower score threshold | direction: Reduce leakage | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.58 Model 58 — Wire Stripping

| **Model Code**                 | TM-RMF-058                                                                                 |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Rapid-Movement Family                                                                      |
| **Business Problem Solved**    | Removal of originator data in cross-border wires.                                          |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                          |
| **Typology Detected**          | Wire Stripping — flags removal of originator data in cross-border wires.                   |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity H)                  |
| **Booking Entity / Segment**   | Entity H · Corporate · APAC                                                                |
| **Accountable Owner**          | H. Woźniak                                                                                 |
| **Lifecycle / Risk Tier**      | Tuning · Tier 2 - High                                                                     |
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