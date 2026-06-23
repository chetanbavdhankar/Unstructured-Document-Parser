<model id="Model 43" code="TM-GEO-043">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 495 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1149 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 27 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 33633 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1644 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 35304 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.301094890510949 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.948275862068966 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.457063711911357 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.966965671899258 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1644 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 262 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.159367396593674 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 46.5669612508498 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.56 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.457063711911357 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.159367396593674 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.337985185784284 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 47 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 38 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 9 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.808510638297872 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 93 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 1 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 92 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.010752688172043 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1922 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 163 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0848074921956296 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1400 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 128 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0914285714285714 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -522 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1967 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 200 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.101677681748856 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 567 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1667 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 72 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0431913617276545 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -300 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Extend lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1922 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 163 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0848074921956296 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1400 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 128 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0914285714285714 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -522 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1967 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 200 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.101677681748856 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 567 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1667 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 72 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0431913617276545 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -300 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 200921 | Data_Quality.xlsx/Completeness |
    | Populated Records | 199327 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.992066533612714 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 137492 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2544 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.981497105286126 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 59 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 51 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.864406779661017 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | C. Lewandowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | High-Risk Jurisdiction | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Geographic-Risk Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 6 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.6 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 58 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.66 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 19.72 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.6 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-10-26 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-10-26 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | C. Lewandowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity C | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-07-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-006 | source_system: CoreBanking-T24 | issue_description: Stale reference data | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Extend lookback window | direction: Reduce leakage | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.43 Model 43 — High-Risk Jurisdiction

| **Model Code**                 | TM-GEO-043                                                                               |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Geographic-Risk Family                                                                   |
| **Business Problem Solved**    | Exposure to FATF grey/black-list geographies.                                            |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                |
| **Typology Detected**          | High-Risk Jurisdiction — flags exposure to FATF grey/black-list geographies.             |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity C)                |
| **Booking Entity / Segment**   | Entity C · Corporate · Americas                                                          |
| **Accountable Owner**          | C. Lewandowska                                                                           |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                             |
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
    - gap_id: GAP-005 | typology_/_segment: SME | gap_description: High-risk jurisdiction logic disabled on 22 models | severity: High | remediation_owner: AML Tuning Team | typology_segment: SME | description: High-risk jurisdiction logic disabled on 22 models
    - gap_id: GAP-006 | typology_/_segment: High-Risk Jurisdictions | gap_description: No model tuned for Private Banking segment in APAC | severity: Low | remediation_owner: AML Tuning Team | typology_segment: High-Risk Jurisdictions | description: No model tuned for Private Banking segment in APAC
    - gap_id: GAP-007 | typology_/_segment: High-Risk Jurisdictions | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: Medium | remediation_owner: 1st LoD | typology_segment: High-Risk Jurisdictions | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-010 | typology_/_segment: Americas | gap_description: High-risk jurisdiction logic disabled on 22 models | severity: High | remediation_owner: 1st LoD | typology_segment: Americas | description: High-risk jurisdiction logic disabled on 22 models
    - gap_id: GAP-015 | typology_/_segment: Americas | gap_description: High-risk jurisdiction logic disabled on 22 models | severity: Low | remediation_owner: AML Tuning Team | typology_segment: Americas | description: High-risk jurisdiction logic disabled on 22 models
    - gap_id: GAP-016 | typology_/_segment: High-Risk Jurisdictions | gap_description: No model tuned for Private Banking segment in APAC | severity: Medium | remediation_owner: 1st LoD | typology_segment: High-Risk Jurisdictions | description: No model tuned for Private Banking segment in APAC
  </relevant_coverage_gaps>

</estate_context>

</model>