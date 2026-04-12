---
concept: Degree of Representation
slug: degree-of-representation
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
aliases: ["dimension of representation"]
prerequisites: [group-representation]
extends: []
related: [main-theorem-on-characters]
contrasts_with: []
answers_questions: ["What is the degree (dimension) of a representation?"]
---
# Quick Definition
The degree (or dimension) of a matrix representation R: G -> GL_n is n, the size of the matrices. It equals chi(1), the character evaluated at the identity.
# Core Definition
The number n in R: G -> GL_n is the dimension (or degree) of the representation (Artin, p. 301). For a representation rho on a vector space V, the dimension is dim V. Equivalently, chi(1) = trace(I_n) = n (Proposition 10.4.2(a)). The Main Theorem constrains dimensions: |G| = d_1^2 + ... + d_r^2.
# Prerequisites
- **Group representation** — Degree is a basic attribute of representations
# Key Properties
1. n = size of matrices in R: G -> GL_n
2. chi(1) = n
3. Dimensions of irreducibles satisfy |G| = d_1^2 + ... + d_r^2
4. Each d_i divides |G|
# Examples
**Example 1** (p. 302): The standard representation A of S_3 has degree 2. The sign representation has degree 1.
# Relationships
## Related
- **Main theorem on characters** — Constrains the degrees of irreducible representations
# Source Reference
Chapter 10: Group Representations, Section 10.1, page 301.
# Verification Notes
- Definition source: Direct from p. 301
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
