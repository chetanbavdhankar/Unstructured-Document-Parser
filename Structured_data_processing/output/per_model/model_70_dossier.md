<model id="Model 70" code="TM-BEHAV-070">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 357 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1630 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 85 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 20343 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1987 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 22415 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.179667840966281 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.807692307692308 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.293948126801153 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.925818049424294 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1987 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 236 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.118772018117765 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 88.6459959848316 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.54 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.293948126801153 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.118772018117765 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.223877683327798 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 83 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 52 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 31 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.626506024096386 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 186 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 1 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 185 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.00537634408602151 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2118 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 226 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.106704438149197 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2353 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 108 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0458988525286868 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 235 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2120 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 97 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0457547169811321 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -233 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1654 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 92 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0556227327690447 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -466 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | No change - retain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2118 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 226 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.106704438149197 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2353 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 108 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0458988525286868 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 235 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2120 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 97 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0457547169811321 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -233 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1654 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 92 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0556227327690447 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -466 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 243985 | Data_Quality.xlsx/Completeness |
    | Populated Records | 225119 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.922675574318093 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 106989 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3733 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.965108562562506 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 109 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 97 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.889908256880734 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5.8 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
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
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 3 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.3 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 95 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.48 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 49.4 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.4 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-11-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-11-11 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | J. Kozłowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity J | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-10-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: No change - retain | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.70 Model 70 — Funnel Account

| **Model Code**                 | TM-BEHAV-070                                                                                 |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Behavioural-Anomaly Family                                                                   |
| **Business Problem Solved**    | Many-to-one inflow with single rapid outflow.                                                |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                            |
| **Typology Detected**          | Funnel Account — flags many-to-one inflow with single rapid outflow.                         |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity J)                |
| **Booking Entity / Segment**   | Entity J · Correspondent · APAC                                                              |
| **Accountable Owner**          | J. Kozłowska                                                                                 |
| **Lifecycle / Risk Tier**      | Tuning · Tier 2 - High                                                                       |
| **Primary Source System**      | Sanctions-Screening                                                                          |
| **Linked Change Request(s)**   | —                                                                                            |
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