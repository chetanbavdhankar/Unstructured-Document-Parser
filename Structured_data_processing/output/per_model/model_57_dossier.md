<model id="Model 57" code="TM-STR-057">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 489 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 1731 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 44 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 54115 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2220 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 56379 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.22027027027027 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.917448405253283 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.355248819469669 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.969004046843104 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2220 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 384 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.172972972972973 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 39.3763635396158 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.63 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.355248819469669 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.172972972972973 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.282338480870991 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 82 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 23 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 59 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.280487804878049 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 59 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 0 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 59 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Pass | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2077 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 84 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0404429465575349 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1938 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 163 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0841073271413829 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2341 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 205 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0875694147800085 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 403 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2347 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 153 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0651896037494674 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 6 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Raise score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | CR-003 | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2077 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 84 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0404429465575349 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1938 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 163 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0841073271413829 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2341 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 205 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0875694147800085 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 403 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2347 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 153 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0651896037494674 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 6 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 126254 | Data_Quality.xlsx/Completeness |
    | Populated Records | 114366 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.905840607030272 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 132237 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 5340 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.959617958665124 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 90 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 87 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.966666666666667 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 5.2 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Secondary Feed | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | G. Szymański | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Smurfing Network | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Strong | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Structuring Detection Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 1 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 56 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.73 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 15.12 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.6 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-06-18 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-06-18 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | G. Szymański | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity G | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-09-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 4 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Low | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-008 | source_system: CoreBanking-T24 | issue_description: Null counterparty IDs in feed | status: In Progress | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Raise score threshold | direction: Reduce FP | linked_change_request: CR-003 | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.57 Model 57 — Smurfing Network

| **Model Code**                 | TM-STR-057                                                                               |
|--------------------------------|------------------------------------------------------------------------------------------|
| **Scenario Family**            | Structuring Detection Family                                                             |
| **Business Problem Solved**    | Coordinated small transactions across linked parties.                                    |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                |
| **Typology Detected**          | Smurfing Network — flags coordinated small transactions across linked parties.           |
| **Data Inputs**                | CoreBanking-T24 transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity G)                      |
| **Booking Entity / Segment**   | Entity G · SME · EMEA                                                                    |
| **Accountable Owner**          | G. Szymański                                                                             |
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