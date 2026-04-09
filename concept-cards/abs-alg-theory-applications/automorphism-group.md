---
concept: Automorphism Group
slug: automorphism-group
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
  - "Aut(G)"
prerequisites:
  - automorphism
  - group
extends:
  - group
related:
  - inner-automorphism
  - symmetric-group
contrasts_with: []
answers_questions:
  - "What is the automorphism group of a group?"
---

# Quick Definition

The automorphism group $\operatorname{Aut}(G)$ is the group of all automorphisms of $G$ under composition. It is a subgroup of the symmetric group on the underlying set of $G$.

# Core Definition

"Let $\operatorname{Aut}(G)$ be the set of all automorphisms of $G$; that is, isomorphisms from $G$ to itself. Prove this set forms a group and is a subgroup of the group of permutations of $G$; that is, $\operatorname{Aut}(G) \leq S_G$" (Judson, p. 152, Exercise 11.5.1).

# Prerequisites

- **Automorphism** — Elements of $\operatorname{Aut}(G)$
- **Group** — $\operatorname{Aut}(G)$ is itself a group

# Key Properties

1. $\operatorname{Aut}(G)$ is a group under composition
2. $\operatorname{Aut}(G) \leq S_G$
3. $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$
4. $\operatorname{Aut}(\mathbb{Z}_n) \cong U(n)$
5. $\operatorname{Aut}(\mathbb{Z}) \cong \mathbb{Z}_2$

# Examples

**Example 1** (p. 153): $\operatorname{Aut}(\mathbb{Z}_8) \cong U(8) = \{1, 3, 5, 7\}$, a group of order 4.

# Relationships

## Builds Upon
- **Automorphism** — The elements of this group

## Related
- **Inner automorphism** — $\operatorname{Inn}(G)$ is a normal subgroup of $\operatorname{Aut}(G)$

# Source Reference

Chapter 11: Homomorphisms, Section 11.5, p. 152-153.

# Verification Notes

- Definition source: Exercise 11.5.1
- Confidence: HIGH — explicitly stated
