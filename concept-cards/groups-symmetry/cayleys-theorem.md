---
# === CORE IDENTIFICATION ===
concept: "Cayley's Theorem"
slug: cayleys-theorem

# === CLASSIFICATION ===
category: symmetry-groups
subcategory: representation
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Plato's Solids and Cayley's Theorem"
chapter_number: 8
pdf_page: 44
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - isomorphism
  - symmetric-group
  - left-translation
extends: []
related:
  - permutation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can every group be represented as a group of permutations?"
  - "What is Cayley's theorem?"
---

# Quick Definition

Cayley's theorem states that every group $G$ is isomorphic to a subgroup of the symmetric group $S_G$ (permutations of the underlying set of $G$).

# Core Definition

"(8.1) Cayley's Theorem. Let $G$ be a group, then $G$ is isomorphic to a subgroup of $S_G$" (Armstrong, p. 48). The proof constructs, for each $g \in G$, the left translation $L_g: G \to G$ defined by $L_g(x) = gx$. The set $G' = \{L_g \mid g \in G\}$ is a subgroup of $S_G$, and the correspondence $g \mapsto L_g$ is an isomorphism from $G$ to $G'$.

# Prerequisites

- **Isomorphism** — The theorem produces an isomorphism
- **Symmetric group** — $G$ embeds into a symmetric group
- **Left translation** — The isomorphism is built from left translations

# Key Properties

1. Every group is isomorphic to a group of permutations
2. The embedding uses left translation: $g \mapsto L_g$ where $L_g(x) = gx$
3. $L_g L_h = L_{gh}$ (composition matches group multiplication)
4. The map is injective: $L_g = L_h$ implies $g = L_g(e) = L_h(e) = h$
5. For a finite group of order $n$, $G$ is isomorphic to a subgroup of $S_n$ (Theorem 8.2)

# Construction / Recognition

## To Apply Cayley's Theorem:
1. Label the elements of $G$ as $g_1, g_2, \ldots, g_n$
2. For each $g \in G$, compute $L_g$: the permutation sending each $g_i$ to $gg_i$
3. The collection $\{L_g \mid g \in G\}$ is the desired subgroup of $S_n$

# Context & Application

Cayley's theorem is a foundational result showing that abstract groups are no more general than permutation groups. While the embedding into $S_G$ (or $S_n$) may be inefficient (the image may be a tiny subgroup of a much larger group), the theorem guarantees that every group-theoretic question can in principle be answered by studying permutations.

# Examples

**Example** (p. 49): For the chessboard symmetry group $\{e, r, q_1, q_2\}$:
- $L_r$: $e \to r$, $r \to e$, $q_1 \to q_2$, $q_2 \to q_1$, giving permutation $(12)(34)$
- Similarly computing $L_{q_1}$, $L_{q_2}$
- The resulting subgroup of $S_4$ is $\{\varepsilon, (12)(34), (13)(24), (14)(23)\}$

**Example** (p. 48): When $G = \mathbb{R}$, $L_g$ is physical translation through distance $g$.

# Relationships

## Builds Upon
- **Left translation** — The isomorphism is built from left translations
- **Symmetric group** — The target of the embedding

## Related
- **Permutation** — Every group element corresponds to a permutation

# Common Errors

- **Error**: Thinking Cayley's theorem gives a minimal embedding.
  **Correction**: The embedding into $S_n$ may be far from optimal. For example, $\mathbb{Z}_6$ embeds into $S_6$ (order 720) even though it is a tiny cyclic group.

# Common Confusions

- **Confusion**: Thinking Cayley's theorem means every group IS a symmetric group.
  **Clarification**: The theorem says every group is isomorphic to a *subgroup* of a symmetric group, not to the whole symmetric group.

# Source Reference

Chapter 8: Plato's Solids and Cayley's Theorem, pages 48-49 (pdf pp. 48-49). Theorem 8.1 with proof; Theorem 8.2 (finite case); worked example.

# Verification Notes

- Theorem: Direct from p. 48, Theorem 8.1
- Proof: Complete on p. 48
- Example: Worked on p. 49
- Confidence: HIGH — theorem with complete proof and example
