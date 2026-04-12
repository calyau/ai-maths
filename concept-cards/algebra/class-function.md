---
concept: Class Function
slug: class-function
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
answers_questions: ["What is a class function?"]
---
# Quick Definition
A class function is a complex-valued function on a group that is constant on each conjugacy class. Characters are class functions, and the irreducible characters form an orthonormal basis for the space of class functions.
# Core Definition
A complex-valued function phi on G that is constant on each conjugacy class is called a class function (Artin, p. 313). The vector space of class functions has dimension equal to the number of conjugacy classes. The irreducible characters form an orthonormal basis of this space (Corollary 10.4.11), using the Hermitian product (phi, psi) = (1/|G|) sum_g phi(g)-bar psi(g).
# Prerequisites
- **Character of a representation** — Characters are class functions; they form a basis
# Key Properties
1. phi(hgh^{-1}) = phi(g) for all g, h
2. The space of class functions has dimension r (number of conjugacy classes)
3. The irreducible characters form an orthonormal basis (Corollary 10.4.11)
4. A class function can be specified by giving values on conjugacy classes (r values)
# Context & Application
Class functions are the natural domain for characters. The fact that irreducible characters form a basis shows that any class function can be expressed as a linear combination of irreducible characters.
# Examples
**Example 1** (p. 313): For S_3 with 3 conjugacy classes, the space of class functions is 3-dimensional with basis chi_1, chi_2, chi_3.
# Relationships
## Related
- **Orthogonality of characters** — Irreducible characters are an orthonormal basis for class functions
# Source Reference
Chapter 10: Group Representations, Section 10.4, page 313. Corollary 10.4.11.
# Verification Notes
- Definition source: Direct from p. 313
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
