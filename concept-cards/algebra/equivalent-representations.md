---
concept: Equivalent Representations
slug: equivalent-representations
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
aliases: ["isomorphic representations"]
prerequisites: [group-representation]
extends: []
related: [character-of-a-representation]
contrasts_with: []
answers_questions: ["When are two representations equivalent?"]
---
# Quick Definition
Two representations rho: G -> GL(V) and rho': G -> GL(V') are equivalent (isomorphic) if there exists an invertible linear map T: V -> V' such that T(gv) = gT(v) for all g and v. Equivalently, their characters are equal.
# Core Definition
An isomorphism from rho to rho' is an invertible linear transformation T: V -> V' compatible with the G-actions: T(gv) = gT(v) for all g and v (Artin, (10.1.16), p. 304). In matrix form, the corresponding matrix representations R and R' are equal when compatible bases are chosen. Two representations are isomorphic iff their characters are equal (Corollary 10.4.8(c)).
# Prerequisites
- **Group representation** — Equivalence is a relation between representations
# Key Properties
1. T is an invertible linear map intertwining the G-actions
2. Characters determine equivalence: rho = rho' iff chi_rho = chi_rho'
3. A change of basis conjugates matrix representations: R'_g = P^{-1} R_g P
# Examples
**Example 1** (p. 304): Two matrix representations related by R'_g = P^{-1} R_g P are equivalent.
# Relationships
## Related
- **Character of a representation** — Characters determine equivalence
# Source Reference
Chapter 10: Group Representations, Section 10.1, pages 304-305. Corollary 10.4.8(c).
# Verification Notes
- Definition source: Direct from (10.1.16)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
