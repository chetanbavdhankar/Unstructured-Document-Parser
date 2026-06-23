<model id="Model 78" code="TM-BEHAV-078">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 418 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2998 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 29 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 55216 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 3416 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 58661 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.122365339578454 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.935123042505593 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.216412114936578 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.948500360737967 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 3416 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 189 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.055327868852459 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 58.2328974957809 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.51 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.216412114936578 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.055327868852459 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.15197841650293 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 118 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 97 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 21 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.822033898305085 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 109 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 9 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 100 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0825688073394496 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3371 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 333 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0987837436962326 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2870 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 276 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0961672473867596 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -501 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2784 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 118 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0423850574712644 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -86 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3003 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 327 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.108891108891109 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 219 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | No change - retain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 3371 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 333 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0987837436962326 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2870 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 276 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0961672473867596 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -501 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2784 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 118 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0423850574712644 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -86 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 3003 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 327 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.108891108891109 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 219 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 492806 | Data_Quality.xlsx/Completeness |
    | Populated Records | 461816 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.937115213694639 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 68635 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3406 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.950375173016682 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 26 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 25 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.961538461538462 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.3 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | H. Woźniak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Wire Stripping | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Behavioural-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 9 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.9 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 58 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.4 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 34.8 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.8 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-12-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-12-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | H. Woźniak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity H | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-06-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 3 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-011 | source_system: CoreBanking-T24 | issue_description: Currency code mismatch | status: Closed | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: No change - retain | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.78 Model 78 — Wire Stripping

| **Model Code**                 | TM-BEHAV-078                                                                             |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Behavioural-Anomaly Family                                                               |
| **Business Problem Solved**    | Removal of originator data in cross-border wires.                                        |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                        |
| **Typology Detected**          | Wire Stripping — flags removal of originator data in cross-border wires.                 |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity H)                |
| **Booking Entity / Segment**   | Entity H · Corporate · APAC                                                              |
| **Accountable Owner**          | H. Woźniak                                                                               |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 2 - High                                                          |
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

  <relevant_coverage_gaps>None identified</relevant_coverage_gaps>

</estate_context>

</model>