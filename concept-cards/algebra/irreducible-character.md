---
concept: Irreducible Character
slug: irreducible-character
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
prerequisites: [character-of-a-representation, irreducible-representation]
extends: [character-of-a-representation]
related: [character-table, orthogonality-of-characters]
contrasts_with: []
answers_questions: ["What is an irreducible character?"]
---
# Quick Definition
An irreducible character is the character of an irreducible representation. The irreducible characters form an orthonormal basis for the space of class functions. A character chi is irreducible if and only if (chi, chi) = 1.
# Core Definition
The character of an irreducible representation is called an irreducible character (Artin, p. 308). Irreducible characters are orthonormal: (chi_i, chi_j) = delta_{ij} (Main Theorem 10.4.6(a)). They form an orthonormal basis for the space of class functions (Corollary 10.4.11). A character chi is irreducible iff (chi, chi) = 1 (from (10.4.10)).
# Prerequisites
- **Character of a representation** — An irreducible character is a character
- **Irreducible representation** — Of an irreducible representation
# Key Properties
1. (chi, chi) = 1 characterizes irreducible characters
2. Orthonormal: (chi_i, chi_j) = delta_{ij}
3. Form a basis for class functions
4. Number of irreducible characters = number of conjugacy classes
# Examples
**Example 1** (p. 311): For S_3, chi_A is irreducible: (chi_A, chi_A) = (1/6)(4+2+0) = 1.
# Relationships
## Builds Upon
- **Character of a representation** — Special case
- **Irreducible representation** — Characters of these
## Enables
- **Character table** — Rows are irreducible characters
# Source Reference
Chapter 10: Group Representations, Section 10.4, pages 308-313.
# Verification Notes
- Definition source: Direct from p. 308
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
