---
# === CORE IDENTIFICATION ===
concept: Making Outer Automorphisms Inner
slug: making-outer-automorphisms-inner

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
pdf_page: 48
section: "Semidirect products"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - outer-automorphism
  - semidirect-product
extends: []
related:
  - inner-automorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can an outer automorphism become inner in a larger group?"
---

# Quick Definition

Any outer automorphism $\alpha$ of $N$ can be realized as the restriction of an inner automorphism of a larger group $G \supset N$, by forming $G = N \rtimes_\theta C_\infty$ with $\theta$ sending a generator to $\alpha$.

# Core Definition

"Let $\alpha$ be an automorphism, possibly outer, of a group $N$. We can realize $N$ as a normal subgroup of a group $G$ in such a way that $\alpha$ becomes the restriction to $N$ of an inner automorphism of $G$" (Milne, Example 3.16, p. 48). Specifically, let $\theta: C_\infty \to \operatorname{Aut}(N)$ send a generator $a$ to $\alpha$, and let $G = N \rtimes_\theta C_\infty$. Then $g = (1, a)$ satisfies $g(n,1)g^{-1} = (\alpha(n), 1)$.

# Prerequisites

- **Outer automorphism** — The automorphism being internalized
- **Semidirect product** — The construction uses a semidirect product

# Key Properties

1. Demonstrates that the distinction inner/outer depends on the ambient group
2. An inner automorphism of $G$ may restrict to an outer automorphism of a normal subgroup $N$
3. This is why a normal subgroup of a normal subgroup need not be normal (Remark 3.7a)

# Context & Application

This construction shows that "inner" and "outer" are relative concepts. It explains why characteristic subgroups (invariant under all automorphisms) are better behaved than merely normal subgroups.

# Relationships

## Related
- **outer-automorphism**, **inner-automorphism**, **semidirect-product**

# Source Reference

Chapter 3: Automorphisms and Extensions, Example 3.16, page 48.

# Verification Notes

- Definition source: Example 3.16, p. 48
- Confidence: HIGH — explicit construction
- Uncertainties: None
