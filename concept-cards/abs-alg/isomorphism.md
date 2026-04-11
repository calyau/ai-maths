---
concept: Isomorphism
slug: isomorphism
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
  - "group isomorphism"
prerequisites:
  - homomorphism
  - bijection
extends:
  - homomorphism
related:
  - automorphism
  - first-isomorphism-theorem
contrasts_with: []
answers_questions:
  - "What is an isomorphism?"
  - "When are two groups isomorphic?"
  - "What properties are preserved by isomorphisms?"
---

# Quick Definition
An isomorphism is a bijective homomorphism $\varphi: G \to H$. Groups G and H are isomorphic ($G \cong H$) if such a map exists, meaning they have identical group-theoretic structure.

# Core Definition
The map $\varphi: G \to H$ is an *isomorphism* and G and H are *isomorphic*, written $G \cong H$, if (1) $\varphi$ is a homomorphism and (2) $\varphi$ is a bijection. Any property depending only on group structure is preserved: if $G \cong H$ then $|G| = |H|$, G is abelian iff H is, and for all $x \in G$, $|x| = |\varphi(x)|$ (Dummit & Foote, pp. 37-39).

# Prerequisites
- **Homomorphism** — an isomorphism is a homomorphism
- **Bijection** — an isomorphism is bijective

# Key Properties
1. Preserves group order: $|G| = |H|$
2. Preserves commutativity: G abelian iff H abelian
3. Preserves element orders: $|x| = |\varphi(x)|$
4. Preserves number of elements of each order
5. "Is isomorphic to" is an equivalence relation on groups
6. $\varphi$ is an isomorphism iff it is injective (trivial kernel) and surjective

# Construction / Recognition
## To Construct/Create:
1. Define a map between generators and check relations are preserved
2. Verify bijectivity (often by showing surjectivity when groups have equal finite order)

## To Identify/Recognize:
1. Find a bijective homomorphism, OR
2. Use structural invariants to rule out isomorphism (order, abelianness, element orders)

# Context & Application
Isomorphism is the fundamental equivalence relation in group theory. Classification theorems characterize groups up to isomorphism. For example, any non-abelian group of order 6 is isomorphic to $S_3$.

# Examples
**Example 1** (p. 38): $\exp: (\mathbb{R},+) \to (\mathbb{R}^+, \times)$ is an isomorphism.
**Example 2** (p. 40): $D_6 \cong S_3$ via $r \mapsto (123)$, $s \mapsto (12)$.
**Example 3** (p. 39): $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$ since one is abelian and the other is not.

# Relationships
## Builds Upon
- **homomorphism**, **bijection**

## Enables
- **first-isomorphism-theorem** — $G/\ker\varphi \cong \text{im}(\varphi)$

## Related
- **automorphism** — an isomorphism from G to itself

# Common Errors
- **Error**: Trying to prove isomorphism by checking a few elements. **Correction**: Must verify the map is a well-defined bijective homomorphism on all elements.

# Common Confusions
- **Confusion**: Thinking isomorphic groups are equal. **Clarification**: Isomorphic groups have the same structure but may consist of completely different elements with different operations.

# Source Reference
Chapter 1: Introduction to Groups, Section 1.6, pages 37-42.

# Verification Notes
- Definition source: direct from source pp. 37-38
- Confidence rationale: extensively discussed with examples
- Uncertainties: none
- Cross-reference status: verified
