---
# === CORE IDENTIFICATION ===
concept: Laws of Exponents in Groups
slug: laws-of-exponents-groups

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
  - exponential notation in groups

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - order-of-element
  - abelian-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "How do I find the order of an element in a group?"
---

# Quick Definition

In a group, exponential notation $g^n$ denotes repeated application of the group operation, and the usual laws of exponents hold: $g^m g^n = g^{m+n}$ and $(g^m)^n = g^{mn}$.

# Core Definition

For $g \in G$, define $g^0 = e$, $g^n = g \cdot g \cdots g$ ($n$ times), and $g^{-n} = g^{-1} \cdots g^{-1}$ ($n$ times).

**Theorem 3.23**: For all $g, h \in G$:
1. $g^m g^n = g^{m+n}$ for all $m, n \in \mathbb{Z}$
2. $(g^m)^n = g^{mn}$ for all $m, n \in \mathbb{Z}$
3. $(gh)^n = (h^{-1}g^{-1})^{-n}$ for all $n \in \mathbb{Z}$. Furthermore, if $G$ is abelian, then $(gh)^n = g^n h^n$.

(Judson, p. 50).

# Prerequisites

- **Group** — Exponent laws hold in groups

# Key Properties

1. $g^m g^n = g^{m+n}$
2. $(g^m)^n = g^{mn}$
3. $(gh)^n = g^n h^n$ ONLY if $G$ is abelian
4. In additive notation: $mg + ng = (m+n)g$ and $m(ng) = (mn)g$

# Context & Application

These laws justify manipulating powers of group elements, which is essential for working with cyclic groups and computing orders of elements.

# Examples

**Example 1** (p. 50): In a nonabelian group, $(gh)^2 = ghgh \neq g^2 h^2$ in general because $hg \neq gh$.

# Relationships

## Builds Upon
- **group** — Laws hold in groups

## Enables
- **order-of-element** — Computing powers to find order

## Related
- **abelian-group** — $(gh)^n = g^n h^n$ only in abelian groups

# Common Errors

- **Error**: Assuming $(gh)^n = g^n h^n$ in nonabelian groups
  **Correction**: This equality holds only when $G$ is abelian

# Source Reference

Chapter 3: Groups, Section 3.2, Theorem 3.23, page 50.

# Verification Notes

- Definition source: Direct from Theorem 3.23
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
