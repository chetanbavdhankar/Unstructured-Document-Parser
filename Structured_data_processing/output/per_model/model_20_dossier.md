<model id="Model 20" code="TM-CASH-020">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 69 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1124 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 102 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 21616 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1193 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 22911 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.057837384744342 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.403508771929825 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.101173020527859 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.950571679859279 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1193 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 49 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0410729253981559 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 52.0710575705993 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.53 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.101173020527859 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0410729253981559 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.0771329824759779 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 41 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 35 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 6 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.853658536585366 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 55 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 1 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 54 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0181818181818182 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1394 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 152 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.109038737446198 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1391 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 99 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0711718188353702 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -3 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1053 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 91 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0864197530864198 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -338 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1087 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 108 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0993560257589696 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 34 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1394 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 152 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.109038737446198 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1391 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 99 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0711718188353702 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -3 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1053 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 91 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0864197530864198 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -338 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1087 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 108 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0993560257589696 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 34 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 490012 | Data_Quality.xlsx/Completeness |
    | Populated Records | 485453 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.990696146216827 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 105625 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 5047 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.95221775147929 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 120 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 117 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.975 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | KYC-Master | Data_Quality.xlsx/Lineage |
    | Secondary Feed | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | J. Kozłowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Layering via Securities | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Cash-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
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
    | Inherent Risk Score | 61 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.8 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 12.2 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.1 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-09-10 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-09-10 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | J. Kozłowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity J | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-08-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-017 | source_system: KYC-Master | issue_description: Late feed beyond SLA cut-off | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Shorten lookback window | direction: Maintain | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.20 Model 20 — Layering via Securities

| **Model Code**                 | TM-CASH-020                                                                         |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                 |
| **Business Problem Solved**    | Round-trip securities trades for obfuscation.                                       |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.      |
| **Typology Detected**          | Layering via Securities — flags round-trip securities trades for obfuscation.       |
| **Data Inputs**                | KYC-Master transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity J)       |
| **Booking Entity / Segment**   | Entity J · Correspondent · High-Risk Jurisdictions                                  |
| **Accountable Owner**          | J. Kozłowska                                                                        |
| **Lifecycle / Risk Tier**      | Production · Tier 4 - Low                                                           |
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