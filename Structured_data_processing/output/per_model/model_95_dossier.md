<model id="Model 95" code="TM-CRYPTO-095">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 197 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 993 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 42 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 74862 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1190 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 76094 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.165546218487395 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.824267782426778 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.275717284814556 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.986909234724145 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1190 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 92 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0773109243697479 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 15.6385523168712 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.72 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.275717284814556 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0773109243697479 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.196354740636633 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 116 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 91 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 25 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.78448275862069 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 200 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 0 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 200 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1192 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 135 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.113255033557047 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1321 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 145 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.109765329295988 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 129 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1305 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 156 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.119540229885057 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -16 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1243 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 94 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0756234915526951 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -62 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Re-segment population | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1192 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 135 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.113255033557047 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1321 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 145 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.109765329295988 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 129 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1305 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 156 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.119540229885057 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -16 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1243 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 94 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0756234915526951 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -62 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 239425 | Data_Quality.xlsx/Completeness |
    | Populated Records | 231929 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.968691657095124 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 134436 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1518 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.988708381683478 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 29 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 26 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.896551724137931 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | E. Kamiński | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Nested Correspondent | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Virtual-Asset Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 3 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.3 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 77 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.51 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 37.73 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.3 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-11-12 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-11-12 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | E. Kamiński | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity E | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-11-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 4 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Re-segment population | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.95 Model 95 — Nested Correspondent

| **Model Code**                 | TM-CRYPTO-095                                                                             |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Virtual-Asset Family                                                                      |
| **Business Problem Solved**    | Hidden nested relationships in correspondent banking.                                     |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                         |
| **Typology Detected**          | Nested Correspondent — flags hidden nested relationships in correspondent banking.        |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity E)             |
| **Booking Entity / Segment**   | Entity E · Correspondent · Americas                                                       |
| **Accountable Owner**          | E. Kamiński                                                                               |
| **Lifecycle / Risk Tier**      | Validation · Tier 3 - Medium                                                              |
| **Primary Source System**      | TradeFinance-CTS                                                                          |
| **Linked Change Request(s)**   | —                                                                                         |
</functional_requirements>

<change_requests>
  <not provided>
</change_requests>

<estate_context>
  <sampling_methodology>
    ATL Sample Basis: Stratified random, 95% CI; BTL Sample Basis: Boundary band ±15% of threshold; Confidence Level: 99%
  </sampling_methodology>

  <relevant_coverage_gaps>
    - gap_id: GAP-004 | typology_/_segment: Corporate | gap_description: Nested correspondent typology single-model dependency | severity: Low | remediation_owner: 2nd LoD MRM | typology_segment: Corporate | description: Nested correspondent typology single-model dependency
    - gap_id: GAP-009 | typology_/_segment: Retail | gap_description: Nested correspondent typology single-model dependency | severity: Medium | remediation_owner: 2nd LoD MRM | typology_segment: Retail | description: Nested correspondent typology single-model dependency
    - gap_id: GAP-014 | typology_/_segment: Private Banking | gap_description: Nested correspondent typology single-model dependency | severity: Low | remediation_owner: 2nd LoD MRM | typology_segment: Private Banking | description: Nested correspondent typology single-model dependency
  </relevant_coverage_gaps>

</estate_context>

</model>