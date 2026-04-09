---
# === CORE IDENTIFICATION ===
concept: Galois Group
slug: galois-group

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
section: "23.1 Field Automorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "G(E/F)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - field-automorphism
  - extension-field
  - splitting-field
extends: []
related:
  - fixed-field
  - fundamental-theorem-of-galois-theory
  - galois-group-of-polynomial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Galois group?"
  - "How does the Galois group connect field theory and group theory?"
  - "What must I know before understanding Galois theory?"
---

# Quick Definition

The Galois group $G(E/F)$ of a field extension $E$ over $F$ is the group of all automorphisms of $E$ that fix every element of $F$. If $f(x) \in F[x]$ has splitting field $E$, then $G(E/F)$ is the Galois group of $f(x)$.

# Core Definition

Let $E$ be a field extension of $F$. The **Galois group** of $E$ over $F$ is the group of automorphisms of $E$ that fix $F$ elementwise:

$$G(E/F) = \{\sigma \in \operatorname{Aut}(E) : \sigma(\alpha) = \alpha \text{ for all } \alpha \in F\}$$

(Judson, p. 308).

If $f(x)$ is a polynomial in $F[x]$ and $E$ is the splitting field of $f(x)$ over $F$, then the **Galois group of $f(x)$** is defined to be $G(E/F)$.

# Prerequisites

- **Field automorphism** — Galois group elements are automorphisms
- **Extension field** — Defined for field extensions
- **Splitting field** — Galois group of a polynomial uses its splitting field

# Key Properties

1. $G(E/F)$ is a subgroup of $\operatorname{Aut}(E)$
2. Elements of $G(E/F)$ permute the roots of any $f(x) \in F[x]$ (Proposition 23.5)
3. If $f(x)$ has no repeated roots and $E$ is its splitting field, then $|G(E/F)| = [E:F]$ (Theorem 23.7)
4. $G(E/F)$ is a subgroup of $S_n$ where $n = \deg f(x)$
5. For finite fields: $G(GF(p^{nk})/GF(p^n))$ is cyclic of order $k$ (Corollary 23.9)
6. The Galois group is well-defined because splitting fields are unique up to isomorphism

# Construction / Recognition

## To Compute:
1. Find the splitting field $E$ of $f(x)$ over $F$
2. Determine all automorphisms of $E$ that fix $F$
3. Each automorphism is determined by its action on the roots of $f(x)$
4. Verify the group operation (composition) and identify the group structure

# Context & Application

The Galois group is the central concept of Galois theory. It captures the symmetries of the roots of a polynomial and connects field extensions to group theory. The Fundamental Theorem of Galois Theory establishes a correspondence between subgroups of the Galois group and intermediate fields.

# Examples

**Example 1** (p. 308): $G(\mathbb{C}/\mathbb{R}) = \{\text{id}, \sigma\}$ where $\sigma$ is complex conjugation. This group is $\mathbb{Z}_2$.

**Example 2** (p. 308): $G(\mathbb{Q}(\sqrt{3}, \sqrt{5})/\mathbb{Q}) = \{\text{id}, \sigma, \tau, \mu\} \cong \mathbb{Z}_2 \times \mathbb{Z}_2$, where $\sigma(\sqrt{3}) = -\sqrt{3}$, $\tau(\sqrt{5}) = -\sqrt{5}$, and $\mu = \sigma\tau$.

**Example 3** (p. 310): The Galois group of $x^4 + x^3 + x^2 + x + 1$ over $\mathbb{Q}$ is $\mathbb{Z}_4$.

**Example 4** (p. 315): The Galois group of $x^4 - 2$ over $\mathbb{Q}$ is $D_4$ (the dihedral group of order 8).

# Relationships

## Builds Upon
- **Field automorphism** — Galois group consists of automorphisms
- **Extension field** — Defined for extensions
- **Splitting field** — Used to define the Galois group of a polynomial

## Enables
- **Fundamental Theorem of Galois Theory** — The main result connecting subgroups and subfields
- **Solvability by radicals** — Determined by solvability of the Galois group
- **Insolvability of the quintic** — Follows when the Galois group is $S_5$

## Related
- **Fixed field** — The field fixed by the Galois group is the base field

# Common Errors

- **Error**: Computing the Galois group using only one root of $f(x)$
  **Correction**: The Galois group acts on all roots; one must find the full splitting field

# Common Confusions

- **Confusion**: Thinking the Galois group depends on which splitting field is chosen
  **Clarification**: Splitting fields are unique up to isomorphism, so the Galois group is well-defined

# Source Reference

Chapter 23: Galois Theory, Section 23.1, pages 308–310. See Propositions 23.2, 23.5, Theorem 23.7, Corollary 23.9.

# Verification Notes

- Definition source: Direct from p. 308
- Confidence: HIGH — explicit definition with examples
- Cross-reference status: Verified
- Uncertainties: None
