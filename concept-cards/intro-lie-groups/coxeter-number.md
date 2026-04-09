---
# === CORE IDENTIFICATION ===
concept: Coxeter Number and Dual Coxeter Number
slug: coxeter-number

# === CLASSIFICATION ===
category: lie-algebras
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 122
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "h"
  - "h^vee"
  - "dual Coxeter number"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - highest-root
  - weyl-group
extends: []
related:
  - rho-half-sum
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the Coxeter number and dual Coxeter number?"
---

# Quick Definition
The Coxeter number $h$ and dual Coxeter number $h^\vee$ are fundamental numerical invariants of a root system. $h = \mathrm{ht}(\theta) + 1$ and $h^\vee = \mathrm{ht}(\theta^\vee) + 1 = \langle \rho, \theta^\vee \rangle + 1$.

# Core Definition
(Kirillov, p. 122):

$$h = \mathrm{ht}(\theta) + 1, \qquad h^\vee = \mathrm{ht}(\theta^\vee) + 1 = \langle \rho, \theta^\vee \rangle + 1$$

where $\theta$ is the highest root and $\rho = \frac{1}{2}\sum_{R_+} \alpha$.

# Prerequisites
- **Highest root** -- $h$ is defined in terms of $\theta$
- **Weyl group** -- related to the order of a Coxeter element

# Key Properties
1. For simply-laced root systems: $h = h^\vee$
2. Values for classical types:
   - $A_n$: $h = h^\vee = n+1$
   - $B_n$: $h = 2n$, $h^\vee = 2n-1$
   - $C_n$: $h = 2n$, $h^\vee = n+1$
   - $D_n$: $h = h^\vee = 2n-2$

# Examples
**Example** (pp. 123-129): See key properties for explicit values.

# Relationships
## Builds Upon
- **Highest root** -- defines $h$

## Related
- **Rho half-sum** -- appears in the formula for $h^\vee$

# Source Reference
Appendix C, notation section, p. 122, with values pp. 123-129.

# Verification Notes
- Definition source: Direct from p. 122
- Confidence rationale: Explicit definition and values
- Uncertainties: None
- Cross-reference status: Verified
