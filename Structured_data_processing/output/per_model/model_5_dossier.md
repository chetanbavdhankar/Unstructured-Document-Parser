<model id="Model 5" code="TM-TBML-005">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 580 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2959 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 83 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 65185 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 3539 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 68807 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.163888103984176 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.874811463046757 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.276059019514517 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.956577248180324 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 3539 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 347 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0980502966939814 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 51.433720406354 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.61 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.276059019514517 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0980502966939814 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.204855530386303 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 41 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 21 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 20 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.51219512195122 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 116 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 10 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 106 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0862068965517241 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 4180 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 377 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0901913875598086 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2917 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 322 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.110387384298937 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -1263 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3090 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 312 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.100970873786408 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 173 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3041 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 348 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.114436040776061 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -49 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Tighten min-amount floor | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 4180 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 377 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0901913875598086 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2917 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 322 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.110387384298937 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -1263 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 3090 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 312 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.100970873786408 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 173 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 3041 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 348 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.114436040776061 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -49 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 245965 | Data_Quality.xlsx/Completeness |
    | Populated Records | 238447 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.969434675665237 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 62349 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2267 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.963640154613546 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 35 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 32 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.914285714285714 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.9 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | E. Kamiński | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Trade-Based ML | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Trade-Based Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 72 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.5 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 36 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.8 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-10-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-10-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | E. Kamiński | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity E | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-05-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Tighten min-amount floor | direction: Reduce FP | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.5 Model 5 — Trade-Based ML

| **Model Code**                 | TM-TBML-005                                                                            |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Trade-Based Family                                                                     |
| **Business Problem Solved**    | Over/under-invoicing and phantom shipment indicators.                                  |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.              |
| **Typology Detected**          | Trade-Based ML — flags over/under-invoicing and phantom shipment indicators.           |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity E)          |
| **Booking Entity / Segment**   | Entity E · Correspondent · EMEA                                                        |
| **Accountable Owner**          | E. Kamiński                                                                            |
| **Lifecycle / Risk Tier**      | Validation · Tier 1 - Critical                                                         |
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
    - gap_id: GAP-003 | typology_/_segment: APAC | gap_description: Trade-based ML weak in Americas corridor | severity: Low | remediation_owner: 2nd LoD MRM | typology_segment: APAC | description: Trade-based ML weak in Americas corridor
    - gap_id: GAP-008 | typology_/_segment: Correspondent | gap_description: Trade-based ML weak in Americas corridor | severity: Low | remediation_owner: AML Tuning Team | typology_segment: Correspondent | description: Trade-based ML weak in Americas corridor
    - gap_id: GAP-013 | typology_/_segment: Americas | gap_description: Trade-based ML weak in Americas corridor | severity: Low | remediation_owner: AML Tuning Team | typology_segment: Americas | description: Trade-based ML weak in Americas corridor
    - gap_id: GAP-018 | typology_/_segment: SME | gap_description: Trade-based ML weak in Americas corridor | severity: High | remediation_owner: 1st LoD | typology_segment: SME | description: Trade-based ML weak in Americas corridor
  </relevant_coverage_gaps>

</estate_context>

</model>