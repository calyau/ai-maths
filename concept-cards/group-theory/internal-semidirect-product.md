---
# === CORE IDENTIFICATION ===
concept: Internal Semidirect Product
slug: internal-semidirect-product

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: products
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 45
section: "Semidirect products"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semidirect-product
extends: []
related:
  - external-semidirect-product
contrasts_with:
  - external-semidirect-product

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct a semidirect product from a normal subgroup and a complement?"
---

# Quick Definition

An internal semidirect product identifies a group $G$ as $N \rtimes Q$ where $N$ and $Q$ are actual subgroups of $G$ with $N \trianglelefteq G$, $NQ = G$, and $N \cap Q = \{1\}$.

# Core Definition

When $G$ contains subgroups $N$ and $Q$ satisfying $N \trianglelefteq G$, $NQ = G$, $N \cap Q = \{1\}$ (equation (15), p. 45), then $G$ is the internal semidirect product $N \rtimes Q$. The action $\theta: Q \to \operatorname{Aut}(N)$ is conjugation: $\theta(q)(n) = qnq^{-1}$.

# Prerequisites

- **Semidirect product** — This is one perspective on semidirect products

# Key Properties

1. Every element $g$ can be written uniquely as $g = nq$
2. The product rule follows from conjugation: $gg' = n \cdot \theta(q)(n') \cdot qq'$
3. The action is automatically given by conjugation within $G$

# Context & Application

Internal semidirect products arise when analyzing the structure of a given group. Recognizing a group as an internal semidirect product decomposes it into simpler pieces.

# Examples

**Example 1** (p. 45): $D_n = \langle r \rangle \rtimes \langle s \rangle$, with $\langle r \rangle \trianglelefteq D_n$.

**Example 2** (p. 46): $B = U \rtimes T$ in $\operatorname{GL}_n(F)$.

# Relationships

## Contrasts With
- **external-semidirect-product** — External construction starts from separate groups and an action map

# Source Reference

Chapter 3: Automorphisms and Extensions, "Semidirect products", pages 45-46.

# Verification Notes

- Definition source: Equation (15), p. 45
- Confidence: MEDIUM — synthesized from discussion
- Uncertainties: None
