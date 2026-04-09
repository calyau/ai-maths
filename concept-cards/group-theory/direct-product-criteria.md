---
# === CORE IDENTIFICATION ===
concept: Criteria for Direct Products
slug: direct-product-criteria

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 23
section: "Direct products"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - direct-product-internal
  - normal-subgroup
  - commutator
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can I tell if a group is a direct product of two subgroups?"
  - "What conditions guarantee G = H1 x H2?"
---

# Quick Definition

A group $G$ is a direct product of $H_1, H_2$ if and only if $G = H_1 H_2$, $H_1 \cap H_2 = \{e\}$, and either both are normal or every element of $H_1$ commutes with every element of $H_2$.

# Core Definition

**Proposition 1.50**: $G$ is a direct product of $H_1, H_2$ iff (a) $G = H_1 H_2$, (b) $H_1 \cap H_2 = \{e\}$, (c) every element of $H_1$ commutes with every element of $H_2$.

**Proposition 1.51**: $G$ is a direct product of $H_1, H_2$ iff (a) $G = H_1 H_2$, (b) $H_1 \cap H_2 = \{e\}$, (c) both $H_1$ and $H_2$ are normal in $G$.

**Proposition 1.52** (general case): $G = H_1 \times \cdots \times H_k$ iff (a) $G = H_1 \cdots H_k$, (b) $H_j \cap (H_1 \cdots \hat{H_j} \cdots H_k) = \{e\}$ for each $j$, (c) each $H_i$ is normal.

# Prerequisites

- **Internal direct product** — these criteria characterize direct products
- **Normal subgroup** — normality is one of the criteria
- **Commutator** — the proof that (1.51) implies (1.50) uses commutators

# Key Properties

1. In Proposition 1.51, normality of both factors forces commutativity between them
2. The proof uses the commutator: $[h_1, h_2] = h_1 h_2 h_1^{-1} h_2^{-1} \in H_1 \cap H_2$ (by normality of both), hence $= e$

# Context & Application

These criteria are the standard tools for recognizing when a group decomposes as a direct product. They are used throughout finite group theory.

# Examples

**Example 1**: $D_2 = \{e, r, s, rs\}$ satisfies: $\langle r \rangle \cap \langle s \rangle = \{e\}$, $\langle r \rangle \langle s \rangle = D_2$, and both have index 2 (hence normal). So $D_2 \cong C_2 \times C_2$.

# Relationships

## Builds Upon
- **direct-product-internal**, **normal-subgroup**, **commutator**

# Source Reference

Chapter 1, Propositions 1.50-1.52, pages 23-24.

# Verification Notes

- Definition source: Direct from Propositions 1.50-1.52
- Confidence: HIGH
- Uncertainties: None
