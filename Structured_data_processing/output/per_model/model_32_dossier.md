<model id="Model 32" code="TM-NETWORK-032">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 304 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2767 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 85 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 40987 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 3071 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 44143 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0989905568218821 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.781491002570694 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.175722543352601 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.936760067650958 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 3071 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 125 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.040703353956366 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 69.569354144485 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.68 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.175722543352601 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.040703353956366 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.121714867594107 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 106 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 27 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 79 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.254716981132075 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 82 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 2 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 80 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.024390243902439 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3214 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 184 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0572495332918482 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2617 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 251 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0959113488727551 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -597 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3311 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 279 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0842645726366657 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 694 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3283 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 192 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0584830947304295 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -28 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Add geography filter | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 3214 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 184 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0572495332918482 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2617 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 251 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0959113488727551 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -597 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 3311 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 279 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0842645726366657 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 694 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 3283 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 192 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0584830947304295 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -28 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 377281 | Data_Quality.xlsx/Completeness |
    | Populated Records | 369279 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.978790344597263 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 194934 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2734 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.985974740168467 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 112 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 103 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.919642857142857 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.1 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | B. Nowak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | PEP Activity | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Network-Linkage Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 8 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.8 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 80 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.56 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 35.2 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.6 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-03-27 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-03-27 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | B. Nowak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity B | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-08-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 5 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-033 | source_system: TradeFinance-CTS | issue_description: Truncated narrative field | status: In Progress | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Add geography filter | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.32 Model 32 — PEP Activity

| **Model Code**                 | TM-NETWORK-032                                                                            |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Network-Linkage Family                                                                    |
| **Business Problem Solved**    | Politically exposed person unusual flow.                                                  |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                         |
| **Typology Detected**          | PEP Activity — flags politically exposed person unusual flow.                             |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity B)                       |
| **Booking Entity / Segment**   | Entity B · SME · High-Risk Jurisdictions                                                  |
| **Accountable Owner**          | B. Nowak                                                                                  |
| **Lifecycle / Risk Tier**      | Production · Tier 4 - Low                                                                 |
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