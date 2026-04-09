---
# === CORE IDENTIFICATION ===
concept: Multiplicity of an Irreducible Representation
slug: multiplicity-of-irreducible

# === CLASSIFICATION ===
category: representations
subcategory: irreducibility
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 41
section: "4.3 Irreducible representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "isotypic component"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - completely-reducible-representation
  - irreducible-representation
extends: []
related:
  - multiplicity-formula
  - character-of-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the multiplicity of an irreducible in a representation?"
---

# Quick Definition

In a completely reducible representation $V \simeq \bigoplus n_i V_i$, the multiplicity $n_i$ is the number of times the irreducible $V_i$ appears as a direct summand. It can be computed as $n_i = (\chi_V, \chi_{V_i})$.

# Core Definition

**Definition 4.17** (Kirillov, p. 41): In a completely reducible representation $V \simeq \bigoplus n_i V_i$ where $V_i$ are pairwise non-isomorphic irreducible representations, the numbers $n_i \in \mathbb{Z}_+$ are called multiplicities.

**Corollary 4.44** (p. 49): $n_i = (\chi_V, \chi_{V_i})$.

# Prerequisites

- **Completely reducible representation** — Must decompose to define multiplicities
- **Irreducible representation** — The building blocks

# Key Properties

1. Multiplicities are uniquely determined
2. $(\chi_V, \chi_V) = \sum n_i^2$
3. $V$ is irreducible iff exactly one $n_i = 1$ and all others are 0

# Examples

**Example**: For $\mathfrak{sl}(2,\mathbb{C})$, $P_n \simeq V_0 \oplus V_2 \oplus \cdots \oplus V_{2n}$, so each $V_{2k}$ appears with multiplicity 1 in $P_n$ (equation 5.10).

# Relationships

## Builds Upon
- **Completely reducible representation** — Provides the decomposition

## Related
- **Multiplicity formula** — $n_i = (\chi_V, \chi_{V_i})$
- **Character** — Encodes multiplicities

# Source Reference

Chapter 4, Section 4.3, Definition 4.17, p. 41; Corollary 4.44, p. 49.

# Verification Notes

- Definition source: Direct from Definition 4.17
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
