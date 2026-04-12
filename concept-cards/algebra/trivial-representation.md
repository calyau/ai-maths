---
concept: Trivial Representation
slug: trivial-representation
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
aliases: []
prerequisites: [group-representation]
extends: [group-representation]
related: [one-dimensional-character]
contrasts_with: [faithful-representation]
answers_questions: ["What is the trivial representation?"]
---
# Quick Definition
The trivial representation is the one-dimensional representation T_g = [1] for all g in G. Its character is identically 1. It appears as a summand in every permutation representation.
# Core Definition
The trivial representation of G is the one-dimensional representation T: G -> GL_1 defined by T_g = [1] for all g (Artin, (10.1.5), p. 302). Its character chi_T(g) = 1 for all g. By convention, it occupies the first row of the character table.
# Prerequisites
- **Group representation** — The trivial representation is the simplest representation
# Key Properties
1. Dimension 1
2. T_g = [1] for all g
3. chi_T = 1 identically
4. Always irreducible (dimension 1)
5. Appears in every permutation representation (Lemma 10.6.4)
# Examples
**Example 1** (p. 302): For S_3: T_x = [1], T_y = [1].
# Relationships
## Related
- **One-dimensional character** — The trivial character is the simplest one-dimensional character
## Contrasts With
- **Faithful representation** — The trivial representation has kernel = G (maximally unfaithful)
# Source Reference
Chapter 10: Group Representations, Section 10.1, page 302.
# Verification Notes
- Definition source: Direct from (10.1.5)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
