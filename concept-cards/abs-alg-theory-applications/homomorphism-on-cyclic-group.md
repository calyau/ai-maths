---
concept: Homomorphism on a Cyclic Group
slug: homomorphism-on-cyclic-group
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
aliases: []
prerequisites:
  - group-homomorphism
  - cyclic-group
extends:
  - group-homomorphism
related:
  - automorphism
contrasts_with: []
answers_questions:
  - "How is a homomorphism on a cyclic group determined?"
---

# Quick Definition

A homomorphism defined on a cyclic group is completely determined by its action on the generator. If $G = \langle g \rangle$, then $\phi(g)$ determines $\phi(g^n) = [\phi(g)]^n$ for all $n$.

# Core Definition

**Exercise 11.4.11**: "Show that a homomorphism defined on a cyclic group is completely determined by its action on the generator of the group" (Judson, p. 152). If $\phi: \mathbb{Z}_n \to H$ maps $1 \mapsto h$, then the image of $\phi$ is $\langle h \rangle$ and $|h|$ must divide $n$.

# Prerequisites

- **Group homomorphism** — The type of map
- **Cyclic group** — The domain

# Key Properties

1. $\phi$ is determined by $\phi(g)$ where $g$ generates $G$
2. $\phi(g^n) = [\phi(g)]^n$
3. If $G$ is cyclic, $\phi(G)$ is cyclic
4. The order of $\phi(g)$ divides the order of $g$
5. Counting: homomorphisms $\mathbb{Z}_n \to \mathbb{Z}_m$ correspond to elements of $\mathbb{Z}_m$ whose order divides $n$

# Examples

**Example 1** (p. 148): The only homomorphism from $\mathbb{Z}_7$ to $\mathbb{Z}_{12}$ is the trivial one, since $\mathbb{Z}_{12}$ has no element whose order divides 7 (other than 0).

# Relationships

## Builds Upon
- **Group homomorphism** — Specific case for cyclic domains

## Related
- **Automorphism** — $\operatorname{Aut}(\mathbb{Z}_n) \cong U(n)$ via this principle

# Source Reference

Chapter 11: Homomorphisms, Exercise 11.4.11, p. 152. Also Example 11.8.

# Verification Notes

- Definition source: Exercise 11.4.11
- Confidence: HIGH
