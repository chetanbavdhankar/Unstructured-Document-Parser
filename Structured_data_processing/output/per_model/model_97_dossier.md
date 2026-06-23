<model id="Model 97" code="TM-STR-097">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 319 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 236 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 18 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 60227 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 555 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 60800 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.574774774774775 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.946587537091988 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.7152466367713 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.996096786464449 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 555 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 250 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.45045045045045 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 9.12828947368421 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.77 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.7152466367713 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.45045045045045 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.60932816224296 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 115 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 96 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 19 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.834782608695652 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 55 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 4 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 51 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0727272727272727 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 609 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 58 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0952380952380952 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 643 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 36 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0559875583203733 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 34 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 494 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 38 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0769230769230769 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -149 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 453 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 26 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0573951434878587 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -41 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Raise score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | CR-003 | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 609 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 58 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0952380952380952 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 643 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 36 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0559875583203733 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 34 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 494 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 38 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0769230769230769 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -149 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 453 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 26 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0573951434878587 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -41 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 185764 | Data_Quality.xlsx/Completeness |
    | Populated Records | 183604 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.988372343403458 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Green | Data_Quality.xlsx/Completeness |
    | Records Checked | 51584 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1806 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.964989143920596 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 54 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 53 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.981481481481482 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.6 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | KYC-Master | Data_Quality.xlsx/Lineage |
    | Secondary Feed | Sanctions-Screening | Data_Quality.xlsx/Lineage |
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
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 5 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.5 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 83 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.71 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 24.07 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2023-01-16 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2025-01-16 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | G. Szymański | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity G | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-01-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-028 | source_system: KYC-Master | issue_description: Missing originator country on cross-border wires | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Raise score threshold | direction: Reduce FP | linked_change_request: CR-003 | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.97 Model 97 — Smurfing Network

| **Model Code**                 | TM-STR-097                                                                          |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Scenario Family**            | Structuring Detection Family                                                        |
| **Business Problem Solved**    | Coordinated small transactions across linked parties.                               |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                   |
| **Typology Detected**          | Smurfing Network — flags coordinated small transactions across linked parties.      |
| **Data Inputs**                | KYC-Master transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity G)                 |
| **Booking Entity / Segment**   | Entity G · SME · EMEA                                                               |
| **Accountable Owner**          | G. Szymański                                                                        |
| **Lifecycle / Risk Tier**      | Production · Tier 1 - Critical                                                      |
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