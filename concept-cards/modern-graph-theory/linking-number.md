---
concept: Linking Number
slug: linking-number
category: knot-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 380
section: "X.7 Exercises"
extraction_confidence: medium
aliases:
  - "lk(C_1, C_2)"
prerequisites:
  - link-diagram
  - writhe
extends: []
related:
  - hopf-link
  - conway-gordon-intrinsic-linking
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The linking number $\text{lk}(C_1, C_2)$ of two oriented link components is half the sum of crossing signs at crossings between $C_1$ and $C_2$. It is an ambient isotopy invariant.

# Core Definition
Exercise 24 (p. 380): "Given an oriented link diagram with two sets of components $C_1$ and $C_2$, let $C_1 \sqcap C_2$ be the set of crossings of $C_1$ and $C_2$. The linking number is $\text{lk}(C_1, C_2) = \frac{1}{2}\sum_{v \in C_1 \sqcap C_2}\varepsilon(v)$."

# Prerequisites
- **Link diagram** — Linking number computed from crossings
- **Writhe** — Uses the same sign convention

# Key Properties
1. An integer (half the sum of $\pm 1$ signs, with even total)
2. Ambient isotopy invariant
3. $\text{lk} = 0$ does not guarantee components are unlinked (e.g., Whitehead link)
4. Hopf link has $|\text{lk}| = 1$

# Relationships
## Builds Upon
- **link-diagram**, **writhe**

## Related
- **hopf-link** — $|\text{lk}| = 1$
- **conway-gordon-intrinsic-linking** — Uses linking numbers

# Source Reference
Chapter X, Exercise 24, page 380.

# Verification Notes
- Definition source: From Exercise 24
- Confidence rationale: Medium -- defined in exercises
- Uncertainties: None
- Cross-reference status: Verified
