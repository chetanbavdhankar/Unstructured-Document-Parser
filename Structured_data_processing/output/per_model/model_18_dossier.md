<model id="Model 18" code="TM-RMF-018">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 490 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 283 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 112 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 36059 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 773 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 36944 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.633893919793014 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.813953488372093 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.712727272727273 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.99221286665566 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 773 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 374 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.483829236739974 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 20.9235599826765 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.77 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.712727272727273 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.483829236739974 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.621168058332353 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 40 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 38 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 2 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.95 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 193 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 8 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 185 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0414507772020725 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 824 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 67 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0813106796116505 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 804 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 49 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0609452736318408 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -20 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 858 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 42 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.048951048951049 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 54 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 623 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 49 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0786516853932584 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -235 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Lower score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 824 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 67 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0813106796116505 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 804 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 49 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0609452736318408 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -20 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 858 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 42 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.048951048951049 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 54 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 623 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 49 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0786516853932584 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -235 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 123648 | Data_Quality.xlsx/Completeness |
    | Populated Records | 119304 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.96486801242236 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 43754 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2366 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.94592494400512 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 26 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 23 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.884615384615385 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.8 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | H. Woźniak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Wire Stripping | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Rapid-Movement Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 9 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.9 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 57 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.4 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 34.2 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.3 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-05-27 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-05-27 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | H. Woźniak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity H | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-06-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 5 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-031 | source_system: TradeFinance-CTS | issue_description: Late feed beyond SLA cut-off | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Lower score threshold | direction: Reduce leakage | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.18 Model 18 — Wire Stripping

| **Model Code**                 | TM-RMF-018                                                                                |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Rapid-Movement Family                                                                     |
| **Business Problem Solved**    | Removal of originator data in cross-border wires.                                         |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                         |
| **Typology Detected**          | Wire Stripping — flags removal of originator data in cross-border wires.                  |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity H)                 |
| **Booking Entity / Segment**   | Entity H · Corporate · APAC                                                               |
| **Accountable Owner**          | H. Woźniak                                                                                |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 2 - High                                                           |
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