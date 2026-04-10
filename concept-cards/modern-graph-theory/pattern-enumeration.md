---
# === CORE IDENTIFICATION ===
concept: Pattern Enumeration
slug: pattern-enumeration

# === CLASSIFICATION ===
category: graph-enumeration
subcategory: orbit-counting
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 287
section: "VIII.4 Enumeration and Pólya's Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - configuration counting
  - counting under symmetry

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-orbit
  - cycle-index
extends: []
related:
  - polya-enumeration-theorem
  - cauchy-frobenius-lemma
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I count configurations up to symmetry?"
---

# Quick Definition

A pattern is an equivalence class of configurations (functions from a domain $D$ to a range $R$) under a group $\Gamma^*$ of permutations, and the pattern sum $S = \sum_i w(O_i)$ counts (weighted) orbits.

# Core Definition

The set $D$ is the domain (places), $R$ is the range (figures), functions $f \in R^D$ are configurations, and $\Gamma^*$-orbits are patterns. Each $\alpha \in \Gamma$ induces $\alpha^*: R^D \to R^D$ by $(\alpha^*f)(d) = f(\alpha d)$. The pattern sum $S = \sum_i w(O_i)$ over orbits $O_1, \ldots, O_\ell$ encodes all enumerative information, and is computed by Polya's theorem: $|\Gamma|S = \widetilde{Z}(\Gamma; s_1, \ldots, s_d)$ (Bollobas, pp. 287--288).

# Prerequisites

- **Group orbit** -- Patterns are orbits in a function space
- **Cycle index** -- Required for computation

# Key Properties

1. Counting graphs up to isomorphism is a pattern enumeration problem
2. The weight ring $A$ and weight function $w$ can be chosen to extract specific information
3. Choosing $A = \mathbb{Z}$ and $w \equiv 1$ counts total patterns
4. Choosing polynomial weights gives generating functions by type

# Construction / Recognition

## Setup for Pattern Enumeration
1. Identify the domain $D$ (places), range $R$ (figures), and symmetry group $\Gamma$
2. Configurations are functions $f: D \to R$
3. Two configurations are equivalent if related by $\Gamma^*$
4. Patterns = equivalence classes = $\Gamma^*$-orbits

# Context & Application

Pattern enumeration unifies a wide class of counting problems: necklace problems, colorings of polyhedra, graph isomorphism counting, and chemical isomer enumeration.

# Examples

**Example** (p. 288): Bracelets of 5 beads with 3 colors: $D = \{1,\ldots,5\}$, $R = \{r, b, g\}$, $\Gamma = C_5$.

# Relationships

## Builds Upon
- **Group orbit** -- Patterns are orbits
- **Cycle index** -- Computational tool

## Enables
- Counting graphs up to isomorphism

## Related
- **Polya's enumeration theorem** -- The computation engine

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting that configurations in the same pattern have the same weight
  **Correction**: The weight function must be constant on orbits, which is guaranteed when $w$ is defined on figures

# Common Confusions

- **Confusion**: Thinking patterns depend on the labeling of places
  **Clarification**: Patterns are equivalence classes under $\Gamma^*$; they are independent of labeling

# Source Reference

Chapter VIII, Section VIII.4, pages 287--288.

# Verification Notes

- Definition source: Direct from pp. 287--288
- Confidence rationale: Explicit framework
- Uncertainties: None
- Cross-reference status: Verified
