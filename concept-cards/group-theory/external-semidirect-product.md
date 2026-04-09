---
# === CORE IDENTIFICATION ===
concept: External Semidirect Product
slug: external-semidirect-product

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
pdf_page: 46
section: "Semidirect products"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semidirect-product
  - automorphism-group
extends: []
related:
  - internal-semidirect-product
contrasts_with:
  - internal-semidirect-product

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct a semidirect product from a normal subgroup and a complement?"
---

# Quick Definition

The external semidirect product constructs a new group from a triple $(N, Q, \theta: Q \to \operatorname{Aut}(N))$ using the set $N \times Q$ with a twisted multiplication.

# Core Definition

Given groups $N$, $Q$ and a homomorphism $\theta: Q \to \operatorname{Aut}(N)$, define on the set $N \times Q$ the operation $(n,q)(n',q') = (n \cdot \theta(q)(n'), qq')$. This makes $N \times Q$ into a group, the semidirect product $N \rtimes_\theta Q$ (Milne, Proposition 3.10, p. 46).

# Prerequisites

- **Semidirect product** — This is the explicit construction
- **Automorphism group** — The action $\theta$ maps into $\operatorname{Aut}(N)$

# Key Properties

1. Identity element is $(1,1)$
2. Inverse of $(n,q)$ is $(\theta(q^{-1})(n^{-1}), q^{-1})$
3. $N \cong \{(n,1)\} \trianglelefteq G$ and $Q \cong \{(1,q)\} \leq G$
4. When $\theta$ is trivial, recovers the direct product $N \times Q$

# Construction / Recognition

## Steps:
1. Choose groups $N$ and $Q$
2. Choose a homomorphism $\theta: Q \to \operatorname{Aut}(N)$
3. Define $(n,q)(n',q') = (n \cdot \theta(q)(n'), qq')$ on $N \times Q$
4. Verify: this is a group with $N \trianglelefteq G$, $NQ = G$, $N \cap Q = \{1\}$

# Examples

**Example 1** (p. 47): $C_3 \rtimes_\theta C_4$ with $\theta$ the unique nontrivial homomorphism $C_4 \to \operatorname{Aut}(C_3) \simeq C_2$ gives a noncommutative group of order 12 not isomorphic to $A_4$.

**Example 2** (p. 47): Both $S_3$ and $C_6$ are semidirect products of $C_3$ by $C_2$, corresponding to the two homomorphisms $C_2 \to \operatorname{Aut}(C_3)$.

# Relationships

## Contrasts With
- **internal-semidirect-product** — Internal starts from subgroups of a given group; external builds a new group from scratch

# Source Reference

Chapter 3: Automorphisms and Extensions, "Semidirect products", Proposition 3.10, page 46.

# Verification Notes

- Definition source: Proposition 3.10, p. 46
- Confidence: HIGH — explicit construction with proof
- Uncertainties: None
