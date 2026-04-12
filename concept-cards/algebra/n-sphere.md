---
concept: n-Sphere
slug: n-sphere
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.2 Interlude: Spheres"
extraction_confidence: high
aliases: ["unit sphere"]
prerequisites: []
extends: []
related: [stereographic-projection, special-unitary-group-su2]
contrasts_with: []
answers_questions: ["What is the n-sphere?"]
---
# Quick Definition
The n-dimensional unit sphere S^n is the locus {x_0^2 + x_1^2 + ... + x_n^2 = 1} in R^{n+1}. The 3-sphere S^3 is homeomorphic to SU_2.
# Core Definition
The n-sphere S^n is the set of unit vectors in R^{n+1}: {x_0^2 + ... + x_n^2 = 1} (Artin, p. 266). The 1-sphere S^1 is the unit circle, the 2-sphere S^2 is the ordinary sphere, and the 3-sphere S^3 is homeomorphic to SU_2 via the correspondence a = x_0 + x_1 i, b = x_2 + x_3 i (9.3.2). The famous theorem of topology states that the only spheres with continuous group structures are S^1 and S^3 (p. 268).
# Prerequisites
This is a foundational topological concept for the chapter.
# Key Properties
1. S^n lives in R^{n+1}
2. Can be constructed as the union of two n-balls glued along their boundary (n-1)-spheres
3. Stereographic projection maps S^n minus a point homeomorphically to R^n
4. Only S^1 and S^3 admit group structures (p. 268)
5. S^3 = SU_2 as a topological space with group structure
# Context & Application
Spheres provide the topological foundations for understanding the classical groups. SU_2 is homeomorphic to S^3, SO_3 is homeomorphic to projective 3-space P^3 (obtained by identifying antipodal points of S^3).
# Examples
**Example 1** (p. 266): S^1 is the unit circle, S^2 is the unit sphere in R^3.
**Example 2** (p. 268): S^3 = SU_2 = {(x_0, x_1, x_2, x_3) | x_0^2 + x_1^2 + x_2^2 + x_3^2 = 1}.
# Relationships
## Enables
- **Special unitary group SU_2** — SU_2 is homeomorphic to S^3
## Related
- **Stereographic projection** — Maps S^n minus a point to R^n
# Source Reference
Chapter 9: Linear Groups, Section 9.2, pages 266-268.
# Verification Notes
- Definition source: Direct from p. 266
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
