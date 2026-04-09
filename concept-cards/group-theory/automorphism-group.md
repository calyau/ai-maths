---
# === CORE IDENTIFICATION ===
concept: Automorphism Group
slug: automorphism-group

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
  - "Aut(G)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - automorphism
extends:
  - automorphism
related:
  - inner-automorphism-group
  - outer-automorphism-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an automorphism of a group?"
  - "How do the automorphisms of a group form a group?"
---

# Quick Definition

The automorphism group $\operatorname{Aut}(G)$ of a group $G$ is the group of all automorphisms of $G$ under composition.

# Core Definition

"The set $\operatorname{Aut}(G)$ of automorphisms of $G$ becomes a group under composition" (Milne, p. 42). The group operation is function composition, the identity is the identity map, and inverses are inverse functions.

# Prerequisites

- **Automorphism** — The elements of $\operatorname{Aut}(G)$ are automorphisms

# Key Properties

1. $\operatorname{Aut}(G)$ is a subgroup of $\operatorname{Sym}(G)$
2. $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$ — inner automorphisms form a normal subgroup
3. $\operatorname{Out}(G) = \operatorname{Aut}(G)/\operatorname{Inn}(G)$
4. $\operatorname{Aut}(C_n) \simeq (\mathbb{Z}/n\mathbb{Z})^\times$

# Construction / Recognition

## Computing $\operatorname{Aut}(G)$:
1. Determine all isomorphisms $G \to G$
2. An automorphism of $G$ is determined by its values on generators
3. For cyclic $G = \langle a \rangle$ of order $n$: $\alpha(a) = a^m$ with $\gcd(m,n)=1$

# Context & Application

The automorphism group encodes all symmetries of a group's structure. It appears in semidirect product constructions and extension theory.

# Examples

**Example 1** (p. 42): $\operatorname{Aut}(\mathbb{F}_p^n) = \operatorname{GL}_n(\mathbb{F}_p)$.

**Example 2** (p. 42): $\operatorname{Aut}(C_2 \times C_2) = \operatorname{GL}_2(\mathbb{F}_2) \approx S_3$.

**Example 3** (p. 42): $\operatorname{Aut}(Q) \approx S_4$ for the quaternion group $Q$.

# Relationships

## Builds Upon
- **automorphism** — Elements of the automorphism group

## Enables
- **semidirect-product** — Defined via homomorphism $Q \to \operatorname{Aut}(N)$
- **complete-group** — A group where $G \to \operatorname{Aut}(G)$ is an isomorphism

## Related
- **inner-automorphism-group** — Normal subgroup $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$

# Common Errors

- **Error**: Assuming nonisomorphic groups have nonisomorphic automorphism groups
  **Correction**: $C_2 \times C_2$ and $S_3$ are not isomorphic but both have automorphism group $\operatorname{GL}_2(\mathbb{F}_2) \approx S_3$ (Milne, p. 43)

# Source Reference

Chapter 3: Automorphisms and Extensions, "Automorphisms of groups", page 42.

# Verification Notes

- Definition source: Direct from p. 42
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
