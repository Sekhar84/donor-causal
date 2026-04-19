# donor-causal · Causal Inference for Fundraising Campaigns

> Formalising causal questions in direct mail fundraising — two independent
> client analyses with different assignment mechanisms, compared at the
> methodological level. Delivered as a management report (CEO level) and
> a conference slide insert (8 slides).
> Part of the donor intelligence system — see
> [donor-intelligence-system](https://github.com/Sekhar84/donor-intelligence-system)

## The causal question

Campaigns with physical inserts (pen, badge, charm) show higher response
rates than standard packs. Does including an insert **cause** higher
response — or does the lift reflect selection bias in who receives them?

## Why two clients

The ability to draw causal conclusions from observational data depends on
how the data was generated — specifically, how insert assignment was
determined. Two clients with different assignment mechanisms are studied
independently. The question is not which client is "better" — it is
whether the assignment mechanism determines what conclusions are reachable
from existing data.

## Methods applied

For each client: randomisation check → PSM → DiD → RDD → IV → uplift
modelling (S/T/X-learner) → power analysis for proposed RCT.

## Key principle

**Conclusions are not pre-specified.** The README documents the design.
`reports/` contains conclusions written after analysis runs.

## Deliverables

| Output | Audience | Length | Due |
|--------|----------|--------|-----|
| Management report | CEO level | 4–6 pages | Jun 14 |
| Conference slide insert | GM presentation | 8 slides | Jun 14 |

## Part of the DS modernisation project

[donor-ev-scorer](https://github.com/Sekhar84/donor-ev-scorer) ·
[donor-cltv](https://github.com/Sekhar84/donor-cltv) ·
[ds-mlops-stack](https://github.com/Sekhar84/ds-mlops-stack) ·
[donor-intelligence-system](https://github.com/Sekhar84/donor-intelligence-system)
