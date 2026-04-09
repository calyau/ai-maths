---
# === CORE IDENTIFICATION ===
concept: Galois Correspondence
slug: galois-correspondence

# === CLASSIFICATION ===
category: galois-theory
subcategory: field-automorphisms
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.2 The Fundamental Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Galois connection"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fundamental-theorem-of-galois-theory
  - galois-group
  - fixed-field
extends: []
related:
  - normal-extension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Galois correspondence work?"
  - "How do subgroups correspond to intermediate fields?"
---

# Quick Definition

The Galois correspondence is the inclusion-reversing bijection between subgroups of the Galois group $G(E/F)$ and intermediate fields between $F$ and $E$. A subgroup $H$ corresponds to its fixed field $E_H$, and an intermediate field $K$ corresponds to $G(E/K)$.

# Core Definition

For a Galois extension $E/F$, the **Galois correspondence** consists of two mutually inverse maps (from Theorem 23.23, Judson, p. 314):

- **Subgroups to fields:** $H \mapsto E_H$ (the fixed field of $H$)
- **Fields to subgroups:** $K \mapsto G(E/K)$ (the automorphisms fixing $K$)

These maps are inclusion-reversing: $H_1 \leq H_2$ if and only if $E_{H_1} \supseteq E_{H_2}$.

# Prerequisites

- **Fundamental Theorem of Galois Theory** — Establishes the correspondence
- **Galois group** — One side of the correspondence
- **Fixed field** — The map from subgroups to fields

# Key Properties

1. The correspondence reverses inclusions (bigger subgroup = smaller field)
2. $[K:F] = [G(E/F):G(E/K)]$ (degree = index)
3. Normal subgroups correspond to normal extensions of $F$
4. When $G(E/K)$ is normal in $G(E/F)$: $G(K/F) \cong G(E/F)/G(E/K)$

# Context & Application

The Galois correspondence is the heart of Galois theory. It transforms field-theoretic questions (about field extensions) into group-theoretic questions (about subgroup structure), which are often easier to answer. This is the tool that allows us to determine solvability by radicals.

# Examples

**Example 1** (p. 314): For $\mathbb{Q}(\sqrt{3}, \sqrt{5})/\mathbb{Q}$ with $G \cong \mathbb{Z}_2 \times \mathbb{Z}_2$:
- $\{id, \sigma\}$ corresponds to $\mathbb{Q}(\sqrt{5})$
- $\{id, \tau\}$ corresponds to $\mathbb{Q}(\sqrt{3})$
- $\{id, \mu\}$ corresponds to $\mathbb{Q}(\sqrt{15})$

**Example 2** (p. 315): For $x^4 - 2$ over $\mathbb{Q}$, the Galois group $D_4$ has 10 subgroups, corresponding to 10 intermediate fields.

# Relationships

## Builds Upon
- **Fundamental Theorem of Galois Theory** — Establishes the correspondence

## Related
- **Normal extension** — Normal subgroups $\leftrightarrow$ normal intermediate extensions

# Source Reference

Chapter 23: Galois Theory, Section 23.2, pages 314–316.

# Verification Notes

- Definition source: Synthesized from Theorem 23.23
- Confidence: HIGH — direct consequence of the Fundamental Theorem
- Cross-reference status: Verified
- Uncertainties: None
