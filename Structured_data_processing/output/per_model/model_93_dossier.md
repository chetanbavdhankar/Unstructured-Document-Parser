<model id="Model 93" code="TM-TBML-093">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 181 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 500 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 14 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 42423 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 681 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 43118 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.265785609397944 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.928205128205128 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.41324200913242 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.988351233604361 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 681 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 117 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.171806167400881 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 15.7938679901665 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.57 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.41324200913242 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.171806167400881 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.316667672439805 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 108 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 25 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 83 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.231481481481481 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 163 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 5 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 158 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0306748466257669 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 648 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 32 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0493827160493827 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 690 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 58 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0840579710144928 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 42 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 582 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 58 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0996563573883162 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -108 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 775 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 68 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.087741935483871 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 193 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Tighten min-amount floor | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 648 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 32 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0493827160493827 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 690 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 58 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0840579710144928 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 42 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 582 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 58 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0996563573883162 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -108 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 775 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 68 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.087741935483871 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 193 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 292425 | Data_Quality.xlsx/Completeness |
    | Populated Records | 269700 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.92228776609387 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 145992 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 4140 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.971642281768864 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 115 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 107 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.930434782608696 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
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
    | Entities Covered | 2 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.2 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 87 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.93 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 6.09 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.5 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-11-24 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-11-24 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | C. Lewandowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity C | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-09-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Tighten min-amount floor | direction: Reduce FP | linked_change_request: None | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.93 Model 93 — Sanctions Proximity

| **Model Code**                 | TM-TBML-093                                                                                |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Trade-Based Family                                                                         |
| **Business Problem Solved**    | Counterparty proximity to sanctioned entities.                                             |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                          |
| **Typology Detected**          | Sanctions Proximity — flags counterparty proximity to sanctioned entities.                 |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity C)                  |
| **Booking Entity / Segment**   | Entity C · Corporate · EMEA                                                                |
| **Accountable Owner**          | C. Lewandowska                                                                             |
| **Lifecycle / Risk Tier**      | Production · Tier 1 - Critical                                                             |
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