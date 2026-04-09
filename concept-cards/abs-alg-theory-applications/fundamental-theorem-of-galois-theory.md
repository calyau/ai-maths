---
# === CORE IDENTIFICATION ===
concept: Fundamental Theorem of Galois Theory
slug: fundamental-theorem-of-galois-theory

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
aliases:
  - "FTGT"
  - "Galois correspondence"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - galois-group
  - normal-extension
  - separable-extension
  - fixed-field
extends: []
related:
  - solvable-by-radicals
  - insolvability-of-quintic
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Fundamental Theorem of Galois Theory connect field extensions and group theory?"
  - "What is the Galois correspondence?"
---

# Quick Definition

The Fundamental Theorem of Galois Theory establishes a bijective correspondence between intermediate fields of a Galois extension $E/F$ and subgroups of the Galois group $G(E/F)$, reversing the inclusion order. Normal subextensions correspond to normal subgroups.

# Core Definition

**Theorem 23.23 (Fundamental Theorem of Galois Theory).** Let $F$ be a finite field or a field of characteristic zero. If $E$ is a finite normal extension of $F$ with Galois group $G(E/F)$, then (Judson, p. 314):

1. The map $K \mapsto G(E/K)$ is a bijection between subfields $K$ of $E$ containing $F$ and subgroups of $G(E/F)$.
2. If $F \subset K \subset E$, then $[E:K] = |G(E/K)|$ and $[K:F] = [G(E/F):G(E/K)]$.
3. $F \subset K \subset L \subset E$ if and only if $\{\text{id}\} \subset G(E/L) \subset G(E/K) \subset G(E/F)$.
4. $K$ is a normal extension of $F$ if and only if $G(E/K)$ is a normal subgroup of $G(E/F)$. In this case, $G(K/F) \cong G(E/F)/G(E/K)$.

# Prerequisites

- **Galois group** — The theorem concerns the Galois group and its subgroups
- **Normal extension** — The theorem requires $E/F$ to be a normal extension
- **Separable extension** — Separability is needed (automatic in char 0 and finite fields)
- **Fixed field** — The inverse of the correspondence uses fixed fields

# Key Properties

1. **Bijection**: Subgroups $\leftrightarrow$ intermediate fields, in inclusion-reversing fashion
2. **Degree formula**: $[K:F] = [G(E/F):G(E/K)]$ (index of subgroup = degree of extension)
3. **Normal correspondence**: Normal subgroups $\leftrightarrow$ normal subextensions
4. **Quotient correspondence**: $G(K/F) \cong G(E/F)/G(E/K)$ when $K/F$ is normal
5. The theorem converts field-theoretic questions into group-theoretic ones

# Construction / Recognition

## To Apply:
1. Verify $E$ is a finite normal separable extension of $F$
2. Compute the Galois group $G(E/F)$
3. List all subgroups of $G(E/F)$
4. For each subgroup $H$, the fixed field $E_H$ is the corresponding intermediate field
5. Larger subgroups correspond to smaller fields (inclusion reversal)

# Context & Application

This theorem is the climax of Judson's text. It reveals a deep structural connection between two seemingly different mathematical objects: the lattice of intermediate fields and the lattice of subgroups. This connection is the foundation for proving that polynomials of degree 5 or higher may not be solvable by radicals.

# Examples

**Example 1** (p. 314): For $\mathbb{Q}(\sqrt{3}, \sqrt{5})/\mathbb{Q}$, the Galois group is $\mathbb{Z}_2 \times \mathbb{Z}_2$. Its three nontrivial subgroups correspond to the three intermediate fields $\mathbb{Q}(\sqrt{3})$, $\mathbb{Q}(\sqrt{5})$, $\mathbb{Q}(\sqrt{15})$.

**Example 2** (p. 315): For the splitting field of $x^4 - 2$ over $\mathbb{Q}$, the Galois group is $D_4$. The lattice of subgroups of $D_4$ (10 subgroups) corresponds to the lattice of intermediate fields.

# Relationships

## Builds Upon
- **Galois group** — The theorem describes its subgroup structure
- **Normal extension** — Required for the theorem
- **Separable extension** — Required for the theorem
- **Fixed field** — Provides one direction of the correspondence

## Enables
- **Solvability by radicals** — The Galois group determines solvability
- **Insolvability of the quintic** — Follows when the Galois group is $S_5$ (which is not solvable)

# Common Errors

- **Error**: Applying the theorem to extensions that are not normal
  **Correction**: The theorem requires the extension to be normal (and separable). For non-normal extensions, the correspondence fails.

# Common Confusions

- **Confusion**: Expecting larger subgroups to correspond to larger fields
  **Clarification**: The correspondence is inclusion-reversing: larger subgroups fix fewer elements, hence correspond to smaller fields

# Source Reference

Chapter 23: Galois Theory, Section 23.2, pages 314–316. Theorem 23.23 with Examples 23.21 and 23.25.

# Verification Notes

- Definition source: Direct from Theorem 23.23, p. 314
- Confidence: HIGH — explicit theorem statement with full proof and examples
- Cross-reference status: Verified
- Uncertainties: None
