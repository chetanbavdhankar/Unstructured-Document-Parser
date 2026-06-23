<model id="Model 72" code="TM-NETWORK-072">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 491 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 412 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 91 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 84599 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 903 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 85593 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.5437430786268 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.843642611683849 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.661279461279461 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.995153568361741 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 903 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 314 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.347729789590255 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 10.5499281483299 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.82 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.661279461279461 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.347729789590255 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.535859592603779 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 53 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 7 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 46 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.132075471698113 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Review | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 82 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 2 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 80 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.024390243902439 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 783 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 72 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0919540229885058 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1036 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 67 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0646718146718147 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 253 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 858 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 68 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0792540792540793 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -178 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1008 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 53 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0525793650793651 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 150 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Add geography filter | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 783 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 72 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0919540229885058 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1036 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 67 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0646718146718147 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 253 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 858 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 68 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0792540792540793 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -178 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1008 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 53 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0525793650793651 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 150 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 55772 | Data_Quality.xlsx/Completeness |
    | Populated Records | 50194 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.899985655884673 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 51644 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1427 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.972368522964914 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 27 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 24 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.888888888888889 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.9 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | B. Nowak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | PEP Activity | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Network-Linkage Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 8 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.8 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 72 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.94 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 4.32 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.4 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-09-18 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-09-18 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | B. Nowak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity B | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-12-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Low | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Add geography filter | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.72 Model 72 — PEP Activity

| **Model Code**                 | TM-NETWORK-072                                                                             |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Network-Linkage Family                                                                     |
| **Business Problem Solved**    | Politically exposed person unusual flow.                                                   |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                  |
| **Typology Detected**          | PEP Activity — flags politically exposed person unusual flow.                              |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity B)                        |
| **Booking Entity / Segment**   | Entity B · SME · High-Risk Jurisdictions                                                   |
| **Accountable Owner**          | B. Nowak                                                                                   |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 4 - Low                                                             |
| **Primary Source System**      | PaymentsHub-SWIFT                                                                          |
| **Linked Change Request(s)**   | —                                                                                          |
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