<model id="Model 94" code="TM-BEHAV-094">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 597 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 665 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 18 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 83284 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1262 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 84564 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.473058637083994 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.970731707317073 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.63612147043154 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.99207852386568 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1262 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 450 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.356576862123613 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 14.9236081547704 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.53 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.63612147043154 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.356576862123613 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.524303627108369 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 66 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 29 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 37 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.439393939393939 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 114 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 5 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 109 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.043859649122807 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1280 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 71 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.05546875 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1427 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 147 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.103013314646111 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 147 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1061 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 51 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0480678605089538 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -366 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1453 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 93 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0640055058499656 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 392 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | No change - retain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1280 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 71 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.05546875 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1427 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 147 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.103013314646111 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 147 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1061 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 51 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0480678605089538 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -366 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1453 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 93 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0640055058499656 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 392 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 439394 | Data_Quality.xlsx/Completeness |
    | Populated Records | 401428 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.913594632607637 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 104076 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2815 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.972952457819286 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 50 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 45 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.9 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.8 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CardSwitch | Data_Quality.xlsx/Lineage |
    | Secondary Feed | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
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
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 77 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.6 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 30.8 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.6 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-02-08 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-02-08 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | D. Wójcik | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity D | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-10-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: No change - retain | direction: Maintain | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.94 Model 94 — Crypto On/Off-Ramp

| **Model Code**                 | TM-BEHAV-094                                                                        |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Behavioural-Anomaly Family                                                          |
| **Business Problem Solved**    | Fiat-crypto conversion layering pattern.                                            |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.      |
| **Typology Detected**          | Crypto On/Off-Ramp — flags fiat-crypto conversion layering pattern.                 |
| **Data Inputs**                | CardSwitch transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity D)     |
| **Booking Entity / Segment**   | Entity D · Private Banking · APAC                                                   |
| **Accountable Owner**          | D. Wójcik                                                                           |
| **Lifecycle / Risk Tier**      | Tuning · Tier 2 - High                                                              |
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

  <relevant_coverage_gaps>
    - gap_id: GAP-002 | typology_/_segment: Correspondent | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: High | remediation_owner: 2nd LoD MRM | typology_segment: Correspondent | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-007 | typology_/_segment: High-Risk Jurisdictions | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: Medium | remediation_owner: 1st LoD | typology_segment: High-Risk Jurisdictions | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-012 | typology_/_segment: APAC | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: Low | remediation_owner: 1st LoD | typology_segment: APAC | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-017 | typology_/_segment: Corporate | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: High | remediation_owner: 1st LoD | typology_segment: Corporate | description: Crypto on/off-ramp coverage limited to Entity A
  </relevant_coverage_gaps>

</estate_context>

</model>