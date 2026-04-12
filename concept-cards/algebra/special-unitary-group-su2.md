---
concept: Special Unitary Group SU(2)
slug: special-unitary-group-su2
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.3 The Special Unitary Group SU_2"
extraction_confidence: high
aliases: ["SU_2", "SU(2)"]
prerequisites: [unitary-group]
extends: [unitary-group]
related: [quaternion-algebra, covering-map-su2-to-so3, special-orthogonal-group, n-sphere]
contrasts_with: []
answers_questions: ["What is SU(2)?", "How does SU(2) relate to SO(3)?"]
---
# Quick Definition
SU_2 is the group of 2x2 unitary matrices with determinant 1. Its elements have the form [[a, -b-bar],[b, a-bar]] with |a|^2 + |b|^2 = 1. It is homeomorphic to the 3-sphere S^3.
# Core Definition
SU_2 consists of complex 2x2 matrices P = [[a, -b-bar],[b, a-bar]] where a-bar a + b-bar b = 1 (Artin, (9.3.1), p. 268). Writing a = x_0 + x_1 i and b = x_2 + x_3 i gives a bijection SU_2 <-> S^3 (9.3.2). The identity I corresponds to the north pole (1,0,0,0). The latitudes (xo = c) are conjugacy classes (Proposition 9.3.5), and the longitudes are conjugate subgroups (Proposition 9.3.9).
# Prerequisites
- **Unitary group** — SU_2 = U_2 intersect SL_2
# Key Properties
1. Homeomorphic to S^3 via a = x_0 + x_1 i, b = x_2 + x_3 i
2. Center is {+/- I}
3. Conjugacy classes are latitudes on S^3 (trace = 2c surfaces)
4. Longitudes are conjugate subgroups isomorphic to U_1
5. The equator (trace = 0) consists of matrices with eigenvalues +/- i
6. SU_2 maps surjectively onto SO_3 with kernel {+/- I} (Theorem 9.4.1)
7. The only proper normal subgroup is {+/- I} (Theorem 9.7.10)
# Construction / Recognition
## To Recognize:
1. Check P*P = I and det P = 1 for a 2x2 complex matrix
2. Or verify the form [[a, -b-bar],[b, a-bar]] with |a|^2 + |b|^2 = 1
# Context & Application
SU_2 is one of the most important groups in mathematics and physics. It is the spin group covering SO_3, fundamental to quantum mechanics (spin-1/2 particles), and the simplest non-abelian compact Lie group. Artin's approach through the geometry of the 3-sphere is distinctive.
# Examples
**Example 1** (p. 269): The quaternion generators i = [[i,0],[0,-i]], j = [[0,1],[-1,0]], k = [[0,i],[i,0]] are elements of SU_2 on the equator.
**Example 2** (p. 270): The longitude cI + si = [[e^{i theta}, 0],[0, e^{-i theta}]] is the group of diagonal matrices in SU_2.
# Relationships
## Builds Upon
- **Unitary group** — SU_2 is a subgroup of U_2
## Enables
- **Covering map SU_2 to SO_3** — The 2:1 surjection gamma
- **Quaternion algebra** — SU_2 is the unit quaternions
## Related
- **n-sphere** — SU_2 is homeomorphic to S^3
# Common Errors
- **Error**: Thinking SU_2 and SO_3 are isomorphic
  **Correction**: SU_2 is a double cover of SO_3; they differ by the kernel {+/- I}
# Common Confusions
- **Confusion**: Thinking the 2-sphere has a group structure like SU_2
  **Clarification**: Only S^1 and S^3 can be given continuous group laws; S^2 cannot
# Source Reference
Chapter 9: Linear Groups, Section 9.3, pages 268-271.
# Verification Notes
- Definition source: Direct from (9.3.1) and (9.3.2)
- Confidence rationale: Extensively developed
- Uncertainties: None
- Cross-reference status: Verified
