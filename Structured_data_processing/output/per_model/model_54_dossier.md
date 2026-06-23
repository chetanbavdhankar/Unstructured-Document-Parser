<model id="Model 54" code="TM-BEHAV-054">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 121 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2651 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 83 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 45607 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2772 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 48462 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0436507936507937 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.593137254901961 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.0813172043010753 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.94506610302955 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2772 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 78 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0281385281385281 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 57.1994552432834 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.47 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.0813172043010753 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0281385281385281 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.0600457338360564 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 42 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 12 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 30 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.285714285714286 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 116 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 2 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 114 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0172413793103448 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2772 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 286 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.103174603174603 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2657 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 176 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0662401204365826 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -115 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2687 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 175 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0651283959806476 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 30 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3301 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 317 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0960315056043623 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 614 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | No change - retain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2772 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 286 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.103174603174603 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2657 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 176 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0662401204365826 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -115 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2687 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 175 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0651283959806476 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 30 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 3301 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 317 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0960315056043623 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 614 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 107650 | Data_Quality.xlsx/Completeness |
    | Populated Records | 101749 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.945183464932652 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 113876 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1387 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.987820085004742 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 82 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 77 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.939024390243902 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | D. Wójcik | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Crypto On/Off-Ramp | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Behavioural-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Private Banking | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 2 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.2 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 94 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.49 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 47.94 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.0 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-08-27 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-08-27 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | D. Wójcik | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity D | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-06-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 3 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: No change - retain | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.54 Model 54 — Crypto On/Off-Ramp

| **Model Code**                 | TM-BEHAV-054                                                                           |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Behavioural-Anomaly Family                                                             |
| **Business Problem Solved**    | Fiat-crypto conversion layering pattern.                                               |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                      |
| **Typology Detected**          | Crypto On/Off-Ramp — flags fiat-crypto conversion layering pattern.                    |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity D)        |
| **Booking Entity / Segment**   | Entity D · Private Banking · APAC                                                      |
| **Accountable Owner**          | D. Wójcik                                                                              |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 2 - High                                                        |
| **Primary Source System**      | CryptoGateway                                                                          |
| **Linked Change Request(s)**   | —                                                                                      |
</functional_requirements>

<change_requests>
  <not provided>
</change_requests>

<estate_context>
  <sampling_methodology>
    ATL Sample Basis: Stratified random, 95% CI; BTL Sample Basis: Boundary band ±15% of threshold; Confidence Level: 99%
  </sampling_methodology>

  <relevant_coverage_gaps>
    - gap_id: GAP-002 | typology_/_segment: Correspondent | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: High | remediation_owner: 2nd LoD MRM | typology_segment: Correspondent | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-007 | typology_/_segment: High-Risk Jurisdictions | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: Medium | remediation_owner: 1st LoD | typology_segment: High-Risk Jurisdictions | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-012 | typology_/_segment: APAC | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: Low | remediation_owner: 1st LoD | typology_segment: APAC | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-017 | typology_/_segment: Corporate | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: High | remediation_owner: 1st LoD | typology_segment: Corporate | description: Crypto on/off-ramp coverage limited to Entity A
  </relevant_coverage_gaps>

</estate_context>

</model>