---
# === CORE IDENTIFICATION ===
concept: Vector Space
slug: vector-space

# === CLASSIFICATION ===
category: linear-algebra
subcategory: vector-spaces
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Vector Spaces"
chapter_number: 20
pdf_page: 266
section: "20.1 Definitions and Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "linear space"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - field
  - abelian-group
extends: []
related:
  - subspace
  - linear-combination
  - basis
  - dimension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a vector space?"
  - "What axioms define a vector space?"
  - "How does a vector space relate to fields?"
---

# Quick Definition

A vector space $V$ over a field $F$ is an abelian group equipped with a scalar multiplication by elements of $F$ satisfying four axioms: associativity, two distributive laws, and an identity element for scalar multiplication.

# Core Definition

A **vector space** $V$ over a field $F$ is an abelian group with a **scalar product** $\alpha \cdot v$ or $\alpha v$ defined for all $\alpha \in F$ and all $v \in V$ satisfying the following axioms (Judson, p. 266):

1. $\alpha(\beta v) = (\alpha \beta)v$
2. $(\alpha + \beta)v = \alpha v + \beta v$
3. $\alpha(u + v) = \alpha u + \alpha v$
4. $1v = v$

where $\alpha, \beta \in F$ and $u, v \in V$. The elements of $V$ are called **vectors** and the elements of $F$ are called **scalars**.

# Prerequisites

- **Field** — The scalars must come from a field, which provides the algebraic structure for scalar multiplication
- **Abelian group** — The vector addition must form an abelian group, providing the additive structure

# Key Properties

1. $0v = \mathbf{0}$ for all $v \in V$ (scalar zero times any vector is the zero vector)
2. $\alpha \mathbf{0} = \mathbf{0}$ for all $\alpha \in F$ (any scalar times the zero vector is the zero vector)
3. If $\alpha v = \mathbf{0}$, then either $\alpha = 0$ or $v = \mathbf{0}$
4. $(-1)v = -v$ for all $v \in V$
5. $-(\alpha v) = (-\alpha)v = \alpha(-v)$ for all $\alpha \in F$ and all $v \in V$
6. In general, two vectors cannot be multiplied; only a vector and a scalar can be multiplied

# Construction / Recognition

## To Construct:
1. Start with a field $F$ (the scalars)
2. Define an abelian group $(V, +)$ (the vectors under addition)
3. Define a scalar multiplication $F \times V \to V$
4. Verify the four vector space axioms hold

## To Recognize:
1. Check that the underlying set forms an abelian group under addition
2. Identify the field of scalars
3. Verify that scalar multiplication satisfies all four axioms
4. Confirm closure under both vector addition and scalar multiplication

# Context & Application

Vector spaces are fundamental structures in both pure and applied mathematics. They provide the framework for linear algebra and are essential for understanding field extensions in abstract algebra. The concept appears throughout physics (state spaces), computer science (data representations), and engineering (signal spaces).

In this text, vector spaces serve as a bridge between the group/ring theory of earlier chapters and the field extension theory of Chapter 21. Viewing field extensions as vector spaces over their base fields is a key technique.

# Examples

**Example 1** (p. 266): The $n$-tuples of real numbers $\mathbb{R}^n$ form a vector space over $\mathbb{R}$, with componentwise addition and scalar multiplication: $\alpha(u_1, \ldots, u_n) = (\alpha u_1, \ldots, \alpha u_n)$.

**Example 2** (p. 267): If $F$ is a field, then $F[x]$ (polynomials over $F$) is a vector space over $F$, with polynomial addition and scalar multiplication $\alpha p(x)$.

**Example 3** (p. 267): The set of all continuous real-valued functions on a closed interval $[a,b]$ is a vector space over $\mathbb{R}$.

**Example 4** (p. 267): $\mathbb{Q}(\sqrt{2}) = \{a + b\sqrt{2} : a, b \in \mathbb{Q}\}$ is a vector space over $\mathbb{Q}$.

# Relationships

## Builds Upon
- **Field** — Provides the scalar structure
- **Abelian group** — Provides the additive structure for vectors

## Enables
- **Subspace** — Substructure of a vector space
- **Linear independence** — Key concept defined within vector spaces
- **Basis** — Minimal spanning set in a vector space
- **Dimension** — Fundamental invariant of a vector space
- **Extension field** — Field extensions can be viewed as vector spaces

## Related
- **Linear combination** — Fundamental operation in vector spaces
- **Linear transformation** — Structure-preserving maps between vector spaces

# Common Errors

- **Error**: Attempting to multiply two vectors together as if the operation were defined
  **Correction**: In general, only scalar-vector multiplication is defined in a vector space; vector-vector multiplication requires additional structure (e.g., an algebra)

- **Error**: Confusing the scalar zero $0$ with the vector zero $\mathbf{0}$
  **Correction**: The scalar zero is an element of the field $F$; the vector zero is an element of $V$. They are distinct objects in different sets.

# Common Confusions

- **Confusion**: Believing that a vector space must consist of "arrows" or tuples of real numbers
  **Clarification**: Vectors can be polynomials, functions, field elements, or any objects satisfying the axioms. The arrow picture is just one model.

- **Confusion**: Thinking the axioms list only four conditions when the full definition has ten
  **Clarification**: Six conditions are implicit in requiring $V$ to be an abelian group (closure, associativity, identity, inverses, commutativity under addition, plus closure under scalar multiplication). The four listed axioms govern scalar multiplication specifically.

# Source Reference

Chapter 20: Vector Spaces, Section 20.1 "Definitions and Examples," pages 266–267. See Proposition 20.5 for basic properties.

# Verification Notes

- Definition source: Direct from p. 266, paragraph 1
- Key Properties: From Proposition 20.5, p. 267
- Confidence: HIGH — explicit axiomatic definition with multiple examples
- Cross-reference status: Verified against planned extractions
- Uncertainties: None
