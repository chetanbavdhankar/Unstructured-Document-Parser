<model id="Model 15" code="TM-CRYPTO-015">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 488 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1758 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 65 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 44009 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2246 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 46320 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.217275155832591 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.88245931283906 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.348695962843873 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.961588043787008 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2246 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 318 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.141585040071238 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 48.4887737478411 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.56 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.348695962843873 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.141585040071238 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.265851593734819 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 49 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 34 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 15 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.693877551020408 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 163 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 3 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 160 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0184049079754601 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2642 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 242 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0915972747918244 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2186 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 202 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0924062214089662 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -456 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1869 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 200 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.107009095773141 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -317 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2449 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 195 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0796243364638628 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 580 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Re-segment population | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2642 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 242 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0915972747918244 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2186 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 202 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0924062214089662 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -456 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1869 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 200 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.107009095773141 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -317 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2449 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 195 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0796243364638628 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 580 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 59685 | Data_Quality.xlsx/Completeness |
    | Populated Records | 54835 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.918740051939348 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 32470 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 660 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.979673544810594 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 37 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 33 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.891891891891892 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3.6 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | E. Kamiński | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Nested Correspondent | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Virtual-Asset Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 2 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.2 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 98 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.82 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 17.64 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.8 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-03-04 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-03-04 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | E. Kamiński | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity E | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-03-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Low | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-002 | source_system: CoreBanking-T24 | issue_description: Duplicate transaction records | status: Closed | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Re-segment population | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.15 Model 15 — Nested Correspondent

| **Model Code**                 | TM-CRYPTO-015                                                                            |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Virtual-Asset Family                                                                     |
| **Business Problem Solved**    | Hidden nested relationships in correspondent banking.                                    |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                        |
| **Typology Detected**          | Nested Correspondent — flags hidden nested relationships in correspondent banking.       |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity E)            |
| **Booking Entity / Segment**   | Entity E · Correspondent · Americas                                                      |
| **Accountable Owner**          | E. Kamiński                                                                              |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                             |
| **Primary Source System**      | CoreBanking-T24                                                                          |
| **Linked Change Request(s)**   | —                                                                                        |
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