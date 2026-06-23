<model id="Model 14" code="TM-BEHAV-014">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 556 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2252 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 70 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 59979 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2808 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 62857 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.198005698005698 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.888178913738019 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.323820617355853 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.963812247915026 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2808 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 394 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.14031339031339 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 44.6728288018836 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.68 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.323820617355853 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.14031339031339 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.250417726538868 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 117 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 32 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 85 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.273504273504274 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 92 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 8 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 84 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0869565217391304 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3245 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 193 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0594761171032358 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2418 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 111 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0459057071960298 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -827 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2279 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 129 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0566037735849057 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2632 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 159 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0604103343465046 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 353 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | No change - retain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 3245 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 193 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0594761171032358 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2418 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 111 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0459057071960298 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -827 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2279 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 129 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0566037735849057 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2632 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 159 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0604103343465046 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 353 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 378589 | Data_Quality.xlsx/Completeness |
    | Populated Records | 356265 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.941033680323517 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 20227 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1154 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.942947545360162 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 22 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 18 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.818181818181818 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5.8 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | D. Wójcik | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Crypto On/Off-Ramp | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Behavioural-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Private Banking | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 4 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.4 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 72 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.71 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 20.88 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-07-17 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-07-17 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | D. Wójcik | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity D | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-02-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: No change - retain | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.14 Model 14 — Crypto On/Off-Ramp

| **Model Code**                 | TM-BEHAV-014                                                                                 |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Behavioural-Anomaly Family                                                                   |
| **Business Problem Solved**    | Fiat-crypto conversion layering pattern.                                                     |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                            |
| **Typology Detected**          | Crypto On/Off-Ramp — flags fiat-crypto conversion layering pattern.                          |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity D)              |
| **Booking Entity / Segment**   | Entity D · Private Banking · APAC                                                            |
| **Accountable Owner**          | D. Wójcik                                                                                    |
| **Lifecycle / Risk Tier**      | Production · Tier 2 - High                                                                   |
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
    - gap_id: GAP-002 | typology_/_segment: Correspondent | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: High | remediation_owner: 2nd LoD MRM | typology_segment: Correspondent | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-007 | typology_/_segment: High-Risk Jurisdictions | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: Medium | remediation_owner: 1st LoD | typology_segment: High-Risk Jurisdictions | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-012 | typology_/_segment: APAC | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: Low | remediation_owner: 1st LoD | typology_segment: APAC | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-017 | typology_/_segment: Corporate | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: High | remediation_owner: 1st LoD | typology_segment: Corporate | description: Crypto on/off-ramp coverage limited to Entity A
  </relevant_coverage_gaps>

</estate_context>

</model>