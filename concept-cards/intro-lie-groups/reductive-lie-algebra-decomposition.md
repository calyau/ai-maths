---
# === CORE IDENTIFICATION ===
concept: Reductive Algebra Decomposition Theorem
slug: reductive-lie-algebra-decomposition

# === CLASSIFICATION ===
category: structure-theory
subcategory: complete-reducibility
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 81
section: "6.9. Complete reducibility of representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - reductive-lie-algebra
  - complete-reducibility
extends:
  - reductive-lie-algebra
related:
  - levi-decomposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a reductive Lie algebra decompose?"
---

# Quick Definition

Every reductive Lie algebra splits as a direct sum $\mathfrak{g} = \mathfrak{z} \oplus \mathfrak{g}_{ss}$ with $\mathfrak{z}$ commutative and $\mathfrak{g}_{ss}$ semisimple. This is proved using complete reducibility of the adjoint representation.

# Core Definition

**Theorem 6.61** (Kirillov, p. 81): Any reductive Lie algebra can be written as $\mathfrak{g} = \mathfrak{z} \oplus \mathfrak{g}_{ss}$ with $\mathfrak{z}$ commutative and $\mathfrak{g}_{ss}$ semisimple.

# Prerequisites

- **Reductive Lie algebra** — The algebra being decomposed
- **Complete reducibility** — The adjoint representation of $\mathfrak{g}/\mathfrak{z}(\mathfrak{g})$ is used

# Key Properties

1. $\mathfrak{z} = \mathfrak{z}(\mathfrak{g})$ is the center
2. $\mathfrak{g}_{ss} \cong \mathfrak{g}/\mathfrak{z}(\mathfrak{g})$ is semisimple
3. The decomposition is as Lie algebras: $[\mathfrak{z}, \mathfrak{g}_{ss}] = 0$
4. Proved without Levi theorem, using only complete reducibility

# Examples

**Example**: $\mathfrak{gl}(n, \mathbb{C}) = \mathbb{C} \cdot \operatorname{id} \oplus \mathfrak{sl}(n, \mathbb{C})$.

# Relationships

## Builds Upon
- **Complete reducibility** — Used to split the adjoint representation
- **Reductive Lie algebra** — The hypothesis

## Related
- **Levi decomposition** — A more general decomposition for arbitrary algebras

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.9, page 81. Theorem 6.61.

# Verification Notes

- Definition source: Direct from Theorem 6.61
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
