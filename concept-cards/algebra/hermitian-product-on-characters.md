---
concept: Hermitian Product on Characters
slug: hermitian-product-on-characters
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.4 Characters"
extraction_confidence: high
aliases: []
prerequisites: [character-of-a-representation]
extends: []
related: [orthogonality-of-characters]
contrasts_with: []
answers_questions: ["How is the inner product on characters defined?"]
---
# Quick Definition
The Hermitian product on characters is (chi, chi') = (1/|G|) sum_g chi(g)-bar chi'(g). It can also be written by grouping conjugacy classes: (1/|G|) sum_i c_i chi(g_i)-bar chi'(g_i), where c_i is the size of the i-th class.
# Core Definition
The Hermitian product on characters is defined by (chi, chi') = (1/|G|) sum_g chi(g)-bar chi'(g) (Artin, (10.4.3), p. 310). Grouping by conjugacy class: (chi, chi') = (1/|G|) sum_{i=1}^r c_i chi(g_i)-bar chi'(g_i) (10.4.4). The irreducible characters are orthonormal with respect to this product. For any character chi = n_1 chi_1 + ... + n_r chi_r, the multiplicities are n_i = (chi, chi_i).
# Prerequisites
- **Character of a representation** — The objects being paired
# Key Properties
1. (chi, chi') = (1/|G|) sum_g chi(g)-bar chi'(g)
2. Irreducible characters are orthonormal
3. (chi, chi') is always an integer for characters (Corollary 10.4.9)
4. n_i = (chi, chi_i) gives multiplicities in the irreducible decomposition
5. (chi, chi) = 1 iff chi is irreducible
# Examples
**Example 1** (p. 311): For S_3: (chi_A, chi_A) = (1/6)(1*4 + 2*1*1 + 3*0*0) = 1.
# Relationships
## Enables
- **Orthogonality of characters** — Characters are orthonormal under this product
# Source Reference
Chapter 10: Group Representations, Section 10.4, (10.4.3), (10.4.4), pages 310-311.
# Verification Notes
- Definition source: Direct from (10.4.3)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
