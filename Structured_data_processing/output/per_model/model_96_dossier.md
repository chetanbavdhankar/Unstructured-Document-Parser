<model id="Model 96" code="TM-NETWORK-096">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 101 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 945 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 62 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 23301 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1046 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 24409 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0965583173996176 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.619631901840491 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.167080231596361 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.961024498886414 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1046 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 59 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0564053537284895 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 42.8530460076201 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.8 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.167080231596361 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0564053537284895 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.122810280449212 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 107 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 84 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 23 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.785046728971963 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 199 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 6 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 193 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0301507537688442 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1197 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 105 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.087719298245614 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 938 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 61 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0650319829424307 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -259 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1125 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 47 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0417777777777778 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 187 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1234 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 127 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.10291734197731 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 109 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Add geography filter | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1197 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 105 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.087719298245614 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 938 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 61 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0650319829424307 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -259 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1125 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 47 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0417777777777778 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 187 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1234 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 127 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.10291734197731 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 109 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 220817 | Data_Quality.xlsx/Completeness |
    | Populated Records | 220187 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.997146958793933 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 146552 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2292 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.984360500027294 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 53 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 52 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.981132075471698 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 6 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | F. Zielińska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Shell Company Flow | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Network-Linkage Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 10 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 59 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.65 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 20.65 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.2 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-08-21 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-08-21 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | F. Zielińska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity F | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-12-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 5 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-019 | finding: Threshold not re-tuned within policy window | status: Closed | target_date: 2025-Q4 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Add geography filter | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.96 Model 96 — Shell Company Flow

| **Model Code**                 | TM-NETWORK-096                                                                         |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Network-Linkage Family                                                                 |
| **Business Problem Solved**    | Flows through entities with no economic substance.                                     |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                      |
| **Typology Detected**          | Shell Company Flow — flags flows through entities with no economic substance.          |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity F)                 |
| **Booking Entity / Segment**   | Entity F · Retail · High-Risk Jurisdictions                                            |
| **Accountable Owner**          | F. Zielińska                                                                           |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 4 - Low                                                         |
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

  <relevant_coverage_gaps>None identified</relevant_coverage_gaps>

</estate_context>

</model>