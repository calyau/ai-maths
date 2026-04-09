---
# === CORE IDENTIFICATION ===
concept: Group Cancellation Laws
slug: group-cancellation-laws

# === CLASSIFICATION ===
category: group-theory
subcategory: group-properties
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 50
section: "Basic Properties of Groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - cancellation laws

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - inverse-uniqueness
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

In a group, left and right cancellation laws hold: $ba = ca$ implies $b = c$, and $ab = ac$ implies $b = c$.

# Core Definition

**Proposition 3.22**: "If $G$ is a group and $a, b, c \in G$, then $ba = ca$ implies $b = c$ and $ab = ac$ implies $b = c$" (Judson, p. 50).

Also, **Proposition 3.21**: The equations $ax = b$ and $xa = b$ have unique solutions in any group $G$.

# Prerequisites

- **Group** — Cancellation laws hold in groups
- **Inverse uniqueness** — Follows from unique inverses

# Key Properties

1. Left cancellation: $ab = ac \Rightarrow b = c$
2. Right cancellation: $ba = ca \Rightarrow b = c$
3. Equations $ax = b$ and $xa = b$ have unique solutions: $x = a^{-1}b$ and $x = ba^{-1}$

# Context & Application

The cancellation laws distinguish groups from general algebraic structures. For example, in $\mathbb{Z}_{12}$, $3 \cdot 4 = 3 \cdot 0 = 0$ but $4 \neq 0$, so cancellation fails for multiplication in $\mathbb{Z}_{12}$ (which is not a group under multiplication).

# Examples

**Example 1** (p. 50): If $ax = b$, multiply both sides on the left by $a^{-1}$: $x = a^{-1}b$. Uniqueness: if $ax_1 = ax_2$, then $x_1 = a^{-1}ax_1 = a^{-1}ax_2 = x_2$.

# Relationships

## Builds Upon
- **group** — Cancellation laws hold in groups
- **inverse-uniqueness** — Needed for the proof

# Source Reference

Chapter 3: Groups, Section 3.2, Propositions 3.21-3.22, pages 49-50.

# Verification Notes

- Definition source: Direct from Propositions 3.21-3.22
- Confidence: HIGH — explicit propositions
- Cross-reference status: Verified
- Uncertainties: None
