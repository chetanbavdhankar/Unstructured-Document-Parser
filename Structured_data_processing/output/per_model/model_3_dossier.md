<model id="Model 3" code="TM-GEO-003">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 140 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2888 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 5 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 20892 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 3028 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 23925 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0462351387054161 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.96551724137931 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.0882445635045698 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.878553406223717 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 3028 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 64 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0211360634081902 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 126.562173458725 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.78 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.0882445635045698 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0211360634081902 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.061401163466018 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 52 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 19 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 33 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.365384615384615 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 125 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 3 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 122 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.024 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3559 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 352 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.098904186569261 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2930 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 284 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0969283276450512 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -629 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3360 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 181 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0538690476190476 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 430 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2914 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 129 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0442690459849005 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -446 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Extend lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 3559 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 352 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.098904186569261 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2930 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 284 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0969283276450512 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -629 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 3360 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 181 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0538690476190476 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 430 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2914 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 129 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0442690459849005 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -446 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 124314 | Data_Quality.xlsx/Completeness |
    | Populated Records | 116955 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.940803127564072 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 147164 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 7618 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.948234622597918 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 20 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 17 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.85 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.3 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CardSwitch | Data_Quality.xlsx/Lineage |
    | Secondary Feed | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | C. Lewandowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | High-Risk Jurisdiction | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Geographic-Risk Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 1 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 81 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.94 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 4.86000000000001 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.7 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-05-16 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-05-16 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | C. Lewandowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity C | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-03-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Extend lookback window | direction: Reduce leakage | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.3 Model 3 — High-Risk Jurisdiction

| **Model Code**                 | TM-GEO-003                                                                          |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Geographic-Risk Family                                                              |
| **Business Problem Solved**    | Exposure to FATF grey/black-list geographies.                                       |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.           |
| **Typology Detected**          | High-Risk Jurisdiction — flags exposure to FATF grey/black-list geographies.        |
| **Data Inputs**                | CardSwitch transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity C)           |
| **Booking Entity / Segment**   | Entity C · Corporate · Americas                                                     |
| **Accountable Owner**          | C. Lewandowska                                                                      |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                        |
| **Primary Source System**      | CardSwitch                                                                          |
| **Linked Change Request(s)**   | —                                                                                   |
</functional_requirements>

<change_requests>
  <not provided>
</change_requests>

<estate_context>
  <sampling_methodology>
    ATL Sample Basis: Stratified random, 95% CI; BTL Sample Basis: Boundary band ±15% of threshold; Confidence Level: 97.5%
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