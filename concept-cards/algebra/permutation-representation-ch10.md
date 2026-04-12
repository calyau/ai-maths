---
concept: Permutation Representation
slug: permutation-representation-ch10
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.6 The Regular Representation"
extraction_confidence: high
aliases: []
prerequisites: [group-representation, group-action]
extends: [group-representation]
related: [regular-representation]
contrasts_with: []
answers_questions: ["What is a permutation representation?"]
---
# Quick Definition
A permutation representation is the matrix representation associated to an operation of G on a finite set S. Its character chi(g) equals the number of elements of S fixed by g.
# Core Definition
Let S = (s_1, ..., s_n) be a finite ordered set on which G operates. The permutation representation R assigns to each g the permutation matrix R_g (Artin, (10.6.1), p. 317). Equivalently, on the vector space V_S with basis {e_s}, define rho_g(e_s) = e_{gs}. The character is especially simple: chi(g) = number of fixed points of g (Lemma 10.6.3). The trivial character always appears as a summand (Lemma 10.6.4).
# Prerequisites
- **Group representation** — A permutation representation is a specific type
- **Group action** — The operation of G on S
# Key Properties
1. chi(g) = number of fixed points of g on S (Lemma 10.6.3)
2. Always contains the trivial representation as a summand (Lemma 10.6.4)
3. Dimension = |S|
4. Generally reducible unless |S| = 1
# Examples
**Example 1** (p. 308): S_3 acting on {1,2,3} gives the permutation representation N with N_x = [[0,0,1],[1,0,0],[0,1,0]], N_y = [[0,1,0],[1,0,0],[0,0,1]].
**Example 2** (p. 318): The tetrahedral group T acting on the 4 vertices gives a 4D representation with chi^vert = (4, 1, 1, 0), decomposing as chi_1 + chi_4.
# Relationships
## Builds Upon
- **Group action** — The operation of G on S
## Enables
- **Regular representation** — The permutation representation for G acting on itself
# Source Reference
Chapter 10: Group Representations, Section 10.6, pages 317-318.
# Verification Notes
- Definition source: Direct from (10.6.1) and (10.6.2)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
