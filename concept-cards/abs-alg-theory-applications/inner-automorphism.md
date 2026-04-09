---
concept: Inner Automorphism
slug: inner-automorphism
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
  - "i_g"
  - "conjugation automorphism"
prerequisites:
  - automorphism
  - conjugation-of-elements
extends:
  - automorphism
related:
  - automorphism-group
  - center-of-group
  - normal-subgroup
contrasts_with:
  - automorphism
answers_questions:
  - "What is an inner automorphism?"
  - "How do inner automorphisms relate to conjugation?"
---

# Quick Definition

An inner automorphism of $G$ is the map $i_g: G \to G$ defined by $i_g(x) = gxg^{-1}$ for a fixed $g \in G$. The set of all inner automorphisms forms a normal subgroup $\operatorname{Inn}(G)$ of $\operatorname{Aut}(G)$, and $G/Z(G) \cong \operatorname{Inn}(G)$.

# Core Definition

"An **inner automorphism** of $G$, $i_g: G \to G$, is defined by the map $i_g(x) = gxg^{-1}$, for $g \in G$" (Judson, p. 152, Exercise 11.5.2). Each $i_g$ is indeed an automorphism, and the set $\operatorname{Inn}(G)$ of all inner automorphisms is a subgroup of $\operatorname{Aut}(G)$.

# Prerequisites

- **Automorphism** — Inner automorphisms are a special case
- **Conjugation** — $i_g$ is conjugation by $g$

# Key Properties

1. $i_g \in \operatorname{Aut}(G)$ for every $g \in G$
2. $\operatorname{Inn}(G)$ is a subgroup of $\operatorname{Aut}(G)$
3. The map $g \mapsto i_g$ is a homomorphism $G \to \operatorname{Aut}(G)$ with image $\operatorname{Inn}(G)$ and kernel $Z(G)$
4. $G/Z(G) \cong \operatorname{Inn}(G)$
5. $\operatorname{Inn}(G) = \{e\}$ if and only if $G$ is abelian

# Context & Application

Inner automorphisms measure the non-commutativity of a group. The quotient $G/Z(G) \cong \operatorname{Inn}(G)$ connects the center to the structure of automorphisms. A subgroup $N$ is normal if and only if $i_g(N) = N$ for all inner automorphisms $i_g$.

# Examples

**Example 1** (p. 153): For $S_3$, $\operatorname{Inn}(S_3) \cong S_3/Z(S_3) = S_3/\{(1)\} \cong S_3$.

# Relationships

## Builds Upon
- **Automorphism** — Inner automorphisms are special automorphisms

## Enables
- **Normal subgroup characterization** — $N$ is normal iff invariant under all inner automorphisms

## Related
- **Center of group** — $Z(G)$ is the kernel of $g \mapsto i_g$

## Contrasts With
- **Automorphism** — Not every automorphism is inner (outer automorphisms exist)

# Source Reference

Chapter 11: Homomorphisms, Section 11.5, Exercises 11.5.2-11.5.5, p. 152-153.

# Verification Notes

- Definition source: Exercise 11.5.2
- Key result $G/Z(G) \cong \operatorname{Inn}(G)$: Exercise 11.5.5
- Confidence: HIGH — explicitly defined in exercises
