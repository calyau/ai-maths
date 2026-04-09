---
# === CORE IDENTIFICATION ===
concept: Reductivity from Non-Degenerate Trace Form
slug: reductivity-from-trace-form

# === CLASSIFICATION ===
category: structure-theory
subcategory: bilinear-forms
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 73
section: "6.5. Invariant bilinear forms and semisimplicity of classical Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 6.32"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - trace-form
  - radical-action-on-irreducibles
extends: []
related:
  - reductive-lie-algebra
  - semisimplicity-of-classical-algebras
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a non-degenerate trace form imply reductivity?"
---

# Quick Definition

If $\mathfrak{g}$ has a representation $V$ whose trace form $B_V(x,y) = \operatorname{tr}_V(\rho(x)\rho(y))$ is non-degenerate, then $\mathfrak{g}$ is reductive. This is the practical tool for proving classical algebras are reductive/semisimple.

# Core Definition

**Theorem 6.32** (Kirillov, p. 73): Let $\mathfrak{g}$ be a Lie algebra with a representation $V$ such that $B_V$ is non-degenerate. Then $\mathfrak{g}$ is reductive.

Proof: If $x \in [\mathfrak{g}, \operatorname{rad}(\mathfrak{g})]$, then $x$ acts by zero in every irreducible representation (Theorem 6.27), hence $x \in \operatorname{Ker} B_V = 0$.

# Prerequisites

- **Trace form** — The form $B_V$
- **Radical action on irreducibles** — $[\mathfrak{g}, \operatorname{rad}(\mathfrak{g})]$ acts by zero

# Key Properties

1. The proof uses only that elements of $[\mathfrak{g}, \operatorname{rad}(\mathfrak{g})]$ kill $B_V$
2. Non-degeneracy forces $[\mathfrak{g}, \operatorname{rad}(\mathfrak{g})] = 0$, i.e., reductivity
3. Combined with center computation, gives semisimplicity

# Relationships

## Enables
- **Semisimplicity of classical algebras** — Applied to defining representations

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.5, page 73. Theorem 6.32.

# Verification Notes

- Definition source: Direct from Theorem 6.32
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
