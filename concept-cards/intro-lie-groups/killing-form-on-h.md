---
# === CORE IDENTIFICATION ===
concept: Killing Form on the Cartan Subalgebra
slug: killing-form-on-h

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 86
section: "7.3. Root decomposition and root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "(alpha, beta)"
  - "inner product on h*"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - killing-form
  - cartan-subalgebra
  - root-decomposition
extends:
  - killing-form
related:
  - coroot-of-lie-algebra
  - h-alpha
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Killing form define an inner product on the root space?"
---

# Quick Definition

The restriction of the Killing form to the Cartan subalgebra $\mathfrak{h}$ is non-degenerate, giving an identification $\mathfrak{h} \cong \mathfrak{h}^*$ and an induced inner product $(\alpha, \beta)$ on $\mathfrak{h}^*$. This inner product governs the geometry of the root system.

# Core Definition

(Kirillov, p. 86): Since the Killing form restricted to $\mathfrak{h}$ is non-degenerate (Theorem 7.16), it defines an isomorphism $\mathfrak{h} \xrightarrow{\sim} \mathfrak{h}^*$ and a bilinear form on $\mathfrak{h}^*$. For $\alpha \in \mathfrak{h}^*$, let $H_\alpha \in \mathfrak{h}$ be the corresponding element. Then:

$$(\alpha, \beta) = (H_\alpha, H_\beta) = \langle H_\alpha, \beta \rangle.$$

# Prerequisites

- **Killing form** — The restriction to $\mathfrak{h}$
- **Cartan subalgebra** — The domain of restriction
- **Root decomposition** — Provides the context

# Key Properties

1. $(\alpha, \beta) \in \mathbb{R}$ for $\alpha, \beta \in R$ (since $\langle h_\alpha, \beta \rangle \in \mathbb{Z}$)
2. The form is positive definite on $\mathfrak{h}_{\mathbb{R}}^*$ (Theorem 7.22)
3. For $\mathfrak{sl}(n, \mathbb{C})$: $(\lambda, \mu) = \frac{1}{2n}\sum_i \lambda_i \mu_i$ (Example 7.17)
4. $(\alpha, \alpha) \neq 0$ for all roots $\alpha$ (Lemma 7.19)

# Examples

**Example 7.17** (p. 86): For $\mathfrak{sl}(n, \mathbb{C})$: $(h, h') = 2n \operatorname{tr}(hh')$ on $\mathfrak{h}$. On $\mathfrak{h}^*$: $(\lambda, \mu) = \frac{1}{2n}\sum_i \lambda_i \mu_i$ where $\lambda = \sum \lambda_i e_i$, $\mu = \sum \mu_i e_i$ with $\sum \lambda_i = \sum \mu_i = 0$.

# Relationships

## Builds Upon
- **Killing form** — Restriction to $\mathfrak{h}$

## Enables
- **Coroot** — $h_\alpha = \frac{2H_\alpha}{(\alpha, \alpha)}$ uses this form
- **Root system geometry** — All angles and lengths determined by $(\cdot, \cdot)$

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, pages 86. Equation (7.3), Example 7.17.

# Verification Notes

- Definition source: Direct from p. 86 discussion
- Confidence rationale: Explicit formulas given
- Uncertainties: None
- Cross-reference status: Verified
