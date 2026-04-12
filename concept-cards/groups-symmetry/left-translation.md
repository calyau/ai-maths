---
# === CORE IDENTIFICATION ===
concept: Left Translation
slug: left-translation

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
aliases:
  - "L_g"
  - "left multiplication"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation
extends: []
related:
  - cayleys-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is left translation in group theory?"
  - "How does left translation provide a permutation representation?"
---

# Quick Definition

Left translation by $g$ is the map $L_g: G \to G$ defined by $L_g(x) = gx$. It is a permutation of $G$ and is the key construction in Cayley's theorem.

# Core Definition

"Each element $g$ in $G$ gives a permutation $L_g: G \to G$ defined by $L_g(x) = gx$. ($L_g$ is injective because if $L_g(x) = L_g(y)$ then $gx = gy$, giving $g^{-1}gx = g^{-1}gy$ and $x = y$. It is also surjective since if $z \in G$ then $L_g(g^{-1}z) = gg^{-1}z = z$.) We call $L_g$ **left translation** by $g$" (Armstrong, p. 48).

# Prerequisites

- **Permutation** — Left translation is a permutation of the group

# Key Properties

1. $L_g$ is a bijection from $G$ to $G$ (a permutation)
2. $L_g \circ L_h = L_{gh}$ (composition matches group multiplication)
3. $L_e = \varepsilon$ (identity translation is the identity permutation)
4. $(L_g)^{-1} = L_{g^{-1}}$
5. The map $g \mapsto L_g$ is injective: if $L_g = L_h$ then $g = h$
6. When $G = \mathbb{R}$, $L_g$ is physical translation by distance $g$

# Construction / Recognition

## To Compute $L_g$:
1. Take each element $x \in G$
2. Compute $gx$ (left multiply by $g$)
3. The resulting function $x \mapsto gx$ is $L_g$

# Context & Application

Left translation is the essential construction in Cayley's theorem. It provides a concrete way to realize any abstract group as a group of permutations. The name "left translation" comes from the fact that when $G = \mathbb{R}$, the map $L_g(x) = g + x$ is translation of the real line by $g$.

# Examples

**Example** (p. 49): For the chessboard symmetry group, $L_r(e) = r$, $L_r(r) = r^2 = e$, $L_r(q_1) = rq_1 = q_2$, $L_r(q_2) = rq_2 = q_1$. So $L_r$ interchanges $e \leftrightarrow r$ and $q_1 \leftrightarrow q_2$, corresponding to $(12)(34)$ in $S_4$.

# Relationships

## Enables
- **Cayley's theorem** — Left translations provide the embedding into $S_G$

## Related
- **Permutation** — Each left translation is a permutation

# Common Errors

- **Error**: Confusing left translation $L_g(x) = gx$ with right translation $R_g(x) = xg$.
  **Correction**: Armstrong uses left translation. Right translation also gives a valid (anti-)representation but with $R_g \circ R_h = R_{hg}$ (reversed order).

# Common Confusions

- **Confusion**: Thinking left translation is only defined for abelian groups.
  **Clarification**: Left translation is defined for any group. In non-abelian groups, $L_g \neq R_g$ in general.

# Source Reference

Chapter 8: Plato's Solids and Cayley's Theorem, page 48 (pdf p. 48). Definition and properties in the proof of Cayley's theorem.

# Verification Notes

- Definition: Direct quote from p. 48
- Example: Worked on p. 49
- Confidence: HIGH — explicit definition with proof of bijectivity
