<model id="Model 55" code="TM-CRYPTO-055">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 304 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1454 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 58 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 30790 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1758 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 32606 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.17292377701934 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.839779005524862 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.286792452830189 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.954906339163876 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1758 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 115 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.065415244596132 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 53.9164570937864 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.83 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.286792452830189 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.065415244596132 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.198241569536566 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 48 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 23 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 25 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.479166666666667 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 84 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 9 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 75 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.107142857142857 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1469 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 173 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.117767188563649 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1940 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 200 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.103092783505155 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 471 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1678 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 197 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.117401668653159 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -262 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1907 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 222 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.116413214472994 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 229 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Re-segment population | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1469 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 173 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.117767188563649 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1940 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 200 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.103092783505155 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 471 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1678 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 197 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.117401668653159 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -262 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1907 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 222 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.116413214472994 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 229 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 423347 | Data_Quality.xlsx/Completeness |
    | Populated Records | 406426 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.960030424214651 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 65673 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1134 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.982732629847883 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 52 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 44 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.846153846153846 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | KYC-Master | Data_Quality.xlsx/Lineage |
    | Secondary Feed | Sanctions-Screening | Data_Quality.xlsx/Lineage |
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
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 57 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.84 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 9.12 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-05-24 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-05-24 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | E. Kamiński | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity E | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-07-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-022 | source_system: KYC-Master | issue_description: Null counterparty IDs in feed | status: Closed | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Re-segment population | direction: Maintain | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.55 Model 55 — Nested Correspondent

| **Model Code**                 | TM-CRYPTO-055                                                                       |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Virtual-Asset Family                                                                |
| **Business Problem Solved**    | Hidden nested relationships in correspondent banking.                               |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.      |
| **Typology Detected**          | Nested Correspondent — flags hidden nested relationships in correspondent banking.  |
| **Data Inputs**                | KYC-Master transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity E)       |
| **Booking Entity / Segment**   | Entity E · Correspondent · Americas                                                 |
| **Accountable Owner**          | E. Kamiński                                                                         |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                        |
| **Primary Source System**      | KYC-Master                                                                          |
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
    - gap_id: GAP-004 | typology_/_segment: Corporate | gap_description: Nested correspondent typology single-model dependency | severity: Low | remediation_owner: 2nd LoD MRM | typology_segment: Corporate | description: Nested correspondent typology single-model dependency
    - gap_id: GAP-009 | typology_/_segment: Retail | gap_description: Nested correspondent typology single-model dependency | severity: Medium | remediation_owner: 2nd LoD MRM | typology_segment: Retail | description: Nested correspondent typology single-model dependency
    - gap_id: GAP-014 | typology_/_segment: Private Banking | gap_description: Nested correspondent typology single-model dependency | severity: Low | remediation_owner: 2nd LoD MRM | typology_segment: Private Banking | description: Nested correspondent typology single-model dependency
  </relevant_coverage_gaps>

</estate_context>

</model>