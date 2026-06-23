<model id="Model 88" code="TM-NETWORK-088">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 565 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2197 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 68 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 58456 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2762 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 61286 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.204561911658219 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.892575039494471 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.332842415316642 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.963777554284207 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2762 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 277 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.100289645184649 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 45.0673889632216 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.66 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.332842415316642 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.100289645184649 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.239821307263845 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 71 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 66 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 5 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.929577464788732 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 74 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 12 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 62 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.162162162162162 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2787 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 204 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0731969860064586 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2938 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 305 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.103812117086453 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 151 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2521 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 138 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0547401824672749 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -417 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2608 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 293 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.112346625766871 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 87 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Add geography filter | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2787 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 204 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0731969860064586 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2938 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 305 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.103812117086453 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 151 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2521 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 138 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0547401824672749 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -417 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2608 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 293 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.112346625766871 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 87 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 178333 | Data_Quality.xlsx/Completeness |
    | Populated Records | 172207 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.965648533922493 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 150842 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 7660 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.949218387451771 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 45 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 41 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.911111111111111 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 2.9 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | H. Woźniak | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Velocity Anomaly | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Network-Linkage Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 4 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.4 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 55 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.67 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 18.15 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.2 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-10-25 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-10-25 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | H. Woźniak | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity H | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-04-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Add geography filter | direction: Maintain | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.88 Model 88 — Velocity Anomaly

| **Model Code**                 | TM-NETWORK-088                                                                            |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Network-Linkage Family                                                                    |
| **Business Problem Solved**    | Transaction frequency exceeds peer-group baseline.                                        |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                         |
| **Typology Detected**          | Velocity Anomaly — flags transaction frequency exceeds peer-group baseline.               |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity H)                 |
| **Booking Entity / Segment**   | Entity H · Corporate · High-Risk Jurisdictions                                            |
| **Accountable Owner**          | H. Woźniak                                                                                |
| **Lifecycle / Risk Tier**      | Tuning · Tier 4 - Low                                                                     |
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