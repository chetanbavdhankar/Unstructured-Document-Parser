<model id="Model 7" code="TM-CRYPTO-007">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | True Positives | 256 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Positives | 2264 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | False Negatives | 67 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | True Negatives | 40877 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Alerts | 2520 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Total Population | 43464 | Model_Performance_Metrics.xlsx/Confusion_Matrix |
    | Precision | 0.101587301587302 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Recall | 0.792569659442725 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | F1 Score | 0.18009145269082 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Specificity | 0.947520919774692 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    | Total Alerts | 2520 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | SARs Filed | 157 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Conversion Rate | 0.0623015873015873 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Alerts / 1k Population | 57.9790171176146 | Model_Performance_Metrics.xlsx/Alert_Volumes |
    | Score Threshold | 0.48 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Lookback (days) | 90 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Min Amount ($) | 5000 | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | Sensitivity Band | Aggressive | Model_Performance_Metrics.xlsx/Threshold_Settings |
    | F1 Score | 0.18009145269082 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Conversion Rate | 0.0623015873015873 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |
    | Composite Effectiveness | 0.132975506535127 | Model_Performance_Metrics.xlsx/Effectiveness_Summary |

  </domain>

  <domain name="backtesting">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Alerts Sampled | 117 | Backtesting_Results.xlsx/ATL_Testing |
    | Confirmed Productive | 94 | Backtesting_Results.xlsx/ATL_Testing |
    | False Positive | 23 | Backtesting_Results.xlsx/ATL_Testing |
    | Effective Rate | 0.803418803418804 | Backtesting_Results.xlsx/ATL_Testing |
    | ATL Outcome | Pass | Backtesting_Results.xlsx/ATL_Testing |
    | Below-Line Sampled | 109 | Backtesting_Results.xlsx/BTL_Testing |
    | Missed Alerts (Should-Fire) | 6 | Backtesting_Results.xlsx/BTL_Testing |
    | Confirmed Clean | 103 | Backtesting_Results.xlsx/BTL_Testing |
    | Leakage Rate | 0.055045871559633 | Backtesting_Results.xlsx/BTL_Testing |
    | BTL Outcome | Threshold Review | Backtesting_Results.xlsx/BTL_Testing |
    | Quarter | Q1 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2633 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 183 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0695024686669199 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q2 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2177 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 214 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0983004134129536 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -456 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q3 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2504 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 243 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0970447284345048 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | 327 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Quarter | Q4 2025 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Alerts | 2117 | Backtesting_Results.xlsx/Quarterly_Trend |
    | SARs | 188 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Conversion Rate | 0.0888049126121871 | Backtesting_Results.xlsx/Quarterly_Trend |
    | QoQ Alert Delta | -387 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Recommendation | Re-segment population | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Direction | Maintain | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Linked Change Request | CR-001 | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Priority | Medium | Backtesting_Results.xlsx/Tuning_Recommendations |
    | Q1 2025/Alerts | 2633 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/SARs | 183 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/Conversion Rate | 0.0695024686669199 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q1 2025/QoQ Alert Delta | n/a | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Alerts | 2177 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/SARs | 214 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/Conversion Rate | 0.0983004134129536 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q2 2025/QoQ Alert Delta | -456 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Alerts | 2504 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/SARs | 243 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/Conversion Rate | 0.0970447284345048 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q3 2025/QoQ Alert Delta | 327 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Alerts | 2117 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/SARs | 188 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/Conversion Rate | 0.0888049126121871 | Backtesting_Results.xlsx/Quarterly_Trend |
    | Q4 2025/QoQ Alert Delta | -387 | Backtesting_Results.xlsx/Quarterly_Trend |

  </domain>

  <domain name="data_quality">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Expected Records | 319921 | Data_Quality.xlsx/Completeness |
    | Populated Records | 289402 | Data_Quality.xlsx/Completeness |
    | Completeness | 0.904604574254269 | Data_Quality.xlsx/Completeness |
    | DQ Flag | Red | Data_Quality.xlsx/Completeness |
    | Records Checked | 110276 | Data_Quality.xlsx/Accuracy |
    | Failed Validation | 3384 | Data_Quality.xlsx/Accuracy |
    | Accuracy | 0.969313359207806 | Data_Quality.xlsx/Accuracy |
    | DQ Flag | Red | Data_Quality.xlsx/Accuracy |
    | Feeds Expected | 36 | Data_Quality.xlsx/Timeliness |
    | Feeds On-Time | 34 | Data_Quality.xlsx/Timeliness |
    | On-Time Rate | 0.944444444444444 | Data_Quality.xlsx/Timeliness |
    | Avg Delay (hrs) | 4.7 | Data_Quality.xlsx/Timeliness |
    | Primary Source System | Sanctions-Screening | Data_Quality.xlsx/Lineage |
    | Secondary Feed | CoreBanking-T24 | Data_Quality.xlsx/Lineage |
    | Feed Frequency | Daily Batch | Data_Quality.xlsx/Lineage |
    | Steward | G. Szymański | Data_Quality.xlsx/Lineage |

  </domain>

  <domain name="coverage">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Primary Typology | Round-Amount Transactions | Detection_Coverage.xlsx/Typology_Coverage |
    | Coverage Strength | Moderate | Detection_Coverage.xlsx/Typology_Coverage |
    | Models in Family | 12 | Detection_Coverage.xlsx/Typology_Coverage |
    | Family | Virtual-Asset Family | Detection_Coverage.xlsx/Typology_Coverage |
    | Segment | SME | Detection_Coverage.xlsx/Segment_Coverage |
    | Applicable | Yes | Detection_Coverage.xlsx/Segment_Coverage |
    | Segment-Tuned | No | Detection_Coverage.xlsx/Segment_Coverage |
    | Coverage Note | Uses global threshold | Detection_Coverage.xlsx/Segment_Coverage |
    | Geography | Americas | Detection_Coverage.xlsx/Geography_Coverage |
    | High-Risk Jurisdiction Logic | Enabled | Detection_Coverage.xlsx/Geography_Coverage |
    | Entities Covered | 7 | Detection_Coverage.xlsx/Geography_Coverage |
    | Coverage % | 0.7 | Detection_Coverage.xlsx/Geography_Coverage |

  </domain>

  <domain name="governance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Inherent Risk Score | 68 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Control Effectiveness | 0.69 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Residual Risk Score | 21.08 | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Risk Tier | Tier 3 - Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Materiality | Medium | Model_Risk_Governance.xlsx/Risk_Tiering |
    | Version | v1.9 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Deploy Date | 2024-01-09 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Lifecycle Status | Production | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Next Review Due | 2026-01-09 | Model_Risk_Governance.xlsx/Lifecycle_Status |
    | Model Owner | G. Szymański | Model_Risk_Governance.xlsx/Ownership |
    | Developer | Dev Pod 2 | Model_Risk_Governance.xlsx/Ownership |
    | Independent Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Ownership |
    | Booking Entity | Entity G | Model_Risk_Governance.xlsx/Ownership |
    | Last Validation | 2025-07-15 | Model_Risk_Governance.xlsx/Validation_Log |
    | Outcome | Approved | Model_Risk_Governance.xlsx/Validation_Log |
    | Findings Raised | 0 | Model_Risk_Governance.xlsx/Validation_Log |
    | Severity | None | Model_Risk_Governance.xlsx/Validation_Log |
    | Validator | MV-Team Charlie | Model_Risk_Governance.xlsx/Validation_Log |

  </domain>

  <domain name="mrm_issues">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Issue_Tracking | finding_id: MRM-036 | finding: FP rate 38% above structuring peer baseline | status: In Remediation | target_date: 2025-Q3 | linked_cr: CR-001 | Issue_Tracking |

  </domain>

  <domain name="tuning_recommendations">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Tuning_Recommendations | recommendation: Re-segment population | direction: Maintain | linked_change_request: CR-001 | priority: Medium | Tuning_Recommendations |

  </domain>

