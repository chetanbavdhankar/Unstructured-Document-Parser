<model id="Model 4" code="TM-CASH-004">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 282 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 604 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 97 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 36969 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 886 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 37952 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.318284424379233 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.744063324538259 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.445849802371542 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.983924626726639 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 886 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 126 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.142212189616253 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 23.3452782462057 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.58 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.445849802371542 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.142212189616253 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.324394757269426 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 61 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 13 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 48 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.213114754098361 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 93 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 12 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 81 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.129032258064516 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 794 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 48 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0604534005037783 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1007 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 47 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0466732869910626 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 213 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 710 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 81 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.114084507042254 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -297 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1005 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 50 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0497512437810945 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 295 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Shorten lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 794 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 48 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0604534005037783 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1007 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 47 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0466732869910626 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 213 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 710 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 81 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.114084507042254 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -297 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1005 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 50 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0497512437810945 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 295 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 302661 | Data_Quality.xlsx/Completeness |
    | Populated Records | 280041 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.925262917918067 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 51750 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1866 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.963942028985507 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 59 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 55 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.932203389830508 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3.9 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | D. Wójcik | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Cash-Intensive Business | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Cash-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Private Banking | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 1 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 93 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.52 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 44.64 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.1 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-10-18 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-10-18 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | D. Wójcik | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity D | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-04-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-029 | source_system: TradeFinance-CTS | issue_description: Null counterparty IDs in feed | status: Closed | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Shorten lookback window | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.4 Model 4 — Cash-Intensive Business

| **Model Code**                 | TM-CASH-004                                                                               |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Cash-Anomaly Family                                                                       |
| **Business Problem Solved**    | Cash activity inconsistent with business profile.                                         |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                 |
| **Typology Detected**          | Cash-Intensive Business — flags cash activity inconsistent with business profile.         |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity D)           |
| **Booking Entity / Segment**   | Entity D · Private Banking · High-Risk Jurisdictions                                      |
| **Accountable Owner**          | D. Wójcik                                                                                 |
| **Lifecycle / Risk Tier**      | Tuning · Tier 4 - Low                                                                     |
| **Primary Source System**      | TradeFinance-CTS                                                                          |
| **Linked Change Request(s)**   | —                                                                                         |
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