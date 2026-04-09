---
concept: Automorphism
slug: automorphism
category: morphisms
subcategory: group-maps
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Homomorphisms"
chapter_number: 11
pdf_page: 152
section: "Additional Exercises: Automorphisms"
extraction_confidence: high
aliases:
  - "group automorphism"
prerequisites:
  - isomorphism
  - group-homomorphism
extends:
  - isomorphism
related:
  - inner-automorphism
  - automorphism-group
contrasts_with: []
answers_questions:
  - "What is a group automorphism?"
---

# Quick Definition

An automorphism of a group $G$ is an isomorphism from $G$ to itself. Automorphisms capture the internal symmetries of a group's structure.

# Core Definition

An **automorphism** of $G$ is an isomorphism $\phi: G \to G$ (Judson, p. 152, Exercise 11.5.1). The set of all automorphisms of $G$, denoted $\operatorname{Aut}(G)$, forms a group under composition and is a subgroup of the symmetric group $S_G$ on the underlying set of $G$.

# Prerequisites

- **Isomorphism** — An automorphism is an isomorphism from a group to itself
- **Group homomorphism** — Automorphisms are bijective homomorphisms

# Key Properties

1. $\operatorname{Aut}(G)$ is a group under composition
2. $\operatorname{Aut}(G) \leq S_G$
3. $\operatorname{Aut}(\mathbb{Z}_n) \cong U(n)$, the group of units modulo $n$

# Construction / Recognition

## To Verify an Automorphism:
1. Check that $\phi: G \to G$ is a homomorphism
2. Verify $\phi$ is bijective (injective and surjective)

# Examples

**Example 1** (p. 153): Every automorphism of $\mathbb{Z}_n$ has the form $\phi_k: a \mapsto ka$ where $k$ is a generator of $\mathbb{Z}_n$. Hence $\operatorname{Aut}(\mathbb{Z}_n) \cong U(n)$.

# Relationships

## Builds Upon
- **Isomorphism** — Automorphisms are self-isomorphisms

## Enables
- **Automorphism group** — $\operatorname{Aut}(G)$ is itself a group
- **Inner automorphism** — A special type of automorphism

# Source Reference

Chapter 11: Homomorphisms, Section 11.5, p. 152-153.

# Verification Notes

- Definition source: Exercise 11.5.1
- Confidence: HIGH — standard definition stated in exercises
