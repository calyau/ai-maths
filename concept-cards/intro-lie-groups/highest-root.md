---
# === CORE IDENTIFICATION ===
concept: Highest Root
slug: highest-root

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
  - "theta"
  - "maximal root"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system
  - positive-roots
extends: []
related:
  - coxeter-number
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the highest root of a root system?"
---

# Quick Definition
The highest root $\theta$ is the unique root that is maximal in the partial order defined by the positive roots: it is the largest root when expanded in simple roots. The Coxeter number is $h = \mathrm{ht}(\theta) + 1$.

# Core Definition
(Kirillov, p. 122): The notation $\theta$ denotes the highest root of the root system. For each classical type:
- $A_n$: $\theta = e_1 - e_{n+1}$
- $B_n$: $\theta = e_1 + e_2$
- $C_n$: $\theta = 2e_1$
- $D_n$: $\theta = e_1 + e_2$

# Prerequisites
- **Root system** -- the highest root is a specific root
- **Positive roots** -- maximal among positive roots

# Key Properties
1. $\theta$ is unique
2. $\theta = \sum n_i \alpha_i$ with all $n_i > 0$ (all simple roots appear with positive coefficient)
3. $\mathrm{ht}(\theta) = h - 1$ where $h$ is the Coxeter number
4. The adjoint representation has highest weight $\theta$

# Examples
**Example** (pp. 123-129):
- $A_n$: $\theta = e_1 - e_{n+1} = \alpha_1 + \cdots + \alpha_n$, $h = n+1$
- $B_n$: $\theta = e_1 + e_2$, $h = 2n$
- $C_n$: $\theta = 2e_1$, $h = 2n$
- $D_n$: $\theta = e_1 + e_2$, $h = 2n-2$

# Relationships
## Related
- **Coxeter number** -- $h = \mathrm{ht}(\theta) + 1$

# Source Reference
Appendix C, notation section p. 122, with explicit values pp. 123-129.

# Verification Notes
- Definition source: Direct from p. 122 notation
- Confidence rationale: Explicit for each type
- Uncertainties: None
- Cross-reference status: Verified
