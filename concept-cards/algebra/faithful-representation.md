---
concept: Faithful Representation
slug: faithful-representation
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
related: []
contrasts_with: [trivial-representation]
answers_questions: ["What is a faithful representation?"]
---
# Quick Definition
A representation R is faithful if the homomorphism R: G -> GL_n is injective, mapping G isomorphically to its image, a subgroup of GL_n.
# Core Definition
A representation R is faithful if the homomorphism R: G -> GL_n is injective (Artin, p. 302). Equivalently, R_g = I implies g = 1. The standard representation of S_3 is faithful.
# Prerequisites
- **Group representation** — Faithfulness is a property of representations
# Key Properties
1. R is injective: R_g = I implies g = 1
2. G is isomorphic to its image in GL_n
3. Not all representations are faithful; the trivial representation is never faithful (for |G| > 1)
# Examples
**Example 1** (p. 302): The standard 2D representation A of S_3 is faithful.
**Example 2** (p. 302): The sign representation Sigma of S_3 is NOT faithful (kernel = A_3).
# Relationships
## Builds Upon
- **Group representation** — Property of representations
## Contrasts With
- **Trivial representation** — Always has kernel = G
# Source Reference
Chapter 10: Group Representations, Section 10.1, page 302.
# Verification Notes
- Definition source: Direct from p. 302
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
