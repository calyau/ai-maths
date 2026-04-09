---
# === CORE IDENTIFICATION ===
concept: Automorphism of a Group
slug: automorphism

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: automorphisms
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 42
section: "Automorphisms of groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - group automorphism

# === TYPED RELATIONSHIPS ===
prerequisites:
  - isomorphism
extends:
  - isomorphism
related:
  - automorphism-group
  - inner-automorphism
  - outer-automorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an automorphism of a group?"
---

# Quick Definition

An automorphism of a group $G$ is an isomorphism from $G$ to itself.

# Core Definition

"An automorphism of a group $G$ is an isomorphism of the group with itself" (Milne, p. 42). The set $\operatorname{Aut}(G)$ of all automorphisms of $G$ forms a group under composition.

# Prerequisites

- **Isomorphism** — An automorphism is a special case of isomorphism (source = target)

# Key Properties

1. The composite of two automorphisms is an automorphism
2. Composition of maps is associative
3. The identity map $g \mapsto g$ is the identity element
4. Every automorphism is a bijection whose inverse is also an automorphism
5. $\operatorname{Aut}(G)$ is a group under composition

# Construction / Recognition

## To verify a map is an automorphism:
1. Confirm it is a homomorphism $G \to G$
2. Confirm it is bijective (or equivalently, has an inverse homomorphism)

# Context & Application

Automorphisms capture the internal symmetries of a group. They are essential for constructing semidirect products and understanding extensions.

# Examples

**Example 1** (p. 42): For $G = \mathbb{F}_p^n$, $\operatorname{Aut}(G) = \operatorname{GL}_n(\mathbb{F}_p)$ — automorphisms as a commutative group are vector space automorphisms.

**Example 2** (p. 42): $\operatorname{Aut}(C_2 \times C_2) = \operatorname{GL}_2(\mathbb{F}_2)$.

**Example 3** (p. 42): For the quaternion group $Q$, $\operatorname{Aut}(Q) \approx S_4$.

# Relationships

## Builds Upon
- **isomorphism** — Automorphism is an isomorphism from a group to itself

## Enables
- **automorphism-group** — Automorphisms form the group $\operatorname{Aut}(G)$
- **inner-automorphism** — Conjugation automorphisms are a special case
- **semidirect-product** — Constructed via homomorphisms into $\operatorname{Aut}(N)$

## Related
- **outer-automorphism** — Automorphisms that are not inner

# Common Errors

- **Error**: Assuming every automorphism is inner (given by conjugation)
  **Correction**: Commutative groups have only trivial inner automorphisms; all nontrivial automorphisms are outer

# Common Confusions

- **Confusion**: Confusing automorphism with endomorphism
  **Clarification**: An automorphism must be bijective; an endomorphism is any homomorphism from $G$ to $G$

# Source Reference

Chapter 3: Automorphisms and Extensions, "Automorphisms of groups", page 42.

# Verification Notes

- Definition source: Direct quote from p. 42
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
