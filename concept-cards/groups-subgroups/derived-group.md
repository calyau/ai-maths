---
concept: Derived Group
slug: derived-group
category: group-structure
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 186
section: "16c The derived group of algebraic group"
extraction_confidence: high
aliases:
  - commutator subgroup
  - first derived group
  - "G^der"
  - DG
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - solvable-algebraic-group
contrasts_with: []
answers_questions:
  - "What is the derived group of an algebraic group?"
---

# Quick Definition

The derived group DG (or G^der) of an algebraic group G is the smallest normal subgroup N such that G/N is commutative. It is the algebraic analogue of the commutator subgroup [G,G].

# Core Definition

The *derived group* DG of an algebraic group G is the intersection of all normal algebraic subgroups N of G such that G/N is commutative (Definition 16.17). The quotient G/DG is commutative (Proposition 16.18). The coordinate ring O(DG) = O(G)/I where I = intersect I_n and I_n is the kernel of the map O(G) -> O(G^{2n}) defined by the commutator map. For smooth connected G, DG(k^al) = D(G(k^al)), the abstract derived group (Corollary 16.22). DG is connected if G is connected, and smooth if G is smooth (Corollary 16.21, Milne, pp. 186-188).

# Prerequisites

- **Affine algebraic group** -- DG is defined for algebraic groups

# Key Properties

1. DG is the smallest normal subgroup with commutative quotient
2. DG is connected (resp. smooth) if G is (Corollary 16.21)
3. For smooth connected G, DG(k^al) equals the abstract derived group (Corollary 16.22)
4. Formation of DG commutes with field extension (Corollary 16.20)
5. DG is the unique smooth subgroup with DG(k^al) = D(G(k^al)) (Corollary 16.23)

# Context & Application

The derived series G > DG > D^2G > ... determines solvability. The derived group captures the non-commutative part of G. For reductive groups, DG is semisimple and G = DG . Z(G)^0.

# Examples

**Example 1** (p. 188): For GL_n, the derived group is SL_n (since GL_n/SL_n = G_m is commutative).

**Example 2** (p. 189): For the Borel subgroup B = T_n, DB = U_n (the unipotent radical).

# Relationships

## Enables
- **Solvable algebraic group** -- Solvability is defined via the derived series

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 16c, pages 186-188. Definition 16.17, Propositions 16.18-16.19, Corollaries 16.20-16.23.

# Verification Notes

- Definition source: Direct from Definition 16.17
- Confidence rationale: Explicit definition with structural results
- Uncertainties: None
- Cross-reference status: Verified
