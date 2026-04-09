---
# === CORE IDENTIFICATION ===
concept: Linear Dependence
slug: linear-dependence

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
section: "20.3 Linear Independence"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "linearly dependent"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-combination
  - vector-space
extends: []
related:
  - spanning-set
contrasts_with:
  - linear-independence

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean for vectors to be linearly dependent?"
  - "How can I tell if vectors are linearly dependent?"
---

# Quick Definition

A set of vectors $\{v_1, \ldots, v_n\}$ is linearly dependent if there exist scalars $\alpha_1, \ldots, \alpha_n$, not all zero, such that $\alpha_1 v_1 + \cdots + \alpha_n v_n = \mathbf{0}$.

# Core Definition

Let $S = \{v_1, v_2, \ldots, v_n\}$ be a set of vectors in a vector space $V$. If there exist scalars $\alpha_1, \alpha_2, \ldots, \alpha_n \in F$ such that not all of the $\alpha_i$'s are zero and

$$\alpha_1 v_1 + \alpha_2 v_2 + \cdots + \alpha_n v_n = \mathbf{0},$$

then $S$ is said to be **linearly dependent** (Judson, p. 268).

# Prerequisites

- **Linear combination** — Dependence is defined via a nontrivial linear combination equaling zero
- **Vector space** — The concept is defined within a vector space

# Key Properties

1. A set is linearly dependent if and only if one of its vectors is a linear combination of the rest (Proposition 20.10)
2. Any set containing the zero vector is linearly dependent
3. If a vector space is spanned by $n$ vectors, then any set of more than $n$ vectors is linearly dependent (Proposition 20.11)

# Construction / Recognition

## To Recognize:
1. Set up the equation $\alpha_1 v_1 + \cdots + \alpha_n v_n = \mathbf{0}$
2. Solve the resulting system of equations
3. If a nontrivial solution exists (not all $\alpha_i = 0$), the set is linearly dependent

# Context & Application

Linear dependence indicates redundancy in a set of vectors — at least one vector can be expressed in terms of the others. Identifying and removing such redundancy leads to the concept of a basis.

# Examples

**Example 1** (p. 271): Any set of vectors containing $\mathbf{0}$ is linearly dependent, since $1 \cdot \mathbf{0} + 0 \cdot v_1 + \cdots + 0 \cdot v_n = \mathbf{0}$ is a nontrivial relation.

# Relationships

## Builds Upon
- **Linear combination** — Dependence is a nontrivial linear combination equal to zero

## Related
- **Spanning set** — Dependent spanning sets can be reduced

## Contrasts With
- **Linear independence** — A set is either dependent or independent; these are mutually exclusive

# Common Errors

- **Error**: Checking only pairs of vectors for dependence
  **Correction**: Dependence is a property of the entire set; three vectors can be dependent even if every pair is independent

# Common Confusions

- **Confusion**: Thinking linearly dependent means "the vectors point in the same direction"
  **Clarification**: Dependence means one vector is a linear combination of the others; this is an algebraic, not geometric, condition (though geometrically it can mean coplanarity for three vectors in $\mathbb{R}^3$)

# Source Reference

Chapter 20: Vector Spaces, Section 20.3 "Linear Independence," pages 268–269. See Propositions 20.10 and 20.11.

# Verification Notes

- Definition source: Direct from p. 268
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
