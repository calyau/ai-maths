---
concept: G-Invariant Vector
slug: g-invariant-vector
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
aliases: ["fixed vector"]
prerequisites: [group-representation]
extends: []
related: [g-invariant-subspace]
contrasts_with: []
answers_questions: ["What is a G-invariant vector?"]
---
# Quick Definition
A vector v is G-invariant if gv = v for all g in G. Starting from any vector v, the average v-tilde = (1/|G|) sum_{g in G} gv is always G-invariant (though it may be zero).
# Core Definition
A vector v is G-invariant if rho_g(v) = v for all g in G (Artin, (10.2.1), p. 306). The averaging process produces G-invariant vectors: v-tilde = (1/|G|) sum_g gv (10.2.2). The proof uses the reindexing trick: left multiplication by h permutes the group elements (10.2.3).
# Prerequisites
- **Group representation** — G-invariant vectors are defined within representations
# Key Properties
1. gv = v for all g in G
2. Averaging any vector v produces a G-invariant vector v-tilde
3. If v is already G-invariant, then v-tilde = v
4. v-tilde may be the zero vector
5. The set of G-invariant vectors forms a G-invariant subspace
# Examples
**Example 1** (p. 306): In the permutation representation of S_3 on C^3, the vector (1,1,1)^t is G-invariant.
# Relationships
## Related
- **G-invariant subspace** — G-invariant vectors span a G-invariant subspace
# Source Reference
Chapter 10: Group Representations, Section 10.2, pages 305-306.
# Verification Notes
- Definition source: Direct from (10.2.1) and (10.2.2)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
