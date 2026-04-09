---
# === CORE IDENTIFICATION ===
concept: Representations of sl(n,C)
slug: representations-of-sln

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Semisimple Lie Algebras"
chapter_number: 9
pdf_page: 116
section: "9.6 Representations of sl(n,C)"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "representations of type A"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finite-dimensional-criterion
  - dominant-integral-weight
  - root-system-type-a
extends: []
related:
  - exterior-power-representation
  - fundamental-weights-type-a
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are irreducible representations of sl(n,C) constructed explicitly?"
---

# Quick Definition
The irreducible finite-dimensional representations of $\mathfrak{sl}(n, \mathbb{C})$ are parametrized by dominant integral weights $\lambda = (\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n \geq 0)$ with $\lambda_i \in \mathbb{Z}$. They can be constructed explicitly using exterior powers and Schur functors applied to the standard representation.

# Core Definition
(Kirillov, Section 9.6, p. 116): For $\mathfrak{g} = \mathfrak{sl}(n, \mathbb{C})$, the irreducible representations $L_\lambda$ can be constructed explicitly, typically using exterior powers $\Lambda^k \mathbb{C}^{n+1}$ as the fundamental representations and combining them via tensor products and projections.

# Prerequisites
- **Finite-dimensional criterion** -- $L_\lambda$ is finite-dimensional iff $\lambda \in P_+$
- **Dominant integral weight** -- the parametrizing data
- **Root system type A** -- the underlying root system

# Key Properties
1. Dominant integral weights for $A_n$ are tuples $(\lambda_1, \ldots, \lambda_n, 0)$ with $\lambda_1 \geq \cdots \geq \lambda_n \geq 0$, $\lambda_i \in \mathbb{Z}$
2. The fundamental representations are $\Lambda^k \mathbb{C}^{n+1}$ for $k = 1, \ldots, n$
3. Every irreducible representation can be realized inside tensor products of the standard representation
4. The dimension is given by the Weyl dimension formula or by hook-length formulas

# Context & Application
Section 9.6 provides the explicit construction of representations of $\mathfrak{sl}(n, \mathbb{C})$ that complements the abstract classification via highest weights. This is the most important special case since many applications involve $\mathfrak{sl}(n, \mathbb{C})$ and its compact real form $\mathfrak{su}(n)$.

# Examples
**Example**: For $\mathfrak{sl}(2, \mathbb{C})$: $L_n = \mathrm{Sym}^n(\mathbb{C}^2)$, the $n$-th symmetric power of the standard representation.

**Example**: For $\mathfrak{sl}(3, \mathbb{C})$: the fundamental representations are $\mathbb{C}^3$ (standard) and $\Lambda^2 \mathbb{C}^3 \cong (\mathbb{C}^3)^*$ (dual standard).

# Relationships
## Builds Upon
- **Finite-dimensional criterion** -- identifies which representations are finite-dimensional
- **Root system type A** -- the root system data

## Related
- **Exterior power representation** -- provides the fundamental representations

# Source Reference
Chapter 9, Section 9.6 "Representations of sl(n,C)," p. 116.

# Verification Notes
- Definition source: Synthesized from section heading; content is truncated in source markdown
- Confidence rationale: Medium -- section is listed but content not fully present
- Uncertainties: Exact constructions presented by Kirillov not verified from truncated section
- Cross-reference status: Verified
