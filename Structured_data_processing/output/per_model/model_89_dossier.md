<model id="Model 89" code="TM-STR-089">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 198 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1271 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 77 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 66257 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1469 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 67803 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.134785568413887 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.72 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.227064220183486 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.981178177941002 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1469 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 126 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0857726344452008 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 21.6657080070203 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.67 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.227064220183486 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0857726344452008 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.170547585888172 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 98 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 21 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 77 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.214285714285714 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 110 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 9 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 101 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0818181818181818 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1205 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0879668049792531 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1617 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 161 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0995670995670996 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 412 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1387 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 160 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.115356885364095 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -230 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1545 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 121 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0783171521035599 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 158 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Raise score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | CR-003 | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Low | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1205 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 106 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0879668049792531 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1617 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 161 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0995670995670996 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 412 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1387 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 160 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.115356885364095 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -230 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1545 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 121 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0783171521035599 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 158 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 200173 | Data_Quality.xlsx/Completeness |
    | Populated Records | 182099 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.909708102491345 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 47458 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2367 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.950124320451768 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 60 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 54 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.9 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | I. Dąbrowski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Threshold Avoidance | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Structuring Detection Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Private Banking | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 6 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.6 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 59 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.66 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 20.06 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Low | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.6 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-03-09 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-03-09 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | I. Dąbrowski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 4 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity I | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-05-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Raise score threshold | direction: Reduce FP | linked_change_request: CR-003 | priority: Low | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.89 Model 89 — Threshold Avoidance

| **Model Code**                 | TM-STR-089                                                                             |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Structuring Detection Family                                                           |
| **Business Problem Solved**    | Transactions clustered just below reporting limits.                                    |
| **Business Value / Rationale** | Provides supplementary coverage and corroborating signal for linked scenarios.         |
| **Typology Detected**          | Threshold Avoidance — flags transactions clustered just below reporting limits.        |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Private Banking investigations queue (Entity I)        |
| **Booking Entity / Segment**   | Entity I · Private Banking · EMEA                                                      |
| **Accountable Owner**          | I. Dąbrowski                                                                           |
| **Lifecycle / Risk Tier**      | Validation · Tier 1 - Critical                                                         |
| **Primary Source System**      | CryptoGateway                                                                          |
| **Linked Change Request(s)**   | CR-003                                                                                 |
</functional_requirements>

<change_requests>
  <cr id="CR-003" source="CR-003_Change_Request.md">
**CHANGE REQUEST**

Annual recalibration of the Structuring Detection family

| **CR ID**                    | CR-003                                                                                 |
|------------------------------|----------------------------------------------------------------------------------------|
| **Date Raised**              | 2025-09-19                                                                             |
| **Requester**                | Model Risk Management (2nd LoD)                                                        |
| **Change Type**              | Model Family Recalibration                                                             |
| **Affected Model(s) / Feed** | Structuring Detection Family (Models 1, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97) |
| **Family**                   | Structuring Detection Family (STR)                                                     |
| **Booking Entity**           | All entities                                                                           |
| **Priority**                 | High                                                                                   |
| **Linked Findings**          | MRM-037; Tuning_Recommendations (STR family)                                           |

**1. Problem Statement**

The Structuring family is past its policy recalibration window. Population drift since the last calibration has widened the gap between modelled and observed sub-threshold deposit behaviour across all booking entities.

Quarterly trend analysis shows rising alert volumes without a corresponding rise in SAR conversion, indicating threshold decay across the family rather than a single-model issue.

**2. Proposed Change**

Re-estimate structuring thresholds per entity using the trailing four quarters of confirmed-productive alerts.

Harmonise the minimum-amount floor across the family and introduce segment-specific bands for Retail vs SME.

Re-baseline all 13 family members in a single coordinated release to preserve cross-entity comparability.

**3. Expected Impact**

| **Metric**                 | **Current**     | **Expected Post-Change**   |
|----------------------------|-----------------|----------------------------|
| Family Models Recalibrated | 0               | 13                         |
| Aggregate Alert Volume     | Baseline        | Est. −18% to −24%          |
| Family SAR Conversion      | Baseline        | Est. +3 to +5 pts          |
| Calibration Age            | > policy window | Reset to 0 months          |

**4. Risk Assessment**

Coordinated family release carries higher aggregate risk than a single-model change; staged rollout per entity with BTL validation at each stage is required.

Leakage risk is mitigated by retaining the prior threshold set in shadow mode for one quarter for parallel comparison.

**5. Rollback Plan**

Each entity stage is independently reversible; the prior family configuration is version-pinned and restorable per entity without affecting other entities.

Shadow-mode parallel run allows immediate fallback to prior thresholds if family-level leakage exceeds tolerance.

**6. Approval Chain**

| **Role**                          | **Approver**           | **Status**   |
|-----------------------------------|------------------------|--------------|
| Family Owner                      | A. Kowalski            | Approved     |
| 2nd LoD MRM Validator             | MV-Team Alpha          | Approved     |
| Head of Financial Crime Analytics | —                      | Pending      |
| AML Governance Forum              | Quarterly Tuning Board | Pending      |
  </cr>

</change_requests>

<estate_context>
  <sampling_methodology>
    ATL Sample Basis: Stratified random, 95% CI; BTL Sample Basis: Boundary band ±15% of threshold; Confidence Level: 99%
  </sampling_methodology>

  <relevant_coverage_gaps>None identified</relevant_coverage_gaps>

</estate_context>

</model>