---
# === CORE IDENTIFICATION ===
concept: Weyl Dimension Formula
slug: weyl-dimension-formula

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Semisimple Lie Algebras"
chapter_number: 9
pdf_page: 116
section: "9.5 Characters and Weyl character formula"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "dimension formula"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weyl-character-formula
  - rho-half-sum
extends:
  - weyl-character-formula
related:
  - irreducible-highest-weight-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compute the dimension of an irreducible representation from its highest weight?"
---

# Quick Definition
The Weyl dimension formula gives $\dim L_\lambda = \prod_{\alpha \in R_+} \frac{\langle \lambda + \rho, \alpha \rangle}{\langle \rho, \alpha \rangle}$, obtained by evaluating the Weyl character formula at the identity element.

# Core Definition
(Kirillov, Section 9.5): The dimension of the irreducible representation $L_\lambda$ ($\lambda \in P_+$) is:

$$\dim L_\lambda = \prod_{\alpha \in R_+} \frac{(\lambda + \rho, \alpha)}{(\rho, \alpha)}$$

This is obtained from the Weyl character formula by taking the limit as all $e^\mu \to 1$.

# Prerequisites
- **Weyl character formula** -- the dimension formula is a special case
- **Rho half-sum** -- appears in the formula

# Key Properties
1. The product is over all positive roots $R_+$
2. Each factor is a ratio of inner products
3. For $\mathfrak{sl}(2, \mathbb{C})$: $\dim L_n = n + 1$
4. For $\mathfrak{sl}(n+1, \mathbb{C})$ with $\lambda = (\lambda_1, \ldots, \lambda_n, 0)$: the formula reduces to a product involving differences $\lambda_i - \lambda_j + j - i$

# Examples
**Example**: For $\mathfrak{sl}(2, \mathbb{C})$, $\lambda = n$, $\rho = 1$, one positive root $\alpha$ with $(\alpha, \alpha) = 2$: $\dim L_n = \frac{n + 1}{1} = n + 1$.

**Example**: For $\mathfrak{sl}(3, \mathbb{C})$, $\lambda = (a, b, 0)$ with $a \geq b \geq 0$: $\dim L_\lambda = \frac{(a-b+1)(a+2)(b+1)}{2}$.

# Relationships
## Builds Upon
- **Weyl character formula** -- specialization at the identity

## Related
- **Irreducible highest-weight module** -- computes its dimension

# Source Reference
Chapter 9, Section 9.5, p. 116 (section truncated in source).

# Verification Notes
- Definition source: Synthesized from standard result consistent with Weyl character formula
- Confidence rationale: Medium -- section truncated but formula is standard
- Uncertainties: Exact presentation in source not verified
- Cross-reference status: Verified