</structured_metrics>

<functional_requirements>
### 3.7 Model 7 — Round-Amount Transactions

| **Model Code**                 | TM-CRYPTO-007                                                                                |
|--------------------------------|----------------------------------------------------------------------------------------------|
| **Scenario Family**            | Virtual-Asset Family                                                                         |
| **Business Problem Solved**    | Unusual frequency of round-figure transfers.                                                 |
| **Business Value / Rationale** | Supports core monitoring coverage with balanced alert efficiency.                            |
| **Typology Detected**          | Round-Amount Transactions — flags unusual frequency of round-figure transfers.               |
| **Data Inputs**                | Sanctions-Screening transactions; KYC-Master customer profile; Sanctions-Screening reference |
| **Alert Output**               | Risk-scored alert routed to the SME investigations queue (Entity G)                          |
| **Booking Entity / Segment**   | Entity G · SME · Americas                                                                    |
| **Accountable Owner**          | G. Szymański                                                                                 |
| **Lifecycle / Risk Tier**      | Production · Tier 3 - Medium                                                                 |
| **Primary Source System**      | Sanctions-Screening                                                                          |
| **Linked Change Request(s)**   | CR-001                                                                                       |
</functional_requirements>

<change_requests>
  <cr id="CR-001" source="CR-001_Change_Request.md">
