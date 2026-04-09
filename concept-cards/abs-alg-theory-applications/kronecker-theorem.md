---
# === CORE IDENTIFICATION ===
concept: Kronecker's Theorem
slug: kronecker-theorem

# === CLASSIFICATION ===
category: field-theory
subcategory: field-extensions
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.1 Extension Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Fundamental Theorem of Field Theory"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-field
  - irreducible-polynomial
  - maximal-ideal
extends: []
related:
  - splitting-field
  - algebraic-element
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can every polynomial find a root in some extension field?"
  - "How do I construct a field extension containing a root of a polynomial?"
---

# Quick Definition

Kronecker's Theorem states that for any field $F$ and any nonconstant polynomial $p(x) \in F[x]$, there exists an extension field $E$ of $F$ containing an element $\alpha$ such that $p(\alpha) = 0$.

# Core Definition

**Theorem 21.5 (Kronecker's Theorem).** Let $F$ be a field and let $p(x)$ be a nonconstant polynomial in $F[x]$. Then there exists an extension field $E$ of $F$ and an element $\alpha \in E$ such that $p(\alpha) = 0$ (Judson, p. 275).

The construction is: if $p(x)$ is irreducible, form $E = F[x]/\langle p(x) \rangle$, and let $\alpha = x + \langle p(x) \rangle$.

# Prerequisites

- **Extension field** — The theorem guarantees the existence of extensions
- **Irreducible polynomial** — The construction uses the fact that $\langle p(x) \rangle$ is maximal when $p(x)$ is irreducible
- **Maximal ideal** — $F[x]/\langle p(x) \rangle$ is a field because $\langle p(x) \rangle$ is maximal

# Key Properties

1. The theorem is often called the "Fundamental Theorem of Field Theory"
2. The construction $F[x]/\langle p(x) \rangle$ provides an explicit field extension
3. The coset $\alpha = x + \langle p(x) \rangle$ serves as the root of $p(x)$ in the extension

# Context & Application

This theorem is foundational — it guarantees that every polynomial has a root in some extension field, enabling the construction of splitting fields and the development of Galois theory.

# Examples

**Example 1** (p. 275): For $p(x) = x^2 + x + 1 \in \mathbb{Z}_2[x]$, the extension $E = \mathbb{Z}_2[x]/\langle x^2 + x + 1 \rangle$ is a field with 4 elements containing a root $\alpha$ of $p(x)$.

**Example 2** (p. 278): For $p(x) = x^2 + 1 \in \mathbb{R}[x]$, the extension $\mathbb{R}[x]/\langle x^2 + 1 \rangle \cong \mathbb{C}$.

# Relationships

## Builds Upon
- **Irreducible polynomial** — Uses the fact that $\langle p(x) \rangle$ is maximal
- **Maximal ideal** — Ensures the quotient is a field

## Enables
- **Splitting field** — Iterating Kronecker's Theorem builds splitting fields
- **Algebraic element** — The root $\alpha$ is algebraic by construction

# Source Reference

Chapter 21: Fields, Section 21.1, pages 275–276. Theorem 21.5.

# Verification Notes

- Definition source: Direct from Theorem 21.5, p. 275
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
