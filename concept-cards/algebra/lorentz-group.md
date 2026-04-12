---
concept: Lorentz Group
slug: lorentz-group
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.1 The Classical Groups"
extraction_confidence: high
aliases: ["O_{3,1}"]
prerequisites: [lorentz-form]
extends: [general-linear-group]
related: [classical-groups]
contrasts_with: [orthogonal-group]
answers_questions: ["What is the Lorentz group?"]
---
# Quick Definition
The Lorentz group O_{3,1} is the group of real matrices preserving the Lorentz form on R^4. Its elements are called Lorentz transformations.
# Core Definition
O_{3,1} = {P in GL_n | P^t I_{3,1} P = I_{3,1}} where I_{3,1} = diag(1,1,1,-1) (Artin, (9.1.5), p. 265). Analogous groups O_{p,m} can be defined for any signature (p, m).
# Prerequisites
- **Lorentz form** — The Lorentz group preserves this form
# Key Properties
1. Preserves the Lorentz form x_1 y_1 + x_2 y_2 + x_3 y_3 - x_4 y_4
2. Contains spatial rotations as a subgroup
3. det P = +/- 1 for P in O_{3,1}
4. Generalizes to O_{p,m} for signature (p, m)
# Context & Application
The Lorentz group is the symmetry group of special relativity. Lorentz transformations include rotations, boosts, and parity/time-reversal operations.
# Examples
**Example 1** (p. 265): O_{3,1} contains all rotations in the spatial coordinates (fixing the time coordinate).
# Relationships
## Builds Upon
- **Lorentz form** — Preserved by the group
## Contrasts With
- **Orthogonal group** — Preserves positive definite form, not indefinite
# Source Reference
Chapter 9: Linear Groups, Section 9.1, page 265.
# Verification Notes
- Definition source: Direct from (9.1.5)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
