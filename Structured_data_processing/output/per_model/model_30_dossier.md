<model id="Model 30" code="TM-BEHAV-030">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 159 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1652 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 29 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 64299 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1811 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 66139 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0877967973495307 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.845744680851064 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.159079539769885 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.974951100059135 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1811 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 96 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0530093870789619 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 27.3817263641724 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.66 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.159079539769885 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0530093870789619 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.116651478693516 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 46 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 18 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 28 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.391304347826087 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 94 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 4 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 90 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0425531914893617 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1587 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 82 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0516698172652804 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1635 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0648318042813456 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 48 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2047 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 192 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0937957987298486 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 412 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1586 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 141 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0889029003783102 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -461 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | No change - retain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1587 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 82 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0516698172652804 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1635 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0648318042813456 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 48 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2047 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 192 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0937957987298486 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 412 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1586 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 141 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0889029003783102 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -461 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 114018 | Data_Quality.xlsx/Completeness |
    | Populated Records | 105427 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.924652247890684 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 84987 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3783 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.955487309823855 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 55 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 54 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.981818181818182 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.1 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | J. Kozłowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Funnel Account | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Behavioural-Anomaly Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 1 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 56 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.75 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 14 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.7 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-01-03 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-01-03 | Model_Risk_Governance.xlsx/Lifecycle_Status |
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

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: No change - retain | direction: Maintain | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.30 Model 30 — Funnel Account

| **Model Code**                 | TM-BEHAV-030                                                                               |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Behavioural-Anomaly Family                                                                 |
| **Business Problem Solved**    | Many-to-one inflow with single rapid outflow.                                              |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.             |
| **Typology Detected**          | Funnel Account — flags many-to-one inflow with single rapid outflow.                       |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity J)              |
| **Booking Entity / Segment**   | Entity J · Correspondent · APAC                                                            |
| **Accountable Owner**          | J. Kozłowska                                                                               |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 2 - High                                                            |
| **Primary Source System**      | PaymentsHub-SWIFT                                                                          |
| **Linked Change Request(s)**   | —                                                                                          |
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