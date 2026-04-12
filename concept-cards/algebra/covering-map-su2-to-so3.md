---
concept: Covering Map SU(2) to SO(3)
slug: covering-map-su2-to-so3
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.4 The Rotation Group SO_3"
extraction_confidence: high
aliases: ["spin homomorphism", "orthogonal representation of SU_2"]
prerequisites: [special-unitary-group-su2, special-orthogonal-group]
extends: []
related: [quaternion-algebra]
contrasts_with: []
answers_questions: ["How does SU(2) relate to SO(3)?"]
---
# Quick Definition
The spin homomorphism gamma: SU_2 -> SO_3 is a surjective group homomorphism with kernel {+/- I}. It sends a matrix P in SU_2 to the rotation gamma_P that acts by conjugation on the space of trace-zero skew-Hermitian matrices.
# Core Definition
Theorem 9.4.1: (a) The rule P -> gamma_P, where gamma_P(U) = PUP*, defines a surjective homomorphism gamma: SU_2 -> SO_3 with kernel {+/- I}. (b) If P = cos(theta) I + sin(theta) A with A on the equator and 0 < theta < pi, then gamma_P rotates the equatorial sphere E about pole A through angle 2*theta (Artin, p. 271).
# Prerequisites
- **Special unitary group SU_2** — The domain of the map
- **Special orthogonal group** — SO_3 is the target
# Key Properties
1. gamma is surjective with kernel {+/- I} (a 2:1 map)
2. SO_3 = SU_2 / {+/- I}
3. gamma_P acts on the 3D space V of trace-zero skew-Hermitian matrices by conjugation
4. gamma_P is a rotation: it preserves the inner product (U,V) = -1/2 trace(UV) (Lemma 9.4.4)
5. The angle of rotation is 2*theta when P = cos(theta) I + sin(theta) A
6. SU_2 is the "double cover" or "spin group" of SO_3
# Construction / Recognition
## To Compute gamma_P:
1. Write P in SU_2
2. For U in V (trace-zero, skew-Hermitian), compute gamma_P(U) = PUP*
3. Express in the basis {i, j, k} to get the 3x3 rotation matrix
# Context & Application
This covering map is fundamental to the theory of spin in quantum mechanics. A rotation by 2*pi in SO_3 corresponds to going only halfway around SU_2 (from I to -I), explaining why spin-1/2 particles require a 4*pi rotation to return to their original state. Artin proves SO_3 is simple using this map (Theorem 9.7.10).
# Examples
**Example 1** (p. 274): For P = cos(theta) I + sin(theta) i (a diagonal matrix), gamma_P rotates the (j, k)-plane through angle 2*theta. Specifically, gamma_P(j) = cos(2*theta) j + sin(2*theta) k.
# Relationships
## Builds Upon
- **Special unitary group SU_2** — Domain of gamma
- **Special orthogonal group** — Codomain of gamma
## Related
- **Quaternion algebra** — gamma_P acts by quaternion conjugation
# Common Errors
- **Error**: Thinking theta in P = cos(theta) I + sin(theta) A is the rotation angle
  **Correction**: The rotation angle is 2*theta, not theta
# Common Confusions
- **Confusion**: Thinking SU_2 and SO_3 are isomorphic
  **Clarification**: They are not isomorphic; SU_2 is a double cover, and {+/- I} in SU_2 both map to the identity rotation in SO_3
# Source Reference
Chapter 9: Linear Groups, Section 9.4, pages 271-275. Theorem 9.4.1.
# Verification Notes
- Definition source: Direct from Theorem 9.4.1
- Confidence rationale: Central theorem, fully proved
- Uncertainties: None
- Cross-reference status: Verified
