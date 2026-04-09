---
concept: Properties of Group Homomorphisms
slug: properties-of-homomorphisms
category: morphisms
subcategory: group-maps
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Homomorphisms"
chapter_number: 11
pdf_page: 147
section: "Group Homomorphisms"
extraction_confidence: high
aliases: []
prerequisites:
  - group-homomorphism
extends:
  - group-homomorphism
related:
  - kernel-of-homomorphism
  - homomorphic-image
contrasts_with: []
answers_questions:
  - "What properties do group homomorphisms preserve?"
---

# Quick Definition

Group homomorphisms automatically preserve identity elements, inverses, and subgroup structure. If $\phi: G_1 \to G_2$ is a homomorphism, then $\phi(e) = e'$, $\phi(g^{-1}) = [\phi(g)]^{-1}$, images of subgroups are subgroups, and preimages of subgroups are subgroups.

# Core Definition

**Proposition 11.4**: "Let $\phi: G_1 \to G_2$ be a homomorphism of groups. Then (1) If $e$ is the identity of $G_1$, then $\phi(e)$ is the identity of $G_2$; (2) For any element $g \in G_1$, $\phi(g^{-1}) = [\phi(g)]^{-1}$; (3) If $H_1$ is a subgroup of $G_1$, then $\phi(H_1)$ is a subgroup of $G_2$; (4) If $H_2$ is a subgroup of $G_2$, then $\phi^{-1}(H_2)$ is a subgroup of $G_1$. Furthermore, if $H_2$ is normal in $G_2$, then $\phi^{-1}(H_2)$ is normal in $G_1$" (Judson, p. 147).

# Prerequisites

- **Group homomorphism** — These are properties of homomorphisms

# Key Properties

1. Identity preservation: $\phi(e) = e'$
2. Inverse preservation: $\phi(g^{-1}) = [\phi(g)]^{-1}$
3. Forward subgroup preservation: images of subgroups are subgroups
4. Backward subgroup preservation: preimages of subgroups are subgroups
5. Normality pullback: preimage of a normal subgroup is normal

# Source Reference

Chapter 11: Homomorphisms, Section 11.1, p. 147. Proposition 11.4.

# Verification Notes

- Definition source: Proposition 11.4
- Confidence: HIGH
