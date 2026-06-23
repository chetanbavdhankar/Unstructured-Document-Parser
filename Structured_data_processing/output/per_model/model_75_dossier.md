<model id="Model 75" code="TM-GEO-075">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 315 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2226 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 8 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 64085 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2541 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 66634 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.12396694214876 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.975232198142415 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.219972067039106 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.966430908898976 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2541 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 224 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0881542699724518 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 38.1336855058979 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.8 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.219972067039106 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0881542699724518 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.167244948212444 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 69 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 33 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 36 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.478260869565217 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 181 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 10 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 171 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0552486187845304 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2871 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 134 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0466736328805294 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2601 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 104 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0399846212995002 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -270 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2634 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 145 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0550493545937737 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 33 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2530 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 174 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0687747035573123 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -104 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Extend lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2871 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 134 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0466736328805294 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2601 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 104 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0399846212995002 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -270 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2634 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 145 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0550493545937737 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 33 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2530 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 174 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0687747035573123 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -104 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 323366 | Data_Quality.xlsx/Completeness |
    | Populated Records | 305095 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.943497461081252 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 58175 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1934 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.966755479157714 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 41 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 37 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.902439024390244 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.9 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | E. Kamiński | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Nested Correspondent | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Geographic-Risk Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 10 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 57 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.44 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 31.92 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.4 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-10-01 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-10-01 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | E. Kamiński | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity E | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-03-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 5 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Extend lookback window | direction: Reduce leakage | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.75 Model 75 — Nested Correspondent

| **Model Code**                 | TM-GEO-075                                                                             |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Geographic-Risk Family                                                                 |
| **Business Problem Solved**    | Hidden nested relationships in correspondent banking.                                  |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                      |
| **Typology Detected**          | Nested Correspondent — flags hidden nested relationships in correspondent banking.     |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity E)          |
| **Booking Entity / Segment**   | Entity E · Correspondent · Americas                                                    |
| **Accountable Owner**          | E. Kamiński                                                                            |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                           |
| **Primary Source System**      | CryptoGateway                                                                          |
| **Linked Change Request(s)**   | —                                                                                      |
</functional_requirements>

<change_requests>
  <not provided>
</change_requests>

<estate_context>
  <sampling_methodology>
    ATL Sample Basis: Stratified random, 95% CI; BTL Sample Basis: Boundary band ±15% of threshold; Confidence Level: 97.5%
  </sampling_methodology>

  <relevant_coverage_gaps>
    - gap_id: GAP-004 | typology_/_segment: Corporate | gap_description: Nested correspondent typology single-model dependency | severity: Low | remediation_owner: 2nd LoD MRM | typology_segment: Corporate | description: Nested correspondent typology single-model dependency
    - gap_id: GAP-009 | typology_/_segment: Retail | gap_description: Nested correspondent typology single-model dependency | severity: Medium | remediation_owner: 2nd LoD MRM | typology_segment: Retail | description: Nested correspondent typology single-model dependency
    - gap_id: GAP-014 | typology_/_segment: Private Banking | gap_description: Nested correspondent typology single-model dependency | severity: Low | remediation_owner: 2nd LoD MRM | typology_segment: Private Banking | description: Nested correspondent typology single-model dependency
  </relevant_coverage_gaps>

</estate_context>

</model>