---
concept: College Admissions Problem
slug: college-admissions-problem
category: matchings
subcategory: stable-matchings
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.5 Stable Matchings"
extraction_confidence: high
aliases:
  - "Theorem 22"
  - "stable admissions scheme"
prerequisites:
  - stable-matching
  - optimal-stable-matching
extends:
  - optimal-stable-matching
related:
  - gale-shapley-algorithm
contrasts_with: []
answers_questions:
  - "How does stable matching extend to many-to-one assignments?"
---

# Quick Definition
The college admissions problem assigns $n$ applicants to $m$ colleges (each with quota $n_i$) such that the assignment is stable — no student-college pair would both prefer to be matched to each other. An optimal stable admissions scheme always exists.

# Core Definition
**Theorem 22**: No matter what the orders of preferences are, there is always an optimal stable admissions scheme. The proof reduces to the one-to-one case by replacing each college $A_i$ with $n_i$ copies, each having the same preference ordering over students (Bollobás, p. 100).

# Prerequisites
- **Stable matching** — The assignment must be stable
- **Optimal stable matching** — Optimality for the applicants

# Key Properties
1. Reduces to one-to-one stable matching by replicating colleges
2. The adapted Gale-Shapley algorithm: students apply, colleges keep best applicants
3. Satisfies: (i) each college admits at most $n_i$, (ii) unfilled colleges have no rejected applicants, (iii) stability
4. Every student gets as good a college as under any other stable scheme

# Construction / Recognition
1. All students apply to their top-ranked colleges
2. Each college $A_i$ keeps its $n_i$ highest-ranked applicants, rejects others
3. Rejected students apply to next choices
4. Repeat until no rejections occur

# Context & Application
Models real-world assignment problems like medical residency matching (NRMP), school choice, and university admissions.

# Examples
**Example** (p. 100): Replace college $A_i$ by $n_i$ identical copies. Run boy-optimal Gale-Shapley. The resulting assignment is optimal for applicants.

# Relationships
## Builds Upon
- **optimal-stable-matching** — Generalized to many-to-one

## Related
- **gale-shapley-algorithm** — Adapted for this setting

# Source Reference
Chapter III, Section III.5, pages 100-101. Theorem 22.

# Verification Notes
- Definition source: Direct from pp. 100-101
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
