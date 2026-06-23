<model id="Model 64" code="TM-NETWORK-064">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 294 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1750 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 65 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 26785 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2044 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 28894 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.143835616438356 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.818941504178273 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.244694132334582 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.938671806553356 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2044 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 205 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.100293542074364 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 70.7413303800097 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.83 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.244694132334582 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.100293542074364 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.186933896230495 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 94 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 41 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 53 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.436170212765957 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 174 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 2 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 172 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0114942528735632 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2251 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 123 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0546423811639271 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1851 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 126 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0680713128038898 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -400 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1935 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 218 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.11266149870801 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 84 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1911 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 121 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0633176347462062 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -24 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Add geography filter | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2251 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 123 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0546423811639271 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1851 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 126 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0680713128038898 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -400 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1935 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 218 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.11266149870801 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 84 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1911 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 121 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0633176347462062 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -24 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 473763 | Data_Quality.xlsx/Completeness |
    | Populated Records | 435800 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.919869217309076 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 162455 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 6673 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.95892400972577 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 41 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 36 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.878048780487805 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 0.1 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Weekly Batch | Data_Quality.xlsx/Lineage |
    | Steward | D. Wójcik | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Cash-Intensive Business | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Network-Linkage Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Private Banking | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | High-Risk Jurisdictions | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 2 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.2 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 61 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.55 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 27.45 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.1 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-09-27 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Tuning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-09-27 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | D. Wójcik | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity D | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-04-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-009 | source_system: CoreBanking-T24 | issue_description: Duplicate transaction records | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Add geography filter | direction: Maintain | linked_change_request: None | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.64 Model 64 — Cash-Intensive Business

| **Model Code**                 | TM-NETWORK-064                                                                           |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Network-Linkage Family                                                                   |
| **Business Problem Solved**    | Cash activity inconsistent with business profile.                                        |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                |
| **Typology Detected**          | Cash-Intensive Business — flags cash activity inconsistent with business profile.        |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity D)          |
| **Booking Entity / Segment**   | Entity D · Private Banking · High-Risk Jurisdictions                                     |
| **Accountable Owner**          | D. Wójcik                                                                                |
| **Lifecycle / Risk Tier**      | Tuning · Tier 4 - Low                                                                    |
| **Primary Source System**      | CoreBanking-T24                                                                          |
| **Linked Change Request(s)**   | —                                                                                        |
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