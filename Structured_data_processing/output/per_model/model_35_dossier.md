<model id="Model 35" code="TM-GEO-035">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 227 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2502 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 92 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 54787 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2729 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 57608 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0831806522535727 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.711598746081505 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.148950131233596 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.95632669447887 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2729 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 120 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0439721509710517 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 47.3718927926677 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.84 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.148950131233596 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0439721509710517 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.106958939128578 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 44 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 6 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 38 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.136363636363636 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Review | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 193 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 11 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 182 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0569948186528497 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2532 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 237 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0936018957345972 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2502 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 172 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0687450039968026 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -30 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2787 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 265 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0950843200574094 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 285 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3027 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 145 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0479022134126198 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 240 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Extend lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2532 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 237 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0936018957345972 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2502 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 172 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0687450039968026 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -30 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2787 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 265 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0950843200574094 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 285 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 3027 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 145 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0479022134126198 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 240 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 64634 | Data_Quality.xlsx/Completeness |
    | Populated Records | 58647 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.907370733669586 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 41505 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 187 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.995494518732683 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Green | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 42 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 39 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.928571428571429 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | E. Kamiński | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Nested Correspondent | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Geographic-Risk Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 8 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.8 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 78 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.7 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 23.4 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.2 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-05-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-05-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | E. Kamiński | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity E | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-11-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 5 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Extend lookback window | direction: Reduce leakage | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.35 Model 35 — Nested Correspondent

| **Model Code**                 | TM-GEO-035                                                                                   |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Geographic-Risk Family                                                                       |
| **Business Problem Solved**    | Hidden nested relationships in correspondent banking.                                        |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                            |
| **Typology Detected**          | Nested Correspondent — flags hidden nested relationships in correspondent banking.           |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity E)                |
| **Booking Entity / Segment**   | Entity E · Correspondent · Americas                                                          |
| **Accountable Owner**          | E. Kamiński                                                                                  |
| **Lifecycle / Risk Tier**      | Validation · Tier 3 - Medium                                                                 |
| **Primary Source System**      | Sanctions-Screening                                                                          |
| **Linked Change Request(s)**   | —                                                                                            |
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