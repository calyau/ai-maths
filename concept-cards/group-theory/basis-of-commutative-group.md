---
# === CORE IDENTIFICATION ===
concept: Basis of a Commutative Group
slug: basis-of-commutative-group

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: commutative-groups
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 25
section: "Commutative groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - direct-product-internal
extends: []
related:
  - fundamental-theorem-finitely-generated-abelian-groups
  - invariant-factors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a basis for a commutative group?"
  - "When does a commutative group have a basis?"
---

# Quick Definition

A basis for a commutative group $M$ (written additively) is a set $\{x_1, \ldots, x_k\}$ that generates $M$ and satisfies: $m_1 x_1 + \cdots + m_k x_k = 0 \Rightarrow m_i x_i = 0$ for every $i$. Then $M = \langle x_1 \rangle \oplus \cdots \oplus \langle x_k \rangle$.

# Core Definition

"A subset $\{x_1, \ldots, x_k\}$ of $M$ is a **basis** for $M$ if it generates $M$ and $m_1 x_1 + \cdots + m_k x_k = 0$, $m_i \in \mathbb{Z}$ $\Rightarrow$ $m_i x_i = 0$ for every $i$." (Milne, p. 25)

# Prerequisites

- **Internal direct product** — a basis gives a direct sum decomposition

# Key Properties

1. A basis gives $M = \langle x_1 \rangle \oplus \cdots \oplus \langle x_k \rangle$
2. Each $\langle x_i \rangle$ is cyclic (finite or infinite)
3. Every finitely generated commutative group has a basis (Theorem 1.54)

# Context & Application

The existence of a basis is the core content of the fundamental theorem of finitely generated abelian groups: every such group is a direct sum of cyclic groups.

# Examples

**Example 1**: $\{1\}$ is a basis for $\mathbb{Z}$ (infinite cyclic).

**Example 2**: $\{(1,0), (0,1)\}$ is a basis for $\mathbb{Z}^2$.

# Relationships

## Builds Upon
- **direct-product-internal**

## Enables
- **fundamental-theorem-finitely-generated-abelian-groups**

# Source Reference

Chapter 1, page 25. Theorem 1.54.

# Verification Notes

- Definition source: Direct from p. 25
- Confidence: HIGH — explicit definition
- Uncertainties: None
