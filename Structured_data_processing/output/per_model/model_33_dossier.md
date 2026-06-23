<model id="Model 33" code="TM-STR-033">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 504 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2265 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 31 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 67457 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2769 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 70257 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.182015167930661 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.942056074766355 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.305084745762712 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.967513840681564 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2769 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 347 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.125315998555435 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 39.4124428882531 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.51 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 60 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.305084745762712 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.125315998555435 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.233177246879801 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 94 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 89 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 5 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.946808510638298 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 164 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 11 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 153 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0670731707317073 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2446 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 254 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.103843008994276 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2794 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 206 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0737294201861131 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 348 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2742 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 145 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0528811086797958 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -52 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2600 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 140 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0538461538461539 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -142 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Raise score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | CR-003 | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2446 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 254 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.103843008994276 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2794 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 206 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0737294201861131 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | 348 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2742 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 145 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0528811086797958 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -52 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2600 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 140 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0538461538461539 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -142 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 462345 | Data_Quality.xlsx/Completeness |
    | Populated Records | 447362 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.967593463755421 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 48061 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 970 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.979817315494892 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 91 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 79 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.868131868131868 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.8 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Secondary Feed | KYC-Master | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | C. Lewandowska | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Sanctions Proximity | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Structuring Detection Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Corporate | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 1 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.1 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 71 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.56 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 31.24 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v2.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-02-01 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-02-01 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | C. Lewandowska | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 3 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity C | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-09-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Remediation Required | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Medium | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Raise score threshold | direction: Reduce FP | linked_change_request: CR-003 | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.33 Model 33 — Sanctions Proximity

| **Model Code**                 | TM-STR-033                                                                             |
|--------------------------------|----------------------------------------------------------------------------------------|
| **Scenario Family**            | Structuring Detection Family                                                           |
| **Business Problem Solved**    | Counterparty proximity to sanctioned entities.                                         |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.              |
| **Typology Detected**          | Sanctions Proximity — flags counterparty proximity to sanctioned entities.             |
| **Data Inputs**                | CryptoGateway transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Corporate investigations queue (Entity C)              |
| **Booking Entity / Segment**   | Entity C · Corporate · EMEA                                                            |
| **Accountable Owner**          | C. Lewandowska                                                                         |
| **Lifecycle / Risk Tier**      | Production · Tier 1 - Critical                                                         |
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