---
concept: Normalizer
slug: normalizer
category: group-structure
subcategory: subgroup-types
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Sylow Theorems"
chapter_number: 15
pdf_page: 196
section: "The Sylow Theorems"
extraction_confidence: high
aliases:
  - "N(H)"
  - "normalizer of H"
prerequisites:
  - subgroup
  - normal-subgroup
  - conjugation-of-subgroups
extends:
  - subgroup
related:
  - centralizer-of-element
  - sylow-p-subgroup
  - second-sylow-theorem
contrasts_with:
  - centralizer-of-element
answers_questions:
  - "What is the normalizer of a subgroup?"
  - "How does the normalizer relate to normality?"
---

# Quick Definition

The normalizer of a subgroup $H$ in $G$ is $N(H) = \{g \in G : gHg^{-1} = H\}$, the largest subgroup of $G$ in which $H$ is normal. $H$ is normal in $G$ if and only if $N(H) = G$.

# Core Definition

"The set $N(H) = \{g \in G : gHg^{-1} = H\}$ is a subgroup of $G$ called the **normalizer** of $H$ in $G$. Notice that $H$ is a normal subgroup of $N(H)$. In fact, $N(H)$ is the largest subgroup of $G$ in which $H$ is normal" (Judson, p. 196).

# Prerequisites

- **Subgroup** — $N(H)$ is a subgroup
- **Normal subgroup** — $H \trianglelefteq N(H)$
- **Conjugation of subgroups** — $N(H)$ collects elements that normalize $H$

# Key Properties

1. $N(H)$ is a subgroup of $G$
2. $H \trianglelefteq N(H)$
3. $H \trianglelefteq G$ iff $N(H) = G$
4. The number of conjugates of $H$ is $[G:N(H)]$ (Lemma 15.6)
5. $H \leq N(H) \leq G$

# Context & Application

The normalizer is crucial for the Sylow theorems. The number of Sylow $p$-subgroups equals $[G:N(P)]$ for any Sylow $p$-subgroup $P$. It also appears in counting arguments used to prove groups are not simple.

# Relationships

## Builds Upon
- **Conjugation of subgroups** — $N(H)$ is the set of elements preserving $H$ under conjugation

## Enables
- **Second Sylow theorem** — Uses normalizers in the proof
- **Third Sylow theorem** — Number of Sylow subgroups $= [G:N(P)]$

## Contrasts With
- **Centralizer of element** — $C(g) = \{x : xg = gx\}$ involves individual elements; $N(H)$ involves subgroups

# Source Reference

Chapter 15: The Sylow Theorems, Section 15.1, p. 196-197. Lemma 15.5, 15.6.

# Verification Notes

- Definition source: Direct from p. 196
- Confidence: HIGH
