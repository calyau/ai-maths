---
concept: Homomorphism Injectivity Criterion
slug: homomorphism-injectivity-criterion
category: morphisms
subcategory: group-maps
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Homomorphisms"
chapter_number: 11
pdf_page: 152
section: "Exercises"
extraction_confidence: high
aliases:
  - "trivial kernel criterion"
prerequisites:
  - group-homomorphism
  - kernel-of-homomorphism
extends: []
related:
  - isomorphism
contrasts_with: []
answers_questions:
  - "How do I determine if a group homomorphism is injective?"
---

# Quick Definition

A group homomorphism $\phi: G \to H$ is injective (one-to-one) if and only if $\ker\phi = \{e\}$. This provides a simple test: instead of checking all pairs of elements, just check if only the identity maps to the identity.

# Core Definition

**Exercise 11.4.18**: "Let $\phi: G \to H$ be a group homomorphism. Show that $\phi$ is one-to-one if and only if $\phi^{-1}(e) = \{e\}$" (Judson, p. 152).

# Prerequisites

- **Group homomorphism** — The map being tested
- **Kernel of homomorphism** — Trivial kernel means injective

# Key Properties

1. $\phi$ injective $\iff$ $\ker\phi = \{e\}$
2. This is simpler than checking $\phi(a) = \phi(b) \Rightarrow a = b$ for all pairs
3. If $\phi(a) = \phi(b)$, then $\phi(ab^{-1}) = e$, so $ab^{-1} \in \ker\phi$

# Relationships

## Builds Upon
- **Kernel of homomorphism** — Trivial kernel characterizes injectivity

## Related
- **Isomorphism** — An injective surjective homomorphism

# Source Reference

Chapter 11: Homomorphisms, Exercise 11.4.18, p. 152.

# Verification Notes

- Definition source: Exercise 11.4.18
- Confidence: HIGH
