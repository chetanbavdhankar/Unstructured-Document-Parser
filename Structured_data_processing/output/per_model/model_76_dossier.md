<model id="Model 76" code="TM-CASH-076">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 86 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2583 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 49 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 23193 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2669 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 25911 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0322218059198202 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.637037037037037 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.0613409415121255 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.899790502793296 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2669 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 65 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0243536905207943 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 103.00644513913 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.83 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.0613409415121255 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0243536905207943 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.046546041115593 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 113 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 97 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 16 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.858407079646018 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 147 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 2 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 145 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0136054421768707 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3198 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 342 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.106941838649156 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3069 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 179 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0583251873574454 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -129 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3127 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 328 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.104892868564119 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 58 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2619 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 191 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0729285987017946 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -508 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 3198 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 342 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.106941838649156 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 3069 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 179 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0583251873574454 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -129 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 3127 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 328 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.104892868564119 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 58 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2619 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 191 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0729285987017946 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -508 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 492672 | Data_Quality.xlsx/Completeness |
    | Populated Records | 487351 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.989199710963887 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 153117 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1981 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.987062181207835 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 93 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 81 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.870967741935484 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.2 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | KYC-Master | Data_Quality.xlsx/Lineage |
    | Secondary Feed | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | F. Zielińska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Shell Company Flow | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Cash-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 9 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.9 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 100 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.84 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 16 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.4 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-06-21 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-06-21 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | F. Zielińska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity F | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-04-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-015 | finding: Documentation gap in scenario logic | status: Closed | target_date: 2025-Q4 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-035 | finding: Calibration outside tolerance | status: In Remediation | target_date: 2025-Q4 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-025 | source_system: KYC-Master | issue_description: Currency code mismatch | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Shorten lookback window | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.76 Model 76 — Shell Company Flow

| **Model Code**                 | TM-CASH-076                                                                         |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                 |
| **Business Problem Solved**    | Flows through entities with no economic substance.                                  |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.           |
| **Typology Detected**          | Shell Company Flow — flags flows through entities with no economic substance.       |
| **Data Inputs**                | KYC-Master transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity F)              |
| **Booking Entity / Segment**   | Entity F · Retail · High-Risk Jurisdictions                                         |
| **Accountable Owner**          | F. Zielińska                                                                        |
| **Lifecycle / Risk Tier**      | Tuning · Tier 4 - Low                                                               |
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

  <relevant_coverage_gaps>None identified</relevant_coverage_gaps>

</estate_context>

</model>