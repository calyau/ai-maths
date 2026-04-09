---
# === CORE IDENTIFICATION ===
concept: Height Function
slug: height-function

# === CLASSIFICATION ===
category: root-systems
subcategory: simple-positive-roots
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 96
section: "8.4. Positive roots and simple roots"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "height of a root"
  - "$\\operatorname{ht}$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots
  - positive-roots
extends: []
related:
  - weyl-length
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the height of a root?"
---

# Quick Definition
The height of a positive root $\alpha = \sum n_i\alpha_i$ is $\operatorname{ht}(\alpha) = \sum n_i$, the sum of its coefficients in the simple root basis. Simple roots have height 1.

# Core Definition
For a positive root $\alpha = \sum_{i=1}^r n_i\alpha_i \in R_+$, the height is defined by (equation 8.8, p. 96):

$$\operatorname{ht}\left(\sum n_i\alpha_i\right) = \sum n_i \in \mathbb{Z}_+$$

so that $\operatorname{ht}(\alpha_i) = 1$ for each simple root.

# Prerequisites
- **simple-roots** -- the height is defined using the simple root expansion
- **positive-roots** -- height is defined for positive roots

# Key Properties
1. $\operatorname{ht}(\alpha_i) = 1$ for every simple root
2. $\operatorname{ht}(\alpha) \geq 1$ for every $\alpha \in R_+$
3. Height provides a useful filtration for induction arguments on positive roots
4. For negative roots, one can define $\operatorname{ht}(\alpha) = -\operatorname{ht}(-\alpha) < 0$

# Construction / Recognition
1. Express $\alpha$ in the simple root basis: $\alpha = \sum n_i\alpha_i$
2. Sum the coefficients: $\operatorname{ht}(\alpha) = \sum n_i$

# Context & Application
Height is a key tool for inductive arguments. Many statements about positive roots are proved by induction on height, since any non-simple positive root can be decomposed into pieces of strictly smaller height.

# Examples
**Example 8.19** (p. 96): For $A_{n-1}$, $\operatorname{ht}(e_i - e_j) = j - i$. For instance, $e_2 - e_4 = \alpha_2 + \alpha_3$ has height 2.

# Relationships
## Builds Upon
- **simple-roots** -- the basis for computing height

## Enables
- Inductive arguments on root systems

## Related
- **weyl-length** -- a different notion of "size" defined on the Weyl group

## Contrasts With
(none)

# Common Errors
- **Error**: Confusing height with the Euclidean length of a root
  **Correction**: Height is a combinatorial quantity (sum of coefficients), not a metric one

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.4, page 96. Equation (8.8).

# Verification Notes
- Definition source: Direct from equation (8.8)
- Confidence rationale: HIGH -- explicit formula
- Uncertainties: None
- Cross-reference status: Verified
