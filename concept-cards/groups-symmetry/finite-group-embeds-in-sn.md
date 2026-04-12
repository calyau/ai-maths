---
# === CORE IDENTIFICATION ===
concept: Finite Group Embeds in S_n
slug: finite-group-embeds-in-sn

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
  - "Theorem 8.2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cayleys-theorem
  - composition-of-isomorphisms
extends:
  - cayleys-theorem
related:
  - symmetric-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can every finite group be embedded in a symmetric group S_n?"
---

# Quick Definition

Every finite group of order $n$ is isomorphic to a subgroup of $S_n$. This is the finite version of Cayley's theorem.

# Core Definition

"(8.2) Theorem. If $G$ is a finite group of order $n$, then $G$ is isomorphic to a subgroup of $S_n$" (Armstrong, p. 49). The proof proceeds by numbering the elements of $G$ as $1, 2, \ldots, n$, then composing the Cayley embedding $G \hookrightarrow S_G$ with the natural isomorphism $S_G \cong S_n$.

# Prerequisites

- **Cayley's theorem** — $G$ embeds in $S_G$; Theorem 8.2 refines this for finite groups
- **Composition of isomorphisms** — Used to compose the two isomorphisms

# Key Properties

1. Every finite group of order $n$ embeds in $S_n$
2. The embedding is constructed by Cayley's theorem followed by numbering
3. This gives a concrete permutation representation of any finite group

# Construction / Recognition

## To Embed:
1. Number the elements of $G$ as $1, 2, \ldots, n$
2. Apply Cayley's theorem to get $G \cong G' \le S_G$
3. The numbering gives $S_G \cong S_n$
4. Composing: $G \cong G'' \le S_n$

# Context & Application

This theorem shows that abstract finite group theory is equivalent to the study of subgroups of symmetric groups. While the embedding may be inefficient (a group of order 6 embeds in $S_6$ which has 720 elements), it guarantees that every finite group can be concretely realized.

# Examples

**Example** (p. 49): The chessboard symmetry group (order 4) embeds as $\{\varepsilon, (12)(34), (13)(24), (14)(23)\} \le S_4$.

# Relationships

## Builds Upon
- **Cayley's theorem** — The infinite version

## Related
- **Symmetric group** — The target of the embedding

# Common Errors

- **Error**: Thinking the embedding is unique.
  **Correction**: The embedding depends on the numbering of elements; different numberings give different (conjugate) subgroups of $S_n$.

# Common Confusions

- **Confusion**: Thinking this gives the smallest symmetric group containing $G$.
  **Clarification**: $S_n$ may be much larger than necessary. Some groups embed in $S_m$ for $m < n$.

# Source Reference

Chapter 8: Plato's Solids and Cayley's Theorem, page 49 (pdf p. 49). Theorem 8.2.

# Verification Notes

- Theorem: Direct from p. 49
- Example: Worked on p. 49
- Confidence: HIGH — theorem with proof
