<model id="Model 24" code="TM-NETWORK-024">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 348 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2371 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 93 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 35037 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2719 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 37849 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.127988230967267 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.789115646258503 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.220253164556962 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.936617835757057 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2719 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 161 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0592129459360059 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 71.8380934767101 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.71 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 180 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.220253164556962 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0592129459360059 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.15583707710858 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 84 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 31 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 53 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.369047619047619 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 126 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 5 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 121 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0396825396825397 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2626 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 170 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0647372429550647 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2376 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 174 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0732323232323232 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -250 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2862 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 132 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0461215932914046 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 486 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3206 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 206 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0642545227698066 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 344 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Add geography filter | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | — | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2626 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 170 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0647372429550647 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2376 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 174 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0732323232323232 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -250 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2862 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 132 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0461215932914046 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 486 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 3206 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 206 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0642545227698066 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 344 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 66735 | Data_Quality.xlsx/Completeness |
    | Populated Records | 65097 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.975455158462576 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 74974 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 216 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.997119001253768 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Green | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 97 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 95 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.979381443298969 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3.3 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CardSwitch | Data_Quality.xlsx/Lineage |
    | Secondary Feed | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
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
    | Entities Covered | 9 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.9 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 92 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.89 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 10.12 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 4 - Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.6 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-02-12 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Decommissioning | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-02-12 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | D. Wójcik | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Delta | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity D | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-12-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
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
### 3.24 Model 24 — Cash-Intensive Business

| **Model Code**                 | TM-NETWORK-024                                                                      |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Network-Linkage Family                                                              |
| **Business Problem Solved**    | Cash activity inconsistent with business profile.                                   |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.           |
| **Typology Detected**          | Cash-Intensive Business — flags cash activity inconsistent with business profile.   |
| **Data Inputs**                | CardSwitch transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity D)     |
| **Booking Entity / Segment**   | Entity D · Private Banking · High-Risk Jurisdictions                                |
| **Accountable Owner**          | D. Wójcik                                                                           |
| **Lifecycle / Risk Tier**      | Decommissioning · Tier 4 - Low                                                      |
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