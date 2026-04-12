---
# === CORE IDENTIFICATION ===
concept: Isomorphic Groups
slug: isomorphic-groups

# === CLASSIFICATION ===
category: fundamentals
subcategory: maps
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Isomorphisms"
chapter_number: 7
pdf_page: 39
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "G isomorphic to G'"
  - "G ≅ G'"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - isomorphism
extends: []
related:
  - isomorphism-preserves-identity
  - isomorphism-preserves-order
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I determine whether two groups are isomorphic?"
  - "What does it mean for two groups to be isomorphic?"
---

# Quick Definition

Two groups are isomorphic ($G \cong G'$) if there exists an isomorphism between them. They are algebraically identical, differing only in the labelling of elements.

# Core Definition

Groups $G$ and $G'$ are isomorphic if there exists a bijection $\varphi: G \to G'$ satisfying $\varphi(xy) = \varphi(x)\varphi(y)$. Armstrong writes: "To all intents and purposes then, $G$ and $G'$ are 'the same'" (p. 40). The notation $G \cong G'$ is used.

# Prerequisites

- **Isomorphism** — Isomorphic groups are connected by an isomorphism

# Key Properties

1. Isomorphic groups have the same order
2. Isomorphism is an equivalence relation (reflexive, symmetric, transitive)
3. Isomorphic groups share all group-theoretic properties (abelianness, element orders, subgroup structure, etc.)
4. The relation is symmetric: if $G \cong G'$ then $G' \cong G$

# Construction / Recognition

## To Show Groups Are Isomorphic:
1. Construct an explicit bijection $\varphi: G \to G'$
2. Verify $\varphi(xy) = \varphi(x)\varphi(y)$

## To Show Groups Are Not Isomorphic:
1. Compare orders (must be equal)
2. Compare abelianness
3. Compare orders of elements
4. Compare number/structure of subgroups
5. If any property differs, the groups are not isomorphic

# Context & Application

Determining whether two groups are isomorphic is a fundamental problem in group theory. Armstrong demonstrates several techniques: direct construction of isomorphisms, and proving non-isomorphism via group-theoretic invariants. The concept allows us to classify groups "up to isomorphism."

# Examples

**Example** (p. 41): The rotational symmetry group of the tetrahedron is isomorphic to $A_4$ (both non-abelian, order 12).

**Example** (p. 41): $D_3 \cong S_3$ (labelling vertices of a triangle gives the isomorphism).

**Example** (p. 42): $D_6 \not\cong A_4$ because $D_6$ contains an element of order 6 while $A_4$ does not. Neither is isomorphic to $\mathbb{Z}_{12}$ because $\mathbb{Z}_{12}$ is abelian while the other two are not.

**Example** (p. 41): $\mathbb{Q} \not\cong \mathbb{Q}^{pos}$ because any candidate isomorphism would require $\sqrt{2} \in \mathbb{Q}$.

# Relationships

## Builds Upon
- **Isomorphism** — The function witnessing the relationship

## Related
- **Isomorphism preserves identity** — Same identity structure
- **Isomorphism preserves order** — Same element orders
- **Cayley's theorem** — Every group is isomorphic to a permutation group

# Common Errors

- **Error**: Concluding groups are isomorphic because they have the same order.
  **Correction**: Same order is necessary but not sufficient. For example, $\mathbb{Z}_4 \not\cong \mathbb{Z}_2 \times \mathbb{Z}_2$ (one is cyclic, the other is not).

# Common Confusions

- **Confusion**: Thinking isomorphic groups must have the same elements.
  **Clarification**: Isomorphic groups can have completely different elements. The chessboard symmetry group and $\{1, 3, 5, 7\}$ mod 8 are isomorphic but have different elements.

# Source Reference

Chapter 7: Isomorphisms, pages 39-43 (pdf pp. 39-43). Multiple examples of proving and disproving isomorphism.

# Verification Notes

- Definition: From p. 40
- Non-isomorphism techniques: pp. 41-42
- Confidence: HIGH — concept is thoroughly treated with many examples
