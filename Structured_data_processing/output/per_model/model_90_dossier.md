<model id="Model 90" code="TM-RMF-090">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 107 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1665 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 39 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 54893 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1772 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 56704 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0603837471783296 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.732876712328767 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.111574556830031 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.970561193818735 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1772 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 76 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0428893905191874 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 31.25 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.84 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.111574556830031 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0428893905191874 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.0841004903056937 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 62 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 32 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 30 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.516129032258065 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 163 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 11 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 152 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0674846625766871 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1820 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 140 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0769230769230769 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1536 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 107 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0696614583333333 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -284 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1589 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 148 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0931403398363751 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 53 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1614 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 143 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0885997521685254 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 25 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Lower score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1820 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 140 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0769230769230769 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1536 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 107 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0696614583333333 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -284 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1589 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 148 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0931403398363751 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 53 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1614 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 143 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0885997521685254 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 25 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 94128 | Data_Quality.xlsx/Completeness |
    | Populated Records | 90499 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.961446115927248 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 56364 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 624 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.988929103683202 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 76 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 74 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.973684210526316 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3.2 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | KYC-Master | Data_Quality.xlsx/Lineage |
    | Secondary Feed | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | J. Kozłowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Funnel Account | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Rapid-Movement Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 2 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.2 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 98 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.54 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 45.08 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.8 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-10-08 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-10-08 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | J. Kozłowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity J | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-06-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 3 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-027 | source_system: KYC-Master | issue_description: Stale reference data | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Lower score threshold | direction: Reduce leakage | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.90 Model 90 — Funnel Account

| **Model Code**                 | TM-RMF-090                                                                          |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Rapid-Movement Family                                                               |
| **Business Problem Solved**    | Many-to-one inflow with single rapid outflow.                                       |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.           |
| **Typology Detected**          | Funnel Account — flags many-to-one inflow with single rapid outflow.                |
| **Data Inputs**                | KYC-Master transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity J)       |
| **Booking Entity / Segment**   | Entity J · Correspondent · APAC                                                     |
| **Accountable Owner**          | J. Kozłowska                                                                        |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 2 - High                                                     |
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