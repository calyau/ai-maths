---
concept: Groups of Order p-Squared are Abelian
slug: groups-of-order-p-squared
category: group-structure
subcategory: p-group-theory
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 185
section: "The Class Equation"
extraction_confidence: high
aliases: []
prerequisites:
  - nontrivial-center-of-p-group
  - class-equation
extends: []
related:
  - p-group
  - fundamental-theorem-of-finite-abelian-groups
contrasts_with: []
answers_questions:
  - "Why is every group of order p^2 abelian?"
---

# Quick Definition

Every group of order $p^2$ (where $p$ is prime) is abelian, and is isomorphic to either $\mathbb{Z}_{p^2}$ or $\mathbb{Z}_p \times \mathbb{Z}_p$.

# Core Definition

**Corollary 14.16**: "Let $G$ be a group of order $p^2$ where $p$ is prime. Then $G$ is abelian" (Judson, p. 185). The proof: $|Z(G)| = p$ or $p^2$. If $|Z(G)| = p^2$, done. If $|Z(G)| = p$, then $G/Z(G)$ is cyclic of order $p$, which forces $G$ to be abelian — contradiction.

# Prerequisites

- **Nontrivial center of p-group** — $|Z(G)| \geq p$
- **Class equation** — Determines $|Z(G)|$

# Key Properties

1. Groups of order $p^2$ are abelian
2. They are isomorphic to $\mathbb{Z}_{p^2}$ or $\mathbb{Z}_p \times \mathbb{Z}_p$
3. Groups of orders 4, 9, 25, 49 are all abelian

# Context & Application

This result is used in the Sylow theory to determine the structure of Sylow $p$-subgroups of order $p^2$.

# Examples

**Example 1**: Groups of order 4: $\mathbb{Z}_4$ and $\mathbb{Z}_2 \times \mathbb{Z}_2$ (both abelian).

**Example 2**: Groups of order 9: $\mathbb{Z}_9$ and $\mathbb{Z}_3 \times \mathbb{Z}_3$ (both abelian).

# Relationships

## Builds Upon
- **Nontrivial center of p-group** — $|Z(G)| = p$ or $p^2$

## Enables
- **Classification of groups of small order** — Used with Sylow theorems

# Source Reference

Chapter 14: Group Actions, Section 14.2, p. 185. Corollary 14.16.

# Verification Notes

- Definition source: Corollary 14.16
- Confidence: HIGH
