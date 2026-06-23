<model id="Model 23" code="TM-CRYPTO-023">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 592 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 570 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 88 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 37799 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1162 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 39049 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.509466437177281 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.870588235294118 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.642779587404995 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.985144257082541 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1162 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 227 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.195352839931153 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 29.7574841865349 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.59 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.642779587404995 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.195352839931153 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.463808888415458 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 101 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 5 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 96 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.0495049504950495 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Review | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 64 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 6 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 58 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.09375 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1393 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 148 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.106245513280689 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1338 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 73 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.054559043348281 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -55 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 992 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 101 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.101814516129032 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -346 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1062 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 57 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0536723163841808 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 70 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Re-segment population | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1393 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 148 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.106245513280689 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1338 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 73 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.054559043348281 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -55 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 992 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 101 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.101814516129032 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -346 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1062 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 57 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0536723163841808 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 70 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 350137 | Data_Quality.xlsx/Completeness |
    | Populated Records | 337292 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.963314359807732 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 132697 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 7590 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.942802022653112 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 69 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 66 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.956521739130435 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.3 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | C. Lewandowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | High-Risk Jurisdiction | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Virtual-Asset Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 8 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.8 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 91 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.72 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 25.48 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-12-21 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-12-21 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | C. Lewandowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity C | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-11-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Low | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Re-segment population | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.23 Model 23 — High-Risk Jurisdiction

| **Model Code**                 | TM-CRYPTO-023                                                                              |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Virtual-Asset Family                                                                       |
| **Business Problem Solved**    | Exposure to FATF grey/black-list geographies.                                              |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                          |
| **Typology Detected**          | High-Risk Jurisdiction — flags exposure to FATF grey/black-list geographies.               |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity C)                  |
| **Booking Entity / Segment**   | Entity C · Corporate · Americas                                                            |
| **Accountable Owner**          | C. Lewandowska                                                                             |
| **Lifecycle / Risk Tier**      | Validation · Tier 3 - Medium                                                               |
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

  <relevant_coverage_gaps>
    - gap_id: GAP-005 | typology_/_segment: SME | gap_description: High-risk jurisdiction logic disabled on 22 models | severity: High | remediation_owner: AML Tuning Team | typology_segment: SME | description: High-risk jurisdiction logic disabled on 22 models
    - gap_id: GAP-006 | typology_/_segment: High-Risk Jurisdictions | gap_description: No model tuned for Private Banking segment in APAC | severity: Low | remediation_owner: AML Tuning Team | typology_segment: High-Risk Jurisdictions | description: No model tuned for Private Banking segment in APAC
    - gap_id: GAP-007 | typology_/_segment: High-Risk Jurisdictions | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: Medium | remediation_owner: 1st LoD | typology_segment: High-Risk Jurisdictions | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-010 | typology_/_segment: Americas | gap_description: High-risk jurisdiction logic disabled on 22 models | severity: High | remediation_owner: 1st LoD | typology_segment: Americas | description: High-risk jurisdiction logic disabled on 22 models
    - gap_id: GAP-015 | typology_/_segment: Americas | gap_description: High-risk jurisdiction logic disabled on 22 models | severity: Low | remediation_owner: AML Tuning Team | typology_segment: Americas | description: High-risk jurisdiction logic disabled on 22 models
    - gap_id: GAP-016 | typology_/_segment: High-Risk Jurisdictions | gap_description: No model tuned for Private Banking segment in APAC | severity: Medium | remediation_owner: 1st LoD | typology_segment: High-Risk Jurisdictions | description: No model tuned for Private Banking segment in APAC
  </relevant_coverage_gaps>

</estate_context>

</model>