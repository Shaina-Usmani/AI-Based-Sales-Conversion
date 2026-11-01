# Sales Insights Report

## Objective

Predict lead-to-conversion probability so sales teams can prioritize high-value opportunities, reduce response delay, and focus manual follow-up on leads with the strongest conversion signals.

## Key Conversion Drivers

- Referral and inbound sources show stronger conversion potential than cold outreach.
- Fast response time increases the chance of conversion, especially for high-engagement leads.
- Higher engagement score and higher budget improve lead value and priority.
- Repeated interactions help when they are paired with quick response and strong engagement.
- The engineered High Intent Lead flag captures leads with high engagement and rapid follow-up.

## Sales Prioritization Strategy

- High-priority leads should be assigned to senior sales representatives immediately.
- Medium-priority leads should receive personalized follow-up and nurturing.
- Low-priority leads should stay in automated campaigns until engagement improves.
- Batch scoring should be used to sort uploaded lead lists by conversion probability before outreach planning.

## Model-Backed Action Plan

- Use the conversion probability score as the primary lead ranking metric.
- Use SHAP and LIME explanations to identify why a lead was scored high or low.
- Improve low-scoring leads by reducing response time, increasing touchpoints, and targeting better lead sources.
- Review ROC-AUC, F1-score, and confusion matrix plots before deciding production thresholds.

## Deliverables Covered

- Conversion prediction model saved in `models/best_model.pkl`.
- Logistic Regression and Random Forest models saved separately for comparison.
- Preprocessing pipeline saved in `models/preprocessor.pkl`.
- Sales insights documented here and surfaced through the Streamlit dashboard.
