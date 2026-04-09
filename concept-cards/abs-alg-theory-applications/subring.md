---
# === CORE IDENTIFICATION ===
concept: Subring
slug: subring

# === CLASSIFICATION ===
category: ring-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Rings"
chapter_number: 16
pdf_page: 207
section: "16.1 Rings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ring
extends: []
related:
  - ideal
contrasts_with:
  - ideal

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a subring?"
  - "How do I verify that a subset is a subring?"
---

# Quick Definition

A subring $S$ of a ring $R$ is a subset of $R$ that is itself a ring under the same operations inherited from $R$.

# Core Definition

"A subring $S$ of a ring $R$ is a subset $S$ of $R$ such that $S$ is also a ring under the inherited operations from $R$" (Judson, p. 207). By Proposition 16.10, $S$ is a subring iff: (1) $S \neq \emptyset$; (2) $rs \in S$ for all $r, s \in S$; (3) $r - s \in S$ for all $r, s \in S$.

# Prerequisites

- **Ring** — Subrings are subsets of rings

# Key Properties

1. $S \neq \emptyset$
2. Closed under multiplication: $rs \in S$ for all $r, s \in S$
3. Closed under subtraction: $r - s \in S$ for all $r, s \in S$
4. A subring need not contain the identity of the parent ring
5. Every ideal is a subring, but not every subring is an ideal

# Construction / Recognition

## To Verify (Proposition 16.10):
1. Check $S$ is nonempty
2. Check closure under multiplication
3. Check closure under subtraction

# Context & Application

Subrings are the ring-theoretic analog of subgroups. They provide a way to study smaller ring structures within a larger ring. The chain $\mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$ is a chain of subrings.

# Examples

**Example 1** (p. 207): $n\mathbb{Z}$ is a subring of $\mathbb{Z}$. Note $n\mathbb{Z}$ does not have a unity for $n > 1$.

**Example 2** (p. 207): The chain $\mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$ is a chain of subrings.

**Example 3** (p. 207): The set of upper triangular $2 \times 2$ matrices is a subring of $M_2(\mathbb{R})$.

# Relationships

## Builds Upon
- **Ring** — A subring is a subset that is a ring

## Enables
- **Ideal** — An ideal is a subring with an additional absorption property

## Contrasts With
- **Ideal** — An ideal absorbs multiplication by arbitrary ring elements; a subring need not

# Common Errors

- **Error**: Checking only closure under addition and multiplication
  **Correction**: Must also verify closure under additive inverses (subtraction)

# Common Confusions

- **Confusion**: Assuming a subring of a ring with unity must contain the unity
  **Clarification**: $2\mathbb{Z}$ is a subring of $\mathbb{Z}$ but does not contain $1$

# Source Reference

Chapter 16: Rings, Section 16.1, pages 207. See Proposition 16.10 and Examples 16.9, 16.11.

# Verification Notes

- Definition source: Direct from p. 207
- Confidence: HIGH — explicit definition with subring test
- Cross-reference status: Verified
- Uncertainties: None
