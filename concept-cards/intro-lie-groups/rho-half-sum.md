---
# === CORE IDENTIFICATION ===
concept: Half-Sum of Positive Roots (rho)
slug: rho-half-sum

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
  - "rho"
  - "Weyl vector"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - positive-roots
  - weight-lattice
extends: []
related:
  - weyl-character-formula
  - coxeter-number
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is rho (the half-sum of positive roots)?"
  - "What must I know before understanding the Weyl character formula?"
---

# Quick Definition
The element $\rho = \frac{1}{2}\sum_{\alpha \in R_+} \alpha$ is the half-sum of all positive roots. It equals the sum of fundamental weights $\rho = \omega_1 + \cdots + \omega_r$ and plays a central role in the Weyl character formula.

# Core Definition
(Kirillov, p. 122): $\rho = \frac{1}{2}\sum_{R_+} \alpha$ (see equation (8.22)). For each classical type:
- $A_n$: $\rho = (n, n-1, \ldots, 1, 0)$
- $B_n$: $\rho = (n - \frac{1}{2}, n - \frac{3}{2}, \ldots, \frac{1}{2})$
- $C_n$: $\rho = (n, n-1, \ldots, 1)$
- $D_n$: $\rho = (n-1, n-2, \ldots, 0)$

# Prerequisites
- **Positive roots** -- $\rho$ is their half-sum
- **Weight lattice** -- $\rho$ is always in the weight lattice

# Key Properties
1. $\rho = \omega_1 + \omega_2 + \cdots + \omega_r$ (sum of all fundamental weights)
2. $\langle \rho, \alpha_i^\vee \rangle = 1$ for all simple roots $\alpha_i$
3. Appears in the Weyl character formula: $\mathrm{ch}(L_\lambda) = \frac{\sum_w (-1)^{\ell(w)} e^{w(\lambda+\rho)}}{\sum_w (-1)^{\ell(w)} e^{w\rho}}$
4. The shifted action of the Weyl group is $w \cdot \lambda = w(\lambda + \rho) - \rho$

# Context & Application
$\rho$ appears throughout representation theory as a "correction term." It arises naturally in the Weyl character formula, the dimension formula, and the BGG resolution. The shifted Weyl group action $w \cdot \lambda = w(\lambda + \rho) - \rho$ is often more natural than the unshifted action.

# Examples
**Example** (pp. 123-129): See explicit values in Core Definition above.

# Relationships
## Enables
- **Weyl character formula** -- $\rho$ appears in both numerator and denominator
- **Shifted Weyl group action** -- $w \cdot \lambda = w(\lambda + \rho) - \rho$

## Related
- **Coxeter number** -- $h^\vee = \langle \rho, \theta^\vee \rangle + 1$

# Source Reference
Appendix C, p. 122, with explicit values pp. 123-129.

# Verification Notes
- Definition source: Direct from p. 122 (referencing equation (8.22))
- Confidence rationale: Explicit definition and values
- Uncertainties: None
- Cross-reference status: Verified
