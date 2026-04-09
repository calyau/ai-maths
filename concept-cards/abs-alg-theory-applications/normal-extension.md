---
# === CORE IDENTIFICATION ===
concept: Normal Extension
slug: normal-extension

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-field
  - irreducible-polynomial
extends:
  - extension-field
related:
  - splitting-field
  - separable-extension
  - fundamental-theorem-of-galois-theory
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a normal extension?"
  - "How do normal extensions relate to splitting fields?"
---

# Quick Definition

An algebraic extension $E$ of $F$ is normal if every irreducible polynomial in $F[x]$ that has a root in $E$ splits completely (into linear factors) in $E[x]$.

# Core Definition

Let $E$ be an algebraic extension of $F$. If every irreducible polynomial in $F[x]$ with a root in $E$ has all of its roots in $E$, then $E$ is called a **normal extension** of $F$ (Judson, p. 313).

By Theorem 23.19, the following are equivalent:
1. $E$ is a finite, normal, separable extension of $F$
2. $E$ is a splitting field over $F$ of a separable polynomial
3. $F = E_G$ for some finite group $G$ of automorphisms of $E$

# Prerequisites

- **Extension field** — Normal extensions are field extensions
- **Irreducible polynomial** — Normality concerns irreducible polynomials with roots in $E$

# Key Properties

1. $E$ is normal over $F$ if and only if $E$ is the splitting field of some polynomial over $F$ (when also finite and separable)
2. Normality is needed for the Fundamental Theorem of Galois Theory
3. If $K$ is a normal extension of $F$ and $G(E/K)$ is a normal subgroup of $G(E/F)$, then $G(K/F) \cong G(E/F)/G(E/K)$
4. Normality is not transitive: $F \subset K \subset E$ with $K$ normal over $F$ and $E$ normal over $K$ does not imply $E$ normal over $F$

# Context & Application

Normality ensures that the splitting field "contains all conjugates" of every element. Together with separability, it defines Galois extensions. The Fundamental Theorem requires both conditions.

# Examples

**Example 1**: $\mathbb{Q}(\sqrt{2})$ is a normal extension of $\mathbb{Q}$ because it is the splitting field of $x^2 - 2$.

**Example 2**: $\mathbb{Q}(\sqrt[3]{2})$ is not a normal extension of $\mathbb{Q}$ because $x^3 - 2$ has a root $\sqrt[3]{2}$ in this field but the other two roots (complex) are not in $\mathbb{Q}(\sqrt[3]{2})$.

# Relationships

## Builds Upon
- **Extension field** — Normality is a property of extensions
- **Irreducible polynomial** — Definition involves irreducible polynomials

## Enables
- **Fundamental Theorem of Galois Theory** — Requires normal (and separable) extensions

## Related
- **Splitting field** — Normal + separable + finite = splitting field of separable polynomial
- **Separable extension** — The other condition for Galois extensions

# Common Confusions

- **Confusion**: Thinking normality is transitive
  **Clarification**: $\mathbb{Q} \subset \mathbb{Q}(\sqrt{2}) \subset \mathbb{Q}(\sqrt[4]{2})$ — the first extension is normal, the second is normal, but the composite is not normal over $\mathbb{Q}$

# Source Reference

Chapter 23: Galois Theory, Section 23.2, pages 313–314. See Theorem 23.19.

# Verification Notes

- Definition source: Direct from p. 313
- Confidence: HIGH — explicit definition with equivalence theorem
- Cross-reference status: Verified
- Uncertainties: None
