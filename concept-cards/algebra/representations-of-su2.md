---
concept: Representations of SU(2)
slug: representations-of-su2
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.9 Representations of SU_2"
extraction_confidence: high
aliases: []
prerequisites: [special-unitary-group-su2, irreducible-representation]
extends: []
related: [orthogonality-of-characters]
contrasts_with: []
answers_questions: ["What are the representations of SU(2)?"]
---
# Quick Definition
The irreducible representations of SU_2 are the representations rho_n on the space H_n of homogeneous polynomials of degree n in two variables. The representation rho_n has dimension n+1 and character chi_n(theta) = (alpha^{n+1} - alpha^{-(n+1)})/(alpha - alpha^{-1}) where alpha = e^{i theta}.
# Core Definition
For each n >= 0, define rho_n: SU_2 -> GL(H_n) where H_n is the space of homogeneous polynomials of degree n in u, v, and P acts by substitution: [Pf](u,v) = f((u,v)P) (Artin, (10.9.2), (10.9.3), p. 326). The character on diagonal matrices A_theta = diag(e^{i theta}, e^{-i theta}) is chi_n(theta) = alpha^n + alpha^{n-2} + ... + alpha^{-n} (10.9.5). The orthogonality relations carry over from finite groups using integration over SU_2 (Theorem 10.9.7). Every continuous representation of SU_2 is a direct sum of the rho_n (Theorem 10.9.15).
# Prerequisites
- **Special unitary group SU_2** — The group being represented
- **Irreducible representation** — These are the irreducibles of SU_2
# Key Properties
1. dim(rho_n) = n + 1
2. chi_n is constant on conjugacy classes (latitudes of S^3)
3. Characters are orthonormal using integration: (chi_m, chi_n) = delta_{mn} (Theorem 10.9.7)
4. Every continuous representation decomposes into rho_n's (Theorem 10.9.15)
5. rho_0 = trivial, rho_1 = standard 2D representation
6. The Hermitian product uses integration over the 3-sphere
# Context & Application
This section extends character theory from finite groups to the compact group SU_2, replacing sums with integrals. It connects to the theory of angular momentum in quantum mechanics, where rho_n corresponds to spin n/2.
# Examples
**Example 1** (p. 327): rho_0 is the trivial representation (dimension 1). rho_1 is the standard 2D representation. rho_2 has dimension 3.
**Example 2** (p. 327): On diagonal matrices, chi_0(theta) = 1, chi_1(theta) = alpha + alpha^{-1} = 2 cos theta, chi_2(theta) = alpha^2 + 1 + alpha^{-2}.
# Relationships
## Builds Upon
- **Special unitary group SU_2** — The group
- **Irreducible representation** — These are the irreducibles
## Related
- **Orthogonality of characters** — Generalized to compact groups via integration
# Source Reference
Chapter 10: Group Representations, Section 10.9, pages 326-329.
# Verification Notes
- Definition source: Direct from (10.9.2), (10.9.3), (10.9.5)
- Confidence rationale: Explicitly defined and analyzed
- Uncertainties: Theorem 10.9.15 stated without proof (refers to Sepanski)
- Cross-reference status: Verified
