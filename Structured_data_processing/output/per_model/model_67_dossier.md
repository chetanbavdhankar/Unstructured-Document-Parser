<model id="Model 67" code="TM-GEO-067">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 303 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1463 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 94 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 45927 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1766 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 47787 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.171574178935447 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.763224181360202 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.280166435506241 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.969128508124077 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1766 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 115 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.065118912797282 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 36.955657396363 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.58 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.280166435506241 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.065118912797282 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.194147426422658 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 57 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 29 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 28 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.508771929824561 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 193 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 3 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 190 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0155440414507772 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1751 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0793832095945174 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1744 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 105 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0602064220183486 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -7 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1840 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 122 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.066304347826087 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 96 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2105 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 88 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0418052256532067 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 265 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Extend lookback window | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1751 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0793832095945174 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1744 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 105 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0602064220183486 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -7 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1840 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 122 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.066304347826087 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 96 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2105 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 88 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0418052256532067 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 265 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 320624 | Data_Quality.xlsx/Completeness |
    | Populated Records | 304581 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.949963196766306 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 148978 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 4670 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.968653089717945 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 73 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 66 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.904109589041096 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.7 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | G. Szymański | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Round-Amount Transactions | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Geographic-Risk Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 66 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.91 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 5.94 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.2 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-03-05 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-03-05 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | G. Szymański | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity G | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-07-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-038 | source_system: TradeFinance-CTS | issue_description: Late feed beyond SLA cut-off | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Extend lookback window | direction: Reduce leakage | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.67 Model 67 — Round-Amount Transactions

| **Model Code**                 | TM-GEO-067                                                                                |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Geographic-Risk Family                                                                    |
| **Business Problem Solved**    | Unusual frequency of round-figure transfers.                                              |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                 |
| **Typology Detected**          | Round-Amount Transactions — flags unusual frequency of round-figure transfers.            |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity G)                       |
| **Booking Entity / Segment**   | Entity G · SME · Americas                                                                 |
| **Accountable Owner**          | G. Szymański                                                                              |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                              |
| **Primary Source System**      | TradeFinance-CTS                                                                          |
| **Linked Change Request(s)**   | —                                                                                         |
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