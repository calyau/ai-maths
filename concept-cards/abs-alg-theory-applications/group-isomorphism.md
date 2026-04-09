---
concept: Group Isomorphism
slug: group-isomorphism
category: morphisms
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Isomorphisms"
chapter_number: 9
pdf_page: 127
section: "9.1 Definition and Examples"
extraction_confidence: high
aliases:
  - isomorphism
  - "$\\cong$"
prerequisites: []
extends: []
related:
  - isomorphism-properties
  - cayleys-theorem
  - automorphism
contrasts_with: []
answers_questions:
  - "What is a group isomorphism?"
  - "What distinguishes a homomorphism from an isomorphism?"
  - "How do I show two groups are isomorphic?"
---

# Quick Definition

Two groups $(G, \cdot)$ and $(H, \circ)$ are isomorphic (written $G \cong H$) if there exists a bijective map $\phi : G \to H$ that preserves the group operation: $\phi(a \cdot b) = \phi(a) \circ \phi(b)$.

# Core Definition

"Two groups $(G, \cdot)$ and $(H, \circ)$ are *isomorphic* if there exists a one-to-one and onto map $\phi : G \to H$ such that the group operation is preserved; that is, $\phi(a \cdot b) = \phi(a) \circ \phi(b)$ for all $a$ and $b$ in $G$. If $G$ is isomorphic to $H$, we write $G \cong H$. The map $\phi$ is called an *isomorphism*" (Judson, p. 127).

# Prerequisites

This concept requires understanding of groups and bijective functions from earlier chapters.

# Key Properties

1. An isomorphism is a bijection that preserves the group operation
2. $\phi^{-1} : H \to G$ is also an isomorphism (Theorem 9.6)
3. Isomorphic groups have the same order
4. If $G$ is abelian, then $H$ is abelian (and vice versa)
5. If $G$ is cyclic, then $H$ is cyclic (and vice versa)
6. Isomorphic groups have the same subgroup structure

# Construction / Recognition

## To Show $G \cong H$:
1. Define a map $\phi : G \to H$
2. Show $\phi$ is one-to-one (injective)
3. Show $\phi$ is onto (surjective)
4. Show $\phi(ab) = \phi(a)\phi(b)$ for all $a, b \in G$

## To Show $G \not\cong H$:
1. Find a structural property that differs (order, abelianness, element orders, etc.)

# Context & Application

Isomorphism is the fundamental notion of "sameness" for groups. Two isomorphic groups are algebraically identical. The main goal of group theory is to classify groups up to isomorphism.

# Examples

**Example 1** (p. 127): $\mathbb{Z}_4 \cong \langle i \rangle$ via $\phi(n) = i^n$.

**Example 2** (p. 128): $(\mathbb{R}, +) \cong (\mathbb{R}^+, \cdot)$ via $\phi(x) = e^x$.

**Example 3** (p. 128): $U(8) \cong U(12)$ via $1 \mapsto 1$, $3 \mapsto 5$, $5 \mapsto 7$, $7 \mapsto 11$.

**Example 4** (p. 128): $S_3 \not\cong \mathbb{Z}_6$ because $S_3$ is nonabelian and $\mathbb{Z}_6$ is abelian.

# Relationships

## Enables
- **Isomorphism Properties** — Properties preserved under isomorphism
- **Cayley's Theorem** — Every group is isomorphic to a permutation group
- **Automorphism** — An isomorphism from a group to itself

## Related
- **Classification of Groups** — Groups are classified up to isomorphism
- **Isomorphism Equivalence Relation** — Isomorphism is an equivalence relation on groups

# Common Errors

- **Error**: Defining a map $\phi$ that is not well-defined (e.g., depends on representative choice)
  **Correction**: Always verify the map is well-defined before checking the isomorphism properties

# Common Confusions

- **Confusion**: Thinking isomorphic groups must "look" the same
  **Clarification**: Isomorphic groups may appear very different (e.g., $\mathbb{R}$ under addition vs. $\mathbb{R}^+$ under multiplication) but have identical algebraic structure

- **Confusion**: Confusing isomorphism with homomorphism
  **Clarification**: A homomorphism preserves the operation but need not be bijective; an isomorphism is a bijective homomorphism

# Source Reference

Chapter 9: Isomorphisms, Section 9.1, pages 127-130.

# Verification Notes

- Definition source: Direct from p. 127
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
