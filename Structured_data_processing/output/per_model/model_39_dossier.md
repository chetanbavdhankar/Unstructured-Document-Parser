<model id="Model 39" code="TM-CRYPTO-039">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 430 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2610 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 77 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 71146 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 3040 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 74263 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.141447368421053 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.848126232741617 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.242458415562447 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.964613048429958 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 3040 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 188 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0618421052631579 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 40.9355937680945 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.71 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.242458415562447 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0618421052631579 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.170211891442731 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 84 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 16 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 68 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.19047619047619 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Review | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 196 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 11 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 185 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0561224489795918 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3166 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 374 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.118130132659507 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3640 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 226 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0620879120879121 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 474 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3520 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 178 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0505681818181818 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -120 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3510 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 376 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.107122507122507 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -10 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Re-segment population | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 3166 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 374 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.118130132659507 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 3640 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 226 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0620879120879121 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 474 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 3520 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 178 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0505681818181818 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -120 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 3510 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 376 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.107122507122507 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -10 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 480023 | Data_Quality.xlsx/Completeness |
    | Populated Records | 445942 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.929001318686813 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 42976 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2118 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.950716679076694 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 20 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 17 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.85 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | I. Dąbrowski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | ATM Cycling | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Virtual-Asset Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Private Banking | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 2 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.2 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 89 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.81 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 16.91 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.4 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-09-26 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-09-26 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | I. Dąbrowski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity I | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-03-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 4 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-034 | source_system: TradeFinance-CTS | issue_description: Stale reference data | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Re-segment population | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.39 Model 39 — ATM Cycling

| **Model Code**                 | TM-CRYPTO-039                                                                             |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Virtual-Asset Family                                                                      |
| **Business Problem Solved**    | Geographically dispersed rapid ATM withdrawals.                                           |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                 |
| **Typology Detected**          | ATM Cycling — flags geographically dispersed rapid ATM withdrawals.                       |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity I)           |
| **Booking Entity / Segment**   | Entity I · Private Banking · Americas                                                     |
| **Accountable Owner**          | I. Dąbrowski                                                                              |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                              |
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