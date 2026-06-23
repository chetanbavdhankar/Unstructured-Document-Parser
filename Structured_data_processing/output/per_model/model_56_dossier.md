<model id="Model 56" code="TM-NETWORK-056">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 181 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1822 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 99 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 40121 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2003 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 42223 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.09036445332002 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.646428571428572 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.15856329391152 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.956560093460172 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2003 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 121 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0604093859211183 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 47.4385998152666 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.58 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.15856329391152 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0604093859211183 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.119301730715359 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 52 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 16 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 36 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.307692307692308 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 62 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 6 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 56 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0967741935483871 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1786 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 82 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0459126539753639 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1650 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 73 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0442424242424242 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -136 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2107 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 148 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0702420503084955 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 457 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2186 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 133 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0608417200365965 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 79 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Add geography filter | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1786 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 82 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0459126539753639 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1650 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 73 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0442424242424242 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -136 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2107 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 148 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0702420503084955 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 457 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2186 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 133 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0608417200365965 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 79 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 436119 | Data_Quality.xlsx/Completeness |
    | Populated Records | 436067 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.999880766488046 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 97990 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 294 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.996999693846311 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Green | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 53 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 52 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.981132075471698 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.6 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | F. Zielińska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Shell Company Flow | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Network-Linkage Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 5 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.5 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 85 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.64 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 30.6 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.0 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-09-08 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-09-08 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | F. Zielińska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity F | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-08-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-011 | finding: Calibration outside tolerance | status: Open | target_date: 2025-Q4 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-031 | finding: Threshold not re-tuned within policy window | status: In Remediation | target_date: 2025-Q4 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Add geography filter | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.56 Model 56 — Shell Company Flow

| **Model Code**                 | TM-NETWORK-056                                                                               |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Network-Linkage Family                                                                       |
| **Business Problem Solved**    | Flows through entities with no economic substance.                                           |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                    |
| **Typology Detected**          | Shell Company Flow — flags flows through entities with no economic substance.                |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity F)                       |
| **Booking Entity / Segment**   | Entity F · Retail · High-Risk Jurisdictions                                                  |
| **Accountable Owner**          | F. Zielińska                                                                                 |
| **Lifecycle / Risk Tier**      | Production · Tier 4 - Low                                                                    |
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

  <relevant_coverage_gaps>None identified</relevant_coverage_gaps>

</estate_context>

</model>