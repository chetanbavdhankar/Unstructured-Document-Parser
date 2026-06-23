<model id="Model 41" code="TM-STR-041">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 310 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1381 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 72 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 40202 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1691 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 41965 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.183323477232407 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.81151832460733 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.2990834539315 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.966789312940384 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1691 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 114 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0674157303370787 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 40.2954843321816 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.71 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.2990834539315 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0674157303370787 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.206416364493732 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 109 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 5 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 104 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.0458715596330275 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Review | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 172 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 9 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 163 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0523255813953488 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1706 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 85 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0498241500586166 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1557 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 154 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0989081567116249 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -149 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1415 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 165 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.11660777385159 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -142 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1372 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 108 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0787172011661808 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -43 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Raise score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | CR-003 | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1706 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 85 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0498241500586166 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1557 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 154 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0989081567116249 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -149 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1415 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 165 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.11660777385159 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -142 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1372 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 108 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0787172011661808 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -43 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 437030 | Data_Quality.xlsx/Completeness |
    | Populated Records | 395307 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.904530581424616 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 172310 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 4215 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.975538274040973 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 98 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 90 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.918367346938776 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | KYC-Master | Data_Quality.xlsx/Lineage |
    | Secondary Feed | Sanctions-Screening | Data_Quality.xlsx/Lineage |
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
    | Entities Covered | 3 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.3 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 75 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.86 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 10.5 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v3.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-06-18 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-06-18 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | A. Kowalski | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 1 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity A | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-05-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 2 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | High | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-008 | finding: Insufficient BTL coverage | status: Closed | target_date: 2025-Q1 | linked_cr: None | Issue_Tracking |
    | Issue_Tracking | finding_id: MRM-028 | finding: Population drift detected | status: Open | target_date: 2025-Q1 | linked_cr: None | Issue_Tracking |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-020 | source_system: KYC-Master | issue_description: Stale reference data | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Raise score threshold | direction: Reduce FP | linked_change_request: CR-003 | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.41 Model 41 — Structuring

| **Model Code**                 | TM-STR-041                                                                          |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Structuring Detection Family                                                        |
| **Business Problem Solved**    | Multiple sub-threshold deposits to evade CTR reporting.                             |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                   |
| **Typology Detected**          | Structuring — flags multiple sub-threshold deposits to evade CTR reporting.         |
| **Data Inputs**                | KYC-Master transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Retail investigations queue (Entity A)              |
| **Booking Entity / Segment**   | Entity A · Retail · EMEA                                                            |
| **Accountable Owner**          | A. Kowalski                                                                         |
| **Lifecycle / Risk Tier**      | Validation · Tier 1 - Critical                                                      |
| **Primary Source System**      | KYC-Master                                                                          |
| **Linked Change Request(s)**   | CR-003                                                                              |
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