<model id="Model 85" code="TM-TBML-085">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 216 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2427 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 14 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 69739 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2643 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 72396 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0817253121452894 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.939130434782609 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.15036547163244 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.966369204334451 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2643 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 131 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0495648883844117 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 36.5075418531411 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.47 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.15036547163244 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0495648883844117 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.110045238333229 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 38 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 37 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 1 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.973684210526316 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 183 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 11 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 172 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0601092896174863 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2133 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 190 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0890764181903423 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2831 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 216 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0762981278700106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 698 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2400 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 206 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0858333333333333 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -431 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2382 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 179 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0751469353484467 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -18 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Tighten min-amount floor | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2133 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 190 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0890764181903423 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2831 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 216 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0762981278700106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 698 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2400 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 206 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0858333333333333 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -431 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2382 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 179 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0751469353484467 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -18 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 221437 | Data_Quality.xlsx/Completeness |
    | Populated Records | 214522 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.968772156414691 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 159501 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 827 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.994815079529282 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Green | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 46 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 40 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.869565217391304 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | E. Kamiński | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Trade-Based ML | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Trade-Based Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 10 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 61 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.71 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 17.69 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.3 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-05-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-05-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | E. Kamiński | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity E | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-01-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-012 | source_system: CoreBanking-T24 | issue_description: Truncated narrative field | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Tighten min-amount floor | direction: Reduce FP | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.85 Model 85 — Trade-Based ML

| **Model Code**                 | TM-TBML-085                                                                              |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Trade-Based Family                                                                       |
| **Business Problem Solved**    | Over/under-invoicing and phantom shipment indicators.                                    |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.           |
| **Typology Detected**          | Trade-Based ML — flags over/under-invoicing and phantom shipment indicators.             |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity E)            |
| **Booking Entity / Segment**   | Entity E · Correspondent · EMEA                                                          |
| **Accountable Owner**          | E. Kamiński                                                                              |
| **Lifecycle / Risk Tier**      | Production · Tier 1 - Critical                                                           |
| **Primary Source System**      | CoreBanking-T24                                                                          |
| **Linked Change Request(s)**   | —                                                                                        |
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