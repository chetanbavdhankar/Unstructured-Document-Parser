<model id="Model 80" code="TM-NETWORK-080">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 145 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1531 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 67 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 37956 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1676 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 39699 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0865155131264917 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.683962264150943 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.153601694915254 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.961227745840403 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1676 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 63 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0375894988066826 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 42.2176881029749 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.81 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.153601694915254 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0375894988066826 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.107196816471826 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 116 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 96 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 20 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.827586206896552 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 63 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 5 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 58 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0793650793650794 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1521 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 167 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.109796186719264 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1589 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 111 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0698552548772813 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 68 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1639 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 144 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0878584502745577 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 50 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1627 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 126 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0774431468961278 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -12 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Add geography filter | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1521 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 167 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.109796186719264 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1589 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 111 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0698552548772813 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 68 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1639 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 144 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0878584502745577 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 50 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1627 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 126 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0774431468961278 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -12 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 85253 | Data_Quality.xlsx/Completeness |
    | Populated Records | 79668 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.934489108887664 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 89562 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 617 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.993110917576651 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Green | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 93 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 90 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.967741935483871 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3.5 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CardSwitch | Data_Quality.xlsx/Lineage |
    | Secondary Feed | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | J. Kozłowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Layering via Securities | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Network-Linkage Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 5 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.5 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 67 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.57 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 28.81 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.1 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-11-10 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-11-10 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | J. Kozłowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity J | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-08-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 3 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Add geography filter | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.80 Model 80 — Layering via Securities

| **Model Code**                 | TM-NETWORK-080                                                                      |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Network-Linkage Family                                                              |
| **Business Problem Solved**    | Round-trip securities trades for obfuscation.                                       |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.           |
| **Typology Detected**          | Layering via Securities — flags round-trip securities trades for obfuscation.       |
| **Data Inputs**                | CardSwitch transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity J)       |
| **Booking Entity / Segment**   | Entity J · Correspondent · High-Risk Jurisdictions                                  |
| **Accountable Owner**          | J. Kozłowska                                                                        |
| **Lifecycle / Risk Tier**      | Production · Tier 4 - Low                                                           |
| **Primary Source System**      | CardSwitch                                                                          |
| **Linked Change Request(s)**   | —                                                                                   |
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