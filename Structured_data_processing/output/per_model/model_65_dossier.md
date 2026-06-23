<model id="Model 65" code="TM-STR-065">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 530 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 462 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 80 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 68302 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 992 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 69374 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.534274193548387 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.868852459016393 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.66167290886392 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.993281368157757 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 992 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 360 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.362903225806452 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 14.2993052152103 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.81 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 1000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Conservative | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.66167290886392 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.362903225806452 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.542165035640933 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 31 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 23 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 8 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.741935483870968 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 119 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 4 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 115 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0336134453781513 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1049 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 50 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0476644423260248 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1024 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 44 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.04296875 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -25 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 125 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.109745390693591 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 115 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1110 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 79 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0711711711711712 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -29 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Raise score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | CR-003 | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1049 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 50 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0476644423260248 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1024 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 44 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.04296875 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -25 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 1139 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 125 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.109745390693591 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 115 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 1110 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 79 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0711711711711712 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -29 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 282053 | Data_Quality.xlsx/Completeness |
    | Populated Records | 269823 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.956639355014838 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 179095 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 2337 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.986951059493565 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Amber | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 77 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 70 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.909090909090909 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 1.4 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | PaymentsHub-SWIFT | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CardSwitch | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | E. Kamiński | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Trade-Based ML | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Partial | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Structuring Detection Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Not Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 4 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.4 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 87 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.7 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 26.1 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.4 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2025-11-18 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Validation | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2027-11-18 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | E. Kamiński | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity E | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-05-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved with Conditions | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 1 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | Low | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Raise score threshold | direction: Reduce FP | linked_change_request: CR-003 | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.65 Model 65 — Trade-Based ML

| **Model Code**                 | TM-STR-065                                                                                 |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Scenario Family**            | Structuring Detection Family                                                               |
| **Business Problem Solved**    | Over/under-invoicing and phantom shipment indicators.                                      |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                          |
| **Typology Detected**          | Trade-Based ML — flags over/under-invoicing and phantom shipment indicators.               |
| **Data Inputs**                | PaymentsHub-SWIFT transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity E)              |
| **Booking Entity / Segment**   | Entity E · Correspondent · EMEA                                                            |
| **Accountable Owner**          | E. Kamiński                                                                                |
| **Lifecycle / Risk Tier**      | Validation · Tier 1 - Critical                                                             |
| **Primary Source System**      | PaymentsHub-SWIFT                                                                          |
| **Linked Change Request(s)**   | CR-003                                                                                     |
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

  <relevant_coverage_gaps>
    - gap_id: GAP-003 | typology_/_segment: APAC | gap_description: Trade-based ML weak in Americas corridor | severity: Low | remediation_owner: 2nd LoD MRM | typology_segment: APAC | description: Trade-based ML weak in Americas corridor
    - gap_id: GAP-008 | typology_/_segment: Correspondent | gap_description: Trade-based ML weak in Americas corridor | severity: Low | remediation_owner: AML Tuning Team | typology_segment: Correspondent | description: Trade-based ML weak in Americas corridor
    - gap_id: GAP-013 | typology_/_segment: Americas | gap_description: Trade-based ML weak in Americas corridor | severity: Low | remediation_owner: AML Tuning Team | typology_segment: Americas | description: Trade-based ML weak in Americas corridor
    - gap_id: GAP-018 | typology_/_segment: SME | gap_description: Trade-based ML weak in Americas corridor | severity: High | remediation_owner: 1st LoD | typology_segment: SME | description: Trade-based ML weak in Americas corridor
  </relevant_coverage_gaps>

</estate_context>

</model>