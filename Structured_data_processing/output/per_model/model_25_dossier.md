<model id="Model 25" code="TM-STR-025">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 427 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 725 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 47 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 58457 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 1152 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 59656 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.370659722222222 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.90084388185654 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.525215252152522 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.987749653610895 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 1152 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 219 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.190104166666667 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 19.3107147646507 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.58 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 30 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 10000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Balanced | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.525215252152522 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.190104166666667 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.39117081795818 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 76 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 73 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 3 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.960526315789474 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 192 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 10 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 182 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.0520833333333333 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1312 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 128 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0975609756097561 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 1268 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 124 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0977917981072555 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -44 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 937 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 82 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0875133404482391 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -331 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 953 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 74 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0776495278069255 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 16 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Raise score threshold | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Reduce FP | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | CR-003 | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | High | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 1312 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 128 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0975609756097561 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 1268 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 124 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0977917981072555 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -44 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 937 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 82 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0875133404482391 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | -331 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 953 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 74 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0776495278069255 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | 16 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 266435 | Data_Quality.xlsx/Completeness |
    | Populated Records | 254598 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.955572653742939 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Amber | Data_Quality.xlsx/Completeness |
    | Records Checked | 32110 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 1398 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.956462161320461 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 34 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 33 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.970588235294118 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 3.7 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | TradeFinance-CTS | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CryptoGateway | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Real-time | Data_Quality.xlsx/Lineage |
    | Steward | E. Kamiński | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Trade-Based ML | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 13 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Structuring Detection Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | Correspondent | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Segment-specific thresholds | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | EMEA | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 4 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.4 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 60 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.52 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 28.8 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 1 - Critical | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | High | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v4.4 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2022-01-16 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2024-01-16 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | E. Kamiński | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 5 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity E | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-01-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Alpha | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="dq_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | DQ_Issue_Log | issue_id: DQ-032 | source_system: TradeFinance-CTS | issue_description: Currency code mismatch | status: Open | linked_cr: None | DQ_Issue_Log |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Raise score threshold | direction: Reduce FP | linked_change_request: CR-003 | priority: High | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.25 Model 25 — Trade-Based ML

| **Model Code**                 | TM-STR-025                                                                                |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Scenario Family**            | Structuring Detection Family                                                              |
| **Business Problem Solved**    | Over/under-invoicing and phantom shipment indicators.                                     |
| **Business Value / Rationale** | Directly mitigates a Tier-1 regulatory exposure; high SAR yield expected.                 |
| **Typology Detected**          | Trade-Based ML — flags over/under-invoicing and phantom shipment indicators.              |
| **Data Inputs**                | TradeFinance-CTS transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the Correspondent investigations queue (Entity E)             |
| **Booking Entity / Segment**   | Entity E · Correspondent · EMEA                                                           |
| **Accountable Owner**          | E. Kamiński                                                                               |
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

  <relevant_coverage_gaps>
    - gap_id: GAP-003 | typology_/_segment: APAC | gap_description: Trade-based ML weak in Americas corridor | severity: Low | remediation_owner: 2nd LoD MRM | typology_segment: APAC | description: Trade-based ML weak in Americas corridor
    - gap_id: GAP-008 | typology_/_segment: Correspondent | gap_description: Trade-based ML weak in Americas corridor | severity: Low | remediation_owner: AML Tuning Team | typology_segment: Correspondent | description: Trade-based ML weak in Americas corridor
    - gap_id: GAP-013 | typology_/_segment: Americas | gap_description: Trade-based ML weak in Americas corridor | severity: Low | remediation_owner: AML Tuning Team | typology_segment: Americas | description: Trade-based ML weak in Americas corridor
    - gap_id: GAP-018 | typology_/_segment: SME | gap_description: Trade-based ML weak in Americas corridor | severity: High | remediation_owner: 1st LoD | typology_segment: SME | description: Trade-based ML weak in Americas corridor
  </relevant_coverage_gaps>

</estate_context>

</model>