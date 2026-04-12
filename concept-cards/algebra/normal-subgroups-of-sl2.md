---
concept: Normal Subgroups of SL(2)
slug: normal-subgroups-of-sl2
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.8 Normal Subgroups of SL_2"
extraction_confidence: high
aliases: ["PSL_2"]
prerequisites: [special-linear-group]
extends: []
related: [special-unitary-group-su2, covering-map-su2-to-so3]
contrasts_with: []
answers_questions: ["What are the normal subgroups of SL(2)?"]
---
# Quick Definition
For a field F of order at least 4, the only proper normal subgroup of SL_2(F) is its center {+/- I}. The quotient PSL_2(F) = SL_2(F)/{+/- I} is a simple group. For finite fields F_q, this gives families of finite simple groups.
# Core Definition
Theorem 9.8.1: Let F be a field of order at least 4. (a) The only proper normal subgroup of SL_2(F) is its center Z = {+/- I}. (b) The projective group PSL_2(F) is a simple group (Artin, p. 293). The proof uses a commutator trick to show any normal subgroup containing a non-central element must contain all elementary matrices, hence all of SL_2 (Steps 1-4, pp. 294-295).
# Prerequisites
- **Special linear group** — SL_2(F) is the group being studied
# Key Properties
1. Center of SL_2(F) is {+/- I}
2. PSL_2(F) = SL_2(F)/{+/- I} is simple for |F| >= 4
3. |SL_2(F_q)| = q^3 - q (Lemma 9.8.2)
4. |PSL_2(F_q)| = (q^3 - q)/2 for odd q; = q^3 - q for even q
5. PSL_2(F_4) = PSL_2(F_5) = A_5 (order 60)
6. PSL_2(F_2) = S_3, PSL_2(F_3) = A_4 (not simple)
# Context & Application
The projective groups PSL_2(F_q) provide important families of finite simple groups, alongside the alternating groups. This result parallels Theorem 9.7.10 for SU_2 (the continuous case).
# Examples
**Example 1** (p. 294): PSL_2(F_5) has order 60 and is isomorphic to A_5 and to the icosahedral group I.
# Relationships
## Builds Upon
- **Special linear group** — The group being analyzed
## Related
- **Special unitary group SU_2** — Continuous analogue (Theorem 9.7.10)
- **Covering map SU_2 to SO_3** — Parallel structure
# Source Reference
Chapter 9: Linear Groups, Section 9.8, pages 293-296. Theorem 9.8.1.
# Verification Notes
- Definition source: Direct from Theorem 9.8.1
- Confidence rationale: Major theorem, proof given for |F| > 5
- Uncertainties: Cases |F| = 4, 5 left as exercises
- Cross-reference status: Verified
