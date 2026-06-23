<model id="Model 45" code="TM-TBML-045">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 595 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2258 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 76 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 73000 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2853 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 75929 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.208552400981423 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.886736214605067 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.337684449489217 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.969996545217784 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2853 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 420 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.147213459516299 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 37.5745762488641 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.64 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 9000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.337684449489217 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.147213459516299 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.26149605350005 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 37 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 18 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 19 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.486486486486487 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 167 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 8 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 159 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0479041916167665 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2285 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 224 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0980306345733042 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2975 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 156 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.052436974789916 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 690 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3013 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 164 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.054430799867242 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 38 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2425 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 264 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.108865979381443 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -588 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Tighten min-amount floor | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2285 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 224 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0980306345733042 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2975 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 156 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.052436974789916 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 690 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 3013 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 164 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.054430799867242 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 38 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2425 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 264 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.108865979381443 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -588 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 151294 | Data_Quality.xlsx/Completeness |
    | Populated Records | 146325 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.967156661863656 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 88382 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1848 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.979090765087914 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 60 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 51 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.85 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CardSwitch | Data_Quality.xlsx/Lineage |
    | Secondary Feed | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | E. Kamiński | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Trade-Based ML | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Trade-Based Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 5 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.5 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 93 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.67 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 30.69 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-01-19 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-01-19 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | E. Kamiński | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity E | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-09-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Tighten min-amount floor | direction: Reduce FP | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.45 Model 45 — Trade-Based ML

| **Model Code**                 | TM-TBML-045                                                                         |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Trade-Based Family                                                                  |
| **Business Problem Solved**    | Over/under-invoicing and phantom shipment indicators.                               |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.      |
| **Typology Detected**          | Trade-Based ML — flags over/under-invoicing and phantom shipment indicators.        |
| **Data Inputs**                | CardSwitch transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity E)       |
| **Booking Entity / Segment**   | Entity E · Correspondent · EMEA                                                     |
| **Accountable Owner**          | E. Kamiński                                                                         |
| **Lifecycle / Risk Tier**      | Production · Tier 1 - Critical                                                      |
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

  <relevant_coverage_gaps>
    - gap_id: GAP-003 | typology_/_segment: APAC | gap_description: Trade-based ML weak in Americas corridor | severity: Low | remediation_owner: 2nd LoD MRM | typology_segment: APAC | description: Trade-based ML weak in Americas corridor
    - gap_id: GAP-008 | typology_/_segment: Correspondent | gap_description: Trade-based ML weak in Americas corridor | severity: Low | remediation_owner: AML Tuning Team | typology_segment: Correspondent | description: Trade-based ML weak in Americas corridor
    - gap_id: GAP-013 | typology_/_segment: Americas | gap_description: Trade-based ML weak in Americas corridor | severity: Low | remediation_owner: AML Tuning Team | typology_segment: Americas | description: Trade-based ML weak in Americas corridor
    - gap_id: GAP-018 | typology_/_segment: SME | gap_description: Trade-based ML weak in Americas corridor | severity: High | remediation_owner: 1st LoD | typology_segment: SME | description: Trade-based ML weak in Americas corridor
  </relevant_coverage_gaps>

</estate_context>

</model>