**CHANGE REQUEST**

Threshold and lookback re-tuning for Model 7 (Velocity Anomaly)

| **CR ID**                    | CR-001                                    |
|------------------------------|-------------------------------------------|
| **Date Raised**              | 2025-07-14                                |
| **Requester**                | AML Tuning Team (1st LoD)                 |
| **Change Type**              | Model Parameter Change                    |
| **Affected Model(s) / Feed** | Model 7 (TM-BEHAV-007)                    |
| **Family**                   | Behavioural-Anomaly Family                |
| **Booking Entity**           | Entity G                                  |
| **Priority**                 | High                                      |
| **Linked Findings**          | MRM-036; Tuning_Recommendations (Model 7) |

**1. Problem Statement**

Backtesting for Q2 2025 shows Model 7 generating a false-positive rate approximately 38% above the velocity-anomaly peer baseline, with a SAR conversion rate below 5%.

ATL sampling confirmed a high volume of unproductive alerts driven by an overly sensitive score threshold and a lookback window that double-counts intra-day bursts.

**2. Proposed Change**

Raise the score threshold from 0.52 to 0.61 to suppress low-confidence velocity alerts.

Shorten the lookback window from 90 to 60 days to reduce duplicate burst attribution.

Retain the existing minimum-amount floor ($5,000); no change to population scope.

**3. Expected Impact**

| **Metric**           | **Current**   | **Expected Post-Change**   |
|----------------------|---------------|----------------------------|
| Score Threshold      | 0.52          | 0.61                       |
| Lookback Window      | 90 days       | 60 days                    |
| Monthly Alert Volume | ~2,100        | ~1,350 (est. −36%)         |
| SAR Conversion Rate  | 4.8%          | 7.5% (est.)                |

**4. Risk Assessment**

Primary risk is a marginal increase in detection leakage (false negatives). BTL sampling at the new threshold band must confirm leakage remains within the 3% tolerance before promotion.

Change is reversible and confined to a single model; no upstream data or feed dependency is affected.

**5. Rollback Plan**

Revert threshold to 0.52 and lookback to 90 days via the scenario configuration store; prior parameter set is version-tagged and restorable within one batch cycle.

Trigger a re-run of the affected period to restore the original alert population if leakage breaches tolerance.

**6. Approval Chain**

| **Role**              | **Approver**           | **Status**   |
|-----------------------|------------------------|--------------|
| Model Owner           | G. Szymański           | Approved     |
| 2nd LoD MRM Validator | MV-Team Charlie        | Pending      |
| AML Governance Forum  | Quarterly Tuning Board | Pending      |
  </cr>

</change_requests>

<estate_context>
  <sampling_methodology>
    ATL Sample Basis: Stratified random, 95% CI; BTL Sample Basis: Boundary band ±15% of threshold; Confidence Level: 99%
  </sampling_methodology>

  <relevant_coverage_gaps>None identified</relevant_coverage_gaps>

</estate_context>

</model>