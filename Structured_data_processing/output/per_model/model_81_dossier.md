<model id="Model 81" code="TM-STR-081">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 412 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2521 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 85 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 53477 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2933 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 56495 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.140470508012274 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.82897384305835 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.240233236151604 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.954980535019108 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2933 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 322 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.109785202863962 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 51.9160987698026 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.64 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 3000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.240233236151604 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.109785202863962 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.188054022836547 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 61 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 29 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 32 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.475409836065574 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 161 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 3 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 158 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0186335403726708 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2947 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 193 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0654903291482864 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2435 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 131 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0537987679671458 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -512 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2711 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 286 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.105496126890446 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 276 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 3048 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 277 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0908792650918635 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 337 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Raise score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | CR-003 | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2947 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 193 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0654903291482864 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2435 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 131 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0537987679671458 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -512 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2711 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 286 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.105496126890446 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 276 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 3048 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 277 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0908792650918635 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 337 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 422491 | Data_Quality.xlsx/Completeness |
    | Populated Records | 387175 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.916410053705286 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 70901 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2258 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.968152776406539 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 103 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 92 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.893203883495146 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3.8 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | A. Kowalski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Structuring | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Structuring Detection Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 51 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.56 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 22.44 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.4 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-09-03 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-09-03 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | A. Kowalski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity A | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-09-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 4 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-016 | finding: Population drift detected | status: Open | target_date: 2025-Q1 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-040 | source_system: TradeFinance-CTS | issue_description: Truncated narrative field | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Raise score threshold | direction: Reduce FP | linked_change_request: CR-003 | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.81 Model 81 — Structuring

| **Model Code**                 | TM-STR-081                                                                                |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Structuring Detection Family                                                              |
| **Business Problem Solved**    | Multiple sub-threshold deposits to evade CTR reporting.                                   |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                         |
| **Typology Detected**          | Structuring — flags multiple sub-threshold deposits to evade CTR reporting.               |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity A)                    |
| **Booking Entity / Segment**   | Entity A · Retail · EMEA                                                                  |
| **Accountable Owner**          | A. Kowalski                                                                               |
| **Lifecycle / Risk Tier**      | Production · Tier 1 - Critical                                                            |
| **Primary Source System**      | TradeFinance-CTS                                                                          |
| **Linked Change Request(s)**   | CR-003                                                                                    |
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