---
# === CORE IDENTIFICATION ===
concept: Quaternion Algebra
slug: quaternion-algebra

# === CLASSIFICATION ===
category: classical-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: General Case"
chapter_number: 6
pdf_page: 383
section: "Example: the forms of GL₂"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "H(a,b)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - algebraic-group
extends: []
related:
  - form-of-algebraic-group
  - inner-form
  - margulis-arithmeticity-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Galois cohomology classify forms of algebraic groups?"
---

# Quick Definition

A quaternion algebra $\mathbb{H}(a,b)$ over a field $k$ is a 4-dimensional $k$-algebra with basis $1, i, j, ij$ and relations $i^2 = a$, $j^2 = b$, $ij = -ji$. It is either a division algebra or isomorphic to $M_2(k)$, and its unit group defines a form of $\mathrm{GL}_2$.

# Core Definition

"For any $a, b \in k^\times$, define $\mathbb{H}(a,b)$ to be the algebra over $k$ with basis $1, i, j, ij$ as a $k$-vector space, and with the multiplication given by $i^2 = a$, $j^2 = b$, $ij = -ji$. This is a $k$-algebra with centre $k$, and it is either a division algebra or is isomorphic to $M_2(k)$." (Milne, p. 383)

Each $\mathbb{H}(a,b)$ defines an algebraic group $G(a,b)$ with $G(R) = (R \otimes \mathbb{H}(a,b))^\times$, and these are exactly the forms of $\mathrm{GL}_2$ over $k$.

# Prerequisites

- **Algebraic group** — the unit group of a quaternion algebra is an algebraic group

# Key Properties

1. $\mathbb{H}(1,1) \cong M_2(k)$
2. $\mathbb{H}(-1,-1)$ is the usual Hamilton quaternions when $k = \mathbb{R}$
3. $G(a,b) \cong G(a',b') \iff \mathbb{H}(a,b) \cong \mathbb{H}(a',b')$
4. Over $\mathbb{R}$: exactly two forms of $\mathrm{GL}_2$ ($M_2(\mathbb{R})$ and $\mathbb{H}$)
5. Over $\mathbb{Q}$: infinitely many forms, classified by even-cardinality subsets of $\{2,3,5,7,\ldots,\infty\}$
6. The norm form is $\mathrm{Nm}(w+xi+yj+zk) = w^2 - ax^2 - by^2 + abz^2$

# Construction / Recognition

## To Construct:
1. Choose $a, b \in k^\times$
2. Form $\mathbb{H}(a,b)$ with the given multiplication rules
3. The unit group $\mathbb{H}(a,b)^\times$ is a form of $\mathrm{GL}_2$
4. The norm-1 elements form a form of $\mathrm{SL}_2$

# Context & Application

Quaternion algebras are the simplest example of the classification of forms by Galois cohomology. They illustrate key phenomena: a group can have finitely many forms over $\mathbb{R}$ but infinitely many over $\mathbb{Q}$, and division algebras give rise to groups with very different properties (compact vs. non-compact, cocompact vs. non-cocompact arithmetic subgroups).

# Examples

**Example 1** (p. 383): Over $\mathbb{R}$, there are exactly two quaternion algebras: $M_2(\mathbb{R})$ and $\mathbb{H}(-1,-1)$.

**Example 2** (p. 383): Over $\mathbb{Q}$, quaternion algebras are classified by even-cardinality subsets of primes $\cup \{\infty\}$, using the quadratic reciprocity law.

**Example 3** (p. 410): Quaternion algebras over totally real fields give rise to arithmetic subgroups of $\mathrm{SL}_2(\mathbb{R})$, and all commensurability classes arise this way.

# Relationships

## Enables
- **Form of algebraic group** — quaternion algebras give forms of $\mathrm{GL}_2$ and $\mathrm{SL}_2$
- **Margulis arithmeticity theorem** — quaternion algebras give all arithmetic lattices in $\mathrm{SL}_2(\mathbb{R})$

## Related
- **Inner form** — forms of $\mathrm{SL}_2$ from quaternion algebras are inner forms

# Common Errors

- **Error**: Assuming all quaternion algebras are division algebras
  **Correction**: $\mathbb{H}(a,b)$ is either a division algebra or $M_2(k)$; the split case $M_2(k)$ is also a quaternion algebra

# Common Confusions

- **Confusion**: Thinking there is only one quaternion algebra (the Hamilton quaternions)
  **Clarification**: $\mathbb{H}(-1,-1)$ is just one quaternion algebra over $\mathbb{R}$; over other fields, many quaternion algebras exist

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, "Example: the forms of GL₂," pages 382-383. Chapter VII, Example 15.2, pages 410-411.

# Verification Notes

- Definition source: Direct quote from p. 383
- Confidence: HIGH — explicit definition with complete examples
- Uncertainties: None
- Cross-reference status: Verified
