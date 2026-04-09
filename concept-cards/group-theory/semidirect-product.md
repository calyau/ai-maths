---
# === CORE IDENTIFICATION ===
concept: Semidirect Product
slug: semidirect-product

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: products
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 45
section: "Semidirect products"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "N ⋊ Q"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - automorphism-group
  - homomorphism
extends:
  - direct-product
related:
  - split-extension
  - internal-semidirect-product
  - external-semidirect-product
contrasts_with:
  - direct-product

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a semidirect product?"
  - "What distinguishes a semidirect product from a direct product?"
  - "How do I construct a semidirect product from a normal subgroup and a complement?"
---

# Quick Definition

A semidirect product $G = N \rtimes Q$ is a group with normal subgroup $N$ and complement $Q$ such that $NQ = G$ and $N \cap Q = \{1\}$, where $Q$ acts on $N$ by conjugation.

# Core Definition

"A group $G$ is a semidirect product of its subgroups $N$ and $Q$ if $N$ is normal and the homomorphism $Q \to G/N$ induces an isomorphism $Q \to G/N$" (Milne, Definition 3.8, p. 45). Equivalently: $N \trianglelefteq G$, $NQ = G$, $N \cap Q = \{1\}$.

# Prerequisites

- **Normal subgroup** — $N$ must be normal in $G$
- **Automorphism group** — The action is a homomorphism $\theta: Q \to \operatorname{Aut}(N)$
- **Homomorphism** — The action map $\theta$ must be a group homomorphism

# Key Properties

1. Every element $g \in G$ can be written uniquely as $g = nq$, $n \in N$, $q \in Q$
2. The multiplication law is $(nq)(n'q') = n \cdot \theta(q)(n') \cdot qq'$
3. $Q$ need not be normal in $G$
4. When $\theta$ is trivial, $N \rtimes Q = N \times Q$ (direct product)
5. Every semidirect product gives a triple $(N, Q, \theta: Q \to \operatorname{Aut}(N))$
6. Every such triple gives a semidirect product (Proposition 3.10)

# Construction / Recognition

## To construct $N \rtimes_\theta Q$:
1. Choose groups $N$ and $Q$ and a homomorphism $\theta: Q \to \operatorname{Aut}(N)$
2. As a set, $G = N \times Q$
3. Define $(n,q)(n',q') = (n \cdot \theta(q)(n'), qq')$
4. This makes $G$ into a group (Proposition 3.10)

## To recognize an internal semidirect product:
1. Find $N \trianglelefteq G$ and subgroup $Q \leq G$
2. Verify $NQ = G$ and $N \cap Q = \{1\}$

# Context & Application

Semidirect products are the simplest way to build non-abelian groups from smaller groups. They correspond to split extensions and are a key tool in classifying groups of small order.

# Examples

**Example 1** (p. 45): $D_n = C_n \rtimes_\theta C_2$, where $\theta$ sends the generator of $C_2$ to the automorphism $r \mapsto r^{-1}$.

**Example 2** (p. 46): $S_n = A_n \rtimes C_2$, since $A_n$ is normal of index 2.

**Example 3** (p. 46): The Borel subgroup $B = U \rtimes T$ of upper triangular matrices, with $U$ unipotent upper triangular and $T$ diagonal.

**Non-Example** (p. 46): The quaternion group $Q$ cannot be written as a nontrivial semidirect product.

**Non-Example** (p. 46): $C_{p^2}$ is not a semidirect product (only one subgroup of order $p$).

# Relationships

## Builds Upon
- **normal-subgroup** — $N$ is required to be normal
- **automorphism-group** — The action $\theta: Q \to \operatorname{Aut}(N)$

## Enables
- **split-extension** — A split extension is exactly a semidirect product
- **extension-of-groups** — Semidirect products are special extensions

## Contrasts With
- **direct-product** — Direct product is the special case where $\theta$ is trivial (and hence $Q$ is also normal)

# Common Errors

- **Error**: Assuming $Q$ is normal in $N \rtimes Q$
  **Correction**: Only $N$ is required to be normal. If both are normal, the product is direct.

- **Error**: Assuming two different homomorphisms $\theta, \theta'$ always give non-isomorphic groups
  **Correction**: Lemmas 3.17-3.19 give criteria for when different $\theta$ yield isomorphic groups

# Common Confusions

- **Confusion**: Confusing semidirect product with direct product
  **Clarification**: A semidirect product becomes a direct product precisely when the action $\theta$ is trivial

# Source Reference

Chapter 3: Automorphisms and Extensions, "Semidirect products", Definition 3.8, pages 45-47.

# Verification Notes

- Definition source: Direct quote from Definition 3.8, p. 45
- Confidence: HIGH — explicit definition
- Uncertainties: None
