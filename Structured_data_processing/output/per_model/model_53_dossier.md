<model id="Model 53" code="TM-TBML-053">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 480 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 655 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 24 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 36438 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1135 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 37597 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.422907488986784 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.952380952380952 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.585723001830384 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.982341681718923 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1135 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 306 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.269603524229075 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 30.1885788759741 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.64 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.585723001830384 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.269603524229075 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.459275210789861 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 82 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 20 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 62 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.24390243902439 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 131 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 6 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 125 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0458015267175573 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1056 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 54 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0511363636363636 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1188 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 95 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.07996632996633 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 132 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1159 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 100 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0862812769628991 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -29 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1269 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 98 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0772261623325453 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 110 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Tighten min-amount floor | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1056 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 54 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0511363636363636 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1188 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 95 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.07996632996633 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 132 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1159 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 100 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0862812769628991 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -29 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1269 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 98 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0772261623325453 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 110 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 111486 | Data_Quality.xlsx/Completeness |
    | Populated Records | 105609 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.947284860879393 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 98780 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 5060 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.948775055679287 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 37 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 35 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.945945945945946 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.1 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | C. Lewandowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Sanctions Proximity | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Trade-Based Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 3 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.3 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 79 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.74 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 20.54 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.6 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-11-22 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-11-22 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | C. Lewandowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity C | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-05-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 5 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-036 | source_system: TradeFinance-CTS | issue_description: Null counterparty IDs in feed | status: Closed | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Tighten min-amount floor | direction: Reduce FP | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.53 Model 53 — Sanctions Proximity

| **Model Code**                 | TM-TBML-053                                                                               |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Trade-Based Family                                                                        |
| **Business Problem Solved**    | Counterparty proximity to sanctioned entities.                                            |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                 |
| **Typology Detected**          | Sanctions Proximity — flags counterparty proximity to sanctioned entities.                |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity C)                 |
| **Booking Entity / Segment**   | Entity C · Corporate · EMEA                                                               |
| **Accountable Owner**          | C. Lewandowska                                                                            |
| **Lifecycle / Risk Tier**      | Validation · Tier 1 - Critical                                                            |
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