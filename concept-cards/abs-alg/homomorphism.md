---
concept: Homomorphism
slug: homomorphism
category: group-theory
subcategory: morphisms
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Groups"
chapter_number: 1
pdf_page: 26
section: "1.6 Homomorphisms and Isomorphisms"
extraction_confidence: high
aliases:
  - "group homomorphism"
prerequisites:
  - group
extends: []
related:
  - isomorphism
  - kernel
  - quotient-group
  - normal-subgroup
contrasts_with:
  - isomorphism
answers_questions:
  - "What is a homomorphism?"
  - "What does it mean for a map to respect group structure?"
---

# Quick Definition
A homomorphism is a map $\varphi: G \to H$ between groups satisfying $\varphi(xy) = \varphi(x)\varphi(y)$ for all $x, y \in G$. It preserves the group operation.

# Core Definition
Let $(G, \star)$ and $(H, \diamond)$ be groups. A map $\varphi: G \to H$ such that $\varphi(x \star y) = \varphi(x) \diamond \varphi(y)$ for all $x, y \in G$ is called a *homomorphism*. The product xy is computed in G while $\varphi(x)\varphi(y)$ is computed in H (Dummit & Foote, pp. 36-37).

# Prerequisites
- **Group** — homomorphisms map between groups

# Key Properties
1. $\varphi(1_G) = 1_H$
2. $\varphi(g^{-1}) = \varphi(g)^{-1}$
3. $\varphi(g^n) = \varphi(g)^n$ for all $n \in \mathbb{Z}$
4. $\ker \varphi$ is a subgroup of G
5. $\text{im}(\varphi)$ is a subgroup of H
6. $|\varphi(x)|$ divides $|x|$

# Construction / Recognition
## To Construct/Create:
1. Define the map on generators of G
2. Verify the relations in G are satisfied by the images in H
3. The map extends uniquely to a homomorphism

## To Identify/Recognize:
1. Check $\varphi(xy) = \varphi(x)\varphi(y)$ for all x, y

# Context & Application
Homomorphisms are the structure-preserving maps in group theory. They connect groups to each other and, via their kernels, give rise to normal subgroups and quotient groups. The study of homomorphic images is equivalent to the study of quotient groups.

# Examples
**Example 1** (p. 38): $\exp: (\mathbb{R}, +) \to (\mathbb{R}^+, \times)$ defined by $x \mapsto e^x$ is an isomorphism since $e^{x+y} = e^x e^y$.
**Example 2** (p. 40): $\varphi: D_{2n} \to D_{2k}$ (k divides n) defined by $r \mapsto r_1$, $s \mapsto s_1$ is a surjective homomorphism.

# Relationships
## Builds Upon
- **group**

## Enables
- **kernel** — $\ker \varphi = \{g \in G \mid \varphi(g) = 1_H\}$
- **isomorphism** — a bijective homomorphism
- **quotient-group** — $G/\ker\varphi \cong \text{im}(\varphi)$

## Related
- **normal-subgroup** — kernels are normal subgroups

## Contrasts With
- **isomorphism** — an isomorphism is additionally bijective

# Common Errors
- **Error**: Assuming a homomorphism preserves element order. **Correction**: $|\varphi(x)|$ divides $|x|$ but need not equal it; the image can have smaller order.

# Common Confusions
- **Confusion**: Thinking a surjective homomorphism is an isomorphism. **Clarification**: Surjectivity alone is not enough; the map must also be injective (trivial kernel).

# Source Reference
Chapter 1: Introduction to Groups, Section 1.6 "Homomorphisms and Isomorphisms," pages 36-44.

# Verification Notes
- Definition source: direct from source p. 37
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
