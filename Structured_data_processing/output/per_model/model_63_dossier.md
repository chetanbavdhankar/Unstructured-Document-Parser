<model id="Model 63" code="TM-CRYPTO-063">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 579 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2847 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 49 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 85941 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 3426 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 89416 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.169001751313485 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.921974522292994 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.285643808584114 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.96793485606163 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 3426 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 296 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0863981319322826 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 38.3152903283529 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.5 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.285643808584114 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0863981319322826 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.205945537923382 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 116 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 14 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 102 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.120689655172414 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Review | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 98 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 1 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 97 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0102040816326531 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3707 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 166 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0447801456703534 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2800 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 156 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0557142857142857 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -907 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3004 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 345 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.114846870838882 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 204 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 4103 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 234 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0570314404094565 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 1099 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Re-segment population | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 3707 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 166 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0447801456703534 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2800 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 156 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0557142857142857 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -907 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 3004 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 345 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.114846870838882 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 204 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 4103 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 234 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0570314404094565 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 1099 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 196383 | Data_Quality.xlsx/Completeness |
    | Populated Records | 183564 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.934724492445884 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 167382 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 4957 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.97038510712024 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 67 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 60 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.895522388059702 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.7 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | C. Lewandowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | High-Risk Jurisdiction | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Virtual-Asset Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 6 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.6 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 57 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.92 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 4.56 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.3 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-02-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-02-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | C. Lewandowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity C | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-03-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
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
### 3.63 Model 63 — High-Risk Jurisdiction

| **Model Code**                 | TM-CRYPTO-063                                                                                |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Virtual-Asset Family                                                                         |
| **Business Problem Solved**    | Exposure to FATF grey/black-list geographies.                                                |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                            |
| **Typology Detected**          | High-Risk Jurisdiction — flags exposure to FATF grey/black-list geographies.                 |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity C)                    |
| **Booking Entity / Segment**   | Entity C · Corporate · Americas                                                              |
| **Accountable Owner**          | C. Lewandowska                                                                               |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                                 |
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