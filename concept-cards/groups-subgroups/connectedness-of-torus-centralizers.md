---
concept: Connectedness of Torus Centralizers
slug: connectedness-of-torus-centralizers
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 356
section: "Borel fixed point theorem and applications"
extraction_confidence: high
aliases: []
prerequisites:
  - reductive-algebraic-group
  - borel-fixed-point-theorem
extends: []
related:
  - split-maximal-torus
  - weyl-group-algebraic
contrasts_with: []
answers_questions:
  - "Is the centralizer of a torus always connected?"
---

# Quick Definition

In a reductive group G, the centralizer C_G(T) of any torus T is connected (and reductive). This is a deep consequence of the Borel fixed point theorem.

# Core Definition

**Theorem 2.7a**: Let T be a torus in a reductive group G. The centralizer C_G(T) is a reductive group (in particular, it is smooth and connected) (Milne, p. 342).

**Theorem 3.25/3.44**: For any torus T in G, C_G(T) is connected (pp. 356, 363). This is proved using the Borel fixed point theorem.

Additionally (Theorem 2.7b): the identity component of N_G(T) is C_G(T), so W(G,T) = N_G(T)/C_G(T) is finite étale.

# Prerequisites

- **Reductive algebraic group** — The ambient group
- **Borel fixed point theorem** — Key tool in the proof

# Key Properties

1. C_G(T) is connected, smooth, and reductive
2. T is maximal iff T = C_G(T)
3. Proved via the Bruhat decomposition and properties of reflection groups

# Source Reference

Chapter V, Sections 2i and 3d, Theorems 2.7 and 3.25/3.44, pages 342–343, 356, 363.

# Verification Notes

- Definition source: Direct from Theorems 2.7 and 3.44
- Confidence: HIGH
- Uncertainties: None
