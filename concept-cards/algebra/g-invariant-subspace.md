---
concept: G-Invariant Subspace
slug: g-invariant-subspace
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.2 Irreducible Representations"
extraction_confidence: high
aliases: ["invariant subspace"]
prerequisites: [group-representation]
extends: []
related: [irreducible-representation, reducible-representation]
contrasts_with: []
answers_questions: ["What is a G-invariant subspace?"]
---
# Quick Definition
A subspace W of V is G-invariant if gw is in W for all w in W and all g in G. The operation of G restricts to W, giving a sub-representation. A representation is irreducible iff its only G-invariant subspaces are {0} and V.
# Core Definition
Let rho be a representation of G on V. A subspace W is G-invariant if gW subset W for all g (Artin, (10.2.4), p. 306). Since group elements are invertible, gW = W for all g (Lemma 10.2.5). When V = W_1 direct-sum W_2 with both G-invariant, the representation is the direct sum of restrictions to W_1 and W_2.
# Prerequisites
- **Group representation** — G-invariant subspaces are defined for representations
# Key Properties
1. gW subset W for all g, or equivalently gW = W (since g is invertible)
2. The restriction of rho to a G-invariant W is again a representation
3. V has no proper G-invariant subspace iff rho is irreducible
4. In a unitary representation, W G-invariant implies W^perp G-invariant
# Examples
**Example 1** (p. 308): In the permutation representation N of S_3 on C^3, the span of (1,1,1)^t is a 1D G-invariant subspace.
# Relationships
## Enables
- **Irreducible representation** — Defined by the absence of proper G-invariant subspaces
- **Reducible representation** — Has a proper G-invariant subspace
# Source Reference
Chapter 10: Group Representations, Section 10.2, pages 306-307.
# Verification Notes
- Definition source: Direct from (10.2.4)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
