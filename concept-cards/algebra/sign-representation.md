---
concept: Sign Representation
slug: sign-representation
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.1 Definitions"
extraction_confidence: high
aliases: ["alternating character"]
prerequisites: [group-representation, one-dimensional-character]
extends: [one-dimensional-character]
related: [trivial-representation]
contrasts_with: [trivial-representation]
answers_questions: ["What is the sign representation?"]
---
# Quick Definition
The sign representation Sigma of the symmetric group S_n is the one-dimensional representation that sends each permutation to its sign (+1 or -1). For S_3: Sigma_x = [1], Sigma_y = [-1].
# Core Definition
The sign representation Sigma of S_n assigns to each group element the 1x1 matrix whose entry is the sign of the permutation (Artin, (10.1.4), p. 302). It is a one-dimensional representation and hence automatically irreducible. It is not faithful (its kernel is the alternating group A_n).
# Prerequisites
- **Group representation** — The sign representation is a specific representation
- **One-dimensional character** — The sign representation is one-dimensional
# Key Properties
1. One-dimensional: Sigma_g = [sign(g)]
2. Irreducible (dimension 1)
3. Not faithful (kernel = A_n)
4. Character: chi_Sigma(g) = sign(g)
# Examples
**Example 1** (p. 302): For S_3: Sigma_x = [1] (x = (123) is an even permutation), Sigma_y = [-1] (y = (12) is odd).
# Relationships
## Contrasts With
- **Trivial representation** — T_g = [1] for all g; Sigma_g = sign(g)
# Source Reference
Chapter 10: Group Representations, Section 10.1, page 302.
# Verification Notes
- Definition source: Direct from (10.1.4)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
