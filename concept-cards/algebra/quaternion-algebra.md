---
concept: Quaternion Algebra
slug: quaternion-algebra
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
aliases: ["quaternions", "Hamilton's quaternions"]
prerequisites: [special-unitary-group-su2]
extends: []
related: [covering-map-su2-to-so3]
contrasts_with: []
answers_questions: ["What are the quaternions?"]
---
# Quick Definition
The quaternion algebra is the real 4-dimensional vector space with basis (I, i, j, k) where i, j, k are specific 2x2 matrices in SU_2 satisfying ij = k, ji = -k, and i^2 = j^2 = k^2 = -I. SU_2 is the set of unit vectors in this algebra.
# Core Definition
The quaternion algebra has basis {I, i, j, k} where i = [[i,0],[0,-i]], j = [[0,1],[-1,0]], k = [[0,i],[i,0]] (Artin, (9.3.3), p. 269). These satisfy the quaternion relations: i^2 = j^2 = k^2 = -I, ij = k, jk = i, ki = j, ji = -k, kj = -i, ik = -j. SU_2 is the set of unit quaternions (those with |a|^2 + |b|^2 = 1).
# Prerequisites
- **Special unitary group SU_2** — The quaternion algebra describes SU_2
# Key Properties
1. Real dimension 4 with basis {I, i, j, k}
2. Multiplication is associative but NOT commutative
3. The quaternion relations: ij = k, ji = -k, etc.
4. Every nonzero quaternion has an inverse (it is a division algebra)
5. SU_2 = {unit quaternions}
6. The equator of SU_2 consists of purely imaginary quaternions x_1 i + x_2 j + x_3 k
# Construction / Recognition
## To Construct:
1. Take a real linear combination q = x_0 I + x_1 i + x_2 j + x_3 k
2. Multiply using the quaternion relations
# Context & Application
Quaternions were discovered by Hamilton in 1843. They provide an elegant description of rotations in 3D (via conjugation in SU_2) and are used in computer graphics, robotics, and spacecraft attitude control. The formula UV = -(u . v)I + u x v (p. 272) connects quaternion multiplication to dot and cross products.
# Examples
**Example 1** (p. 269): The quaternion group {+/- I, +/- i, +/- j, +/- k} is a subgroup of SU_2 of order 8.
**Example 2** (p. 272): For purely imaginary quaternions U, V: UV = -(u_1 v_1 + u_2 v_2 + u_3 v_3)I + U x V (Lemma 9.4.4).
# Relationships
## Builds Upon
- **Special unitary group SU_2** — Unit quaternions = SU_2
## Enables
- **Covering map SU_2 to SO_3** — Conjugation by unit quaternions gives rotations
# Common Errors
- **Error**: Assuming quaternion multiplication is commutative
  **Correction**: ij = k but ji = -k; quaternion multiplication is noncommutative
# Source Reference
Chapter 9: Linear Groups, Section 9.3, pages 269-270. Section 9.4 for the connection to rotations.
# Verification Notes
- Definition source: Direct from (9.3.3) and surrounding text
- Confidence rationale: Explicitly defined with relations
- Uncertainties: None
- Cross-reference status: Verified
