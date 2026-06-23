<model id="Model 74" code="TM-RMF-074">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 573 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1155 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 67 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 20374 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1728 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 22169 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.331597222222222 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.8953125 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.483952702702703 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.946351432950903 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1728 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 444 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.256944444444444 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 77.9466823041184 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.66 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.483952702702703 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.256944444444444 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.393149399399399 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 86 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 34 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 52 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.395348837209302 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 72 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 0 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 72 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1477 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 135 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0914014895057549 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1782 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0594837261503928 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 305 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2022 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 90 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0445103857566766 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 240 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1557 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 178 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.11432241490045 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -465 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Lower score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce leakage | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1477 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 135 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0914014895057549 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1782 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0594837261503928 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 305 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2022 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 90 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0445103857566766 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 240 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1557 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 178 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.11432241490045 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -465 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 318865 | Data_Quality.xlsx/Completeness |
    | Populated Records | 287247 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.900842049143054 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 192289 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 7253 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.962280733687314 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 81 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 76 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.938271604938272 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Intraday | Data_Quality.xlsx/Lineage |
    | Steward | D. Wójcik | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Crypto On/Off-Ramp | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Rapid-Movement Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Private Banking | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | APAC | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 83 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.5 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 41.5 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 2 - High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-05-20 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-05-20 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | D. Wójcik | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity D | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-02-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Bravo | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-039 | source_system: TradeFinance-CTS | issue_description: Currency code mismatch | status: In Progress | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Lower score threshold | direction: Reduce leakage | linked_change_request: None | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.74 Model 74 — Crypto On/Off-Ramp

| **Model Code**                 | TM-RMF-074                                                                                |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Rapid-Movement Family                                                                     |
| **Business Problem Solved**    | Fiat-crypto conversion layering pattern.                                                  |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.            |
| **Typology Detected**          | Crypto On/Off-Ramp — flags fiat-crypto conversion layering pattern.                       |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity D)           |
| **Booking Entity / Segment**   | Entity D · Private Banking · APAC                                                         |
| **Accountable Owner**          | D. Wójcik                                                                                 |
| **Lifecycle / Risk Tier**      | Production · Tier 2 - High                                                                |
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

  <relevant_coverage_gaps>
    - gap_id: GAP-002 | typology_/_segment: Correspondent | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: High | remediation_owner: 2nd LoD MRM | typology_segment: Correspondent | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-007 | typology_/_segment: High-Risk Jurisdictions | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: Medium | remediation_owner: 1st LoD | typology_segment: High-Risk Jurisdictions | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-012 | typology_/_segment: APAC | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: Low | remediation_owner: 1st LoD | typology_segment: APAC | description: Crypto on/off-ramp coverage limited to Entity A
    - gap_id: GAP-017 | typology_/_segment: Corporate | gap_description: Crypto on/off-ramp coverage limited to Entity A | severity: High | remediation_owner: 1st LoD | typology_segment: Corporate | description: Crypto on/off-ramp coverage limited to Entity A
  </relevant_coverage_gaps>

</estate_context>

</model>