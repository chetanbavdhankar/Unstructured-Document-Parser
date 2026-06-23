<model id="Model 1" code="TM-STR-001">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 179 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2208 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 93 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 23658 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2387 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 26138 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.0749895266024298 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.658088235294118 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.134637081609628 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.914636975179773 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2387 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 130 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0544616673648932 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 91.3229780396358 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.57 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.134637081609628 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0544616673648932 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.102566915911734 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 81 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 53 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 28 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.654320987654321 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 51 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 10 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 41 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.196078431372549 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2186 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 173 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0791399817017383 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2674 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 115 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0430067314884069 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 488 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2066 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 195 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0943852855759923 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -608 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2717 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 253 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0931174089068826 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 651 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Raise score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | CR-003 | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2186 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 173 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0791399817017383 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2674 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 115 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0430067314884069 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 488 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2066 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 195 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0943852855759923 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -608 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2717 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 253 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0931174089068826 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 651 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 433951 | Data_Quality.xlsx/Completeness |
    | Populated Records | 397968 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.917080499872105 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 69013 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1423 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.979380696390535 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 35 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 29 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.828571428571429 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5.5 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | A. Kowalski | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Structuring | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Structuring Detection Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Retail | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 10 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 69 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.45 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 37.95 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.0 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-01-14 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-01-14 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | A. Kowalski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity A | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-01-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-020 | finding: Insufficient BTL coverage | status: Closed | target_date: 2025-Q1 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-037 | finding: Structuring family due full recalibration | status: Open | target_date: 2025-Q4 | linked_cr: CR-003 | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Raise score threshold | direction: Reduce FP | linked_change_request: CR-003 | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.1 Model 1 — Structuring

| **Model Code**                 | TM-STR-001                                                                               |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Structuring Detection Family                                                             |
| **Business Problem Solved**    | Multiple sub-threshold deposits to evade CTR reporting.                                  |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                        |
| **Typology Detected**          | Structuring — flags multiple sub-threshold deposits to evade CTR reporting.              |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity A)                   |
| **Booking Entity / Segment**   | Entity A · Retail · EMEA                                                                 |
| **Accountable Owner**          | A. Kowalski                                                                              |
| **Lifecycle / Risk Tier**      | Production · Tier 1 - Critical                                                           |
| **Primary Source System**      | CoreBanking-T24                                                                          |
| **Linked Change Request(s)**   | CR-003                                                                                   |
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